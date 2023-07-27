from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(16, 16)
qc.u(0.76623246,0.76941437,0.0,[0])
qc.u(0.66371225,0.50513073,0.0,[1])
qc.cx([0], [1])
qc.u(0.15763129,0.40087119,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.u(0.10183396,0.43194122,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.u(0.45032624,0.55837037,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.u(0.51736242,0.10135811,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.u(0.81404948,0.57613467,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.u(0.2564205,0.93343506,0.0,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.u(0.73332259,0.51301714,0.0,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.u(0.11737791,0.98423252,0.0,[9])
qc.cx([0], [9])
qc.cx([1], [9])
qc.cx([2], [9])
qc.cx([3], [9])
qc.cx([4], [9])
qc.cx([5], [9])
qc.cx([6], [9])
qc.cx([7], [9])
qc.cx([8], [9])
qc.u(0.76934583,0.32206424,0.0,[10])
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
qc.u(0.95644459,0.94873382,0.0,[11])
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
qc.u(0.31756983,0.6191836,0.0,[12])
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
qc.u(0.4067541,0.66273266,0.0,[13])
qc.cx([0], [13])
qc.cx([1], [13])
qc.cx([2], [13])
qc.cx([3], [13])
qc.cx([4], [13])
qc.cx([5], [13])
qc.cx([6], [13])
qc.cx([7], [13])
qc.cx([8], [13])
qc.cx([9], [13])
qc.cx([10], [13])
qc.cx([11], [13])
qc.cx([12], [13])
qc.u(0.26312283,0.8022065,0.0,[14])
qc.cx([0], [14])
qc.cx([1], [14])
qc.cx([2], [14])
qc.cx([3], [14])
qc.cx([4], [14])
qc.cx([5], [14])
qc.cx([6], [14])
qc.cx([7], [14])
qc.cx([8], [14])
qc.cx([9], [14])
qc.cx([10], [14])
qc.cx([11], [14])
qc.cx([12], [14])
qc.cx([13], [14])
qc.u(0.28692985,0.94742148,0.0,[15])
qc.cx([0], [15])
qc.u(0.011168326,0.46485468,0.0,[0])
qc.cx([1], [15])
qc.u(0.096928071,0.80124752,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [15])
qc.u(0.5262341,0.16027121,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [15])
qc.u(0.40303429,0.80020499,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [15])
qc.u(0.49888948,0.90446922,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [15])
qc.u(0.98574283,0.70719982,0.0,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [15])
qc.u(0.92504379,0.63552246,0.0,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.cx([7], [15])
qc.u(0.73489291,0.036504238,0.0,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.cx([8], [15])
qc.u(0.48260068,0.79917016,0.0,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.cx([9], [15])
qc.cx([10], [15])
qc.u(0.63132234,0.67629702,0.0,[10])
qc.cx([11], [15])
qc.u(0.59907477,0.50825314,0.0,[11])
qc.cx([12], [15])
qc.u(0.64965057,0.87519941,0.0,[12])
qc.cx([13], [15])
qc.u(0.26843545,0.62807353,0.0,[13])
qc.cx([14], [15])
qc.u(0.6870356,0.1963871,0.0,[14])
qc.u(0.22810757,0.9608164,0.0,[15])
qc.u(0.5358415,0.43527875,0.0,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.cx([0], [13])
qc.cx([0], [14])
qc.cx([0], [15])
qc.u(0.709561,0.69886808,0.0,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.cx([1], [13])
qc.cx([1], [14])
qc.cx([1], [15])
qc.u(0.70568828,0.56323369,0.0,[1])
qc.cx([0], [1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.cx([2], [13])
qc.cx([2], [14])
qc.cx([2], [15])
qc.u(0.0094446347,0.16349137,0.0,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.cx([3], [13])
qc.cx([3], [14])
qc.cx([3], [15])
qc.u(0.019434179,0.36987476,0.0,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [9])
qc.cx([4], [10])
qc.cx([4], [11])
qc.cx([4], [12])
qc.cx([4], [13])
qc.cx([4], [14])
qc.cx([4], [15])
qc.u(0.54624257,0.98862153,0.0,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [9])
qc.cx([5], [10])
qc.cx([5], [11])
qc.cx([5], [12])
qc.cx([5], [13])
qc.cx([5], [14])
qc.cx([5], [15])
qc.u(0.72059922,0.29132659,0.0,[5])
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
qc.cx([6], [14])
qc.cx([6], [15])
qc.u(0.16734451,0.24608176,0.0,[6])
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
qc.cx([7], [14])
qc.cx([7], [15])
qc.u(0.66357762,0.92585774,0.0,[7])
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
qc.cx([8], [14])
qc.cx([8], [15])
qc.u(0.43670558,0.7735326,0.0,[8])
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
qc.cx([11], [13])
qc.cx([12], [13])
qc.cx([9], [14])
qc.cx([10], [14])
qc.cx([11], [14])
qc.cx([12], [14])
qc.cx([13], [14])
qc.cx([9], [15])
qc.cx([10], [15])
qc.u(0.84490316,0.52242756,0.0,[10])
qc.cx([11], [15])
qc.u(0.41330533,0.76067687,0.0,[11])
qc.cx([12], [15])
qc.u(0.56123215,0.22908048,0.0,[12])
qc.cx([13], [15])
qc.u(0.77801135,0.48769468,0.0,[13])
qc.cx([14], [15])
qc.u(0.26312718,0.55417141,0.0,[14])
qc.u(0.62528623,0.77558934,0.0,[15])
qc.u(0.090769069,0.018401601,0.0,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.cx([0], [13])
qc.cx([0], [14])
qc.cx([0], [15])
qc.u(0.12543537,0.12310438,0.0,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.cx([1], [13])
qc.cx([1], [14])
qc.cx([1], [15])
qc.u(0.53987508,0.76275989,0.0,[1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.cx([2], [13])
qc.cx([2], [14])
qc.cx([2], [15])
qc.u(0.80084216,0.98631907,0.0,[2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.cx([3], [13])
qc.cx([3], [14])
qc.cx([3], [15])
qc.u(0.54945709,0.88292829,0.0,[3])
qc.cx([4], [9])
qc.cx([4], [10])
qc.cx([4], [11])
qc.cx([4], [12])
qc.cx([4], [13])
qc.cx([4], [14])
qc.cx([4], [15])
qc.u(0.20308,0.25354428,0.0,[4])
qc.cx([5], [9])
qc.cx([5], [10])
qc.cx([5], [11])
qc.cx([5], [12])
qc.cx([5], [13])
qc.cx([5], [14])
qc.cx([5], [15])
qc.u(0.94042494,0.033088646,0.0,[5])
qc.cx([6], [9])
qc.cx([6], [10])
qc.cx([6], [11])
qc.cx([6], [12])
qc.cx([6], [13])
qc.cx([6], [14])
qc.cx([6], [15])
qc.u(0.15794572,0.08696529,0.0,[6])
qc.cx([7], [9])
qc.cx([7], [10])
qc.cx([7], [11])
qc.cx([7], [12])
qc.cx([7], [13])
qc.cx([7], [14])
qc.cx([7], [15])
qc.u(0.8710577,0.4532953,0.0,[7])
qc.cx([8], [9])
qc.cx([8], [10])
qc.cx([8], [11])
qc.cx([8], [12])
qc.cx([8], [13])
qc.cx([8], [14])
qc.cx([8], [15])
qc.u(0.14236405,0.76164193,0.0,[8])
qc.cx([9], [10])
qc.cx([9], [11])
qc.cx([10], [11])
qc.cx([9], [12])
qc.cx([10], [12])
qc.cx([11], [12])
qc.cx([9], [13])
qc.cx([10], [13])
qc.cx([11], [13])
qc.cx([12], [13])
qc.cx([9], [14])
qc.cx([10], [14])
qc.cx([11], [14])
qc.cx([12], [14])
qc.cx([13], [14])
qc.cx([9], [15])
qc.cx([10], [15])
qc.u(0.41206593,0.49231233,0.0,[10])
qc.cx([11], [15])
qc.u(0.5767775,0.30872477,0.0,[11])
qc.cx([12], [15])
qc.u(0.38725963,0.50455524,0.0,[12])
qc.cx([13], [15])
qc.u(0.22485966,0.80355172,0.0,[13])
qc.cx([14], [15])
qc.u(0.007204121,0.088539281,0.0,[14])
qc.u(0.11827715,0.26827013,0.0,[15])
qc.u(0.77663179,0.70525549,0.0,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15])