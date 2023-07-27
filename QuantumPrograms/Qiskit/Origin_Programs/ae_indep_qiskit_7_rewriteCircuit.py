from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(7, 7)
qc.u(1.5707963267948966,0.0,-3.141592653589793,[0])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[1])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[2])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[3])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[4])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[5])
qc.u(0.92729522,0.0,0.0,[6])
qc.cx([0], [6])
qc.u(-0.92729522,0.0,0.0,[6])
qc.cx([0], [6])
qc.u(0.92729522,0.0,0.0,[6])
qc.cx([1], [6])
qc.u(-1.8545904,0.0,0.0,[6])
qc.id([6])
qc.cx([1], [6])
qc.u(1.8545904,0.0,0.0,[6])
qc.cx([2], [6])
qc.u(-3.7091809,0.0,0.0,[6])
qc.cx([2], [6])
qc.u(2.5740044,-3.141592653589793,-3.141592653589793,[6])
qc.cx([3], [6])
qc.u(-7.4183617,0.0,0.0,[6])
qc.cx([3], [6])
qc.u(1.1351764,0.0,0.0,[6])
qc.cx([4], [6])
qc.u(-14.836723,0.0,0.0,[6])
qc.cx([4], [6])
qc.u(2.2703529,0.0,0.0,[6])
qc.cx([5], [6])
qc.u(-29.673447,0.0,0.0,[6])
qc.cx([5], [6])
qc.u(29.673447,0.0,0.0,[6])
qc.h([5])
qc.cp(-1.5707963267948966,[4], [5])
qc.cp(-0.7853981633974483,[3], [5])
qc.cp(-0.39269908169872414,[2], [5])
qc.cp(-0.19634954084936207,[1], [5])
qc.cp(-0.09817477042468103,[0], [5])
qc.h([4])
qc.cp(-1.5707963267948966,[3], [4])
qc.cp(-0.7853981633974483,[2], [4])
qc.cp(-0.39269908169872414,[1], [4])
qc.cp(-0.19634954084936207,[0], [4])
qc.h([3])
qc.cp(-1.5707963267948966,[2], [3])
qc.cp(-0.7853981633974483,[1], [3])
qc.cp(-0.39269908169872414,[0], [3])
qc.h([2])
qc.cp(-1.5707963267948966,[1], [2])
qc.cp(-0.7853981633974483,[0], [2])
qc.h([1])
qc.cp(-1.5707963267948966,[0], [1])
qc.h([0])
qc.barrier([0], [1], [2], [3], [4], [5], [6])
