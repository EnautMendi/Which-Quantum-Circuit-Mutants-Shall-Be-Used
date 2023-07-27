from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(29, 29)
qc.h([0])
qc.h([1])
qc.h([2])
qc.u(1.5707963267948966,0.0,0.0,[3])
qc.h([4])
qc.u(1.5707963267948966,0.0,0.0,[5])
qc.u(1.5707963267948966,0.0,0.0,[6])
qc.u(1.5707963267948966,0.0,0.0,[7])
qc.h([8])
qc.u(1.5707963267948966,0.0,0.0,[9])
qc.h([10])
qc.h([11])
qc.u(1.5707963267948966,0.0,0.0,[12])
qc.u(1.5707963267948966,0.0,0.0,[13])
qc.h([14])
qc.h([15])
qc.u(1.5707963267948966,0.0,0.0,[16])
qc.u(1.5707963267948966,0.0,0.0,[17])
qc.h([18])
qc.h([19])
qc.u(1.5707963267948966,0.0,0.0,[20])
qc.u(1.5707963267948966,0.0,0.0,[21])
qc.h([22])
qc.u(1.5707963267948966,0.0,0.0,[23])
qc.h([24])
qc.u(1.5707963267948966,0.0,0.0,[25])
qc.h([26])
qc.h([27])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[28])
qc.cx([0], [28])
qc.h([0])
qc.cx([1], [28])
qc.h([1])
qc.cx([2], [28])
qc.h([2])
qc.cx([3], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.cx([4], [28])
qc.h([4])
qc.cx([5], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[5])
qc.cx([6], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[6])
qc.cx([7], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[7])
qc.cx([8], [28])
qc.h([8])
qc.cx([9], [28])
qc.cx([10], [28])
qc.h([10])
qc.cx([11], [28])
qc.h([11])
qc.cx([12], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[12])
qc.cx([13], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[13])
qc.cx([14], [28])
qc.h([14])
qc.cx([15], [28])
qc.h([15])
qc.cx([16], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[16])
qc.cx([17], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[17])
qc.cx([18], [28])
qc.h([18])
qc.cx([19], [28])
qc.h([19])
qc.cx([20], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[20])
qc.cx([21], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[21])
qc.cx([22], [28])
qc.h([22])
qc.cx([23], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[23])
qc.cx([24], [28])
qc.h([24])
qc.cx([25], [28])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[25])
qc.cx([26], [28])
qc.h([26])
qc.cx([27], [28])
qc.h([27])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28])