from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(7, 7)
qc.h([0])
qc.h([1])
qc.h([2])
qc.h([3])
qc.h([4])
qc.x([5])
qc.cp(0.19634954084936207,[4], [5])
qc.cx([4], [3])
qc.cp(-0.19634954084936207,[3], [5])
qc.cx([4], [3])
qc.cp(0.19634954084936207,[3], [5])
qc.cx([3], [2])
qc.cp(-0.19634954084936207,[2], [5])
qc.cx([4], [2])
qc.cp(0.19634954084936207,[2], [5])
qc.cx([3], [2])
qc.cp(-0.19634954084936207,[2], [5])
qc.cx([4], [2])
qc.cp(0.19634954084936207,[2], [5])
qc.cx([2], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([3], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([2], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([3], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([1], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([2], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([1], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[1])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([2], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[2])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[3])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[0])
qc.rccx([0], [1], [5])
qc.p(-3.141592653589793,[4])
qc.rccx([2], [5], [6])
qc.ccx([3], [6], [4])
qc.rccx([2], [5], [6])
qc.rccx([0], [1], [5])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[0])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[1])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[2])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.p(-3.141592653589793,[4])
qc.cp(0.19634954084936207,[4], [5])
qc.cx([4], [3])
qc.cp(-0.19634954084936207,[3], [5])
qc.cx([4], [3])
qc.cp(0.19634954084936207,[3], [5])
qc.cx([3], [2])
qc.cp(-0.19634954084936207,[2], [5])
qc.cx([4], [2])
qc.cp(0.19634954084936207,[2], [5])
qc.cx([3], [2])
qc.cp(-0.19634954084936207,[2], [5])
qc.cx([4], [2])
qc.cp(0.19634954084936207,[2], [5])
qc.cx([2], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([3], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([2], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([3], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([1], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([2], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([1], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[1])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([2], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[2])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[3])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[0])
qc.rccx([0], [1], [5])
qc.rccx([2], [5], [6])
qc.p(-3.141592653589793,[4])
qc.ccx([3], [6], [4])
qc.rccx([2], [5], [6])
qc.rccx([0], [1], [5])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[0])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[1])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[2])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.p(-3.141592653589793,[4])
qc.cp(0.19634954084936207,[4], [5])
qc.cx([4], [3])
qc.cp(-0.19634954084936207,[3], [5])
qc.cx([4], [3])
qc.cp(0.19634954084936207,[3], [5])
qc.cx([3], [2])
qc.cp(-0.19634954084936207,[2], [5])
qc.cx([4], [2])
qc.cp(0.19634954084936207,[2], [5])
qc.cx([3], [2])
qc.cp(-0.19634954084936207,[2], [5])
qc.cx([4], [2])
qc.cp(0.19634954084936207,[2], [5])
qc.cx([2], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([3], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([2], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([3], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([1], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([2], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([1], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[1])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([2], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[2])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[3])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[0])
qc.rccx([0], [1], [5])
qc.rccx([2], [5], [6])
qc.p(-3.141592653589793,[4])
qc.ccx([3], [6], [4])
qc.rccx([2], [5], [6])
qc.rccx([0], [1], [5])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[0])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[1])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[2])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.p(-3.141592653589793,[4])
qc.cp(0.19634954084936207,[4], [5])
qc.cx([4], [3])
qc.cp(-0.19634954084936207,[3], [5])
qc.cx([4], [3])
qc.cp(0.19634954084936207,[3], [5])
qc.cx([3], [2])
qc.cp(-0.19634954084936207,[2], [5])
qc.cx([4], [2])
qc.cp(0.19634954084936207,[2], [5])
qc.cx([3], [2])
qc.cp(-0.19634954084936207,[2], [5])
qc.cx([4], [2])
qc.cp(0.19634954084936207,[2], [5])
qc.cx([2], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([3], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([2], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([3], [1])
qc.cp(-0.19634954084936207,[1], [5])
qc.cx([4], [1])
qc.cp(0.19634954084936207,[1], [5])
qc.cx([1], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([2], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([1], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[1])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([2], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[2])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.cx([3], [0])
qc.cp(-0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[3])
qc.cx([4], [0])
qc.cp(0.19634954084936207,[0], [5])
qc.u(1.5707963267948966,0.0,0.0,[0])
qc.rccx([0], [1], [5])
qc.rccx([2], [5], [6])
qc.p(-3.141592653589793,[4])
qc.ccx([3], [6], [4])
qc.rccx([2], [5], [6])
qc.rccx([0], [1], [5])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[0])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[1])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[2])
qc.u(1.5707963267948966,-3.141592653589793,-3.141592653589793,[3])
qc.p(-3.141592653589793,[4])
qc.barrier([0], [1], [2], [3], [4], [5], [6])
