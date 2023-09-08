import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
#x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

# plot
fig, ax = plt.subplots()

ax.stem( y)

plt.show()
