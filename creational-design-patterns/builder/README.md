## Builder

### Intent

- Builder is a creational design pattern that lets you construct complex objects step by step.
- The pattern allows you to produce different types and representations of an object using the same construction code.

### Problems

The Builder Pattern tries to solve:

- How can a class create different representations of a complex object?
- How can a class that includes creating a complex object be simplified?

### Solution

- The Builder pattern suggests that you extract the object construction code out of its own class and move it to separate objects called ***builders.***
- The pattern organizes object construction into a set of steps.  You can call only those steps that are necessary for producing a particular configuration of an object.
- The Builder and Factory patterns are very similar in the fact they both instantiate new objects at runtime. The difference is when the process of creating the object is more complex, so rather than the Factory returning a new instance of ObjectA, it calls the builders' director constructor method ObjectA.construct() that goes through a more complex construction process involving several steps. Both return an Object/Product.

### Applicability

- Use the Builder pattern to get rid of a “telescoping constructor”.  Say you have a constructor with ten optional parameters. Calling such a beast is very inconvenient; therefore, you overload the constructor and create several shorter versions with fewer parameters. These constructors still refer to the main one, passing some default values into any omitted parameters.
- Use the Builder pattern when you want your code to be able to create different representations of some product. The Builder pattern can be applied when construction of various representations of the product involves similar steps that differ only in the details. The base builder interface defines all possible construction steps, and concrete builders implement these steps to construct particular representations of the product. Meanwhile, the director class guides the order of construction.
- Use the Builder to construct Composite trees or other complex objects. The Builder pattern lets you construct products step-by-step. You can even call steps recursively, which comes in handy when you need to build an object tree.

### Pros and Cons

✔️ You can construct objects step-by-step, defer construction steps or run steps recursively.

✔️ You can reuse the same construction code when building various representations of products.

✔️ *Single Responsibility Principle*. You can isolate complex construction code from the business logic of the product.

❌ The overall complexity of the code increases since the pattern requires creating multiple new classes.