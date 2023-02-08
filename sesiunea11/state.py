"""
STATE - is a behavioral design pattern that allows an object to change the behavior when its internal state changes.
* Usage examples: The State pattern is commonly used in Python to convert massive switch-base state machines into objects.
* Identification: State pattern can be recognized by methods that change their behavior depending on the objects state, controlled externally.


PROS:
    * Single Responsibility Principle. Organize the code related to particular states into separate classes.
    * Open/Closed Principle. Introduce new states without changing existing state classes or the context.
    * Simplify the code of the context by eliminating bulky state machine conditionals.
CONS:
    * Applying the pattern can be overkill if a state machine has only a few states or rarely changes.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f'Context: Transition to {type(state).__name__} ')
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


context = Context(ConcreteStateB())
context.request1()
print()
context.request2()


""" REAL LIFE EXAMPLE """