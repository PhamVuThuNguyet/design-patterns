## Abstract Factory

### Intent

- **Abstract Factory** is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.
- In other words, the Abstract Factory Pattern adds an abstraction layer over multiple other creational pattern implementations.

### Problems

- I want to create multiple types of object that belong to the same family.

### Solution

- The first thing the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of the product family. Then you can make all variants of products follow those interfaces.
- The next move is to declare the *Abstract Factory*—an interface with a list of creation methods for all products that are part of the product family. These methods must return **abstract** product types represented by the interfaces we extracted previously.
- For each variant of a product family, we create a separate factory class based on the `AbstractFactory` interface. A factory is a class that returns products of a particular kind.

### Applicability

- Use the Abstract Factory when your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility.
- Consider implementing the Abstract Factory when you have a class with a set of Factory Methods that blur its primary responsibility. In a well-designed program each class is responsible only for one thing. When a class deals with multiple product types, it may be worth extracting its factory methods into a stand-alone factory class or a full-blown Abstract Factory implementation.

### Pros and Cons

✔️ You can be sure that the products you’re getting from a factory are compatible with each other.

✔️ You avoid tight coupling between concrete products and client code.

✔️ *Single Responsibility Principle*. You can extract the product creation code into one place, making the code easier to support.

✔️ *Open/Closed Principle*. You can introduce new variants of products without breaking existing client code.

❌ The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.

### Relations with Others Patterns

- Builder focuses on constructing complex objects step by step. Abstract Factory specializes in creating families of related objects. Abstract Factory returns the product immediately, whereas Builder lets you run some additional construction steps before fetching the product.
- Abstract Factory classes are often based on a set of Factory Methods, but you can also use Prototype to compose the methods on these classes.