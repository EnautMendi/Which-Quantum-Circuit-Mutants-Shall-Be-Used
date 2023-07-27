from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(13, 13)
qc.h([0])
qc.h([1])
qc.h([2])
qc.h([3])
qc.h([4])
qc.rzz(-8.13527256149611,[3], [4])
qc.h([5])
qc.rzz(-8.13527256149611,[1], [5])
qc.h([6])
qc.rzz(-8.13527256149611,[5], [6])
qc.rx(-2.49691267632598,[5])
qc.h([7])
qc.rzz(-8.13527256149611,[2], [7])
qc.h([8])
qc.rzz(-8.13527256149611,[0], [8])
qc.rzz(-8.13527256149611,[3], [8])
qc.rx(-2.49691267632598,[3])
qc.rx(-2.49691267632598,[8])
qc.h([9])
qc.rzz(-8.13527256149611,[1], [9])
qc.rx(-2.49691267632598,[1])
qc.rzz(5.6384216744499,[1], [5])
qc.rzz(-8.13527256149611,[7], [9])
qc.rx(-2.49691267632598,[7])
qc.rx(-2.49691267632598,[9])
qc.rzz(5.6384216744499,[1], [9])
qc.rx(4.99379102182518,[1])
qc.h([10])
qc.rzz(-8.13527256149611,[6], [10])
qc.rx(-2.49691267632598,[6])
qc.rzz(5.6384216744499,[5], [6])
qc.rx(4.99379102182518,[5])
qc.h([11])
qc.rzz(-8.13527256149611,[4], [11])
qc.rzz(-8.13527256149611,[10], [11])
qc.rx(-2.49691267632598,[10])
qc.rx(-2.49691267632598,[11])
qc.rx(-2.49691267632598,[4])
qc.rzz(5.6384216744499,[3], [4])
qc.rzz(5.6384216744499,[4], [11])
qc.rx(4.99379102182518,[4])
qc.rzz(5.6384216744499,[6], [10])
qc.rzz(5.6384216744499,[10], [11])
qc.rx(4.99379102182518,[10])
qc.rx(4.99379102182518,[11])
qc.rx(4.99379102182518,[6])
qc.h([12])
qc.rzz(-8.13527256149611,[0], [12])
qc.rx(-2.49691267632598,[0])
qc.rzz(5.6384216744499,[0], [8])
qc.rzz(-8.13527256149611,[2], [12])
qc.rx(-2.49691267632598,[12])
qc.rzz(5.6384216744499,[0], [12])
qc.rx(4.99379102182518,[0])
qc.rx(-2.49691267632598,[2])
qc.rzz(5.6384216744499,[2], [7])
qc.rzz(5.6384216744499,[2], [12])
qc.rx(4.99379102182518,[12])
qc.rx(4.99379102182518,[2])
qc.rzz(5.6384216744499,[3], [8])
qc.rx(4.99379102182518,[3])
qc.rzz(5.6384216744499,[7], [9])
qc.rx(4.99379102182518,[7])
qc.rx(4.99379102182518,[8])
qc.rx(4.99379102182518,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12])
