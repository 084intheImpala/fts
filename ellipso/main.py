import pandas as pd
import matplotlib.pyplot as plt
import os

ga2o3_nk = pd.read_csv("data/ga2o3_nk.csv", skiprows = 3, names = ["wl n", "n", "wl k", "k", "x nodes", "nodes"])
sio2_nk = pd.read_csv("data/sio2_nk.csv", skiprows = 3, names = ["wl n", "n", "wl k", "k", "x nodes", "nodes"])

ga2o3_psi = pd.read_csv("data/ga2o3_psi.csv", skiprows = 2)
ga2o3_delta = pd.read_csv("data/ga2o3_psi.csv", skiprows = 2)

sio2_psi = pd.read_csv("data/sio2_psi.csv", skiprows = 2)
sio2_delta = pd.read_csv("data/sio2_psi.csv", skiprows = 2)

fig, ax = plt.subplots(figsize = (6, 4))

ax.plot(ga2o3_nk["wl n"], ga2o3_nk["n"], label = "Ga$_2$O$_3$")
ax.plot(sio2_nk["wl n"], sio2_nk["n"], label = "SiO$_2$")

ax.set_xlabel("Wavelength $\lambda$ [nm]")
ax.set_ylabel("Refractive index $n$")

fig.tight_layout()
fig.legend(loc = (0.75, 0.75))

if not os.path.isdir("plots"):
    os.makedirs("plots")
fig.savefig("plots/example.png")

plt.show()

# next steps:

# plot the psi+delta data and fits
# plot the extinction coefficient k
# if you are interested in saving space, you can plot the ks in the same plot as the ns:
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html#sphx-glr-gallery-subplots-axes-and-figures-two-scales-py
# the sio2 fits are not as interesting or important as the ga2o3 ones, so to save space, you can just show the ga2o3 psi-deltas, and put the sio2 ones as an appendix. if you *really* have to save space, one double axes plot showing the psi+delta at 75 degrees for ga2o3 is okay, as the most important is to mention how the fits are done, and (briefly) what the model coefficients mean