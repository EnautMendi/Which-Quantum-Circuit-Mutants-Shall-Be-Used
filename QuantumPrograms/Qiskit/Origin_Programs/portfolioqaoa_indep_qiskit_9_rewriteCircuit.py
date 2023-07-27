from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(9, 9)
qc.u(1.5707963267948966,0.14059963,-3.141592653589793,[0])
qc.u(1.5707963267948966,0.082409025,-3.141592653589793,[1])
qc.rzz(6.23442350793244,[0], [1])
qc.u(1.5707963267948966,0.057802489,-3.141592653589793,[2])
qc.rzz(6.23512370493558,[0], [2])
qc.rzz(6.23425090531118,[1], [2])
qc.u(1.5707963267948966,0.067091474,-3.141592653589793,[3])
qc.rzz(6.23506765430636,[0], [3])
qc.rzz(6.23401465039992,[1], [3])
qc.rzz(6.23434747281187,[2], [3])
qc.u(1.5707963267948966,0.047956392,-3.141592653589793,[4])
qc.rzz(6.23458889552302,[0], [4])
qc.rzz(6.23422358183959,[1], [4])
qc.rzz(6.23412141369661,[2], [4])
qc.rzz(6.2346394745859,[3], [4])
qc.u(1.5707963267948966,0.1366565,-3.141592653589793,[5])
qc.rzz(6.23517186578468,[0], [5])
qc.rzz(6.23457748733653,[1], [5])
qc.rzz(6.23421079187134,[2], [5])
qc.rzz(6.23496282931193,[3], [5])
qc.rzz(6.23482318478054,[4], [5])
qc.u(1.5707963267948966,-0.013625469,-3.141592653589793,[6])
qc.rzz(6.2334200995321,[0], [6])
qc.rzz(6.234119776156,[1], [6])
qc.rzz(6.23341569584497,[2], [6])
qc.rzz(6.23412553073492,[3], [6])
qc.rzz(6.23514813142005,[4], [6])
qc.rzz(6.23544455109819,[5], [6])
qc.u(1.5707963267948966,0.033472564,-3.141592653589793,[7])
qc.rzz(6.23289371629,[0], [7])
qc.rzz(6.23399312109084,[1], [7])
qc.rzz(6.23350650173547,[2], [7])
qc.rzz(6.23435610103826,[3], [7])
qc.rzz(6.23434684800211,[4], [7])
qc.rzz(6.23366331426667,[5], [7])
qc.rzz(6.23517067025314,[6], [7])
qc.u(1.5707963267948966,-0.14890331,-3.141592653589793,[8])
qc.rzz(6.23011699855504,[0], [8])
qc.u(1.9265278,-0.26474099,-1.5707963267948966,[0])
qc.rzz(6.23451445564708,[1], [8])
qc.u(1.9265278,-0.2821296,-1.5707963267948966,[1])
qc.rzz(1.86298044809906,[0], [1])
qc.rzz(6.23350543906189,[2], [8])
qc.u(1.9265278,-0.28948257,-1.5707963267948966,[2])
qc.rzz(1.86318968209239,[0], [2])
qc.rzz(1.8629288707065,[1], [2])
qc.rzz(6.23396772551841,[3], [8])
qc.u(1.9265278,-0.28670682,-1.5707963267948966,[3])
qc.rzz(1.86317293295332,[0], [3])
qc.rzz(1.86285827263437,[1], [3])
qc.rzz(1.86295772716218,[2], [3])
qc.rzz(6.23346044822913,[4], [8])
qc.u(1.9265278,-0.29242479,-1.5707963267948966,[4])
qc.rzz(1.86302986948457,[0], [4])
qc.rzz(1.86292070586282,[1], [4])
qc.rzz(1.8628901758142,[2], [4])
qc.rzz(1.86304498360139,[3], [4])
qc.rzz(6.23574699211864,[5], [8])
qc.u(1.9265278,-0.26591929,-1.5707963267948966,[5])
qc.rzz(1.86320407359469,[0], [5])
qc.rzz(1.86302646047195,[1], [5])
qc.rzz(1.86291688394396,[2], [5])
qc.rzz(1.86314160898009,[3], [5])
qc.rzz(1.86309988017688,[4], [5])
qc.rzz(6.23417937143397,[6], [8])
qc.u(1.9265278,-0.31082678,-1.5707963267948966,[6])
qc.rzz(1.86268060798892,[0], [6])
qc.rzz(1.86288968648169,[1], [6])
qc.rzz(1.86267929207206,[2], [6])
qc.rzz(1.8628914060742,[3], [6])
qc.rzz(1.86319698125372,[4], [6])
qc.rzz(1.86328555785813,[5], [6])
qc.rzz(6.23429269928017,[7], [8])
qc.u(1.9265278,-0.29675288,-1.5707963267948966,[7])
qc.rzz(1.86252331330289,[0], [7])
qc.rzz(1.86285183921165,[1], [7])
qc.rzz(1.86270642683413,[2], [7])
qc.rzz(1.86296030546265,[3], [7])
qc.rzz(1.86295754045553,[4], [7])
qc.rzz(1.86275328580662,[5], [7])
qc.rzz(1.86320371634403,[6], [7])
qc.u(1.9265278,-0.35125073,-1.5707963267948966,[8])
qc.rzz(1.8616935700486,[0], [8])
qc.u(2.1666678,-1.5566364,1.5707963267948966,[0])
qc.rzz(1.86300762524126,[1], [8])
qc.u(2.1666678,-1.5565022,1.5707963267948966,[1])
qc.rzz(-0.0143716796563463,[0], [1])
qc.rzz(1.86270610928431,[2], [8])
qc.u(2.1666678,-1.5564455,1.5707963267948966,[2])
qc.rzz(-0.0143732937602025,[0], [2])
qc.rzz(-0.0143712817703866,[1], [2])
qc.rzz(1.8628442504659,[3], [8])
qc.u(2.1666678,-1.5564669,1.5707963267948966,[3])
qc.rzz(-0.0143731645515136,[0], [3])
qc.rzz(-0.014370737152284,[1], [3])
qc.rzz(-0.0143715043791304,[2], [3])
qc.rzz(1.86269266505138,[4], [8])
qc.u(2.1666678,-1.5564228,1.5707963267948966,[4])
qc.rzz(-0.014372060910117,[0], [4])
qc.rzz(-0.0143712187839404,[1], [4])
qc.rzz(-0.0143709832645183,[2], [4])
qc.rzz(-0.0143721775056753,[3], [4])
qc.rzz(1.86337593376973,[5], [8])
qc.u(2.1666678,-1.5566273,1.5707963267948966,[5])
qc.rzz(-0.0143734047812607,[0], [5])
qc.rzz(-0.0143720346118071,[1], [5])
qc.rzz(-0.014371189300328,[2], [5])
qc.rzz(-0.0143729229074806,[3], [5])
qc.rzz(-0.0143726009969674,[4], [5])
qc.rzz(1.86290749483839,[6], [8])
qc.u(2.1666678,-1.5562808,1.5707963267948966,[6])
qc.rzz(-0.0143693665853661,[0], [6])
qc.rzz(-0.0143709794896369,[1], [6])
qc.rzz(-0.0143693564339254,[2], [6])
qc.rzz(-0.0143709927551721,[3], [6])
qc.rzz(-0.0143733500684738,[4], [6])
qc.rzz(-0.0143740333792326,[5], [6])
qc.rzz(1.86294135964745,[7], [8])
qc.u(2.1666678,-1.5563894,1.5707963267948966,[7])
qc.rzz(-0.0143681531594058,[0], [7])
qc.rzz(-0.0143706875226217,[1], [7])
qc.rzz(-0.0143695657609253,[2], [7])
qc.rzz(-0.0143715242690376,[3], [7])
qc.rzz(-0.0143715029388102,[4], [7])
qc.rzz(-0.0143699272473501,[5], [7])
qc.rzz(-0.0143734020253048,[6], [7])
qc.u(2.1666678,-1.555969,1.5707963267948966,[8])
qc.rzz(-0.0143617522311192,[0], [8])
qc.rx(-11.4431149897736,[0])
qc.rzz(-0.0143718893102812,[1], [8])
qc.rx(-11.4431149897736,[1])
qc.rzz(-0.0143695633112354,[2], [8])
qc.rx(-11.4431149897736,[2])
qc.rzz(-0.0143706289803954,[3], [8])
qc.rx(-11.4431149897736,[3])
qc.rzz(-0.0143694595977429,[4], [8])
qc.rx(-11.4431149897736,[4])
qc.rzz(-0.0143747305704733,[5], [8])
qc.rx(-11.4431149897736,[5])
qc.rzz(-0.0143711168694994,[6], [8])
qc.rx(-11.4431149897736,[6])
qc.rzz(-0.0143713781144244,[7], [8])
qc.rx(-11.4431149897736,[7])
qc.rx(-11.4431149897736,[8])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8])
