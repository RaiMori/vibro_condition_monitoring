import numpy as np
from scipy.stats import kurtosis, skew


class TsStats:
    "Time Series statistics"

    def __init__(self, raw_data):
        self.raw_data = raw_data

    def get_rms(self):
        return np.math.sqrt(np.mean(self.raw_data**2))

    def get_peak(self):
        return np.max(np.abs(self.raw_data))

    def get_peak_to_peak(self):
        return np.max(self.raw_data) - np.min(self.raw_data)

    def get_mean(self):
        return np.mean(self.raw_data)

    def get_median(self):
        return np.median(self.raw_data)

    def get_skewness(self):
        return skew(self.raw_data)

    def get_kurtisis(self):
        return kurtosis(self.raw_data)