import numpy as np
from scipy.stats import kurtosis, skew


class TsStats:
    "Time Series statistics"

    def __init__(self, raw_data: np.array):
        self.raw_data = raw_data

    def rms(self) -> float:
        return np.math.sqrt(np.mean(self.raw_data**2))

    def peak(self) -> float:
        return np.max(np.abs(self.raw_data))

    def peak_to_peak(self) -> float:
        return np.max(self.raw_data) - np.min(self.raw_data)

    def creat_factor(self) -> float:
        return self.peak() / self.rms()

    def mean(self) -> float:
        return np.mean(self.raw_data)

    def median(self) -> float:
        return np.median(self.raw_data)

    def skewness(self) -> float:
        return skew(self.raw_data)

    def kurtosis(self) -> float:
        return kurtosis(self.raw_data)
