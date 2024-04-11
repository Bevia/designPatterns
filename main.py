# Design patterns in Python

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def main():
    # Instantiate the singleton class
    singleton1 = Singleton()
    singleton2 = Singleton()

    # Check if both instances are the same
    print(singleton1 is singleton2)  # Output: True


if __name__ == "__main__":
    main()
