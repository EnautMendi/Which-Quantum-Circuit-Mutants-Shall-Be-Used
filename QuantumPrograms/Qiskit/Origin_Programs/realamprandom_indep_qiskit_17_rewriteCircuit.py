from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(17, 17)
qc.ry(0.0227058568871136,[0])
qc.ry(0.672832421075552,[1])
qc.cx([0], [1])
qc.ry(0.226729318932959,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.ry(0.296366429110743,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.ry(0.230832019631364,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.ry(0.134280096876062,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.ry(0.701711835395929,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.ry(0.570211315447566,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.ry(0.254081384708909,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.ry(0.233174367591907,[9])
qc.cx([0], [9])
qc.cx([1], [9])
qc.cx([2], [9])
qc.cx([3], [9])
qc.cx([4], [9])
qc.cx([5], [9])
qc.cx([6], [9])
qc.cx([7], [9])
qc.cx([8], [9])
qc.ry(0.529921967864969,[10])
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
qc.ry(0.779922508154488,[11])
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
qc.ry(0.0995754955413721,[12])
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
qc.ry(0.325407126680427,[13])
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
qc.ry(0.475028216627048,[14])
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
qc.ry(0.80847278991274,[15])
qc.cx([0], [15])
qc.cx([1], [15])
qc.cx([2], [15])
qc.cx([3], [15])
qc.cx([4], [15])
qc.cx([5], [15])
qc.cx([6], [15])
qc.cx([7], [15])
qc.cx([8], [15])
qc.cx([9], [15])
qc.cx([10], [15])
qc.cx([11], [15])
qc.cx([12], [15])
qc.cx([13], [15])
qc.cx([14], [15])
qc.ry(0.195491202450158,[16])
qc.cx([0], [16])
qc.ry(0.676463932458146,[0])
qc.cx([1], [16])
qc.ry(0.367562198827702,[1])
qc.cx([0], [1])
qc.cx([2], [16])
qc.ry(0.620534571540216,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [16])
qc.ry(0.0911157950508982,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [16])
qc.ry(0.135100237437327,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [16])
qc.ry(0.00819472361409912,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [16])
qc.ry(0.92304636467849,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.cx([7], [16])
qc.ry(0.0736710096875282,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.cx([8], [16])
qc.ry(0.940432131189974,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.cx([9], [16])
qc.cx([10], [16])
qc.ry(0.22470087356363,[10])
qc.cx([11], [16])
qc.ry(0.929006933521285,[11])
qc.cx([12], [16])
qc.ry(0.580257800603702,[12])
qc.cx([13], [16])
qc.ry(0.0299602713981576,[13])
qc.cx([14], [16])
qc.ry(0.460616524996138,[14])
qc.cx([15], [16])
qc.ry(0.981220931740173,[15])
qc.ry(0.87712953810206,[16])
qc.ry(0.707789792534798,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.cx([0], [13])
qc.cx([0], [14])
qc.cx([0], [15])
qc.cx([0], [16])
qc.ry(0.312609577543702,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.cx([1], [13])
qc.cx([1], [14])
qc.cx([1], [15])
qc.cx([1], [16])
qc.ry(0.267433080768668,[1])
qc.cx([0], [1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.cx([2], [13])
qc.cx([2], [14])
qc.cx([2], [15])
qc.cx([2], [16])
qc.ry(0.722483880120942,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.cx([3], [13])
qc.cx([3], [14])
qc.cx([3], [15])
qc.cx([3], [16])
qc.ry(0.00877725365039994,[3])
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
qc.cx([4], [16])
qc.ry(0.790668481881025,[4])
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
qc.cx([5], [16])
qc.ry(0.69613366600588,[5])
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
qc.cx([6], [16])
qc.ry(0.958643169313435,[6])
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
qc.cx([7], [16])
qc.ry(0.206219904573434,[7])
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
qc.cx([8], [16])
qc.ry(0.991144189438134,[8])
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
qc.cx([11], [15])
qc.cx([12], [15])
qc.cx([13], [15])
qc.cx([14], [15])
qc.cx([9], [16])
qc.cx([10], [16])
qc.ry(0.347872949812181,[10])
qc.cx([11], [16])
qc.ry(0.269742796725187,[11])
qc.cx([12], [16])
qc.ry(0.550115648707986,[12])
qc.cx([13], [16])
qc.ry(0.111773376107941,[13])
qc.cx([14], [16])
qc.ry(0.0740217931666743,[14])
qc.cx([15], [16])
qc.ry(0.374467753007798,[15])
qc.ry(0.911242366587788,[16])
qc.ry(0.531021535265009,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.cx([0], [13])
qc.cx([0], [14])
qc.cx([0], [15])
qc.cx([0], [16])
qc.ry(0.749877707326461,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.cx([1], [13])
qc.cx([1], [14])
qc.cx([1], [15])
qc.cx([1], [16])
qc.ry(0.379336536508149,[1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.cx([2], [13])
qc.cx([2], [14])
qc.cx([2], [15])
qc.cx([2], [16])
qc.ry(0.282811643138413,[2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.cx([3], [13])
qc.cx([3], [14])
qc.cx([3], [15])
qc.cx([3], [16])
qc.ry(0.416655733179258,[3])
qc.cx([4], [9])
qc.cx([4], [10])
qc.cx([4], [11])
qc.cx([4], [12])
qc.cx([4], [13])
qc.cx([4], [14])
qc.cx([4], [15])
qc.cx([4], [16])
qc.ry(0.38909562633486,[4])
qc.cx([5], [9])
qc.cx([5], [10])
qc.cx([5], [11])
qc.cx([5], [12])
qc.cx([5], [13])
qc.cx([5], [14])
qc.cx([5], [15])
qc.cx([5], [16])
qc.ry(0.658099855662394,[5])
qc.cx([6], [9])
qc.cx([6], [10])
qc.cx([6], [11])
qc.cx([6], [12])
qc.cx([6], [13])
qc.cx([6], [14])
qc.cx([6], [15])
qc.cx([6], [16])
qc.ry(0.555148561263049,[6])
qc.cx([7], [9])
qc.cx([7], [10])
qc.cx([7], [11])
qc.cx([7], [12])
qc.cx([7], [13])
qc.cx([7], [14])
qc.cx([7], [15])
qc.cx([7], [16])
qc.ry(0.929038997806185,[7])
qc.cx([8], [9])
qc.cx([8], [10])
qc.cx([8], [11])
qc.cx([8], [12])
qc.cx([8], [13])
qc.cx([8], [14])
qc.cx([8], [15])
qc.cx([8], [16])
qc.ry(0.0895161167769063,[8])
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
qc.cx([11], [15])
qc.cx([12], [15])
qc.cx([13], [15])
qc.cx([14], [15])
qc.cx([9], [16])
qc.cx([10], [16])
qc.ry(0.971653229186716,[10])
qc.cx([11], [16])
qc.ry(0.412329877651624,[11])
qc.cx([12], [16])
qc.ry(0.609229808449673,[12])
qc.cx([13], [16])
qc.ry(0.12190858160406,[13])
qc.cx([14], [16])
qc.ry(0.136696944505125,[14])
qc.cx([15], [16])
qc.ry(0.202732935138556,[15])
qc.ry(0.279051566395336,[16])
qc.ry(0.239523268613142,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16])