from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(29, 29)
qc.h([28])
qc.cx([28], [27])
qc.cx([27], [26])
qc.cx([26], [25])
qc.cx([25], [24])
qc.cx([24], [23])
qc.cx([23], [22])
qc.cx([22], [21])
qc.cx([21], [20])
qc.cx([20], [19])
qc.cx([19], [18])
qc.cx([18], [17])
qc.cx([17], [16])
qc.cx([16], [15])
qc.cx([15], [14])
qc.cx([14], [13])
qc.cx([13], [12])
qc.cx([12], [11])
qc.cx([11], [10])
qc.cx([10], [9])
qc.cx([9], [8])
qc.cx([8], [7])
qc.cx([7], [6])
qc.cx([6], [5])
qc.cx([5], [4])
qc.cx([4], [3])
qc.cx([3], [2])
qc.cx([2], [1])
qc.cx([1], [0])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28])
