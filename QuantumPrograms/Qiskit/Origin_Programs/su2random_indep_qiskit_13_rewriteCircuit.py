from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(13, 13)
qc.u(0.81539599,0.59644969,0.0,[0])
qc.u(0.57665304,0.52153593,0.0,[1])
qc.cx([0], [1])
qc.u(0.56754929,0.29713923,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.u(0.59567601,0.20432786,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.u(0.32720445,0.50497815,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.u(0.17577612,0.35572069,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.u(0.83180365,0.25601267,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.u(0.14272133,0.50659914,0.0,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.u(0.62595407,0.28988321,0.0,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.u(0.96177498,0.50776149,0.0,[9])
qc.cx([0], [9])
qc.cx([1], [9])
qc.cx([2], [9])
qc.cx([3], [9])
qc.cx([4], [9])
qc.cx([5], [9])
qc.cx([6], [9])
qc.cx([7], [9])
qc.cx([8], [9])
qc.u(0.42643112,0.94347069,0.0,[10])
qc.cx([0], [10])
qc.cx([1], [10])
qc.cx([2], [10])
qc.cx([3], [10])
qc.cx([4], [10])
qc.cx([5], [10])
qc.cx([6], [10])
qc.cx([7], [10])
qc.cx([8], [10])
qc.cx([9], [10])
qc.u(0.85517631,0.55138115,0.0,[11])
qc.cx([0], [11])
qc.cx([1], [11])
qc.cx([2], [11])
qc.cx([3], [11])
qc.cx([4], [11])
qc.cx([5], [11])
qc.cx([6], [11])
qc.cx([7], [11])
qc.cx([8], [11])
qc.cx([9], [11])
qc.cx([10], [11])
qc.u(0.13370522,0.52315439,0.0,[12])
qc.cx([0], [12])
qc.u(0.71381681,0.36015792,0.0,[0])
qc.cx([1], [12])
qc.u(0.83839747,0.25935194,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [12])
qc.u(0.47373432,0.1835121,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [12])
qc.u(0.40362573,0.99951022,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [12])
qc.u(0.71637637,0.0043456969,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [12])
qc.u(0.61195599,0.11621631,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [12])
qc.u(0.78785621,0.29647856,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.cx([7], [12])
qc.u(0.95815434,0.14058119,0.0,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.cx([8], [12])
qc.u(0.81754486,0.12814533,0.0,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.cx([9], [12])
qc.cx([10], [12])
qc.u(0.80089633,0.67033016,0.0,[10])
qc.cx([11], [12])
qc.u(0.27885714,0.92324621,0.0,[11])
qc.u(0.61328498,0.93948995,0.0,[12])
qc.u(0.10670262,0.95617864,0.0,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.u(0.19942516,0.85856698,0.0,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.u(0.8488962,0.50095993,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.u(0.67568348,0.14074344,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.u(0.62792877,0.7362474,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [9])
qc.cx([4], [10])
qc.cx([4], [11])
qc.cx([4], [12])
qc.u(0.17295464,0.78987868,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [9])
qc.cx([5], [10])
qc.cx([5], [11])
qc.cx([5], [12])
qc.u(0.74574037,0.83362639,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [9])
qc.cx([6], [10])
qc.cx([6], [11])
qc.cx([6], [12])
qc.u(0.73268419,0.34146292,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.cx([7], [9])
qc.cx([7], [10])
qc.cx([7], [11])
qc.cx([7], [12])
qc.u(0.82136985,0.2136547,0.0,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.cx([8], [9])
qc.cx([8], [10])
qc.cx([8], [11])
qc.cx([8], [12])
qc.u(0.49906049,0.15109044,0.0,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.cx([9], [10])
qc.cx([9], [11])
qc.cx([10], [11])
qc.cx([9], [12])
qc.cx([10], [12])
qc.u(0.89822678,0.67616407,0.0,[10])
qc.cx([11], [12])
qc.u(0.4411754,0.13525871,0.0,[11])
qc.u(0.51337143,0.047820869,0.0,[12])
qc.u(0.68884775,0.90984165,0.0,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.u(0.90569209,0.98916241,0.0,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.u(0.92194044,0.25050823,0.0,[1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.u(0.29279278,0.31430576,0.0,[2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.u(0.34402926,0.24923098,0.0,[3])
qc.cx([4], [9])
qc.cx([4], [10])
qc.cx([4], [11])
qc.cx([4], [12])
qc.u(0.93065159,0.50472137,0.0,[4])
qc.cx([5], [9])
qc.cx([5], [10])
qc.cx([5], [11])
qc.cx([5], [12])
qc.u(0.47822024,0.21588717,0.0,[5])
qc.cx([6], [9])
qc.cx([6], [10])
qc.cx([6], [11])
qc.cx([6], [12])
qc.u(0.43024272,0.78869457,0.0,[6])
qc.cx([7], [9])
qc.cx([7], [10])
qc.cx([7], [11])
qc.cx([7], [12])
qc.u(0.24234421,0.49109946,0.0,[7])
qc.cx([8], [9])
qc.cx([8], [10])
qc.cx([8], [11])
qc.cx([8], [12])
qc.u(0.13172695,0.5763358,0.0,[8])
qc.cx([9], [10])
qc.cx([9], [11])
qc.cx([10], [11])
qc.cx([9], [12])
qc.cx([10], [12])
qc.u(0.53798375,0.14437006,0.0,[10])
qc.cx([11], [12])
qc.u(0.92900861,0.35031581,0.0,[11])
qc.u(0.1051361,0.15583084,0.0,[12])
qc.u(0.16306125,0.96548833,0.0,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12])
