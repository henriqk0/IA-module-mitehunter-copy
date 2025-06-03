## DOO 1 - Padrões Criativos

Builder and factory patterns have been implemented in this module. This allows the code to be divided into methods and classes with unique responsibilities and low coupling, compared to the single class responsible for the entire operation of each AI. 

At first, the `ModelFactory` factory has methods for `ultralytics` image recognition AIs, and is compatible with any AI of the same purpose provided by it, through an interface common to all of them.

The `ModelFactory` plays a key role in abstracting the instantiation of AI models. By centralizing creation logic, it allows the code to remain flexible and scalable—new models can be integrated easily without changing the core logic. Through a shared interface, the factory enables consistent interaction with any compatible model (e.g., loading, inference), ensuring that calling code doesn’t need to know specific implementation details. This promotes loose coupling and enhances code reusability.

On the other hand, the builder pattern helps to organize the process of building complex classes by dividing it into distinct stages. This makes the code more maintainable and testable, as each stage can be debugged individually. It also allows you to create different representations of the same class structure without modifying the build logic. In general, the builder improves readability, simplifies the creation of objects and makes it easier to extend or troubleshoot the system, as is evident in `AIRunnerData` (while hiding the values parameterized by the AI from the rest of the code, although it is not itself built by a separate class, which would characterize a standard builder) which is in line with SOLID's principle of single responsibility and decoupling of code.
