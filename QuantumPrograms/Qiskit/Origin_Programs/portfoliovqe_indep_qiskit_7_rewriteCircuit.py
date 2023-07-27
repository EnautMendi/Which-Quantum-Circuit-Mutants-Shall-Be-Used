from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(7, 7)
qc.ry(-2.14290606159216,[0])
qc.ry(5.47833043985983,[1])
qc.cz([0], [1])
qc.ry(-0.288763323793469,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.ry(1.45371914754079,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.ry(-1.77652645063657,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.ry(5.9004582793651,[5])
qc.cz([0], [5])
qc.cz([1], [5])
qc.cz([2], [5])
qc.cz([3], [5])
qc.cz([4], [5])
qc.ry(-5.10335010092611,[6])
qc.cz([0], [6])
qc.ry(3.09034754292102,[0])
qc.cz([1], [6])
qc.ry(2.08217256004961,[1])
qc.cz([0], [1])
qc.cz([2], [6])
qc.ry(2.49099975833541,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.cz([3], [6])
qc.ry(-1.98743147483112,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.cz([4], [6])
qc.ry(-5.24605021380542,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.cz([5], [6])
qc.ry(5.63371638207843,[5])
qc.cz([0], [5])
qc.cz([1], [5])
qc.cz([2], [5])
qc.cz([3], [5])
qc.cz([4], [5])
qc.ry(4.64268871618194,[6])
qc.cz([0], [6])
qc.ry(3.23538208655265,[0])
qc.cz([1], [6])
qc.ry(-1.38861532905733,[1])
qc.cz([0], [1])
qc.cz([2], [6])
qc.ry(1.75262853597122,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.cz([3], [6])
qc.ry(-1.26911746782014,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.cz([4], [6])
qc.ry(-4.91924102202175,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.cz([5], [6])
qc.ry(5.03070528795433,[5])
qc.cz([0], [5])
qc.cz([1], [5])
qc.cz([2], [5])
qc.cz([3], [5])
qc.cz([4], [5])
qc.ry(1.98796434881346,[6])
qc.cz([0], [6])
qc.ry(5.34471502361142,[0])
qc.cz([1], [6])
qc.ry(2.2524035705158,[1])
qc.cz([2], [6])
qc.ry(1.69414899193581,[2])
qc.cz([3], [6])
qc.ry(-2.59646334619788,[3])
qc.cz([4], [6])
qc.ry(5.67266419969344,[4])
qc.cz([5], [6])
qc.ry(4.53830035544274,[5])
qc.ry(2.22307162083226,[6])
qc.barrier([0], [1], [2], [3], [4], [5], [6])
