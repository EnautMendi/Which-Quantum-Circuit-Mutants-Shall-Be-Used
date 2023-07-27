from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(17, 17)
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
qc.cz([0], [8])
qc.cz([2], [8])
qc.h([9])
qc.cz([6], [9])
qc.cz([7], [9])
qc.h([10])
qc.cz([5], [10])
qc.h([11])
qc.cz([10], [11])
qc.h([12])
qc.cz([11], [12])
qc.h([13])
qc.cz([3], [13])
qc.h([14])
qc.cz([4], [14])
qc.h([15])
qc.cz([12], [15])
qc.cz([14], [15])
qc.h([16])
qc.cz([1], [16])
qc.cz([13], [16])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16])
