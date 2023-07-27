from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(11, 11)
qc.u(1.5707963267948966,0.0,0.0,[0])
qc.h([1])
qc.h([2])
qc.u(1.5707963267948966,0.0,0.0,[3])
qc.h([4])
qc.u(1.5707963267948966,0.0,0.0,[5])
qc.h([6])
qc.u(1.5707963267948966,0.0,0.0,[7])
qc.u(1.5707963267948966,0.0,0.0,[8])
qc.u(1.5707963267948966,0.0,0.0,[9])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[10])
qc.cx([0], [10])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[0])
qc.cx([1], [10])
qc.h([1])
qc.cx([2], [10])
qc.h([2])
qc.cx([3], [10])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.cx([4], [10])
qc.h([4])
qc.cx([5], [10])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[5])
qc.cx([6], [10])
qc.h([6])
qc.cx([7], [10])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[7])
qc.cx([8], [10])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[8])
qc.cx([9], [10])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10])