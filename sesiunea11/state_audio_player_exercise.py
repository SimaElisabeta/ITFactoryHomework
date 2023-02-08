from __future__ import annotations
from abc import ABC, abstractmethod


# REAL LIFE example - exercise 1
class AudioPlayerContext:
    def __init__(self, state: State):
        self.transition_to(state)

    def transition_to(self, state: State):
        self._state = state
        self._state.context = self

    def audio_play(self):
        self._state.audio_play()

    def audio_pause(self):
        self._state.audio_pause()

    def audio_stop(self):
        self._state.audio_stop()

    def audio_next(self):
        self._state.audio_next()

    def audio_previous(self):
        self._state.audio_previous()


class State(ABC):
    @property
    def context(self) -> AudioPlayerContext:
        return self._context

    @context.setter
    def context(self, context: AudioPlayerContext):
        self._context = context

    @abstractmethod
    def audio_play(self):
        pass

    @abstractmethod
    def audio_pause(self):
        pass

    @abstractmethod
    def audio_stop(self):
        pass

    @abstractmethod
    def audio_next(self):
        pass

    @abstractmethod
    def audio_previous(self):
        pass


class AudioPlay(State):
    def audio_play(self):
        print('Audio already playing!')

    def audio_pause(self):
        print('Audio paused!')
        self.context.transition_to(AudioPaused())

    def audio_stop(self):
        print('Audio stopped!')
        self.context.transition_to(AudioStopped())

    def audio_next(self):
        print('Audio playing next song!')
        self.context.transition_to(AudioNext())

    def audio_previous(self):
        print('Audio playing previous song!')
        self.context.transition_to(AudioPrevious())


class AudioPaused(State):
    def audio_play(self):
        print('Audio playing!')
        self.context.transition_to(AudioPlay())

    def audio_pause(self):
        print('Audio already paused!')

    def audio_stop(self):
        print('Audio stopped!')
        self.context.transition_to(AudioStopped())

    def audio_next(self):
        print('Audio playing next song!')
        self.context.transition_to(AudioNext())

    def audio_previous(self):
        print('Audio playing previous song!')


class AudioStopped(State):
    def audio_play(self):
        print('Audio playing!')
        self.context.transition_to(AudioPlay())

    def audio_pause(self):
        print("Can't pause the audio, the music is stopped already!")

    def audio_stop(self):
        print('Audio already stopped!')

    def audio_next(self):
        print("Can't play next audio, the music is stopped already!")

    def audio_previous(self):
        print("Can't play previous audio, the music is stopped already!")


class AudioNext(State):
    def audio_play(self):
        print('Audio already playing!')

    def audio_pause(self):
        print('Audio paused!')
        self.context.transition_to(AudioPaused())

    def audio_stop(self):
        print('Audio stopped!')
        self.context.transition_to(AudioStopped())

    def audio_next(self):
        print('Audio playing next song!')
        self.context.transition_to(AudioNext())

    def audio_previous(self):
        print('Audio playing previous song!')
        self.context.transition_to(AudioPrevious())


class AudioPrevious(State):
    def audio_play(self):
        print('Audio already playing!')

    def audio_pause(self):
        print('Audio paused!')
        self.context.transition_to(AudioPaused())

    def audio_stop(self):
        print('Audio stopped!')
        self.context.transition_to(AudioStopped())

    def audio_next(self):
        print('Audio playing next song!')
        self.context.transition_to(AudioNext())

    def audio_previous(self):
        print('Audio playing previous song!')
        self.context.transition_to(AudioPrevious())


walkman = AudioPlayerContext(AudioPlay())
walkman.audio_stop()
walkman.audio_next()
walkman.audio_stop()
walkman.audio_play()
walkman.audio_previous()
walkman.audio_play()
walkman.audio_next()
walkman.audio_pause()
walkman.audio_pause()
walkman.audio_play()

walkman.audio_stop()
walkman.audio_stop()
walkman.audio_next()
walkman.audio_previous()
walkman.audio_pause()
