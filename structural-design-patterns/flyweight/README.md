## Flyweight

### Intent

- **Flyweight** is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.

### Problem

- An object containing plenty of data. When an application needs to create a large number of similar objects, it consumes excessive memory. However, the data for many of these objects often contains identical, redundant information.

### Solution

- **Separating state:** Distinguishes between _intrinsic_ state (common, shared, and immutable data, stored in the flyweight object itself) and _extrinsic_ state (unique to each specific context and passed in as a parameter to methods). The Flyweight pattern suggests that we stop storing the extrinsic state inside the object. Instead, we should pass this state to specific methods which rely on it. Only the intrinsic state stays within the object, letting we reuse it in different contexts.
- **Sharing objects:** Reuses existing flyweight objects (which only contain intrinsic state) instead of creating new, full-sized objects every time. For more convenient access to various flyweights, we can create a factory method that manages a pool of existing flyweight objects. The method accepts the intrinsic state of the desired flyweight from a client, looks for an existing flyweight object matching this state, and returns it if it was found. If not, it creates a new flyweight and adds it to the pool.

### Applicability

- Use the Flyweight pattern only when:
  - The program must support a huge number of _**similar objects**_ which barely fit into available RAM.
  - The objects contain duplicate states which can be extracted and shared between multiple objects.

### Pros and Cons

✔️You can save lots of RAM, assuming your program has tons of similar objects.

❌You might be trading RAM over CPU cycles when some of the context data needs to be recalculated each time somebody calls a flyweight method.

❌The code becomes much more complicated. New team members will always be wondering why the state of an entity was separated in such a way.

### Relations with Other Patterns

- You can implement shared leaf nodes of the Composite tree as Flyweights to save some RAM.
- Flyweight shows how to make lots of little objects, whereas Facade shows how to make a single object that represents an entire subsystem.
- Flyweight would resemble Singleton if you somehow managed to reduce all shared states of the objects to just one flyweight object. But there are two fundamental differences between these patterns:
  - There should be only one Singleton instance, whereas a Flyweight class can have multiple instances with different intrinsic states.
  - The Singleton object can be mutable. Flyweight objects are immutable.
