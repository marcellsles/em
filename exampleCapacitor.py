import em
import numpy as np

E = em.EField()

for x in np.arange(-12,12,1):
    E.add(x, 3, 1e-9)
    #E.add(x, -3, -1e-9)
E.plot("vector")
E.show()
E.clear()

for x in np.arange(-12,12,1):
    #E.add(x, 3, 1e-9)
    E.add(x, -3, -1e-9)
E.plot("vector")
E.show()
E.clear()


for x in np.arange(-12,12,1):
    E.add(x, 3, 1e-9)
    E.add(x, -3, -1e-9)
E.plot("vector")
E.show()
E.clear()

for x in np.arange(-3,3,1):
    E.add(x, 3, 1e-9)
    E.add(x, -3, -1e-9)
E.plot("vector")
E.show()
E.clear()

for x in np.arange(-2,2,1):
    E.add(x, 3, 1e-9)
    E.add(x, -3, -1e-9)
E.plot("vector")
E.show()
E.clear()

for x in [0]:
    E.add(x, 3, 5e-9)
    E.add(x, -3, -5e-9)
E.plot("vector")
E.show()
E.clear()
