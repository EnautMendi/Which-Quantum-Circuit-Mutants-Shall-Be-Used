from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(16, 16)
qc.ry(0.309602454579779,[0])
qc.ry(0.688581737413529,[1])
qc.cx([0], [1])
qc.ry(0.597789766365786,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.ry(0.838352552409257,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.ry(0.505937469028761,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.ry(0.345321113498101,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.ry(0.279714862877441,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.ry(0.433597835289769,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.ry(0.43227606870269,[8])
qc.cx([0], [8])
qc.cx([1], [8])
qc.cx([2], [8])
qc.cx([3], [8])
qc.cx([4], [8])
qc.cx([5], [8])
qc.cx([6], [8])
qc.cx([7], [8])
qc.ry(0.720141259138327,[9])
qc.cx([0], [9])
qc.cx([1], [9])
qc.cx([2], [9])
qc.cx([3], [9])
qc.cx([4], [9])
qc.cx([5], [9])
qc.cx([6], [9])
qc.cx([7], [9])
qc.cx([8], [9])
qc.ry(0.209103749457534,[10])
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
qc.ry(0.525978442190176,[11])
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
qc.ry(0.528042294413316,[12])
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
qc.ry(0.897536892134629,[13])
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
qc.ry(0.186181026298937,[14])
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
qc.ry(0.552606258060479,[15])
qc.cx([0], [15])
qc.ry(0.628723080377272,[0])
qc.cx([1], [15])
qc.ry(0.27160514045646,[1])
qc.cx([0], [1])
qc.cx([2], [15])
qc.ry(0.88295336816042,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [15])
qc.ry(0.254535720966281,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [15])
qc.ry(0.883944180451021,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [15])
qc.ry(0.175419380113107,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.cx([6], [15])
qc.ry(0.606980284816426,[6])
qc.cx([0], [6])
qc.cx([1], [6])
qc.cx([2], [6])
qc.cx([3], [6])
qc.cx([4], [6])
qc.cx([5], [6])
qc.cx([7], [15])
qc.ry(0.353211748533947,[7])
qc.cx([0], [7])
qc.cx([1], [7])
qc.cx([2], [7])
qc.cx([3], [7])
qc.cx([4], [7])
qc.cx([5], [7])
qc.cx([6], [7])
qc.cx([8], [15])
qc.ry(0.952991293389754,[8])
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
qc.ry(0.203309685548777,[10])
qc.cx([11], [15])
qc.ry(0.588747485782231,[11])
qc.cx([12], [15])
qc.ry(0.976382046336365,[12])
qc.cx([13], [15])
qc.ry(0.64523762103144,[13])
qc.cx([14], [15])
qc.ry(0.497214363629023,[14])
qc.ry(0.196954368769536,[15])
qc.ry(0.903269748492472,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.cx([0], [13])
qc.cx([0], [14])
qc.cx([0], [15])
qc.ry(0.911257002974277,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.cx([1], [13])
qc.cx([1], [14])
qc.cx([1], [15])
qc.ry(0.379427522720854,[1])
qc.cx([0], [1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.cx([2], [13])
qc.cx([2], [14])
qc.cx([2], [15])
qc.ry(0.764463193912259,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.cx([3], [13])
qc.cx([3], [14])
qc.cx([3], [15])
qc.ry(0.5864736383109,[3])
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
qc.ry(0.10185020140023,[4])
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
qc.ry(0.680644816801045,[5])
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
qc.ry(0.762512650446397,[6])
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
qc.ry(0.974845460639242,[7])
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
qc.ry(0.0105435391983203,[8])
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
qc.ry(0.685064569882309,[10])
qc.cx([11], [15])
qc.ry(0.457695875700832,[11])
qc.cx([12], [15])
qc.ry(0.445207024305249,[12])
qc.cx([13], [15])
qc.ry(0.0627711106842986,[13])
qc.cx([14], [15])
qc.ry(0.651379347328404,[14])
qc.ry(0.219840591985887,[15])
qc.ry(0.0283490069369944,[9])
qc.cx([0], [9])
qc.cx([0], [10])
qc.cx([0], [11])
qc.cx([0], [12])
qc.cx([0], [13])
qc.cx([0], [14])
qc.cx([0], [15])
qc.ry(0.906384924609017,[0])
qc.cx([1], [9])
qc.cx([1], [10])
qc.cx([1], [11])
qc.cx([1], [12])
qc.cx([1], [13])
qc.cx([1], [14])
qc.cx([1], [15])
qc.ry(0.758180235113576,[1])
qc.cx([2], [9])
qc.cx([2], [10])
qc.cx([2], [11])
qc.cx([2], [12])
qc.cx([2], [13])
qc.cx([2], [14])
qc.cx([2], [15])
qc.ry(0.248352560269009,[2])
qc.cx([3], [9])
qc.cx([3], [10])
qc.cx([3], [11])
qc.cx([3], [12])
qc.cx([3], [13])
qc.cx([3], [14])
qc.cx([3], [15])
qc.ry(0.36023230241525,[3])
qc.cx([4], [9])
qc.cx([4], [10])
qc.cx([4], [11])
qc.cx([4], [12])
qc.cx([4], [13])
qc.cx([4], [14])
qc.cx([4], [15])
qc.ry(0.0706991635502142,[4])
qc.cx([5], [9])
qc.cx([5], [10])
qc.cx([5], [11])
qc.cx([5], [12])
qc.cx([5], [13])
qc.cx([5], [14])
qc.cx([5], [15])
qc.ry(0.944349163589865,[5])
qc.cx([6], [9])
qc.cx([6], [10])
qc.cx([6], [11])
qc.cx([6], [12])
qc.cx([6], [13])
qc.cx([6], [14])
qc.cx([6], [15])
qc.ry(0.827280410483464,[6])
qc.cx([7], [9])
qc.cx([7], [10])
qc.cx([7], [11])
qc.cx([7], [12])
qc.cx([7], [13])
qc.cx([7], [14])
qc.cx([7], [15])
qc.ry(0.997266846702564,[7])
qc.cx([8], [9])
qc.cx([8], [10])
qc.cx([8], [11])
qc.cx([8], [12])
qc.cx([8], [13])
qc.cx([8], [14])
qc.cx([8], [15])
qc.ry(0.398916577299239,[8])
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
qc.ry(0.510746104616321,[10])
qc.cx([11], [15])
qc.ry(0.208390984814663,[11])
qc.cx([12], [15])
qc.ry(0.0490947084642475,[12])
qc.cx([13], [15])
qc.ry(0.144632434423718,[13])
qc.cx([14], [15])
qc.ry(0.235235275126818,[14])
qc.ry(0.904580042808843,[15])
qc.ry(0.795770369089207,[9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15])
