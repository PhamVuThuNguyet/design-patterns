## Factory Method (a.k.a Virtual Constructor)

### Intent

- **Factory Method** is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

### Problems

When developing code, you may instantiate objects directly in methods or in classes. While this is quite normal, you may want to add an extra abstraction between the creation of the object and where it is used in your project. 

### Solution

- The Factory Method pattern suggests that you replace direct object construction calls (using the `new` operator) with calls to a special ***factory* method**. The Factory pattern is really about adding that extra abstraction between the object creation and where it is used. This gives you extra options that you can more easily extend in the future.
- Objects returned by a factory method are often referred to as ***products.***
- Adding an extra abstraction will also allow you to dynamically choose classes to instantiate based on some kind of logic.
- After adding the factory abstraction, the concrete product (object) is no longer created in the current class/method, but in a subclass instead. Adding this extra abstraction also means that the complications of instantiating extra objects can now be hidden from the class or method that is using it.

### Applicability

- Use the Factory Method when you don’t know beforehand the exact types and dependencies of the objects your code should work with. The Factory Method separates product construction code from the code that actually uses the product. Therefore it’s easier to extend the product construction code independently from the rest of the code.
- Use the Factory Method when you want to provide users of your library or framework with a way to extend its internal components. Inheritance is probably the easiest way to extend the default behavior of a library or framework.
- Use the Factory Method when you want to save system resources by reusing existing objects instead of rebuilding them each time.

### **Pros and Cons**

✔️ You avoid tight coupling between the creator and the concrete products.

✔️ ***Single Responsibility Principle***. You can move the product creation code into one place in the program, making the code easier to support.

✔️ ***Open/Closed Principle*.** You can introduce new types of products into the program without breaking existing client code.

❌ The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you’re introducing the pattern into an existing hierarchy of creator classes.