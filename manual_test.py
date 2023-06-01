import sys
from utils import SineWave, HarmonicalWave
from analysis.time_series_analysis import TsStats
#from ..analysis.vibration_signal import VibrationSignalAnalysis
import sys


if __name__=='__main__':
    # Set the parameters
    duration = 5  # Duration of the wave in seconds
    sampling_freq = 44100  # Number of samples per second (standard for audio)
    amplitude = 1  # Amplitude of the wave
    frequency = 3  # Frequency of the wave in Hz

    # Generate the sine wave
    t, sine = SineWave(duration, sampling_freq, amplitude, frequency).generate_wave()
    t1, harm = HarmonicalWave.create_wave(duration, sampling_freq, amplitude, frequency, [0.5]).generate_wave()

    ts = TsStats(sine)
    print(ts)
