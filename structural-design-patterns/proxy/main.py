import time


# Define the interface for the Real Subject
class DatabaseQuery:
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    def execute_query(self, query):
        pass


# Real Subject: Represents the actual database
class RealDatabaseQuery(DatabaseQuery):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """

    def execute_query(self, query):
        print(f"Executing query: {query}")
        # Simulate a database query and return the results
        return f"Results for query: {query}"


# Proxy: Caching Proxy for Database Queries
class CacheProxy(DatabaseQuery):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_database_query, cache_duration_seconds):
        self._real_database_query = real_database_query
        self._cache = {}
        self._cache_duration = cache_duration_seconds

    def execute_query(self, query):
        if (
            query in self._cache
            and time.time() - self._cache[query]["timestamp"] <= self._cache_duration
        ):
            # Return cached result if it's still valid
            print(f"CacheProxy: Returning cached result for query: {query}")
            return self._cache[query]["result"]
        else:
            # Execute the query and cache the result
            result = self._real_database_query.execute_query(query)
            self._cache[query] = {"result": result, "timestamp": time.time()}
            return result


# Client code
if __name__ == "__main__":
    # Create the Real Subject
    real_database_query = RealDatabaseQuery()

    # Create the Cache Proxy with a cache duration of 5 seconds
    cache_proxy = CacheProxy(real_database_query, cache_duration_seconds=5)

    # Perform database queries, some of which will be cached
    print(cache_proxy.execute_query("SELECT * FROM table1"))
    print(cache_proxy.execute_query("SELECT * FROM table2"))
    time.sleep(3)  # Sleep for 3 seconds

    # Should return cached result
    print(cache_proxy.execute_query("SELECT * FROM table1"))
    print(cache_proxy.execute_query("SELECT * FROM table3"))
    print(cache_proxy.execute_query("SELECT * FROM table3"))
