from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(4, 4)
qc.ry(4.38902787056145,[0])
qc.ry(-0.773458764355351,[1])
qc.cz([0], [1])
qc.ry(0.176876102258767,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.ry(-0.481235900285375,[3])
qc.cz([0], [3])
qc.ry(4.11674195428327,[0])
qc.cz([1], [3])
qc.ry(3.55192487880099,[1])
qc.cz([0], [1])
qc.cz([2], [3])
qc.ry(0.891578107475493,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.ry(2.18965537790507,[3])
qc.cz([0], [3])
qc.ry(5.15512553806975,[0])
qc.cz([1], [3])
qc.ry(-2.03561082582181,[1])
qc.cz([0], [1])
qc.cz([2], [3])
qc.ry(3.92551945027863,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.ry(3.56703428476674,[3])
qc.cz([0], [3])
qc.ry(0.877898827626657,[0])
qc.cz([1], [3])
qc.ry(-3.67671218635784,[1])
qc.cz([2], [3])
qc.ry(-3.31120487021356,[2])
qc.ry(3.07010267540377,[3])
qc.barrier([0], [1], [2], [3])