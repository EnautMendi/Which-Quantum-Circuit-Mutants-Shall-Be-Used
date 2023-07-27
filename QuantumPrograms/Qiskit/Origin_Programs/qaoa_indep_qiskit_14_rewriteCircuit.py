from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(14, 14)
qc.h([0])
qc.h([1])
qc.h([2])
qc.h([3])
qc.rzz(-1.72738882967696,[2], [3])
qc.h([4])
qc.h([5])
qc.rzz(-1.72738882967696,[4], [5])
qc.h([6])
qc.rzz(-1.72738882967696,[5], [6])
qc.rx(10.1318791112575,[5])
qc.h([7])
qc.rzz(-1.72738882967696,[4], [7])
qc.rx(10.1318791112575,[4])
qc.rzz(2.43450520081955,[4], [5])
qc.rzz(-1.72738882967696,[6], [7])
qc.rx(10.1318791112575,[6])
qc.rzz(2.43450520081955,[5], [6])
qc.rx(-1.41421095512528,[5])
qc.rx(10.1318791112575,[7])
qc.rzz(2.43450520081955,[4], [7])
qc.rx(-1.41421095512528,[4])
qc.rzz(2.43450520081955,[6], [7])
qc.rx(-1.41421095512528,[6])
qc.rx(-1.41421095512528,[7])
qc.h([8])
qc.h([9])
qc.rzz(-1.72738882967696,[1], [9])
qc.rzz(-1.72738882967696,[8], [9])
qc.rx(10.1318791112575,[9])
qc.h([10])
qc.rzz(-1.72738882967696,[0], [10])
qc.h([11])
qc.rzz(-1.72738882967696,[0], [11])
qc.rx(10.1318791112575,[0])
qc.rzz(-1.72738882967696,[3], [11])
qc.rx(10.1318791112575,[11])
qc.rx(10.1318791112575,[3])
qc.h([12])
qc.rzz(-1.72738882967696,[1], [12])
qc.rx(10.1318791112575,[1])
qc.rzz(2.43450520081955,[1], [9])
qc.rzz(-1.72738882967696,[8], [12])
qc.rx(10.1318791112575,[12])
qc.rzz(2.43450520081955,[1], [12])
qc.rx(-1.41421095512528,[1])
qc.rx(10.1318791112575,[8])
qc.rzz(2.43450520081955,[8], [9])
qc.rzz(2.43450520081955,[8], [12])
qc.rx(-1.41421095512528,[12])
qc.rx(-1.41421095512528,[8])
qc.rx(-1.41421095512528,[9])
qc.h([13])
qc.rzz(-1.72738882967696,[2], [13])
qc.rzz(-1.72738882967696,[10], [13])
qc.rx(10.1318791112575,[10])
qc.rzz(2.43450520081955,[0], [10])
qc.rzz(2.43450520081955,[0], [11])
qc.rx(-1.41421095512528,[0])
qc.rx(10.1318791112575,[13])
qc.rx(10.1318791112575,[2])
qc.rzz(2.43450520081955,[2], [3])
qc.rzz(2.43450520081955,[2], [13])
qc.rzz(2.43450520081955,[10], [13])
qc.rx(-1.41421095512528,[10])
qc.rx(-1.41421095512528,[13])
qc.rx(-1.41421095512528,[2])
qc.rzz(2.43450520081955,[3], [11])
qc.rx(-1.41421095512528,[11])
qc.rx(-1.41421095512528,[3])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13])
