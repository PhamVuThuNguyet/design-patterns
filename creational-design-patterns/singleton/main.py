from typing import Any


class MetaSingleton(type):
    _instances = {}

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in self._instances:
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwds)
        return self._instances[self]


class Logger(metaclass=MetaSingleton):
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name


class Singleton:
    __instance = None

    def __new__(self):
        if not Singleton.__instance:
            Singleton.__instance = object.__new__(self)

        return Singleton.__instance


if __name__ == "__main__":

    """EXAMPLE USING SINGLETON CLASS"""
    instance_1 = Singleton()
    instance_2 = Singleton()

    print(f"Instance 1 object: {instance_1}")
    print(f"Instance 2 object: {instance_2}")
    print(f"Instance 1 is Instance 2: {instance_1 is instance_2}")

    """EXAMPLE USING MEGACLASS"""
    logger_1 = Logger("Instance 1")
    logger_2 = Logger("Instance 2")

    print(f"Logger 1 object: {logger_1}")
    print(f"Logger 2 object: {logger_2}")
    print(f"Logger 1 name: {logger_1.name}")
    print(f"Logger 2 name: {logger_2.name}")
    print(f"Logger 1 is Logger 2: {logger_1 is logger_2}")
