import numpy as np
import h5py
import os
from matplotlib import pyplot as plt


A2ben=os.listdir("Z:/Courses/CSCE614/casim/zsim/outputs/hw2/A2/")[0:]

A2benpaths=[]
for i in range(len(A2ben)):
	A2benpaths.append("Z:/Courses/CSCE614/casim/zsim/outputs/hw2/A2/"+str(A2ben[i])+"/zsim.h5")
	
A3ben=os.listdir("Z:/Courses/CSCE614/casim/zsim/outputs/hw2/A3/")[0:]
for val in A3ben:
	print val
A3benpaths=[]
for i in range(len(A3ben)):
	A3benpaths.append("Z:/Courses/CSCE614/casim/zsim/outputs/hw2/A3/"+str(A3ben[i])+"/zsim.h5")

prediction_accuracy_A2={}
cycles_A2={}
for i in range(len(A2benpaths)):
	f=h5py.File(A2benpaths[i],"r")
	number_of_mispred_branches=np.sum(f["stats"]["root"]["westmere"]["mispredBranches"][-1])
	number_of_cond_branches=np.sum(f["stats"]["root"]["westmere"]["condBranches"][-1])
	number_of_cCycles=np.array(f["stats"]["root"]["westmere"]["cCycles"][-1])
	number_of_Cycles=np.array(f["stats"]["root"]["westmere"]["cycles"][-1])
	cycles_A2[A2ben[i]]=np.max(number_of_cCycles+number_of_Cycles)
	prediction_accuracy_A2[A2ben[i]]=100*(1-(float(number_of_mispred_branches)/number_of_cond_branches))



#Same functions but now for A3

prediction_accuracy_A3={}
cycles_A3={}
for i in range(len(A3benpaths)):
	f=h5py.File(A3benpaths[i],"r")
	number_of_mispred_branches=np.sum(f["stats"]["root"]["westmere"]["mispredBranches"][-1])
	number_of_cond_branches=np.sum(f["stats"]["root"]["westmere"]["condBranches"][-1])
	number_of_cCycles=np.array(f["stats"]["root"]["westmere"]["cCycles"][-1])
	number_of_Cycles=np.array(f["stats"]["root"]["westmere"]["cycles"][-1])
	cycles_A3[A3ben[i]]=np.max(number_of_cCycles+number_of_Cycles)
	prediction_accuracy_A3[A3ben[i]]=100*(1-(float(number_of_mispred_branches)/number_of_cond_branches))

fig,ax=plt.subplots()
width = 0.35
rect1 = plt.bar(np.arange(len(prediction_accuracy_A2)),prediction_accuracy_A2.values(), width,color="green")
plt.hold(True)
rect2 = plt.bar(width+np.arange(len(prediction_accuracy_A3)),prediction_accuracy_A3.values(),width,color="red")

plt.xticks(range(len(prediction_accuracy_A2)),prediction_accuracy_A2.keys()) 
plt.legend((rect1[0], rect2[0]),('A2','A3'))

plt.xlabel("Benchmark")
plt.ylabel("Accuracy (%)")
plt.grid(True)
plt.title("Comparison of Branch prediction Accuracy")
for ticks in ax.get_xticklabels():
	ticks.set_rotation(-90)
plt.figure(1)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%f' % float(height),
                ha='center', va='bottom', rotation = 90)
autolabel(rect1)
autolabel(rect2)

plt.savefig('figure1.pdf', dpi=1000)

fig,ax=plt.subplots()
for i in A2ben:
	cycles_A3[i]=float(cycles_A3[i])/cycles_A2[i]

rect1 = plt.bar(np.arange(len(cycles_A3)),cycles_A3.values(),color="blue")
plt.xticks(np.arange(len(cycles_A3)),cycles_A3.keys())
plt.xlabel("Benchmark")
plt.ylabel("Normalized time taken by A3 compared to A2")
plt.title("Comparison of Time taken by A3 relative to A2")
plt.grid(True)
for tick in ax.get_xticklabels():
	tick.set_rotation(-90)

autolabel(rect1)

plt.savefig('figure2.pdf', dpi=1000)

plt.show()