from functions import *
from matplotlib import pyplot as plt, pylab
import sys

#################################
""" run in console example:
python [file] [scheme] [expected_value]
python graph.py "snbinom(3, 1/6, 75)" "enbinom(3, 1/6)"
schemes:
- sbinom(n, p)
- sgeom(p, last)
- snbinom(n, p, last)
- shyper(r, b, n)
- spois(lam, last)
expected_values:
- ebinom(n, p)
- egeom(p)
- enbinom(n, p)
- ehyper(r, b, n)
- epois(lam)
"""

x, y = eval(sys.argv[1]).keys(), eval(sys.argv[1]).values()
exp = eval(sys.argv[2])

#################################

pylab.gcf().canvas.manager.set_window_title("Probability & Statistics")
plt.suptitle("Probability graph")
plt.xlabel("X")
plt.ylabel("Probability")
plt.bar(x, y)
plt.axvline(x=exp, color="#ff0000")
plt.show()
