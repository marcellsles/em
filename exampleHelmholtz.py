import em
import numpy as np

field = em.BField()

field.add(-2, 4, 1)
field.add(-2, -4, -1)
field.add(2, 4, 1)
field.add(2, -4, -1)

#field.plot("lines")
field.plot("vector")
field.show()
