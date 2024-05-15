# The Facade design pattern is a structural pattern that provides a simplified
# interface to a complex system of classes, library, or framework. It hides the complexities
# of the system and provides an interface to the client through which the client can access the system.
# This pattern involves a single class which provides simplified methods required by client
# and delegates calls to methods of existing system classes.
#
# Below is a simplistic implementation of the Facade pattern in Python, demonstrating it
# with a fictional home theater system:

class Amplifier:
    def on(self):
        print("Amplifier on")

    def set_volume(self, level):
        print(f"Setting volume to {level}")

    def off(self):
        print("Amplifier off")


class Tuner:
    def on(self):
        print("Tuner on")

    def set_am(self):
        print("Setting AM mode")

    def set_fm(self):
        print("Setting FM mode")

    def off(self):
        print("Tuner off")


class DvdPlayer:
    def on(self):
        print("DVD Player on")

    def play(self, movie):
        print(f"Playing \"{movie}\"")

    def stop(self):
        print("Stopping DVD")

    def eject(self):
        print("Ejecting DVD")

    def off(self):
        print("DVD Player off")


class HomeTheaterFacade:
    def __init__(self, amplifier, tuner, dvd_player):
        self.amplifier = amplifier
        self.tuner = tuner
        self.dvd_player = dvd_player

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.dvd_player.stop()
        self.dvd_player.eject()
        self.dvd_player.off()
        self.amplifier.off()


# Usage
if __name__ == "__main__":
    amp = Amplifier()
    tuner = Tuner()
    dvd = DvdPlayer()
    home_theater = HomeTheaterFacade(amp, tuner, dvd)

    home_theater.watch_movie("Raiders of the Lost Ark")
    print("\n")
    home_theater.end_movie()

# In this example, `HomeTheaterFacade` provides two simplified methods `watch_movie`
# and `end_movie` to the client, hiding the complexities of the subsystems (`Amplifier`, `Tuner`,
# and `DvdPlayer`). The client does not need to know about the internals of the subsystems to use the home theater;
# it interacts only with the `HomeTheaterFacade`.
