import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import sum_peaks
from scipy.optimize import curve_fit
import os

# for copper:
ka1 = 1.54059
ka2 = 1.54443
ka = ka1
kb = 1.39223

# bragg's law
def theta(n, l, d):
    return np.arcsin(n * l / (2 * d)) / np.pi * 180

# for sapphire:
# https://www.shalomeo.com/Al2O3-Sapphire.html
c = 13.00 # angstrom
def d_hkl(h, k, l):
    return c / np.sqrt(h**2 + k**2 + l**2)

# calculate 2theta for a given h, k, l
def ttheta_hkl(h, k, l, kk=ka1):
    return 2*theta(1, kk, d_hkl(h, k, l))

df = pd.read_csv("data/sapphire_500C.uxd", skiprows = 90, sep = r"\s+", names = ["2Theta", "Counts"])

fig, ax = plt.subplots(figsize = (6, 4))

ax.plot(df["2Theta"], df["Counts"])

ax.set_yscale("log")

sapphire_peaks = [ttheta_hkl(0, 0, 6, ka1), ttheta_hkl(0, 0, 6, ka2)]

for sapphire_peak in sapphire_peaks:
    ax.axvline(sapphire_peak, color = "black", zorder = -1)

ax.set_xlim(41, 42.5)

# crop the data 
sapphire_data = df[(df['2Theta'] > 41) & (df['2Theta'] < 42.5)]

# initial guess
p0 = [41.7, 5e5, 1e-2, 0, 41.8, 3.5e5, 1e-2, 0, 1e3]

# these parameters are defined in utils.py
# basically each peak has a position, amplitude, sigma and eta (mix between gaussian and lorenztian), and then there is a fixed background

popt, pcov = curve_fit(sum_peaks, sapphire_data['2Theta'], sapphire_data['Counts'], p0 = p0)
err = np.sqrt(np.diag(pcov))

params = ["pos 1", "amp 1", "sigma 1", "eta 1",
          "pos 2", "amp 2", "sigma 2", "eta 2",
          "background"]
for i in range(len(popt)):
    print(f"{params[i]}: {round(popt[i], 5)} +- {round(err[i], 5)}")

ax.plot(df['2Theta'], sum_peaks(df['2Theta'], popt[0], popt[1], popt[2], popt[3], popt[4], popt[5], popt[6], popt[7], popt[8]))

deviation = np.mean([popt[0] - ttheta_hkl(0, 0, 6, ka1), popt[4] - ttheta_hkl(0, 0, 6, ka2)])
df["2Theta_corrected"] = df["2Theta"] - deviation

ax.plot(df['2Theta_corrected'], df["Counts"])

ax.set_xlabel("2 $\\Theta$")
ax.set_ylabel("Yield")
fig.tight_layout()

if not os.path.isdir("plots"):
    os.makedirs("plots")
fig.savefig("plots/example.png")

plt.show()