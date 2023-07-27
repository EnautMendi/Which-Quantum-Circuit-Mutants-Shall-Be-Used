from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(14, 14)
qc.ry(-0.7853981633974483,[0])
qc.ry(-0.95531662,[1])
qc.ry(-1.0471975511965976,[2])
qc.ry(-1.1071487,[3])
qc.ry(-1.150262,[4])
qc.ry(-1.1831996,[5])
qc.ry(-1.2094292,[6])
qc.ry(-1.2309594,[7])
qc.ry(-1.2490458,[8])
qc.ry(-1.264519,[9])
qc.ry(-1.2779536,[10])
qc.ry(-1.2897614,[11])
qc.ry(-1.3002466,[12])
qc.x([13])
qc.cz([13], [12])
qc.ry(1.3002466,[12])
qc.cz([12], [11])
qc.ry(1.2897614,[11])
qc.cz([11], [10])
qc.ry(1.2779536,[10])
qc.cz([10], [9])
qc.cx([12], [13])
qc.cx([11], [12])
qc.cx([10], [11])
qc.ry(1.264519,[9])
qc.cz([9], [8])
qc.ry(1.2490458,[8])
qc.cz([8], [7])
qc.ry(1.2309594,[7])
qc.cz([7], [6])
qc.ry(1.2094292,[6])
qc.cz([6], [5])
qc.ry(1.1831996,[5])
qc.cz([5], [4])
qc.ry(1.150262,[4])
qc.cz([4], [3])
qc.ry(1.1071487,[3])
qc.cz([3], [2])
qc.ry(1.0471975511965976,[2])
qc.cz([2], [1])
qc.ry(0.95531662,[1])
qc.cz([1], [0])
qc.ry(0.7853981633974483,[0])
qc.cx([9], [10])
qc.cx([8], [9])
qc.cx([7], [8])
qc.cx([6], [7])
qc.cx([5], [6])
qc.cx([4], [5])
qc.cx([3], [4])
qc.cx([2], [3])
qc.cx([1], [2])
qc.cx([0], [1])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13])