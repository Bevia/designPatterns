# This example includes:
# a `Product` class, which is the complex object being built;
# a `Builder` class, with methods to construct and assemble parts of the product;
# a `ConcreteBuilder` class, which implements the building steps defined in the `Builder` interface;
# and a `Director` class, which controls the construction process.
# The `Director` calls the building steps in a specific sequence to construct different representations of the product.

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Builder:
    def __init__(self):
        self.product = Product()

    def reset(self):
        self.product = Product()

    def produce_part_a(self):
        pass

    def produce_part_b(self):
        pass

    def produce_part_c(self):
        pass

    def get_result(self):
        return self.product


class ConcreteBuilder(Builder):
    def produce_part_a(self):
        self.product.add("PartA")

    def produce_part_b(self):
        self.product.add("PartB")

    def produce_part_c(self):
        self.product.add("PartC")


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_minimal_viable_product(self):
        self.builder.produce_part_a()

    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


# Usage
if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder()
    director.set_builder(builder)

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.get_result().list_parts()

    print("\n\nStandard full featured product: ")
    builder.reset()
    director.build_full_featured_product()
    builder.get_result().list_parts()
