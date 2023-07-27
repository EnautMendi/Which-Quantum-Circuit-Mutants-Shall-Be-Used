from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(5, 5)
qc.h([3])
qc.rccx([3], [1], [4])
qc.ccx([2], [4], [0])
qc.rccx([3], [1], [4])
qc.ccx([3], [2], [1])
qc.cx([3], [2])
qc.x([3])
qc.x([1])
qc.rccx([3], [1], [4])
qc.x([2])
qc.ccx([2], [4], [0])
qc.rccx([3], [1], [4])
qc.ccx([3], [2], [1])
qc.cx([3], [2])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.x([1])
qc.rccx([3], [1], [4])
qc.x([2])
qc.ccx([2], [4], [0])
qc.rccx([3], [1], [4])
qc.ccx([3], [2], [1])
qc.cx([3], [2])
qc.x([3])
qc.x([1])
qc.rccx([3], [1], [4])
qc.x([2])
qc.ccx([2], [4], [0])
qc.rccx([3], [1], [4])
qc.ccx([3], [2], [1])
qc.cx([3], [2])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.x([1])
qc.rccx([3], [1], [4])
qc.x([2])
qc.ccx([2], [4], [0])
qc.rccx([3], [1], [4])
qc.ccx([3], [2], [1])
qc.cx([3], [2])
qc.x([3])
qc.x([1])
qc.rccx([3], [1], [4])
qc.x([2])
qc.ccx([2], [4], [0])
qc.rccx([3], [1], [4])
qc.ccx([3], [2], [1])
qc.cx([3], [2])
qc.x([3])
qc.x([1])
qc.x([2])
qc.barrier([0], [1], [2], [3], [4])
