from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(6, 6)
qc.u(1.3500331,-3.141592653589793,0.0,[0])
qc.u(0.78625794,-3.141592653589793,0.0,[1])
qc.cz([0], [1])
qc.u(0.22841666,0.0,-3.141592653589793,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.u(1.0769188,-3.141592653589793,0.0,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.u(0.59782258,0.0,-3.141592653589793,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.u(1.591018,0.0,-3.141592653589793,[5])
qc.cz([0], [5])
qc.ry(3.94248685615585,[0])
qc.cz([1], [5])
qc.ry(4.63074690329306,[1])
qc.cz([2], [5])
qc.ry(0.787631193173361,[2])
qc.cz([3], [5])
qc.ry(1.58641526847451,[3])
qc.cz([4], [5])
qc.ry(2.80130870428177,[4])
qc.ry(4.05354585996659,[5])
qc.barrier([0], [1], [2], [3], [4], [5])