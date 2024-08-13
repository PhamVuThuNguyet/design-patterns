### Intent

- **Bridge** is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

### Problem

- Adding new dimensions to the Abstract hierarchy will grow it exponentially

### Solution

- The Bridge pattern attempts to solve this problem by switching from inheritance to the object composition. What this means is that you extract one of the dimensions into a separate class hierarchy, so that the original classes will reference an object of the new hierarchy, instead of having all of its state and behaviors within one class.
- **ABSTRATION and IMPLEMENTATION**
    - *Abstraction* (also called *interface*) is a high-level control layer for some entity. This layer isn’t supposed to do any real work on its own. It should delegate the work to the *implementation* layer (also called *platform*).
    - When talking about real applications, the abstraction can be represented by a graphical user interface (GUI), and the implementation could be the underlying operating system code (API) which the GUI layer calls in response to user interactions.

### Applicability

- Use the Bridge pattern ***when you want to divide and organize a monolithic class that has several variants of some functionality*** (for example, if the class can work with various database servers).
- Use the pattern ***when you need to extend a class in several orthogonal (independent) dimensions***. The Bridge suggests that you extract a separate class hierarchy for each of the dimensions. The original class delegates the related work to the objects belonging to those hierarchies instead of doing everything on its own.
- Use the Bridge ***if you need to be able to switch implementations at runtime***. Although it’s optional, the Bridge pattern lets you replace the implementation object inside the abstraction. It’s as easy as assigning a new value to a field.

### Pros and Cons

✔️ You can create platform-independent classes and apps.

✔️ The client code works with high-level abstractions. It isn’t exposed to the platform details.

✔️ *Open/Closed Principle*. You can introduce new abstractions and implementations independently from each other.

✔️ *Single Responsibility Principle*. You can focus on high-level logic in the abstraction and on platform details in the implementation.

❌ You might make the code more complicated by applying the pattern to a highly cohesive class.

### Relation with Other Patterns

- You can use Abstract Factory along with Bridge. This pairing is useful when some abstractions defined by Bridge can only work with specific implementations. In this case, Abstract Factory can encapsulate these relations and hide the complexity from the client code.