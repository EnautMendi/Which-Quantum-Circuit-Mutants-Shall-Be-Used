from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(3, 3)
qc.u(1.5707963267948966,0.41951949,-3.141592653589793,[0])
qc.u(1.5707963267948966,0.41620669,-3.141592653589793,[1])
qc.rzz(-0.420917333908502,[0], [1])
qc.u(1.5707963267948966,0.41905329,-3.141592653589793,[2])
qc.rzz(-0.421016123405307,[0], [2])
qc.u(2.2348228,1.2558831,-1.5707963267948966,[0])
qc.rzz(-0.420940441831552,[1], [2])
qc.u(2.2348228,1.2087537,-1.5707963267948966,[1])
qc.rzz(-5.98815838177421,[0], [1])
qc.u(2.2348228,1.2492507,-1.5707963267948966,[2])
qc.rzz(-5.98956380537088,[0], [2])
qc.u(0.56042125,-1.2358007,1.5707963267948966,[0])
qc.rzz(-5.98848712542991,[1], [2])
qc.u(0.56042125,-1.2880621,1.5707963267948966,[1])
qc.rzz(-6.64023274758061,[0], [1])
qc.u(0.56042125,-1.2431553,1.5707963267948966,[2])
qc.rzz(-6.6417912133385,[0], [2])
qc.rx(-4.06512402388918,[0])
qc.rzz(-6.64059728943955,[1], [2])
qc.rx(-4.06512402388918,[1])
qc.rx(-4.06512402388918,[2])
qc.barrier([0], [1], [2])
qc.barrier([0], [1], [2])
