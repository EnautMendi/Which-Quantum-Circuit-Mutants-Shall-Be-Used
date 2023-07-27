from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(4, 4)
qc.ry(-3.06308642559242,[0])
qc.ry(2.72340535390947,[1])
qc.ry(0.265311444342159,[2])
qc.ry(0.514277021350485,[3])
qc.cx([2], [3])
qc.cx([1], [2])
qc.cx([0], [1])
qc.ry(-0.626185121622286,[0])
qc.ry(-1.50946128815491,[1])
qc.ry(-1.47510618895348,[2])
qc.ry(-2.08850927511392,[3])
qc.cx([2], [3])
qc.cx([1], [2])
qc.cx([0], [1])
qc.ry(0.626161051104292,[0])
qc.ry(-1.70448256544942,[1])
qc.ry(1.15402592474415,[2])
qc.ry(-1.8017500381226,[3])
qc.barrier([0], [1], [2], [3])