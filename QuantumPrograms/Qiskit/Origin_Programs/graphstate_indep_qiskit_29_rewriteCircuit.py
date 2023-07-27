from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(29, 29)
qc.h([0])
qc.h([1])
qc.cz([0], [1])
qc.h([2])
qc.cz([0], [2])
qc.h([3])
qc.h([4])
qc.cz([3], [4])
qc.h([5])
qc.h([6])
qc.cz([5], [6])
qc.h([7])
qc.h([8])
qc.cz([7], [8])
qc.h([9])
qc.h([10])
qc.cz([9], [10])
qc.h([11])
qc.cz([8], [11])
qc.h([12])
qc.cz([3], [12])
qc.h([13])
qc.h([14])
qc.cz([13], [14])
qc.h([15])
qc.cz([10], [15])
qc.h([16])
qc.cz([11], [16])
qc.h([17])
qc.cz([4], [17])
qc.h([18])
qc.cz([17], [18])
qc.h([19])
qc.cz([18], [19])
qc.h([20])
qc.cz([1], [20])
qc.cz([15], [20])
qc.h([21])
qc.cz([13], [21])
qc.h([22])
qc.cz([6], [22])
qc.cz([12], [22])
qc.h([23])
qc.cz([19], [23])
qc.cz([21], [23])
qc.h([24])
qc.cz([2], [24])
qc.cz([16], [24])
qc.h([25])
qc.cz([5], [25])
qc.h([26])
qc.cz([25], [26])
qc.h([27])
qc.cz([9], [27])
qc.cz([14], [27])
qc.h([28])
qc.cz([7], [28])
qc.cz([26], [28])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28])
