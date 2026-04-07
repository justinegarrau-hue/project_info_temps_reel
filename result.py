import os 
import numpy as np
import matplotlib.pyplot as plt

time = []
open("output.txt","w").close()
for i in range(100):
	os.system("/usr/bin/time -f '%e' ./multip 2>>output.txt")

with open("output.txt", "r", encoding="utf-8") as file:
	for line in file:
		valeur = line.strip()
		time.append(float(valeur))

Q1,Q2,Q3 = np.quantile(time, [0.25, 0.5, 0.75])
print(f"min: {np.min(time)}s")
print(f"Q1 (25%) : {Q1}s")
print(f"Médiane (50%) : {Q2}s")
print(f"Q3 (75%) : {Q3}s")
print(f"max: {np.max(time)}s")
print(f"WCET:{np.max(time)*1.2}s")

plt.hist(time)
plt.show()
