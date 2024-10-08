import matplotlib.pyplot as plt #pip install matplotlib
import numpy as np
import pandas as pd #pip install pandas

'''Barchart example'''


labels = ['A', 'B', 'C']
values = [1,4,2]

plt.figure(figsize=(5,3), dpi=800)

bars = plt.bar(labels, values)

patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.savefig('barchart.png', dpi=300)

plt.show()


