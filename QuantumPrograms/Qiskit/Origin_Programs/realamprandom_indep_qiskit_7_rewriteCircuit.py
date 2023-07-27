from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(7, 7)
qc.ry(0.783682709352997,[0])
qc.ry(0.659768782870392,[1])
qc.cx([0], [1])
qc.ry(0.655514283359269,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.ry(0.751855011871936,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.ry(0.11276168580456,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.ry(0.0330204136625072,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.ry(0.697857471840325,[6])
qc.cx([0], [6])
qc.ry(0.942143441444552,[0])
qc.cx([1], [6])
qc.ry(0.436907412462656,[1])
qc.cx([0], [1])
qc.cx([2], [6])
qc.ry(0.989183385317161,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [6])
qc.ry(0.63396522145249,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [6])
qc.ry(0.13439356153129,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [6])
qc.ry(0.818720622344007,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.ry(0.998452330083134,[6])
qc.cx([0], [6])
qc.ry(0.383130249629609,[0])
qc.cx([1], [6])
qc.ry(0.594238834266465,[1])
qc.cx([0], [1])
qc.cx([2], [6])
qc.ry(0.407173230160596,[2])
qc.cx([0], [2])
qc.cx([1], [2])
qc.cx([3], [6])
qc.ry(0.991509901292922,[3])
qc.cx([0], [3])
qc.cx([1], [3])
qc.cx([2], [3])
qc.cx([4], [6])
qc.ry(0.490493392798058,[4])
qc.cx([0], [4])
qc.cx([1], [4])
qc.cx([2], [4])
qc.cx([3], [4])
qc.cx([5], [6])
qc.ry(0.512578486101571,[5])
qc.cx([0], [5])
qc.cx([1], [5])
qc.cx([2], [5])
qc.cx([3], [5])
qc.cx([4], [5])
qc.ry(0.121390517445704,[6])
qc.cx([0], [6])
qc.ry(0.301107294648713,[0])
qc.cx([1], [6])
qc.ry(0.916199465345135,[1])
qc.cx([2], [6])
qc.ry(0.802760350690373,[2])
qc.cx([3], [6])
qc.ry(0.997234060884546,[3])
qc.cx([4], [6])
qc.ry(0.776840379558342,[4])
qc.cx([5], [6])
qc.ry(0.0319601670081443,[5])
qc.ry(0.684727357314778,[6])
qc.barrier([0], [1], [2], [3], [4], [5], [6])
