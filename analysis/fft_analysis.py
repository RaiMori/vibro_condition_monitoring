import numpy as np
import scipy
from scipy import fftpack
from scipy.io.

class FFTVibrationAnalysis:

    def __init__(self, fft_signal, fs):
        self.fft = fft_signal
        self.fs = fs

    def fft_peak_val(self, freq):
        find_peaks()

    def fft_harmonics_val(self, freq, num):
        freqs_list = [f*(num+1) for f in range(num)]
        harmonics = []
        for h in freqs_list:
            harm_val = self.fft_peak_val(h)
            harmonics.append((h, harm_val))
        return harmonics

    def fft_freq_band(self, lower, upper):
        pass

    def fft_freq_bands(self, lower_freqs, upper_freqs):
        if len(upper_freqs) != len(lower_freqs):
            raise ValueError('Length of upper and lower frequencies should be equal')
        freq_bands = []
        for low, upp in zip(lower_freqs, upper_freqs):
            if low >= upp:
                raise ValueError('Lower frequency is hogher or equal than upper frequency')
            freq_band_value = self.fft_freq_band(low, upp)
            freq_bands.append((low, upp, freq_band_value))
        return freq_bands

    def get_octave_bands(self):
        pass
