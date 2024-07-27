## Prototype (a.k.a Clone)

### Intent

- **Prototype** is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

### Problems

Say you have an object, and you want to create an exact copy of it. How would you do it? First, you have to create a new object of the same class. Then you have to go through all the fields of the original object and copy their values over to the new object. But there’s a catch. 

- Not all objects can be copied that way because some of the object’s fields may be private and not visible from outside of the object itself.
- Since you have to know the object’s class to create a duplicate, your code becomes dependent on that class.
- Sometimes you only know the interface that the object follows, but not its concrete class, when, for example, a parameter in a method accepts any objects that follow some interface.

### Solution

- The Prototype pattern delegates the cloning process to the actual objects that are being cloned. The pattern declares a common interface for all objects that support cloning. Usually, such an interface contains just a single `clone` method.
- This method simply creates an object of the current class and carries over all of the field values of the old object into the new one.
- An object that supports cloning is called a ***prototype*.**

### Applicability

- Use the Prototype pattern when your code shouldn’t depend on the concrete classes of objects that you need to copy. This happens a lot when your code works with objects passed to you from 3rd-party code via some interface. The concrete classes of these objects are unknown, and you couldn’t depend on them even if you wanted to.
- Use the pattern when you want to reduce the number of subclasses that only differ in the way they initialize their respective objects. Suppose you have a complex class that requires a laborious configuration before it can be used. There are several common ways to configure this class, and this code is scattered through your app. To reduce the duplication, you create several subclasses and put every common configuration code into their constructors. You solved the duplication problem, but now you have lots of dummy subclasses. The Prototype pattern lets you use a set of pre-built objects configured in various ways as prototypes. Instead of instantiating a subclass that matches some configuration, the client can simply look for an appropriate prototype and clone it.

### Pros and Cons

✔️ You can clone objects without coupling to their concrete classes.

✔️ You can get rid of repeated initialization code in favor of cloning pre-built prototypes.

✔️ You can produce complex objects more conveniently.

✔️ You get an alternative to inheritance when dealing with configuration presets for complex objects.

❌ Cloning complex objects that have circular references might be very tricky.

### Relations with Other Patterns

- Prototypes can be implemented as Singletons.