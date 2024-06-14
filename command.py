from abc import ABC, abstractmethod


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
