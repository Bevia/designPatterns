
# The Strategy pattern is a behavioral design pattern that allows you to define a family
# of algorithms, encapsulate each one of them, and make them interchangeable. It enables
# the client code to choose an algorithm at runtime without modifying the context class
# that uses the algorithm.

class Strategy:
    def execute(self):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing strategy A")


class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing strategy B")


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()


# Example usage
strategy_a = ConcreteStrategyA()
strategy_b = ConcreteStrategyB()

context = Context(strategy_a)
context.execute_strategy()  # Output: Executing strategy A

context.set_strategy(strategy_b)
context.execute_strategy()  # Output: Executing strategy B
