import h5py
import numpy as np
from matplotlib import pyplot as plt

# Open stats file
fileA2 = h5py.File("H:/Courses/CSCE614/casim/zsim/outputs/hw2/A2/blackscholes_8c_simsmall/zsim.h5", "r")
fileA3 = h5py.File("H:/Courses/CSCE614/casim/zsim/outputs/hw2/A3/blackscholes_8c_simsmall/zsim.h5", "r")

# Get the single dataset in the file

A2stats = fileA2["stats"]
A3stats = fileA3["stats"]
A2root = A2stats["root"]
A3root = A3stats["root"]
A2core = A2root["westmere"]
A3core = A3root["westmere"]
A2mispred = A2core["mispredBranches"]

print(A2mispred)
A3mispred = np.array(A3core["mispredBranches"],dtype=float)
#A2condBran=A2core["condBranches"]
A3condBran=np.array(A3core["condBranches"],dtype=float)
#A2misrate=float(A2mispred)/A2condBran
A3misrate=(A3mispred[3])/A3condBran[3]

A3predacc=1-A3misrate
print(A3predacc)
plt.plot(A3predacc,'rx-')
plt.show()
#
# plt.bar(range(len(A2mispred[3])),A2mispred[3],color="blue")
# plt.hold(True)
# plt.figure(2)
# plt.bar(range(len(A3mispred[3])),A3mispred[3],color="red",width=0.5)
# plt.show()