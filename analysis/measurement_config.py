config = {'ts': [
    'rms',
    'peak',
    'peak-to-peak',
    'skewness',
    'kurtosis'

],
    'fft': [
    {'freq_peaks': [10, 50, 80, 100]},
    {'harmonics': [{'base_freq': 50, 'harmonics_num': 5},
                   {'base_freq': 75, 'harmonis_num': 3}]},
    {'freq_bands': [{'lower': 5, 'upper':45}, {'lower': 45, 'upper': 80}]}
]
}

cfg = {}
cfg_ts = ['rms', 'peak', 'peak_to_peak', 'skewness', 'kurtosis']
cfg_fft_freq_peaks = {}