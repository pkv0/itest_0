import matplotlib.pyplot as plt
import numpy as np

data = np.random.default_rng(19680801)

n_points = 10000
n_bins = 20

d1 = data.standard_nornal(n_points)
d2 = 0.5 * data.standard_nornal(n_points)+5

fig, ax = plt.subplots(1,2)
