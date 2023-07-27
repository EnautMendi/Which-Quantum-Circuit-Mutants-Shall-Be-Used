from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(14, 14)
qc.ry(0.927924890448546,[0])
qc.ry(0.0182287053360705,[1])
qc.cx([0], [1])
qc.ry(0.325393609359943,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.ry(0.899794349353552,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.ry(0.632254023305495,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.ry(0.160917974214691,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.ry(0.513104487739389,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.ry(0.819995381226262,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.ry(0.504076634413846,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.ry(0.305591136998612,[9])
qc.cx([0], [9])
qc.cx([1], [9])
qc.cx([2], [9])
qc.cx([3], [9])
qc.cx([4], [9])
qc.cx([5], [9])
qc.cx([6], [9])
qc.cx([7], [9])
qc.cx([8], [9])
qc.ry(0.105998309181109,[10])
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
qc.ry(0.318691524126826,[11])
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
qc.ry(0.776908525899072,[12])
qc.cx([0], [12])
qc.cx([1], [12])
qc.cx([2], [12])
qc.cx([3], [12])
qc.cx([4], [12])
qc.cx([5], [12])
qc.cx([6], [12])
qc.cx([7], [12])
qc.cx([8], [12])
qc.cx([9], [12])
qc.cx([10], [12])
qc.cx([11], [12])
qc.ry(0.578056755534364,[13])
qc.cx([0], [13])
qc.ry(0.632144610220604,[0])
qc.cx([1], [13])
qc.ry(0.685985697384495,[1])
qc.cx([0], [1])
qc.cx([2], [13])
qc.ry(0.358223406120526,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [13])
qc.ry(0.937578912975049,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [13])
qc.ry(0.199102934456653,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [13])
qc.ry(0.595578315256437,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [13])
qc.ry(0.459246990700067,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.cx([7], [13])
qc.ry(0.127561120028196,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.cx([8], [13])
qc.ry(0.458446994323708,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.cx([9], [13])
qc.cx([10], [13])
qc.ry(0.835932617357549,[10])
qc.cx([11], [13])
qc.ry(0.757701847948063,[11])
qc.cx([12], [13])
qc.ry(0.229229721164737,[12])
qc.ry(0.136129820544141,[13])
qc.ry(0.449011808109206,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.cx([0], [13])
qc.ry(0.463135893470527,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.cx([1], [13])
qc.ry(0.742173135358051,[1])
qc.cx([0], [1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.cx([2], [13])
qc.ry(0.0539722962939259,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.cx([3], [13])
qc.ry(0.146461409027544,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [9])
qc.cx([4], [10])
qc.cx([4], [11])
qc.cx([4], [12])
qc.cx([4], [13])
qc.ry(0.479591952781158,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [9])
qc.cx([5], [10])
qc.cx([5], [11])
qc.cx([5], [12])
qc.cx([5], [13])
qc.ry(0.428047477416914,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [9])
qc.cx([6], [10])
qc.cx([6], [11])
qc.cx([6], [12])
qc.cx([6], [13])
qc.ry(0.202460203376376,[6])
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
qc.cx([7], [13])
qc.ry(0.65814991257868,[7])
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
qc.cx([8], [13])
qc.ry(0.259496648342295,[8])
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
qc.cx([11], [12])
qc.cx([9], [13])
qc.cx([10], [13])
qc.ry(0.573952349545806,[10])
qc.cx([11], [13])
qc.ry(0.92207604536996,[11])
qc.cx([12], [13])
qc.ry(0.256686447653142,[12])
qc.ry(0.73047339250647,[13])
qc.ry(0.255070043063025,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.cx([0], [13])
qc.ry(0.195391431996294,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.cx([1], [13])
qc.ry(0.0187512817977433,[1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.cx([2], [13])
qc.ry(0.225339643651838,[2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.cx([3], [13])
qc.ry(0.152800566904636,[3])
qc.cx([4], [9])
qc.cx([4], [10])
qc.cx([4], [11])
qc.cx([4], [12])
qc.cx([4], [13])
qc.ry(0.889823199704199,[4])
qc.cx([5], [9])
qc.cx([5], [10])
qc.cx([5], [11])
qc.cx([5], [12])
qc.cx([5], [13])
qc.ry(0.116494052464662,[5])
qc.cx([6], [9])
qc.cx([6], [10])
qc.cx([6], [11])
qc.cx([6], [12])
qc.cx([6], [13])
qc.ry(0.91472240559736,[6])
qc.cx([7], [9])
qc.cx([7], [10])
qc.cx([7], [11])
qc.cx([7], [12])
qc.cx([7], [13])
qc.ry(0.730056693661726,[7])
qc.cx([8], [9])
qc.cx([8], [10])
qc.cx([8], [11])
qc.cx([8], [12])
qc.cx([8], [13])
qc.ry(0.837749913806449,[8])
qc.cx([9], [10])
qc.cx([9], [11])
qc.cx([10], [11])
qc.cx([9], [12])
qc.cx([10], [12])
qc.cx([11], [12])
qc.cx([9], [13])
qc.cx([10], [13])
qc.ry(0.694525699087507,[10])
qc.cx([11], [13])
qc.ry(0.788958092469402,[11])
qc.cx([12], [13])
qc.ry(0.071329437758482,[12])
qc.ry(0.821904482315219,[13])
qc.ry(0.959753966935657,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13])