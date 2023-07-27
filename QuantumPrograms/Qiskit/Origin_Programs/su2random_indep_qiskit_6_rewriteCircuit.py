from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(6, 6)
qc.u(0.34597359,0.43744856,0.0,[0])
qc.u(0.92896211,0.83968693,0.0,[1])
qc.cx([0], [1])
qc.u(0.17729172,0.75469799,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.u(0.8897231,0.15782943,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.u(0.88806785,0.30535942,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.u(0.44791673,0.20405002,0.0,[5])
qc.cx([0], [5])
qc.u(0.49600037,0.87806698,0.0,[0])
qc.cx([1], [5])
qc.u(0.93053933,0.61534486,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [5])
qc.u(0.36175966,0.58573194,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [5])
qc.u(0.04735545,0.94404993,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [5])
qc.u(0.041646114,0.17231304,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.u(0.54988007,0.1567303,0.0,[5])
qc.cx([0], [5])
qc.u(0.77955409,0.22207655,0.0,[0])
qc.cx([1], [5])
qc.u(0.31187127,0.47021141,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [5])
qc.u(0.99239276,0.20695346,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [5])
qc.u(0.21896571,0.39089583,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [5])
qc.u(0.61000413,0.098510831,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.u(0.9605572,0.62929893,0.0,[5])
qc.cx([0], [5])
qc.u(0.42806545,0.68376035,0.0,[0])
qc.cx([1], [5])
qc.u(0.76834005,0.27471124,0.0,[1])
qc.cx([2], [5])
qc.u(0.15698093,0.96478905,0.0,[2])
qc.cx([3], [5])
qc.u(0.59256226,0.92646702,0.0,[3])
qc.cx([4], [5])
qc.u(0.040194977,0.26254046,0.0,[4])
qc.u(0.6306672,0.91889796,0.0,[5])
qc.barrier([0], [1], [2], [3], [4], [5])