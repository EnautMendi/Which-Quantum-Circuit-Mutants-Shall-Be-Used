from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(6, 6)
qc.h([5])
qc.cx([5], [4])
qc.cx([4], [3])
qc.cx([3], [2])
qc.cx([2], [1])
qc.cx([1], [0])
qc.h([5])
qc.cp(1.5707963267948966,[5], [4])
qc.h([4])
qc.cp(0.7853981633974483,[5], [3])
qc.cp(1.5707963267948966,[4], [3])
qc.h([3])
qc.cp(0.39269908169872414,[5], [2])
qc.cp(0.7853981633974483,[4], [2])
qc.cp(1.5707963267948966,[3], [2])
qc.h([2])
qc.cp(0.19634954084936207,[5], [1])
qc.cp(0.39269908169872414,[4], [1])
qc.cp(0.7853981633974483,[3], [1])
qc.cp(1.5707963267948966,[2], [1])
qc.h([1])
qc.cp(0.09817477042468103,[5], [0])
qc.cp(0.19634954084936207,[4], [0])
qc.cp(0.39269908169872414,[3], [0])
qc.cp(0.7853981633974483,[2], [0])
qc.cp(1.5707963267948966,[1], [0])
qc.h([0])
qc.swap([0], [5])
qc.swap([1], [4])
qc.swap([2], [3])
qc.barrier([0], [1], [2], [3], [4], [5])
