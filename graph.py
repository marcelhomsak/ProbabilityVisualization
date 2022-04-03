from functions import *
from matplotlib import pyplot as plt, pylab
import sys
import mplcursors as mpc

#################################
""" run in console example:

python file scheme [expected_value]

python graph.py "snbinom(3, 1/6, last=75)" "enbinom(3, 1/6)"

schemes:
- sbinom(n, p)
- sgeom(p, to=50)
- snbinom(n, p, to=50)
- shyper(r, b, n)
- spois(lam, to=50)

expected_values:
- ebinom(n, p)
- egeom(p)
- enbinom(n, p)
- ehyper(r, b, n)
- epois(lam)
"""

# evaluate program arguments
x, y = eval(sys.argv[1]).keys(), eval(sys.argv[1]).values()

#################################

# label names
pylab.gcf().canvas.manager.set_window_title("Probability & Statistics")
plt.suptitle("Probability graph")
plt.xlabel("X")
plt.ylabel("Probability")

# plot bar graph given first argument's distribution scheme
plt.bar(x, y)

# if the third (optional) argument for expected value is given, draw it
if len(sys.argv) == 3:
    plt.axvline(x=eval(sys.argv[2]), color="#ff0000")

# format x axis value as integer as it is discrete distribution
plt.gca().format_coord = lambda x, y: f"X=%d, Probability=%.4f" % (round(x), y)
# on mouse hover display value
mpc.cursor(hover=True)

plt.show()