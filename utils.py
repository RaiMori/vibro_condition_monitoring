from typing import List
import numpy as np
import matplotlib.pyplot as plt

class SineWave:
    def __init__(self, duration: float, sampling_freq: int, amplitude: float, frequency: float) -> None:
        self.duration = duration
        self.sampling_freq = sampling_freq
        self.amplitude = amplitude
        self.freq = frequency

    def generate_wave(self):
        # Calculate the time array
        t = np.linspace(0, self.duration, int(self.duration * self.sampling_freq), endpoint=False)

        # Generate the sine wave
        wave = self.amplitude * np.sin(2 * np.pi * self.freq * t)

        return t, wave


class SignalBuilder:
    def __init__(self) -> None:
        self.__wave = []

    def add_wave(self, wave: SineWave, t=None):
        self.__wave.append(wave)

    def reset(self):
        self.__wave = []

    def build(self):
        nested_waves = []
        time = None
        for w in self.__wave:
            t, wave = w.generate_wave()
            if time is not None:
                time = t
            # if not np.array_equal(time, t):
            #     raise ValueError('Time axes for all signals should be the same') 
            nested_waves.append(wave)
        return t, np.sum(nested_waves, axis=0)


class HarmonicalWave:
    def __init__(self, base_sine_wave: SineWave, amplitudes: List[float]) -> None:
        self.base_sine = base_sine_wave
        self.amplitudes = amplitudes
        self.amplitudes.insert(0, base_sine_wave.amplitude)
        self.duration = base_sine_wave.duration
        self.sampling_freq = base_sine_wave.sampling_freq
        self.freq = base_sine_wave.freq

    @classmethod
    def create_wave(cls, duration: float, sampling_freq: int, amplitude: float, frequency: float, amplitudes: List[float]) -> None:
        base_sine = SineWave(duration, sampling_freq, amplitude, frequency)
        return cls(base_sine, amplitudes)

    def generate_wave(self):
        sine_freq = self.freq
        waves = []
        builder = SignalBuilder()
        for a in self.amplitudes:
            sine = SineWave(self.duration, self.sampling_freq, a, sine_freq)
            sine_freq *= 2
            waves.append(sine.generate_wave())
            builder.add_wave(sine)
        return builder.build()


if __name__=='__main__':
    # Set the parameters
    duration = 5  # Duration of the wave in seconds
    sampling_freq = 44100  # Number of samples per second (standard for audio)
    amplitude = 1  # Amplitude of the wave
    frequency = 3  # Frequency of the wave in Hz

    # Generate the sine wave
    #t, sine = SineWave(duration, sampling_freq, amplitude, frequency).generate_wave()
    t1, harm = HarmonicalWave.create_wave(duration, sampling_freq, amplitude, frequency, [0.5]).generate_wave()

    #Plot the sine wave

    plt.plot(t1, harm)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Sine Wave')
    plt.show()
