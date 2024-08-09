import math as m
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn as sns
import jsanalysis as my
import csv
import matplotlib.colors
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import scipy.stats as stats
from scipy import odr


fig, ax = plt.subplots(1, figsize = (16,9))
x_plot = np.arange(0, 7.5e14, 7.5e14/1000)
ax.plot(x_plot, 5.81747438e-34*x_plot + 3.99723360e-20, color='darkviolet', label=r'Trendgerade Grundaufbau, Offset $\Delta E\approx 0,4  \cdot 10^{-19}$ J', linewidth=1.5, linestyle="--")

ax.plot(x_plot, 5.99893010e-34*x_plot +  3.64877003e-20, color='darkgreen', label=r'Trendgerade Box mit Färbung, Offset $\Delta E\approx 0,36  \cdot 10^{-19}$ J', linewidth=1.5, linestyle="--")

ax.plot(x_plot, 5.84900247e-34*x_plot + 3.98082886e-20, color='darkorange', label=r'Trendgerade Box mit Papiervorlage, Offset $\Delta E\approx 0,4  \cdot 10^{-19}$ J', linewidth=1.5, linestyle="--")

ax.plot(x_plot, 5.81747438e-34*x_plot + 3.99723360e-20, color='darkred', label=r'Trendgerade Box mit Klebeband, Offset $\Delta E\approx 0,4  \cdot 10^{-19}$ J', linewidth=1.5, linestyle="--")


ax.plot(x_plot,  6.57736475e-34*x_plot + 2.83619017e-21, color='navy', label=r'Trendgerade Ideal, Offset $\Delta E\approx 0,03  \cdot 10^{-19}$ J', linewidth=1.5, linestyle="-")




#ax.plot([], [], label=r'Offset $\Delta E_{Grundaufbau} \approx 0,4  \cdot 10^{-19}$ J', color='darkviolet', linestyle="--")
#ax.plot([], [], label=r'Offset $\Delta E_{Färbung} \approx 0,36  \cdot 10^{-19}$ J', color='darkgreen', linestyle="--")
#ax.plot([], [], label=r'Offset $\Delta E_{Papiervorlage} \approx 0,4  \cdot 10^{-19}$ J', color='darkorange', linestyle="--")
#ax.plot([], [], label=r'Offset $\Delta E_{Klebeband} \approx 0,4  \cdot 10^{-19}$ J', color='darkred', linestyle="--")
#ax.plot([], [], label=r'Offset $\Delta E_{Ideal} \approx 0,4  \cdot 10^{-19}$ J', color='navy', linestyle="-")

plt.ylabel("Energie [J]", fontsize = 20)
plt.xlabel("Frequenz [Hz]", fontsize = 20)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
tx = ax.xaxis.get_offset_text()
tx.set_size(20)
ty = ax.yaxis.get_offset_text()
ty.set_size(20)
plt.ylim([-0.1e-19, 5.2e-19])
ax.legend(fontsize = 20)
plt.legend(fontsize=15)
plt.tight_layout()
plt.grid()
plt.savefig("testtesttest.png")
