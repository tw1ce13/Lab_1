import numpy as np
import random as rnd

print(np.sum(np.arange(0, 1000000)))
print(np.average(np.arange(0,1000000)))
print(np.average(np.arange(0, 1000000, rnd.randint(0, 1000000))))
print(np.prod(np.arange(1, 1000000, rnd.randint(1, 1000000))))
