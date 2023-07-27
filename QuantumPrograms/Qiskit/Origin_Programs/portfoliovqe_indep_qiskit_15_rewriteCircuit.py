from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(15, 15)
qc.ry(4.8898328481057,[0])
qc.ry(-4.15317199660482,[1])
qc.cz([0], [1])
qc.ry(-5.22116419374587,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.ry(0.757953030744394,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.ry(2.03841835649822,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.ry(-3.54396447158216,[5])
qc.cz([0], [5])
qc.cz([1], [5])
qc.cz([2], [5])
qc.cz([3], [5])
qc.cz([4], [5])
qc.ry(-0.525581306807385,[6])
qc.cz([0], [6])
qc.cz([1], [6])
qc.cz([2], [6])
qc.cz([3], [6])
qc.cz([4], [6])
qc.cz([5], [6])
qc.ry(3.30918382585694,[7])
qc.cz([0], [7])
qc.cz([1], [7])
qc.cz([2], [7])
qc.cz([3], [7])
qc.cz([4], [7])
qc.cz([5], [7])
qc.cz([6], [7])
qc.ry(1.44364019277442,[8])
qc.cz([0], [8])
qc.cz([1], [8])
qc.cz([2], [8])
qc.cz([3], [8])
qc.cz([4], [8])
qc.cz([5], [8])
qc.cz([6], [8])
qc.cz([7], [8])
qc.ry(-2.82732633337571,[9])
qc.cz([0], [9])
qc.cz([1], [9])
qc.cz([2], [9])
qc.cz([3], [9])
qc.cz([4], [9])
qc.cz([5], [9])
qc.cz([6], [9])
qc.cz([7], [9])
qc.cz([8], [9])
qc.ry(6.96849771200161,[10])
qc.cz([0], [10])
qc.cz([1], [10])
qc.cz([2], [10])
qc.cz([3], [10])
qc.cz([4], [10])
qc.cz([5], [10])
qc.cz([6], [10])
qc.cz([7], [10])
qc.cz([8], [10])
qc.cz([9], [10])
qc.ry(4.87231261177424,[11])
qc.cz([0], [11])
qc.cz([1], [11])
qc.cz([2], [11])
qc.cz([3], [11])
qc.cz([4], [11])
qc.cz([5], [11])
qc.cz([6], [11])
qc.cz([7], [11])
qc.cz([8], [11])
qc.cz([9], [11])
qc.cz([10], [11])
qc.ry(-3.29646323455821,[12])
qc.cz([0], [12])
qc.cz([1], [12])
qc.cz([2], [12])
qc.cz([3], [12])
qc.cz([4], [12])
qc.cz([5], [12])
qc.cz([6], [12])
qc.cz([7], [12])
qc.cz([8], [12])
qc.cz([9], [12])
qc.cz([10], [12])
qc.cz([11], [12])
qc.ry(-1.49318621762032,[13])
qc.cz([0], [13])
qc.cz([1], [13])
qc.cz([2], [13])
qc.cz([3], [13])
qc.cz([4], [13])
qc.cz([5], [13])
qc.cz([6], [13])
qc.cz([7], [13])
qc.cz([8], [13])
qc.cz([9], [13])
qc.cz([10], [13])
qc.cz([11], [13])
qc.cz([12], [13])
qc.ry(5.21784508899711,[14])
qc.cz([0], [14])
qc.ry(3.85785570554679,[0])
qc.cz([1], [14])
qc.ry(0.969876790825957,[1])
qc.cz([0], [1])
qc.cz([2], [14])
qc.ry(4.260008284245,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.cz([3], [14])
qc.ry(-2.08447008838339,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.cz([4], [14])
qc.ry(-6.1147507788225,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.cz([5], [14])
qc.ry(-2.16925745550965,[5])
qc.cz([0], [5])
qc.cz([1], [5])
qc.cz([2], [5])
qc.cz([3], [5])
qc.cz([4], [5])
qc.cz([6], [14])
qc.ry(5.98375166105255,[6])
qc.cz([0], [6])
qc.cz([1], [6])
qc.cz([2], [6])
qc.cz([3], [6])
qc.cz([4], [6])
qc.cz([5], [6])
qc.cz([7], [14])
qc.ry(3.59387512118983,[7])
qc.cz([0], [7])
qc.cz([1], [7])
qc.cz([2], [7])
qc.cz([3], [7])
qc.cz([4], [7])
qc.cz([5], [7])
qc.cz([6], [7])
qc.cz([8], [14])
qc.ry(1.74101284790754,[8])
qc.cz([0], [8])
qc.cz([1], [8])
qc.cz([2], [8])
qc.cz([3], [8])
qc.cz([4], [8])
qc.cz([5], [8])
qc.cz([6], [8])
qc.cz([7], [8])
qc.cz([9], [14])
qc.cz([10], [14])
qc.ry(-1.9771817773484,[10])
qc.cz([11], [14])
qc.ry(-2.49277265364506,[11])
qc.cz([12], [14])
qc.ry(4.5114260340439,[12])
qc.cz([13], [14])
qc.ry(-0.821155706864711,[13])
qc.ry(-0.0389552751140041,[14])
qc.ry(-0.763971949356187,[9])
qc.cz([0], [9])
qc.cz([0], [10])
qc.cz([0], [11])
qc.cz([0], [12])
qc.cz([0], [13])
qc.cz([0], [14])
qc.ry(1.88073402197018,[0])
qc.cz([1], [9])
qc.cz([1], [10])
qc.cz([1], [11])
qc.cz([1], [12])
qc.cz([1], [13])
qc.cz([1], [14])
qc.ry(4.50057703711696,[1])
qc.cz([0], [1])
qc.cz([2], [9])
qc.cz([2], [10])
qc.cz([2], [11])
qc.cz([2], [12])
qc.cz([2], [13])
qc.cz([2], [14])
qc.ry(-1.30291408924606,[2])
qc.cz([0], [2])
qc.cz([1], [2])
qc.cz([3], [9])
qc.cz([3], [10])
qc.cz([3], [11])
qc.cz([3], [12])
qc.cz([3], [13])
qc.cz([3], [14])
qc.ry(-2.02155161014493,[3])
qc.cz([0], [3])
qc.cz([1], [3])
qc.cz([2], [3])
qc.cz([4], [9])
qc.cz([4], [10])
qc.cz([4], [11])
qc.cz([4], [12])
qc.cz([4], [13])
qc.cz([4], [14])
qc.ry(6.20859861183761,[4])
qc.cz([0], [4])
qc.cz([1], [4])
qc.cz([2], [4])
qc.cz([3], [4])
qc.cz([5], [9])
qc.cz([5], [10])
qc.cz([5], [11])
qc.cz([5], [12])
qc.cz([5], [13])
qc.cz([5], [14])
qc.ry(-1.54309372561589,[5])
qc.cz([0], [5])
qc.cz([1], [5])
qc.cz([2], [5])
qc.cz([3], [5])
qc.cz([4], [5])
qc.cz([6], [9])
qc.cz([6], [10])
qc.cz([6], [11])
qc.cz([6], [12])
qc.cz([6], [13])
qc.cz([6], [14])
qc.ry(2.64137444315512,[6])
qc.cz([0], [6])
qc.cz([1], [6])
qc.cz([2], [6])
qc.cz([3], [6])
qc.cz([4], [6])
qc.cz([5], [6])
qc.cz([7], [9])
qc.cz([7], [10])
qc.cz([7], [11])
qc.cz([7], [12])
qc.cz([7], [13])
qc.cz([7], [14])
qc.ry(0.195694799095922,[7])
qc.cz([0], [7])
qc.cz([1], [7])
qc.cz([2], [7])
qc.cz([3], [7])
qc.cz([4], [7])
qc.cz([5], [7])
qc.cz([6], [7])
qc.cz([8], [9])
qc.cz([8], [10])
qc.cz([8], [11])
qc.cz([8], [12])
qc.cz([8], [13])
qc.cz([8], [14])
qc.ry(2.05139413141059,[8])
qc.cz([0], [8])
qc.cz([1], [8])
qc.cz([2], [8])
qc.cz([3], [8])
qc.cz([4], [8])
qc.cz([5], [8])
qc.cz([6], [8])
qc.cz([7], [8])
qc.cz([9], [10])
qc.cz([9], [11])
qc.cz([10], [11])
qc.cz([9], [12])
qc.cz([10], [12])
qc.cz([11], [12])
qc.cz([9], [13])
qc.cz([10], [13])
qc.cz([11], [13])
qc.cz([12], [13])
qc.cz([9], [14])
qc.cz([10], [14])
qc.ry(-2.15529706382438,[10])
qc.cz([11], [14])
qc.ry(-5.20911591311842,[11])
qc.cz([12], [14])
qc.ry(4.15068701131486,[12])
qc.cz([13], [14])
qc.ry(1.19487255813962,[13])
qc.ry(-0.341626866681518,[14])
qc.ry(3.93239139416652,[9])
qc.cz([0], [9])
qc.cz([0], [10])
qc.cz([0], [11])
qc.cz([0], [12])
qc.cz([0], [13])
qc.cz([0], [14])
qc.ry(-1.07071939732077,[0])
qc.cz([1], [9])
qc.cz([1], [10])
qc.cz([1], [11])
qc.cz([1], [12])
qc.cz([1], [13])
qc.cz([1], [14])
qc.ry(1.02912997937311,[1])
qc.cz([2], [9])
qc.cz([2], [10])
qc.cz([2], [11])
qc.cz([2], [12])
qc.cz([2], [13])
qc.cz([2], [14])
qc.ry(-3.62511202981549,[2])
qc.cz([3], [9])
qc.cz([3], [10])
qc.cz([3], [11])
qc.cz([3], [12])
qc.cz([3], [13])
qc.cz([3], [14])
qc.ry(2.17084305262621,[3])
qc.cz([4], [9])
qc.cz([4], [10])
qc.cz([4], [11])
qc.cz([4], [12])
qc.cz([4], [13])
qc.cz([4], [14])
qc.ry(2.50379722215675,[4])
qc.cz([5], [9])
qc.cz([5], [10])
qc.cz([5], [11])
qc.cz([5], [12])
qc.cz([5], [13])
qc.cz([5], [14])
qc.ry(-2.06707456620007,[5])
qc.cz([6], [9])
qc.cz([6], [10])
qc.cz([6], [11])
qc.cz([6], [12])
qc.cz([6], [13])
qc.cz([6], [14])
qc.ry(-1.24959483464095,[6])
qc.cz([7], [9])
qc.cz([7], [10])
qc.cz([7], [11])
qc.cz([7], [12])
qc.cz([7], [13])
qc.cz([7], [14])
qc.ry(5.94920009803049,[7])
qc.cz([8], [9])
qc.cz([8], [10])
qc.cz([8], [11])
qc.cz([8], [12])
qc.cz([8], [13])
qc.cz([8], [14])
qc.ry(5.59942964352025,[8])
qc.cz([9], [10])
qc.cz([9], [11])
qc.cz([10], [11])
qc.cz([9], [12])
qc.cz([10], [12])
qc.cz([11], [12])
qc.cz([9], [13])
qc.cz([10], [13])
qc.cz([11], [13])
qc.cz([12], [13])
qc.cz([9], [14])
qc.cz([10], [14])
qc.ry(5.711651932252,[10])
qc.cz([11], [14])
qc.ry(5.94901077016846,[11])
qc.cz([12], [14])
qc.ry(3.09332213825045,[12])
qc.cz([13], [14])
qc.ry(-5.44805038244566,[13])
qc.ry(-5.18158190749963,[14])
qc.ry(1.47450276090364,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14])