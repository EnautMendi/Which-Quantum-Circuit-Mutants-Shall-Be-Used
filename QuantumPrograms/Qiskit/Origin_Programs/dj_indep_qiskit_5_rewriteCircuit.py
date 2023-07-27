from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(5, 5)
qc.h([0])
qc.h([1])
qc.u(1.5707963267948966,0.0,0.0,[2])
qc.u(1.5707963267948966,0.0,0.0,[3])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[4])
qc.cx([0], [4])
qc.h([0])
qc.cx([1], [4])
qc.h([1])
qc.cx([2], [4])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[2])
qc.cx([3], [4])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.barrier([0], [1], [2], [3], [4])