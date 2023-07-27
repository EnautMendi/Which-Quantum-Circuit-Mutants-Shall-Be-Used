from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(4, 4)
qc.ry(6.39895244257109,[0])
qc.ry(-2.65545332677397,[1])
qc.cz([0], [1])
qc.ry(2.24399645113615,[0])
qc.ry(4.30074251662019,[2])
qc.cz([1], [2])
qc.ry(-4.13127412867375,[1])
qc.cz([0], [1])
qc.ry(-2.72510760634829,[0])
qc.ry(-5.00137370937142,[3])
qc.cz([2], [3])
qc.ry(3.11789536237741,[2])
qc.cz([1], [2])
qc.ry(7.01896016901562,[1])
qc.cz([0], [1])
qc.ry(0.92556202682689,[0])
qc.ry(4.04358952341942,[3])
qc.cz([2], [3])
qc.ry(3.4220449620582,[2])
qc.cz([1], [2])
qc.ry(2.52311099453506,[1])
qc.cz([0], [1])
qc.ry(-3.6733347632896,[0])
qc.ry(-3.0969112176004,[3])
qc.cz([2], [3])
qc.ry(3.39875737412341,[2])
qc.cz([1], [2])
qc.ry(5.16959104687041,[1])
qc.cz([0], [1])
qc.ry(-3.11211705088501,[0])
qc.ry(6.9671370300791,[3])
qc.cz([2], [3])
qc.ry(-3.76619289597362,[2])
qc.cz([1], [2])
qc.ry(4.60923563707103,[1])
qc.ry(5.61939718326072,[3])
qc.cz([2], [3])
qc.ry(-4.1423518633464,[2])
qc.ry(5.67284961632846,[3])
qc.barrier([0], [1], [2], [3])