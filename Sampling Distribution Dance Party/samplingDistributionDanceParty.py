from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


spotify_data = pd.read_csv("spotify_data.csv")
print(spotify_data.head())
song_tempos = spotify_data['tempo']
population_distribution(song_tempos)
sampling_distribution(song_tempos, 30, "Mean")
sampling_distribution(song_tempos, 30, "Minimum")
sampling_distribution(song_tempos, 30, "Variance")
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)
standard_error = population_std/(30**.5)
print(stats.norm.cdf(140, population_mean, standard_error))
print(1-stats.norm.cdf(150, population_mean, standard_error))
