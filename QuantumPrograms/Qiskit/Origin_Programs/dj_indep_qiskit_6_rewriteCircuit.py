from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(6, 6)
qc.u(1.5707963267948966,0.0,0.0,[0])
qc.h([1])
qc.u(1.5707963267948966,0.0,0.0,[2])
qc.u(1.5707963267948966,0.0,0.0,[3])
qc.h([4])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[5])
qc.cx([0], [5])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[0])
qc.cx([1], [5])
qc.h([1])
qc.cx([2], [5])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[2])
qc.cx([3], [5])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.cx([4], [5])
qc.h([4])
qc.barrier([0], [1], [2], [3], [4], [5])