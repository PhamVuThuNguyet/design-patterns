import copy
from abc import ABCMeta, abstractmethod
from typing import Any


class SelfReferencingEntity:
    def __init__(self):
        self._parent = None

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent


class IPrototype(metaclass=ABCMeta):
    """Interface with clone method"""

    @staticmethod
    @abstractmethod
    def clone():
        """
        Implement the clone method here
        """


class Prototype(IPrototype):
    def __init__(self, id: int, **kwargs: Any) -> None:
        self._id = id
        self.__dict__.update(kwargs)

    def clone(self, **kwargs: Any):
        """Clone a prototype and update inner attributes dictionary"""
        obj = copy.deepcopy(self)
        obj.__dict__.update(kwargs)
        return obj

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value


if __name__ == "__main__":
    # Create a circular ref
    circular_ref = SelfReferencingEntity()

    # Creating an original document with id = 1
    original_doc = Prototype(id=1, name="Original", circular_ref=circular_ref)

    circular_ref.set_parent(original_doc)

    # Create a clone with id = 2
    copied_doc = original_doc.clone(name="Copy 1")
    copied_doc.set_id(2)

    print(f"Original doc object: {original_doc}")
    print(f"First copied doc object: {copied_doc}")

    print(f"Original doc name: {original_doc.name}")
    print(f"First copied doc name: {copied_doc.name}")

    print(f"Original doc id: {original_doc.get_id()}")
    print(f"First copied doc id: {copied_doc.get_id()}")

    print(f"Original doc is the first copied doc: {original_doc is copied_doc}")

    print(
        f"Deep copied objects are not cloned repeatedly since they contain the same reference: {id(copied_doc.circular_ref.get_parent()) == id(copied_doc.circular_ref.get_parent().circular_ref.get_parent())}"
    )
