import numpy as np
import scipy as sp
from time_series_analysis import TsStats
from fft_analysis import FFTAnalysis

class VibrationSignalAnalysis(TsStats, FFTAnalysis):
    def __init__(self, raw_data):
        super('TsStats').__init__(raw_data)
        super('FFTAnalysis')

    def _read_config(self):
        self.config = None

    def calculate_params(self):
        for p in self.config:
            self.__getattribute__(p)