from abc import ABC, abstractmethod

Explanation:

# 1. **Command Interface**: The `Command` interface defines a method for executing an operation, typically named `execute()`.
#
# 2. **Receiver**: The `Light` class is the receiver object, which contains the actual implementation for performing operations
# such as turning the light on or off.
#
# 3. **Concrete Commands**: `LightOnCommand` and `LightOffCommand` are concrete classes that implement the `Command` interface.
# These classes encapsulate the `Light` receiver and specify the actions to turn the light on or off.
#
# 4. **Invoker**: The `RemoteControl` class acts as the invoker. It is responsible for triggering the execution of commands
# through the `execute()` method. It maintains a collection of commands in a `commands` dictionary and
# can execute a command based on its name.
#
# 5. **Client Code**:
#     - An instance of `Light` (e.g., `living_room_light`) is created.
#     - Instances of concrete commands (`LightOnCommand` and `LightOffCommand`) are created, each taking the `living_room_light` as a receiver.
#     - The commands are registered with an instance of `RemoteControl` (`remote_control`) using unique command names.
#     - Commands are executed by calling `remote_control.execute(command_name)`.
#
# When the client code is executed, it demonstrates the Command pattern in action. This pattern decouples the sender of
# a request (the invoker) from the receiver (the receiver), providing greater flexibility and extensibility in handling various requests.

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Receiver class
class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")


# Concrete command classes
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


# Invoker class
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def register(self, command_name, command):
        self.commands[command_name] = command

    def execute(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"Command '{command_name}' not found")


# Client code
if __name__ == "__main__":
    # Receiver
    living_room_light = Light()

    # Concrete commands
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    # Invoker
    remote_control = RemoteControl()

    # Register commands with the invoker
    remote_control.register("on", living_room_light_on)
    remote_control.register("off", living_room_light_off)

    # Execute commands
    remote_control.execute("on")
    remote_control.execute("off")
    remote_control.execute("undo")  # Command not found
