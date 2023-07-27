from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(5, 5)
qc.ry(1.7376841,[0])
qc.ry(1.459802,[1])
qc.cx([1], [0])
qc.ry(1.3166149,[0])
qc.cx([1], [0])
qc.ry(1.1780972450961724,[2])
qc.cry(0.0,[0], [2])
qc.cry(0.0,[1], [2])
qc.x([1])
qc.x([3])
qc.x([4])
qc.ccx([1], [4], [3])
qc.x([1])
qc.cx([3], [2])
qc.u(0.29425236,0.0,0.0,[2])
qc.cx([3], [2])
qc.u(0.29425236,-3.141592653589793,-3.141592653589793,[2])
qc.cx([3], [2])
qc.u(-0.11449191,0.0,0.0,[2])
qc.cx([3], [2])
qc.u(0.11449191,0.0,0.0,[2])
qc.ccx([3], [0], [2])
qc.cx([3], [2])
qc.u(0.11449191,0.0,0.0,[2])
qc.cx([3], [2])
qc.u(-0.11449191,0.0,0.0,[2])
qc.ccx([3], [0], [2])
qc.cx([3], [2])
qc.u(-0.22898382,0.0,0.0,[2])
qc.cx([3], [2])
qc.u(0.22898382,0.0,0.0,[2])
qc.ccx([3], [1], [2])
qc.cx([3], [2])
qc.u(0.22898382,0.0,0.0,[2])
qc.cx([3], [2])
qc.u(-0.22898382,0.0,0.0,[2])
qc.ccx([3], [1], [2])
qc.x([1])
qc.ccx([1], [4], [3])
qc.x([1])
qc.x([3])
qc.x([4])
qc.barrier([0], [1], [2], [3], [4])