import em
import numpy as np

E = em.EField()

for x in np.arange(0,6.28,0.1):
    E.add(8*np.cos(x), 8*np.sin(x), 0.1*1e-9)

for x in np.arange(4,5.6,0.1):
    if x<4.8:
        E.add(5*np.cos(x), 5*np.sin(x), -0.1*1e-9)
    else:
        E.add(5*np.cos(x), 5*np.sin(x), 0.1*1e-9)

E.add(-3,2,1e-9)
E.add(3,2,-1e-9)

E.plot("vector")
E.show()
E.clear()
