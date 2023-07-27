from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(8, 8)
qc.u(0.72615213,0.74297789,0.0,[0])
qc.u(0.93108527,0.96205144,0.0,[1])
qc.cx([0], [1])
qc.u(0.29653679,0.72632616,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.u(0.53011372,0.097366868,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.u(0.98819601,0.7405613,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.u(0.99239815,0.67205173,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.u(0.43758555,0.65335534,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.u(0.45896413,0.4458605,0.0,[7])
qc.cx([0], [7])
qc.u(0.41447446,0.15665265,0.0,[0])
qc.cx([1], [7])
qc.u(0.0855734,0.21420559,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [7])
qc.u(0.15244139,0.56623369,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [7])
qc.u(0.094965287,0.95707458,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [7])
qc.u(0.67217832,0.39397896,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [7])
qc.u(0.44121573,0.31414276,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [7])
qc.u(0.44697619,0.9555532,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.u(0.057098753,0.041043621,0.0,[7])
qc.cx([0], [7])
qc.u(0.49149724,0.54032652,0.0,[0])
qc.cx([1], [7])
qc.u(0.3786459,0.40116102,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [7])
qc.u(0.3473507,0.40120509,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [7])
qc.u(0.75037997,0.2202503,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [7])
qc.u(0.68210742,0.45324984,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [7])
qc.u(0.15071077,0.92687776,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [7])
qc.u(0.12819036,0.58518614,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.u(0.37261971,0.92546425,0.0,[7])
qc.cx([0], [7])
qc.u(0.18517038,0.28221103,0.0,[0])
qc.cx([1], [7])
qc.u(0.74167581,0.34162706,0.0,[1])
qc.cx([2], [7])
qc.u(0.66519099,0.54938377,0.0,[2])
qc.cx([3], [7])
qc.u(0.45033343,0.52985812,0.0,[3])
qc.cx([4], [7])
qc.u(0.91859379,0.46310197,0.0,[4])
qc.cx([5], [7])
qc.u(0.70680654,0.046963147,0.0,[5])
qc.cx([6], [7])
qc.u(0.21165849,0.029976006,0.0,[6])
qc.u(0.62895544,0.96956114,0.0,[7])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7])
