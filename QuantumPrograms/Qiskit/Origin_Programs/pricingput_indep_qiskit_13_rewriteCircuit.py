from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(13, 13)
qc.ry(1.5947652,[0])
qc.ry(1.6163407,[1])
qc.ry(1.647148,[2])
qc.ry(1.6641835,[3])
qc.ry(1.6479655,[4])
qc.ry(1.5135408,[5])
qc.cx([5], [4])
qc.ry(0.86752035,[4])
qc.cx([5], [4])
qc.cx([4], [3])
qc.ry(0.26514636,[3])
qc.cx([5], [3])
qc.ry(0.11948144,[3])
qc.cx([4], [3])
qc.ry(0.54080891,[3])
qc.cx([5], [3])
qc.cx([3], [2])
qc.ry(0.083022902,[2])
qc.cx([4], [2])
qc.ry(0.020503932,[2])
qc.cx([3], [2])
qc.ry(0.16558102,[2])
qc.cx([5], [2])
qc.ry(0.085907598,[2])
qc.cx([3], [2])
qc.ry(0.0089247848,[2])
qc.cx([4], [2])
qc.ry(0.042252153,[2])
qc.cx([3], [2])
qc.ry(0.31061061,[2])
qc.cx([5], [2])
qc.cx([2], [1])
qc.ry(0.023352368,[1])
qc.cx([3], [1])
qc.ry(0.0036541455,[1])
qc.cx([2], [1])
qc.ry(0.04642649,[1])
qc.cx([4], [1])
qc.ry(0.014284618,[1])
qc.cx([2], [1])
qc.ry(0.0011717076,[1])
qc.cx([3], [1])
qc.ry(0.0071726612,[1])
qc.cx([2], [1])
qc.ry(0.090487054,[1])
qc.cx([5], [1])
qc.ry(0.049684692,[1])
qc.cx([2], [1])
qc.ry(0.0042975585,[1])
qc.cx([3], [1])
qc.ry(0.00071186036,[1])
qc.cx([2], [1])
qc.ry(0.0085779933,[1])
qc.cx([4], [1])
qc.ry(0.025570002,[1])
qc.cx([2], [1])
qc.ry(0.0021735007,[1])
qc.cx([3], [1])
qc.ry(0.0128638,[1])
qc.cx([2], [1])
qc.ry(0.16419765,[1])
qc.cx([5], [1])
qc.cx([1], [0])
qc.ry(0.0060781038,[0])
qc.cx([2], [0])
qc.ry(0.00052904929,[0])
qc.cx([1], [0])
qc.ry(0.012128274,[0])
qc.cx([3], [0])
qc.ry(0.0020831693,[0])
qc.cx([1], [0])
qc.ry(0.00010980752,[0])
qc.cx([2], [0])
qc.ry(0.0010448914,[0])
qc.cx([1], [0])
qc.ry(0.024037705,[0])
qc.cx([4], [0])
qc.ry(0.0078460109,[0])
qc.cx([1], [0])
qc.ry(0.0004078366,[0])
qc.cx([2], [0])
qc.ry(4.9392404e-05,[0])
qc.cx([1], [0])
qc.ry(0.00081254104,[0])
qc.cx([3], [0])
qc.ry(0.0039722403,[0])
qc.cx([1], [0])
qc.ry(0.00020705673,[0])
qc.cx([2], [0])
qc.ry(0.0019923921,[0])
qc.cx([1], [0])
qc.ry(0.046475455,[0])
qc.cx([5], [0])
qc.ry(0.025949313,[0])
qc.cx([1], [0])
qc.ry(0.0012748476,[0])
qc.cx([2], [0])
qc.ry(0.00014903644,[0])
qc.cx([1], [0])
qc.ry(0.0025400077,[0])
qc.cx([3], [0])
qc.ry(0.00058369063,[0])
qc.cx([1], [0])
qc.ry(3.8180209e-05,[0])
qc.cx([2], [0])
qc.ry(0.00029308707,[0])
qc.cx([1], [0])
qc.ry(0.0050038849,[0])
qc.cx([4], [0])
qc.ry(0.013548306,[0])
qc.cx([1], [0])
qc.ry(0.00067507279,[0])
qc.cx([2], [0])
qc.ry(7.953033e-05,[0])
qc.cx([1], [0])
qc.ry(0.0013450437,[0])
qc.cx([3], [0])
qc.ry(0.0068533854,[0])
qc.cx([1], [0])
qc.ry(0.00034263436,[0])
qc.cx([2], [0])
qc.ry(0.0034368196,[0])
qc.cx([1], [0])
qc.ry(0.083493363,[0])
qc.cx([5], [0])
qc.ry(1.9634954084936207,[6])
qc.cry(-0.021807459,[0], [6])
qc.cry(-0.043614917,[1], [6])
qc.x([1])
qc.cry(-0.087229835,[2], [6])
qc.cry(-0.17445967,[3], [6])
qc.x([3])
qc.cry(-0.34891934,[4], [6])
qc.x([4])
qc.cry(-0.69783868,[5], [6])
qc.cx([0], [8])
qc.x([8])
qc.x([9])
qc.ccx([1], [8], [9])
qc.ccx([2], [9], [10])
qc.x([10])
qc.x([11])
qc.ccx([3], [10], [11])
qc.x([11])
qc.x([12])
qc.ccx([4], [11], [12])
qc.ccx([5], [12], [7])
qc.x([12])
qc.ccx([4], [11], [12])
qc.ccx([3], [10], [11])
qc.x([10])
qc.ccx([2], [9], [10])
qc.x([3])
qc.x([4])
qc.cx([7], [6])
qc.u(0.39269908169872414,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(0.39269908169872414,-3.141592653589793,-3.141592653589793,[6])
qc.cx([7], [6])
qc.u(-0.0054518647,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(0.0054518647,0.0,0.0,[6])
qc.x([9])
qc.ccx([1], [8], [9])
qc.x([1])
qc.x([8])
qc.cx([0], [8])
qc.ccx([7], [0], [6])
qc.cx([7], [6])
qc.u(0.0054518647,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(-0.0054518647,0.0,0.0,[6])
qc.ccx([7], [0], [6])
qc.cx([0], [8])
qc.cx([7], [6])
qc.u(-0.010903729,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(0.010903729,0.0,0.0,[6])
qc.ccx([7], [1], [6])
qc.cx([7], [6])
qc.u(0.010903729,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(-0.010903729,0.0,0.0,[6])
qc.ccx([7], [1], [6])
qc.x([1])
qc.cx([7], [6])
qc.u(-0.021807459,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(0.021807459,0.0,0.0,[6])
qc.ccx([7], [2], [6])
qc.cx([7], [6])
qc.u(0.021807459,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(-0.021807459,0.0,0.0,[6])
qc.ccx([7], [2], [6])
qc.cx([7], [6])
qc.u(-0.043614917,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(0.043614917,0.0,0.0,[6])
qc.ccx([7], [3], [6])
qc.cx([7], [6])
qc.u(0.043614917,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(-0.043614917,0.0,0.0,[6])
qc.ccx([7], [3], [6])
qc.x([3])
qc.cx([7], [6])
qc.u(-0.087229835,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(0.087229835,0.0,0.0,[6])
qc.ccx([7], [4], [6])
qc.cx([7], [6])
qc.u(0.087229835,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(-0.087229835,0.0,0.0,[6])
qc.ccx([7], [4], [6])
qc.x([4])
qc.cx([7], [6])
qc.u(-0.17445967,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(0.17445967,0.0,0.0,[6])
qc.ccx([7], [5], [6])
qc.cx([7], [6])
qc.u(0.17445967,0.0,0.0,[6])
qc.cx([7], [6])
qc.u(-0.17445967,0.0,0.0,[6])
qc.ccx([7], [5], [6])
qc.x([8])
qc.ccx([1], [8], [9])
qc.x([9])
qc.ccx([2], [9], [10])
qc.x([10])
qc.ccx([3], [10], [11])
qc.ccx([4], [11], [12])
qc.x([12])
qc.ccx([5], [12], [7])
qc.ccx([4], [11], [12])
qc.x([11])
qc.x([12])
qc.ccx([3], [10], [11])
qc.x([10])
qc.x([11])
qc.ccx([2], [9], [10])
qc.ccx([1], [8], [9])
qc.x([1])
qc.x([3])
qc.x([4])
qc.x([8])
qc.cx([0], [8])
qc.x([9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12])