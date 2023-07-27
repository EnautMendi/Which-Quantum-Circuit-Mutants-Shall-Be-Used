from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(5, 5)
qc.h([0])
qc.h([1])
qc.rzz(-3.66638380291587,[0], [1])
qc.h([2])
qc.rzz(-3.66638380291587,[0], [2])
qc.rx(-2.03854567383379,[0])
qc.h([3])
qc.rzz(-3.66638380291587,[1], [3])
qc.rx(-2.03854567383379,[1])
qc.rzz(2.03847737548037,[0], [1])
qc.h([4])
qc.rzz(-3.66638380291587,[2], [4])
qc.rx(-2.03854567383379,[2])
qc.rzz(2.03847737548037,[0], [2])
qc.rx(-12.0417655497439,[0])
qc.rzz(-3.66638380291587,[3], [4])
qc.rx(-2.03854567383379,[3])
qc.rzz(2.03847737548037,[1], [3])
qc.rx(-12.0417655497439,[1])
qc.rx(-2.03854567383379,[4])
qc.rzz(2.03847737548037,[2], [4])
qc.rx(-12.0417655497439,[2])
qc.rzz(2.03847737548037,[3], [4])
qc.rx(-12.0417655497439,[3])
qc.rx(-12.0417655497439,[4])
qc.barrier([0], [1], [2], [3], [4])
qc.barrier([0], [1], [2], [3], [4])
