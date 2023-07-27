from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(20, 20)
qc.h([0])
qc.h([1])
qc.cz([0], [1])
qc.h([2])
qc.h([3])
qc.cz([2], [3])
qc.h([4])
qc.h([5])
qc.cz([4], [5])
qc.h([6])
qc.h([7])
qc.cz([6], [7])
qc.h([8])
qc.h([9])
qc.cz([8], [9])
qc.h([10])
qc.cz([3], [10])
qc.cz([9], [10])
qc.h([11])
qc.cz([7], [11])
qc.h([12])
qc.cz([2], [12])
qc.h([13])
qc.cz([5], [13])
qc.h([14])
qc.cz([12], [14])
qc.cz([13], [14])
qc.h([15])
qc.cz([6], [15])
qc.cz([11], [15])
qc.h([16])
qc.cz([0], [16])
qc.cz([8], [16])
qc.h([17])
qc.h([18])
qc.cz([1], [18])
qc.cz([17], [18])
qc.h([19])
qc.cz([4], [19])
qc.cz([17], [19])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19])
