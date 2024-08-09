import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn as sns
from scipy import odr
import jsanalysis as my

clist = ["#4d0000",
         "#b80000",
         "#ff0000",
         "#ff0000",
         "#ff6a00",
         "#ffe400",
         "#b3ff00",
         "#57ff00",
         "#04ff00",
         "#00ffff",
         "#009eff",
         "#0042ff", 
         "#1100ff",
         "#5500ff",
         "#6d00c1",
         "#680082",
         "#4d004d"]
norm = plt.Normalize(3.84e+14,7.89e+14)
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", clist)

c = 2.998e+8
e = 1.602e-19

# Einlesen der Daten
df = pd.read_csv('C:/Users/pierr/Desktop/Uni/Python/perfekt.CSV', delimiter=';', decimal=',')


# Wert für die Regression aufbereiten
x = np.array(df["Frequenz (gemessen) [Hz]"])
y = np.array(df["Energie [J]"])
a= np.array(df["Frequenz (gemessen) [Hz]"]).reshape((-1,1))
b= np.array(df["Energie [J]"]).reshape((-1,1))
u_x = np.array(df["Unsicherheit_Frequenz- (gemessen) [Hz]"])
u_y = np.array(df["Unsicherheit_Energie [J]"])


# Regression
def lin_func(B, nu):
    
    return B[0]*nu + B[1]
odr_Data = odr.RealData(x, y, sx = u_x, sy = u_y)
odr_Model = odr.Model(lin_func)
odr_Setup = odr.ODR(odr_Data, odr_Model, beta0 = [6e-34, 1e-19])
odr_out = odr_Setup.run()
print(odr_out.beta, odr_out.sd_beta)
b_hut = odr_out.beta[0]
a_hut = odr_out.beta[1]
u_b = odr_out.sd_beta[0]

# Visualisierung

fig, ax = plt.subplots(1, figsize = (16,9))
sns.scatterplot(data=df, x="Frequenz (gemessen) [Hz]", y="Energie [J]", hue="Wellenlange [nm]", palette="nipy_spectral",s=140)
ax.errorbar(x=df["Frequenz (gemessen) [Hz]"], y=df["Energie [J]"], 
             xerr=[df["Unsicherheit_Frequenz- (gemessen) [Hz]"], df["Unsicherheit_Frequenz+ (gemessen) [Hz]"]],
             yerr=[df["Unsicherheit_Energie [J]"], df["Unsicherheit_Energie [J]"]],
             fmt=' ', capsize=5, color = "black")
plt.ylabel("Energie [J]", fontsize = 20)
plt.xlabel("Frequenz [Hz]", fontsize = 20)

ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
tx = ax.xaxis.get_offset_text()
tx.set_size(20)
ty = ax.yaxis.get_offset_text()
ty.set_size(20)
plt.ylim([-0.1e-19, 5.2e-19])

x_plot = np.arange(0, x.max(), x.max()/1000)
ax.plot(x_plot, b_hut*x_plot + a_hut, color = "blue", label="Trend", linewidth=3)


b_array = my.sciround(u_b*10e33, b_hut*10e33)


plt.legend(fontsize=20)

final_text= r"$h = \frac{\partial E}{\partial f} = (" + f"{b_array[1]:.{b_array[2]}f}" + r"\pm"  + f"{b_array[0]:.{b_array[2]}f}" + r")\cdot 10^{-34}$ Js" 
plt.text(0.6, 0.15, final_text, transform=ax.transAxes,
         fontsize=20, verticalalignment='top', horizontalalignment='left', color = "black", bbox=dict(boxstyle='round,pad=0.5', edgecolor='black', facecolor='white'))


plt.tight_layout()
plt.grid()
plt.savefig("perfekt_diss.png")




