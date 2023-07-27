from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(24, 24)
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
qc.ry(-1.3096389,[13])
qc.ry(-1.3181161,[14])
qc.ry(-1.3258177,[15])
qc.ry(-1.3328552,[16])
qc.ry(-1.339319,[17])
qc.ry(-1.3452829,[18])
qc.ry(-1.3508083,[19])
qc.ry(-1.3559465,[20])
qc.ry(-1.3607406,[21])
qc.ry(-1.3652274,[22])
qc.x([23])
qc.cz([23], [22])
qc.ry(1.3652274,[22])
qc.cz([22], [21])
qc.ry(1.3607406,[21])
qc.cz([21], [20])
qc.ry(1.3559465,[20])
qc.cz([20], [19])
qc.ry(1.3508083,[19])
qc.cz([19], [18])
qc.ry(1.3452829,[18])
qc.cz([18], [17])
qc.ry(1.339319,[17])
qc.cz([17], [16])
qc.ry(1.3328552,[16])
qc.cz([16], [15])
qc.ry(1.3258177,[15])
qc.cz([15], [14])
qc.ry(1.3181161,[14])
qc.cz([14], [13])
qc.ry(1.3096389,[13])
qc.cz([13], [12])
qc.ry(1.3002466,[12])
qc.cz([12], [11])
qc.ry(1.2897614,[11])
qc.cz([11], [10])
qc.ry(1.2779536,[10])
qc.cz([10], [9])
qc.cx([22], [23])
qc.cx([21], [22])
qc.cx([20], [21])
qc.cx([19], [20])
qc.cx([18], [19])
qc.cx([17], [18])
qc.cx([16], [17])
qc.cx([15], [16])
qc.cx([14], [15])
qc.cx([13], [14])
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
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23])
