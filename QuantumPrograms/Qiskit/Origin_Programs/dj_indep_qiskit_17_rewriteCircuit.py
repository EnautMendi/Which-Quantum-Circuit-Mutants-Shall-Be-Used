from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(17, 17)
qc.u(1.5707963267948966,0.0,0.0,[0])
qc.u(1.5707963267948966,0.0,0.0,[1])
qc.h([2])
qc.h([3])
qc.h([4])
qc.h([5])
qc.u(1.5707963267948966,0.0,0.0,[6])
qc.h([7])
qc.h([8])
qc.h([9])
qc.u(1.5707963267948966,0.0,0.0,[10])
qc.h([11])
qc.u(1.5707963267948966,0.0,0.0,[12])
qc.u(1.5707963267948966,0.0,0.0,[13])
qc.u(1.5707963267948966,0.0,0.0,[14])
qc.u(1.5707963267948966,0.0,0.0,[15])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[16])
qc.cx([0], [16])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[0])
qc.cx([1], [16])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[1])
qc.cx([2], [16])
qc.h([2])
qc.cx([3], [16])
qc.h([3])
qc.cx([4], [16])
qc.h([4])
qc.cx([5], [16])
qc.h([5])
qc.cx([6], [16])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[6])
qc.cx([7], [16])
qc.h([7])
qc.cx([8], [16])
qc.h([8])
qc.cx([9], [16])
qc.cx([10], [16])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[10])
qc.cx([11], [16])
qc.h([11])
qc.cx([12], [16])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[12])
qc.cx([13], [16])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[13])
qc.cx([14], [16])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[14])
qc.cx([15], [16])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[15])
qc.h([9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16])