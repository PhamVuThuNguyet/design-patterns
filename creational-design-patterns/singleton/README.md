## Singleton

### Intent

- **Singleton** is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

### Problems

Sometimes you need an object in an application where there is only one instance.

You don't want there to be many versions, for example, you have a game with a score, and you want to adjust it. You may have accidentally created several instances of the class holding the score object. Or, you may be opening a database connection, there is no need to create many, when you can use the existing one that is already in memory. You may want a logging component, and you want to ensure all classes use the same instance. So, every class could declare their own logger component, but behind the scenes, they all point to the same memory address (ID).

The Singleton pattern solves two problems at the same time:

- Ensure that a class has just a single instance. By creating a class and following the Singleton pattern, you can enforce that even if any number of instances were created, they will still refer to the original class.
- Provide a global access point to that instance. The Singleton can be accessible globally, but it is not a global variable. It is a class that can be instanced at any time, but after it is first instanced, any new instances will point to the same instance as the first.

<aside>
🖊️ For a class to behave as a Singleton, it should not contain any references to self but use static variables, static methods and/or class methods.

</aside>

### Solution

- All implementations of the Singleton have these two steps in common:
    - Make the default constructor private, to prevent other objects from using the `new` operator with the Singleton class.
    - Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.

### Applicability

- Use the Singleton pattern when a class in your program should have **just a single instance** available to all clients; for example, a single database object shared by different parts of the program.
- Use the Singleton pattern when you need stricter control over global variables. Unlike global variables, the Singleton pattern guarantees that there’s just one instance of a class. Nothing, except for the Singleton class itself, can replace the cached instance. Note that you can always **adjust this limitation** and **allow creating any number of Singleton instances**.

### Pros and Cons

✔️ You can be sure that a class has only a single instance.

✔️ You gain a global access point to that instance.

✔️ The singleton object is initialized only when it’s requested for the first time.

❌ Violates the *Single Responsibility Principle*. The pattern solves two problems at the time.

❌ The Singleton pattern can mask bad design, for instance, when the components of the program know too much about each other.

❌ The pattern requires special treatment in a multithreaded environment so that multiple threads won’t create a singleton object several times.

❌ It may be difficult to unit test the client code of the Singleton because many test frameworks rely on inheritance when producing mock objects. Since the constructor of the singleton class is private and overriding static methods is impossible in most languages, you will need to think of a creative way to mock the singleton. Or just don’t write the tests. Or don’t use the Singleton pattern.