from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(9, 9)
qc.ry(7.25327787095917,[0])
qc.ry(-6.88788023219094,[1])
qc.cz([0], [1])
qc.ry(8.66182932999031,[0])
qc.ry(9.15472389859815,[2])
qc.cz([1], [2])
qc.ry(6.24076623189969,[1])
qc.cz([0], [1])
qc.ry(-1.24533237955598,[0])
qc.ry(-1.9713111959082,[3])
qc.cz([2], [3])
qc.ry(-1.08830882140974,[2])
qc.cz([1], [2])
qc.ry(3.48639488111997,[1])
qc.cz([0], [1])
qc.ry(0.671455181758693,[0])
qc.ry(0.281324730098761,[4])
qc.cz([3], [4])
qc.ry(4.99201726125454,[3])
qc.cz([2], [3])
qc.ry(0.536404434197177,[2])
qc.cz([1], [2])
qc.ry(-2.57153259794858,[1])
qc.cz([0], [1])
qc.ry(-4.03339367432971,[0])
qc.ry(-3.67583585618042,[5])
qc.cz([4], [5])
qc.ry(5.06435761171533,[4])
qc.cz([3], [4])
qc.ry(7.42957716353456,[3])
qc.cz([2], [3])
qc.ry(2.2711304788871,[2])
qc.cz([1], [2])
qc.ry(-2.56474612790048,[1])
qc.cz([0], [1])
qc.ry(2.64485510292275,[0])
qc.ry(7.69667340844459,[6])
qc.cz([5], [6])
qc.ry(5.85151499522699,[5])
qc.cz([4], [5])
qc.ry(-5.85520581147733,[4])
qc.cz([3], [4])
qc.ry(-1.74840684261686,[3])
qc.cz([2], [3])
qc.ry(-5.17699981322553,[2])
qc.cz([1], [2])
qc.ry(-3.42899429768101,[1])
qc.ry(2.1777075684582,[7])
qc.cz([6], [7])
qc.ry(2.79472936757164,[6])
qc.cz([5], [6])
qc.ry(5.67233223584468,[5])
qc.cz([4], [5])
qc.ry(0.00294870444981293,[4])
qc.cz([3], [4])
qc.ry(-3.02663202888983,[3])
qc.cz([2], [3])
qc.ry(-4.65365084240599,[2])
qc.ry(-0.806286231905951,[8])
qc.cz([7], [8])
qc.ry(-7.2818515194565,[7])
qc.cz([6], [7])
qc.ry(-1.9526962478148,[6])
qc.cz([5], [6])
qc.ry(2.79162845580876,[5])
qc.cz([4], [5])
qc.ry(4.59854628828586,[4])
qc.cz([3], [4])
qc.ry(4.66160248266181,[3])
qc.ry(4.19855983413589,[8])
qc.cz([7], [8])
qc.ry(-3.57712596465951,[7])
qc.cz([6], [7])
qc.ry(4.11592330418091,[6])
qc.cz([5], [6])
qc.ry(2.0103503355065,[5])
qc.cz([4], [5])
qc.ry(-8.00215965024567,[4])
qc.ry(-3.26897007645218,[8])
qc.cz([7], [8])
qc.ry(-0.735486726731869,[7])
qc.cz([6], [7])
qc.ry(-0.12967019386461,[6])
qc.cz([5], [6])
qc.ry(-2.65656277721467,[5])
qc.ry(-0.0635587346876099,[8])
qc.cz([7], [8])
qc.ry(-5.83382185393679,[7])
qc.cz([6], [7])
qc.ry(1.30114232532937,[6])
qc.ry(-6.20760869274277,[8])
qc.cz([7], [8])
qc.ry(1.78108396869468,[7])
qc.ry(6.23096981158631,[8])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8])
