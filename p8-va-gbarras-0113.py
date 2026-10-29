import numpy as np
import matplotlib.pyplot as plt

disax=["lun","mar","mie","jue","vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(disax,califa_va_y)
plt.title("califas en vs con Santiago Pacheco NC 0113")
plt.xlabel("dias de la semana habil")
plt.ylabel("calificaciones en VA")
plt.grid()
plt.show()