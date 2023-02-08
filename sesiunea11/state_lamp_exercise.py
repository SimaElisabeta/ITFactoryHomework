from __future__ import annotations
from abc import ABC, abstractmethod


# REAL LIFE example - exercise 2
class Lamp:
    _state = None
    lamp_on = None
    lamp_off = None

    def __init__(self, name):
        self.name = name

        self.lamp_on = LampOn()
        self.lamp_on.context_lamp = self

        self.lamp_off = LampOff()
        self.lamp_off.context_lamp = self

        self._state = self.lamp_off

    def set_state(self, state: State):
        self._state = state

    def turn_on(self):
        self._state.turn_on()

    def turn_off(self):
        self._state.turn_off()

    def print_light_state(self):
        print(f"Current lamp {self.name} state is: {type(self._state).__name__}")


class State(ABC):
    context_lamp = None

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LampOn(State):
    def turn_on(self):
        print(f'Lamp {self.context_lamp.name} is already on!')

    def turn_off(self):
        self.context_lamp.set_state(self.context_lamp.lamp_off)


class LampOff(State):
    def turn_on(self):
        self.context_lamp.set_state(self.context_lamp.lamp_on)

    def turn_off(self):
        print(f'Lamp {self.context_lamp.name} is already off!')


my_lamp1 = Lamp('1')
my_lamp2 = Lamp('2')

my_lamp1.print_light_state()
my_lamp2.print_light_state()

print()
print('Turning the Lamp 1 on:')
my_lamp1.turn_on()

my_lamp1.print_light_state()
my_lamp2.print_light_state()
print()

print('Turning the Lamp 1 on:')
my_lamp1.turn_on()

print()
my_lamp1.turn_off()
my_lamp1.print_light_state()
