from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(10, 10)
qc.u(0.40601932,0.41951635,0.0,[0])
qc.u(0.84554581,0.39169732,0.0,[1])
qc.cx([0], [1])
qc.u(0.69370628,0.42347122,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.u(0.82451,0.54880734,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.u(0.37963718,0.18774503,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.u(0.33852353,0.97268586,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.u(0.55327228,0.41324435,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.u(0.53422746,0.43804386,0.0,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.u(0.38579938,0.39798042,0.0,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.u(0.26524045,0.70921876,0.0,[9])
qc.cx([0], [9])
qc.u(0.16174228,0.58834918,0.0,[0])
qc.cx([1], [9])
qc.u(0.39600498,0.90023723,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [9])
qc.u(0.63793777,0.95417125,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [9])
qc.u(0.37779426,0.85333324,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [9])
qc.u(0.0044259923,0.45955313,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [9])
qc.u(0.25113833,0.65370828,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [9])
qc.u(0.76015739,0.35149429,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.cx([7], [9])
qc.u(0.012686498,0.92740905,0.0,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.cx([8], [9])
qc.u(0.17922068,0.7049376,0.0,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.u(0.30896749,0.39587579,0.0,[9])
qc.cx([0], [9])
qc.u(0.013408919,0.60448355,0.0,[0])
qc.cx([1], [9])
qc.u(0.23876691,0.040713971,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [9])
qc.u(0.28137415,0.51733826,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [9])
qc.u(0.92137437,0.43395468,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [9])
qc.u(0.39829461,0.022381474,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [9])
qc.u(0.19097258,0.78753438,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [9])
qc.u(0.82136309,0.44944503,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.cx([7], [9])
qc.u(0.3713402,0.61053852,0.0,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.cx([8], [9])
qc.u(0.93953161,0.11504785,0.0,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.u(0.12664409,0.65185928,0.0,[9])
qc.cx([0], [9])
qc.u(0.68212067,0.26893079,0.0,[0])
qc.cx([1], [9])
qc.u(0.4951238,0.500807,0.0,[1])
qc.cx([2], [9])
qc.u(0.41314339,0.70192142,0.0,[2])
qc.cx([3], [9])
qc.u(0.75983943,0.14320458,0.0,[3])
qc.cx([4], [9])
qc.u(0.73572852,0.39791537,0.0,[4])
qc.cx([5], [9])
qc.u(0.77601978,0.059140672,0.0,[5])
qc.cx([6], [9])
qc.u(0.7475417,0.91299932,0.0,[6])
qc.cx([7], [9])
qc.u(0.29953851,0.60604238,0.0,[7])
qc.cx([8], [9])
qc.u(0.21734925,0.37930764,0.0,[8])
qc.u(0.078443248,0.6763985,0.0,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9])
