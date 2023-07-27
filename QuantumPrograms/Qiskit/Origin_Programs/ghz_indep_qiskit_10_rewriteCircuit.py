from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(10, 10)
qc.h([9])
qc.cx([9], [8])
qc.cx([8], [7])
qc.cx([7], [6])
qc.cx([6], [5])
qc.cx([5], [4])
qc.cx([4], [3])
qc.cx([3], [2])
qc.cx([2], [1])
qc.cx([1], [0])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9])