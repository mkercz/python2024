# This script plots sin(x), cos(x), and exp(-x) in a range [0,10] in one figure.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)

plt.plot(x, np.sin(x), "r-", label="sin(x)")
plt.plot(x, np.cos(x), "g--", label="cos(x)")
plt.plot(x, np.exp(-x), "b:", label="exp(-x)")

plt.legend()
plt.show()
