from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(6, 6)
qc.h([0])
qc.h([1])
qc.h([2])
qc.rzz(5.62724885812889,[0], [2])
qc.h([3])
qc.rzz(5.62724885812889,[0], [3])
qc.rx(-5.04047412391158,[0])
qc.h([4])
qc.rzz(5.62724885812889,[1], [4])
qc.rzz(5.62724885812889,[2], [4])
qc.rx(-5.04047412391158,[2])
qc.rzz(-4.38434633329271,[0], [2])
qc.rx(-5.04047412391158,[4])
qc.h([5])
qc.rzz(5.62724885812889,[1], [5])
qc.rx(-5.04047412391158,[1])
qc.rzz(-4.38434633329271,[1], [4])
qc.rzz(-4.38434633329271,[2], [4])
qc.rx(-5.62738622902127,[2])
qc.rzz(5.62724885812889,[3], [5])
qc.rx(-5.04047412391158,[3])
qc.rzz(-4.38434633329271,[0], [3])
qc.rx(-5.62738622902127,[0])
qc.rx(-5.62738622902127,[4])
qc.rx(-5.04047412391158,[5])
qc.rzz(-4.38434633329271,[1], [5])
qc.rx(-5.62738622902127,[1])
qc.rzz(-4.38434633329271,[3], [5])
qc.rx(-5.62738622902127,[3])
qc.rx(-5.62738622902127,[5])
qc.barrier([0], [1], [2], [3], [4], [5])
qc.barrier([0], [1], [2], [3], [4], [5])