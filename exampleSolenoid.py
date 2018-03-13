import em
import numpy as np

field = em.BField()

for i in np.arange(-5,5,1):
    field.add(i, 4, .2)
    field.add(i, -4, -.2)

field.plot("lines")
field.plot("vector")
field.show()
