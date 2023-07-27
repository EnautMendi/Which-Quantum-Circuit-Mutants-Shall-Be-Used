from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(3, 3)
qc.ry(0.836963112359282,[0])
qc.ry(0.571083728275385,[1])
qc.cx([0], [1])
qc.ry(0.0636784390368105,[2])
qc.cx([0], [2])
qc.ry(0.281039345928896,[0])
qc.cx([1], [2])
qc.ry(0.0809992491384852,[1])
qc.cx([0], [1])
qc.ry(0.546810273029464,[2])
qc.cx([0], [2])
qc.ry(0.0555633185371374,[0])
qc.cx([1], [2])
qc.ry(0.80715686876096,[1])
qc.cx([0], [1])
qc.ry(0.288211461126035,[2])
qc.cx([0], [2])
qc.ry(0.351866819664277,[0])
qc.cx([1], [2])
qc.ry(0.131713846323771,[1])
qc.ry(0.152013197833987,[2])
qc.barrier([0], [1], [2])