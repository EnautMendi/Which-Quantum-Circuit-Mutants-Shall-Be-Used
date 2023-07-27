from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(9, 9)
qc.ry(-1.3226481697843,[0])
qc.ry(-4.20602524026502,[1])
qc.cz([0], [1])
qc.ry(1.8595532562595,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.ry(2.17852696015287,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.ry(4.1617533941992,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.ry(4.44798486959114,[5])
qc.cz([0], [5])
qc.cz([1], [5])
qc.cz([2], [5])
qc.cz([3], [5])
qc.cz([4], [5])
qc.ry(4.61948536196202,[6])
qc.cz([0], [6])
qc.cz([1], [6])
qc.cz([2], [6])
qc.cz([3], [6])
qc.cz([4], [6])
qc.cz([5], [6])
qc.ry(6.98652357866358,[7])
qc.cz([0], [7])
qc.cz([1], [7])
qc.cz([2], [7])
qc.cz([3], [7])
qc.cz([4], [7])
qc.cz([5], [7])
qc.cz([6], [7])
qc.ry(3.01272874343115,[8])
qc.cz([0], [8])
qc.ry(5.55203715874441,[0])
qc.cz([1], [8])
qc.ry(-4.89363258669994,[1])
qc.cz([0], [1])
qc.cz([2], [8])
qc.ry(-6.03165744422128,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.cz([3], [8])
qc.ry(3.70626017973588,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.cz([4], [8])
qc.ry(1.52699530056684,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.cz([5], [8])
qc.ry(-0.678264677796328,[5])
qc.cz([0], [5])
qc.cz([1], [5])
qc.cz([2], [5])
qc.cz([3], [5])
qc.cz([4], [5])
qc.cz([6], [8])
qc.ry(1.82954365878692,[6])
qc.cz([0], [6])
qc.cz([1], [6])
qc.cz([2], [6])
qc.cz([3], [6])
qc.cz([4], [6])
qc.cz([5], [6])
qc.cz([7], [8])
qc.ry(6.27395642092228,[7])
qc.cz([0], [7])
qc.cz([1], [7])
qc.cz([2], [7])
qc.cz([3], [7])
qc.cz([4], [7])
qc.cz([5], [7])
qc.cz([6], [7])
qc.ry(1.47197396581119,[8])
qc.cz([0], [8])
qc.ry(-2.75506050539877,[0])
qc.cz([1], [8])
qc.ry(3.32274109359298,[1])
qc.cz([0], [1])
qc.cz([2], [8])
qc.ry(-1.02367543592405,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.cz([3], [8])
qc.ry(0.741761954255242,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.cz([4], [8])
qc.ry(5.49410004850517,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.cz([5], [8])
qc.ry(4.0423185525409,[5])
qc.cz([0], [5])
qc.cz([1], [5])
qc.cz([2], [5])
qc.cz([3], [5])
qc.cz([4], [5])
qc.cz([6], [8])
qc.ry(1.34251557642838,[6])
qc.cz([0], [6])
qc.cz([1], [6])
qc.cz([2], [6])
qc.cz([3], [6])
qc.cz([4], [6])
qc.cz([5], [6])
qc.cz([7], [8])
qc.ry(-2.54276743591053,[7])
qc.cz([0], [7])
qc.cz([1], [7])
qc.cz([2], [7])
qc.cz([3], [7])
qc.cz([4], [7])
qc.cz([5], [7])
qc.cz([6], [7])
qc.ry(1.72518075511131,[8])
qc.cz([0], [8])
qc.ry(-4.50764938765976,[0])
qc.cz([1], [8])
qc.ry(-4.58400923773876,[1])
qc.cz([2], [8])
qc.ry(-5.3821234074437,[2])
qc.cz([3], [8])
qc.ry(-1.02274859782208,[3])
qc.cz([4], [8])
qc.ry(-0.505295793437927,[4])
qc.cz([5], [8])
qc.ry(-6.07076549231012,[5])
qc.cz([6], [8])
qc.ry(-0.453970563708018,[6])
qc.cz([7], [8])
qc.ry(3.20447956487865,[7])
qc.ry(4.10821623363221,[8])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8])