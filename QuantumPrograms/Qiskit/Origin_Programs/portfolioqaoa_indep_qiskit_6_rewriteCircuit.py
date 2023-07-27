from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(6, 6)
qc.u(1.5707963267948966,-3.0353524e-05,-3.141592653589793,[0])
qc.u(1.5707963267948966,-3.7986612e-06,-3.141592653589793,[1])
qc.rzz(-0.0262391625046928,[0], [1])
qc.u(1.5707963267948966,0.00015561292,-3.141592653589793,[2])
qc.rzz(-0.0262375265385264,[0], [2])
qc.rzz(-0.0262381191423384,[1], [2])
qc.u(1.5707963267948966,7.6054596e-05,-3.141592653589793,[3])
qc.rzz(-0.0262391215490247,[0], [3])
qc.rzz(-0.0262388554932538,[1], [3])
qc.rzz(-0.0262389854262818,[2], [3])
qc.u(1.5707963267948966,-3.7946743e-05,-3.141592653589793,[4])
qc.rzz(-0.0262382604459212,[0], [4])
qc.rzz(-0.0262390366673601,[1], [4])
qc.rzz(-0.0262392617513034,[2], [4])
qc.rzz(-0.0262385724310715,[3], [4])
qc.u(1.5707963267948966,-0.00014975057,-3.141592653589793,[5])
qc.rzz(-0.0262403722994893,[0], [5])
qc.u(3.0099168,-1.5703345,1.5707963267948966,[0])
qc.rzz(-0.0262392176399683,[1], [5])
qc.u(3.0099168,-1.5707385,1.5707963267948966,[1])
qc.rzz(0.399245557389473,[0], [1])
qc.rzz(-0.0262378972135298,[2], [5])
qc.u(3.0099168,-1.5731641,1.5707963267948966,[2])
qc.rzz(0.399220665123042,[0], [2])
qc.rzz(0.399229681967204,[1], [2])
qc.rzz(-0.0262381353548895,[3], [5])
qc.u(3.0099168,-1.5719535,1.5707963267948966,[3])
qc.rzz(0.399244934222917,[0], [3])
qc.rzz(0.399240886015031,[1], [3])
qc.rzz(0.399242863028747,[2], [3])
qc.rzz(-0.0262376202159157,[4], [5])
qc.u(3.0099168,-1.5702189,1.5707963267948966,[4])
qc.rzz(0.399231831991148,[0], [4])
qc.rzz(0.399243642694366,[1], [4])
qc.rzz(0.399247067489818,[2], [4])
qc.rzz(0.399236579043772,[3], [4])
qc.u(3.0099168,-1.5685178,1.5707963267948966,[5])
qc.rzz(0.399263965187273,[0], [5])
qc.u(1.2410916,-1.5689178,1.5707963267948966,[0])
qc.rzz(0.39924639630778,[1], [5])
qc.u(1.2410916,-1.5705612,1.5707963267948966,[1])
qc.rzz(1.62388420493979,[0], [1])
qc.rzz(0.399226305179135,[2], [5])
qc.u(1.2410916,-1.5804269,1.5707963267948966,[2])
qc.rzz(1.62378295858267,[0], [2])
qc.rzz(1.62381963353257,[1], [2])
qc.rzz(0.399229928651487,[3], [5])
qc.u(1.2410916,-1.5755032,1.5707963267948966,[3])
qc.rzz(1.62388167028334,[0], [3])
qc.rzz(1.62386520467534,[1], [3])
qc.rzz(1.6238732459454,[2], [3])
qc.rzz(0.399222090484141,[4], [5])
qc.u(1.2410916,-1.5684479,1.5707963267948966,[4])
qc.rzz(1.62382837850132,[0], [4])
qc.rzz(1.62387641714333,[1], [4])
qc.rzz(1.6238903470948,[2], [4])
qc.rzz(1.62384768657785,[3], [4])
qc.u(1.2410916,-1.5615286,1.5707963267948966,[5])
qc.rzz(1.62395907648574,[0], [5])
qc.rx(-10.8720078390703,[0])
qc.rzz(1.62388761714104,[1], [5])
qc.rx(-10.8720078390703,[1])
qc.rzz(1.62380589884546,[2], [5])
qc.rx(-10.8720078390703,[2])
qc.rzz(1.62382063689179,[3], [5])
qc.rx(-10.8720078390703,[3])
qc.rzz(1.62378875607079,[4], [5])
qc.rx(-10.8720078390703,[4])
qc.rx(-10.8720078390703,[5])
qc.barrier([0], [1], [2], [3], [4], [5])
qc.barrier([0], [1], [2], [3], [4], [5])