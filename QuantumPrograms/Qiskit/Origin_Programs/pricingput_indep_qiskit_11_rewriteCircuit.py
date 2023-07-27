from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(11, 11)
qc.ry(1.6198683,[0])
qc.ry(1.6522303,[1])
qc.ry(1.668654,[2])
qc.ry(1.6513284,[3])
qc.ry(1.5137916,[4])
qc.cx([4], [3])
qc.ry(0.8865441,[3])
qc.cx([4], [3])
qc.cx([3], [2])
qc.ry(0.27136875,[2])
qc.cx([4], [2])
qc.ry(0.12296747,[2])
qc.cx([3], [2])
qc.ry(0.55611414,[2])
qc.cx([4], [2])
qc.cx([2], [1])
qc.ry(0.085977103,[1])
qc.cx([3], [1])
qc.ry(0.021285711,[1])
qc.cx([2], [1])
qc.ry(0.17170629,[1])
qc.cx([4], [1])
qc.ry(0.090209643,[1])
qc.cx([2], [1])
qc.ry(0.0092159449,[1])
qc.cx([3], [1])
qc.ry(0.044235404,[1])
qc.cx([2], [1])
qc.ry(0.32183425,[1])
qc.cx([4], [1])
qc.cx([1], [0])
qc.ry(0.024426126,[0])
qc.cx([2], [0])
qc.ry(0.0038978569,[0])
qc.cx([1], [0])
qc.ry(0.048554281,[0])
qc.cx([3], [0])
qc.ry(0.015244745,[0])
qc.cx([1], [0])
qc.ry(0.0012686783,[0])
qc.cx([2], [0])
qc.ry(0.0076534546,[0])
qc.cx([1], [0])
qc.ry(0.094541741,[0])
qc.cx([4], [0])
qc.ry(0.05275865,[0])
qc.cx([1], [0])
qc.ry(0.0046560511,[0])
qc.cx([2], [0])
qc.ry(0.00078021278,[0])
qc.cx([1], [0])
qc.ry(0.0092972183,[0])
qc.cx([3], [0])
qc.ry(0.027179311,[0])
qc.cx([1], [0])
qc.ry(0.0023524332,[0])
qc.cx([2], [0])
qc.ry(0.013674426,[0])
qc.cx([1], [0])
qc.ry(0.17090792,[0])
qc.cx([4], [0])
qc.ry(1.9634954084936207,[5])
qc.cry(-0.044318384,[0], [5])
qc.cry(-0.088636767,[1], [5])
qc.x([1])
qc.cry(-0.17727353,[2], [5])
qc.x([2])
qc.cry(-0.35454707,[3], [5])
qc.x([3])
qc.cry(-0.70909414,[4], [5])
qc.x([7])
qc.x([8])
qc.ccx([1], [7], [8])
qc.x([8])
qc.x([9])
qc.ccx([2], [8], [9])
qc.x([9])
qc.x([10])
qc.ccx([3], [9], [10])
qc.ccx([4], [10], [6])
qc.x([10])
qc.ccx([3], [9], [10])
qc.ccx([2], [8], [9])
qc.ccx([1], [7], [8])
qc.x([1])
qc.x([2])
qc.x([3])
qc.cx([6], [5])
qc.u(0.39269908169872414,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(0.39269908169872414,-3.141592653589793,-3.141592653589793,[5])
qc.cx([6], [5])
qc.u(-0.011079596,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(0.011079596,0.0,0.0,[5])
qc.ccx([6], [0], [5])
qc.cx([6], [5])
qc.u(0.011079596,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(-0.011079596,0.0,0.0,[5])
qc.ccx([6], [0], [5])
qc.cx([6], [5])
qc.u(-0.022159192,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(0.022159192,0.0,0.0,[5])
qc.ccx([6], [1], [5])
qc.cx([6], [5])
qc.u(0.022159192,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(-0.022159192,0.0,0.0,[5])
qc.ccx([6], [1], [5])
qc.x([1])
qc.ccx([1], [7], [8])
qc.cx([6], [5])
qc.u(-0.044318384,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(0.044318384,0.0,0.0,[5])
qc.ccx([6], [2], [5])
qc.cx([6], [5])
qc.u(0.044318384,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(-0.044318384,0.0,0.0,[5])
qc.ccx([6], [2], [5])
qc.x([2])
qc.ccx([2], [8], [9])
qc.cx([6], [5])
qc.u(-0.088636767,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(0.088636767,0.0,0.0,[5])
qc.ccx([6], [3], [5])
qc.cx([6], [5])
qc.u(0.088636767,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(-0.088636767,0.0,0.0,[5])
qc.ccx([6], [3], [5])
qc.x([3])
qc.ccx([3], [9], [10])
qc.x([10])
qc.cx([6], [5])
qc.u(-0.17727353,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(0.17727353,0.0,0.0,[5])
qc.ccx([6], [4], [5])
qc.cx([6], [5])
qc.u(0.17727353,0.0,0.0,[5])
qc.cx([6], [5])
qc.u(-0.17727353,0.0,0.0,[5])
qc.ccx([6], [4], [5])
qc.ccx([4], [10], [6])
qc.ccx([3], [9], [10])
qc.x([10])
qc.x([3])
qc.x([9])
qc.ccx([2], [8], [9])
qc.x([2])
qc.x([8])
qc.ccx([1], [7], [8])
qc.x([1])
qc.x([7])
qc.x([8])
qc.x([9])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10])
