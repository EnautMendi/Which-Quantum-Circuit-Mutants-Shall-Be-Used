from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(7, 7)
qc.ry(0.258478922210402,[0])
qc.ry(0.0377433563975456,[1])
qc.cx([0], [1])
qc.ry(0.41383390209608,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.ry(0.855939156829403,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.ry(0.491278229947736,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.ry(0.924296101608866,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.ry(0.0479441392905744,[6])
qc.cx([0], [6])
qc.ry(0.62020818988841,[0])
qc.cx([1], [6])
qc.ry(0.95747629516361,[1])
qc.cx([0], [1])
qc.cx([2], [6])
qc.ry(0.734681274725259,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [6])
qc.ry(0.999273717710759,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [6])
qc.ry(0.578432516394355,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [6])
qc.ry(0.33328809854314,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.ry(0.742354250092524,[6])
qc.cx([0], [6])
qc.ry(0.292376488525581,[0])
qc.cx([1], [6])
qc.ry(0.876724045995633,[1])
qc.cx([0], [1])
qc.cx([2], [6])
qc.ry(0.949319642115481,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [6])
qc.ry(0.474508953243935,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [6])
qc.ry(0.173733607828499,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [6])
qc.ry(0.922998993134187,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.ry(0.905603808652203,[6])
qc.cx([0], [6])
qc.ry(0.569124528807707,[0])
qc.cx([1], [6])
qc.ry(0.47884780189288,[1])
qc.cx([2], [6])
qc.ry(0.327402814576998,[2])
qc.cx([3], [6])
qc.ry(0.164952618522116,[3])
qc.cx([4], [6])
qc.ry(0.677448705929929,[4])
qc.cx([5], [6])
qc.ry(0.395591950843492,[5])
qc.ry(0.355090054024688,[6])
qc.barrier([0], [1], [2], [3], [4], [5], [6])
