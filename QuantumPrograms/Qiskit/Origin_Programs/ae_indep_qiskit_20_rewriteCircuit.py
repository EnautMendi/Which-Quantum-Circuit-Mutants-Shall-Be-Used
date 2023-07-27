from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(20, 20)
qc.u(1.5707963267948966,0.0,-3.141592653589793,[0])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[1])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[2])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[3])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[4])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[5])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[6])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[7])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[8])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[9])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[10])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[11])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[12])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[13])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[14])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[15])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[16])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[17])
qc.u(1.5707963267948966,0.0,-3.141592653589793,[18])
qc.u(0.92729522,0.0,0.0,[19])
qc.cx([0], [19])
qc.u(-0.92729522,0.0,0.0,[19])
qc.cx([0], [19])
qc.u(0.92729522,0.0,0.0,[19])
qc.cx([1], [19])
qc.u(-1.8545904,0.0,0.0,[19])
qc.cx([1], [19])
qc.u(1.8545904,0.0,0.0,[19])
qc.cx([2], [19])
qc.u(-3.7091809,0.0,0.0,[19])
qc.cx([2], [19])
qc.u(2.5740044,-3.141592653589793,-3.141592653589793,[19])
qc.cx([3], [19])
qc.u(-7.4183617,0.0,0.0,[19])
qc.cx([3], [19])
qc.u(1.1351764,0.0,0.0,[19])
qc.cx([4], [19])
qc.u(-14.836723,0.0,0.0,[19])
qc.cx([4], [19])
qc.u(2.2703529,0.0,0.0,[19])
qc.cx([5], [19])
qc.u(-29.673447,0.0,0.0,[19])
qc.cx([5], [19])
qc.u(1.7424796,-3.141592653589793,-3.141592653589793,[19])
qc.cx([6], [19])
qc.u(-59.346894,0.0,0.0,[19])
qc.cx([6], [19])
qc.u(2.7982262,0.0,0.0,[19])
qc.cx([7], [19])
qc.u(-118.69379,0.0,0.0,[19])
qc.cx([7], [19])
qc.u(0.68673293,-3.141592653589793,-3.141592653589793,[19])
qc.cx([8], [19])
qc.u(-237.38758,0.0,0.0,[19])
qc.cx([8], [19])
qc.u(1.3734659,-3.141592653589793,-3.141592653589793,[19])
qc.cx([9], [19])
qc.u(-474.77515,0.0,0.0,[19])
qc.cx([9], [19])
qc.u(2.7469317,-3.141592653589793,-3.141592653589793,[19])
qc.cx([10], [19])
qc.u(-949.5503,0.0,0.0,[19])
qc.cx([10], [19])
qc.u(0.78932185,0.0,0.0,[19])
qc.cx([11], [19])
qc.u(-1899.1006,0.0,0.0,[19])
qc.cx([11], [19])
qc.u(1.5786437,0.0,0.0,[19])
qc.cx([12], [19])
qc.u(-3798.2012,0.0,0.0,[19])
qc.cx([12], [19])
qc.u(3.1258979,-3.141592653589793,-3.141592653589793,[19])
qc.cx([13], [19])
qc.u(-7596.4024,0.0,0.0,[19])
qc.cx([13], [19])
qc.u(0.031389489,0.0,0.0,[19])
qc.cx([14], [19])
qc.u(-15192.805,0.0,0.0,[19])
qc.cx([14], [19])
qc.u(0.062778978,0.0,0.0,[19])
qc.cx([15], [19])
qc.u(-30385.61,0.0,0.0,[19])
qc.cx([15], [19])
qc.u(0.12555796,0.0,0.0,[19])
qc.cx([16], [19])
qc.u(-60771.219,0.0,0.0,[19])
qc.cx([16], [19])
qc.u(0.25111591,0.0,0.0,[19])
qc.cx([17], [19])
qc.u(-121542.44,0.0,0.0,[19])
qc.cx([17], [19])
qc.u(0.50223183,0.0,0.0,[19])
qc.cx([18], [19])
qc.u(-243084.88,0.0,0.0,[19])
qc.cx([18], [19])
qc.u(243084.88,0.0,0.0,[19])
qc.h([18])
qc.cp(-1.5707963267948966,[17], [18])
qc.cp(-0.7853981633974483,[16], [18])
qc.cp(-0.39269908169872414,[15], [18])
qc.cp(-0.19634954084936207,[14], [18])
qc.cp(-0.09817477042468103,[13], [18])
qc.cp(-0.04908738521234052,[12], [18])
qc.cp(-0.02454369260617026,[11], [18])
qc.cp(-0.01227184630308513,[10], [18])
qc.h([17])
qc.cp(-1.5707963267948966,[16], [17])
qc.cp(-0.7853981633974483,[15], [17])
qc.cp(-0.39269908169872414,[14], [17])
qc.cp(-0.19634954084936207,[13], [17])
qc.cp(-0.09817477042468103,[12], [17])
qc.cp(-0.04908738521234052,[11], [17])
qc.cp(-0.02454369260617026,[10], [17])
qc.h([16])
qc.cp(-1.5707963267948966,[15], [16])
qc.cp(-0.7853981633974483,[14], [16])
qc.cp(-0.39269908169872414,[13], [16])
qc.cp(-0.19634954084936207,[12], [16])
qc.cp(-0.09817477042468103,[11], [16])
qc.cp(-0.04908738521234052,[10], [16])
qc.h([15])
qc.cp(-1.5707963267948966,[14], [15])
qc.cp(-0.7853981633974483,[13], [15])
qc.cp(-0.39269908169872414,[12], [15])
qc.cp(-0.19634954084936207,[11], [15])
qc.cp(-0.09817477042468103,[10], [15])
qc.h([14])
qc.cp(-1.5707963267948966,[13], [14])
qc.cp(-0.7853981633974483,[12], [14])
qc.cp(-0.39269908169872414,[11], [14])
qc.cp(-0.19634954084936207,[10], [14])
qc.h([13])
qc.cp(-1.5707963267948966,[12], [13])
qc.cp(-0.7853981633974483,[11], [13])
qc.cp(-0.39269908169872414,[10], [13])
qc.h([12])
qc.cp(-1.5707963267948966,[11], [12])
qc.cp(-0.7853981633974483,[10], [12])
qc.h([11])
qc.cp(-1.5707963267948966,[10], [11])
qc.h([10])
qc.cp(-0.006135923151542565,[9], [18])
qc.cp(-0.0030679615757712823,[8], [18])
qc.cp(-0.0015339807878856412,[7], [18])
qc.cp(-0.0007669903939428206,[6], [18])
qc.cp(-0.0003834951969714103,[5], [18])
qc.cp(-0.00019174759848570515,[4], [18])
qc.cp(-9.587379924285257e-05,[3], [18])
qc.cp(-4.7936899621426287e-05,[2], [18])
qc.cp(-2.3968449810713143e-05,[1], [18])
qc.cp(-1.1984224905356572e-05,[0], [18])
qc.cp(-0.01227184630308513,[9], [17])
qc.cp(-0.006135923151542565,[8], [17])
qc.cp(-0.0030679615757712823,[7], [17])
qc.cp(-0.0015339807878856412,[6], [17])
qc.cp(-0.0007669903939428206,[5], [17])
qc.cp(-0.0003834951969714103,[4], [17])
qc.cp(-0.00019174759848570515,[3], [17])
qc.cp(-9.587379924285257e-05,[2], [17])
qc.cp(-4.7936899621426287e-05,[1], [17])
qc.cp(-2.3968449810713143e-05,[0], [17])
qc.cp(-0.02454369260617026,[9], [16])
qc.cp(-0.01227184630308513,[8], [16])
qc.cp(-0.006135923151542565,[7], [16])
qc.cp(-0.0030679615757712823,[6], [16])
qc.cp(-0.0015339807878856412,[5], [16])
qc.cp(-0.0007669903939428206,[4], [16])
qc.cp(-0.0003834951969714103,[3], [16])
qc.cp(-0.00019174759848570515,[2], [16])
qc.cp(-9.587379924285257e-05,[1], [16])
qc.cp(-4.7936899621426287e-05,[0], [16])
qc.cp(-0.04908738521234052,[9], [15])
qc.cp(-0.02454369260617026,[8], [15])
qc.cp(-0.01227184630308513,[7], [15])
qc.cp(-0.006135923151542565,[6], [15])
qc.cp(-0.0030679615757712823,[5], [15])
qc.cp(-0.0015339807878856412,[4], [15])
qc.cp(-0.0007669903939428206,[3], [15])
qc.cp(-0.0003834951969714103,[2], [15])
qc.cp(-0.00019174759848570515,[1], [15])
qc.cp(-9.587379924285257e-05,[0], [15])
qc.cp(-0.09817477042468103,[9], [14])
qc.cp(-0.04908738521234052,[8], [14])
qc.cp(-0.02454369260617026,[7], [14])
qc.cp(-0.01227184630308513,[6], [14])
qc.cp(-0.006135923151542565,[5], [14])
qc.cp(-0.0030679615757712823,[4], [14])
qc.cp(-0.0015339807878856412,[3], [14])
qc.cp(-0.0007669903939428206,[2], [14])
qc.cp(-0.0003834951969714103,[1], [14])
qc.cp(-0.00019174759848570515,[0], [14])
qc.cp(-0.19634954084936207,[9], [13])
qc.cp(-0.09817477042468103,[8], [13])
qc.cp(-0.04908738521234052,[7], [13])
qc.cp(-0.02454369260617026,[6], [13])
qc.cp(-0.01227184630308513,[5], [13])
qc.cp(-0.006135923151542565,[4], [13])
qc.cp(-0.0030679615757712823,[3], [13])
qc.cp(-0.0015339807878856412,[2], [13])
qc.cp(-0.0007669903939428206,[1], [13])
qc.cp(-0.0003834951969714103,[0], [13])
qc.cp(-0.39269908169872414,[9], [12])
qc.cp(-0.19634954084936207,[8], [12])
qc.cp(-0.09817477042468103,[7], [12])
qc.cp(-0.04908738521234052,[6], [12])
qc.cp(-0.02454369260617026,[5], [12])
qc.cp(-0.01227184630308513,[4], [12])
qc.cp(-0.006135923151542565,[3], [12])
qc.cp(-0.0030679615757712823,[2], [12])
qc.cp(-0.0015339807878856412,[1], [12])
qc.cp(-0.0007669903939428206,[0], [12])
qc.cp(-0.7853981633974483,[9], [11])
qc.cp(-0.39269908169872414,[8], [11])
qc.cp(-0.19634954084936207,[7], [11])
qc.cp(-0.09817477042468103,[6], [11])
qc.cp(-0.04908738521234052,[5], [11])
qc.cp(-0.02454369260617026,[4], [11])
qc.cp(-0.01227184630308513,[3], [11])
qc.cp(-0.006135923151542565,[2], [11])
qc.cp(-0.0030679615757712823,[1], [11])
qc.cp(-0.0015339807878856412,[0], [11])
qc.cp(-1.5707963267948966,[9], [10])
qc.cp(-0.7853981633974483,[8], [10])
qc.cp(-0.39269908169872414,[7], [10])
qc.cp(-0.19634954084936207,[6], [10])
qc.cp(-0.09817477042468103,[5], [10])
qc.cp(-0.04908738521234052,[4], [10])
qc.cp(-0.02454369260617026,[3], [10])
qc.cp(-0.01227184630308513,[2], [10])
qc.cp(-0.006135923151542565,[1], [10])
qc.cp(-0.0030679615757712823,[0], [10])
qc.h([9])
qc.cp(-1.5707963267948966,[8], [9])
qc.cp(-0.7853981633974483,[7], [9])
qc.cp(-0.39269908169872414,[6], [9])
qc.cp(-0.19634954084936207,[5], [9])
qc.cp(-0.09817477042468103,[4], [9])
qc.cp(-0.04908738521234052,[3], [9])
qc.cp(-0.02454369260617026,[2], [9])
qc.cp(-0.01227184630308513,[1], [9])
qc.cp(-0.006135923151542565,[0], [9])
qc.h([8])
qc.cp(-1.5707963267948966,[7], [8])
qc.cp(-0.7853981633974483,[6], [8])
qc.cp(-0.39269908169872414,[5], [8])
qc.cp(-0.19634954084936207,[4], [8])
qc.cp(-0.09817477042468103,[3], [8])
qc.cp(-0.04908738521234052,[2], [8])
qc.cp(-0.02454369260617026,[1], [8])
qc.cp(-0.01227184630308513,[0], [8])
qc.h([7])
qc.cp(-1.5707963267948966,[6], [7])
qc.cp(-0.7853981633974483,[5], [7])
qc.cp(-0.39269908169872414,[4], [7])
qc.cp(-0.19634954084936207,[3], [7])
qc.cp(-0.09817477042468103,[2], [7])
qc.cp(-0.04908738521234052,[1], [7])
qc.cp(-0.02454369260617026,[0], [7])
qc.h([6])
qc.cp(-1.5707963267948966,[5], [6])
qc.cp(-0.7853981633974483,[4], [6])
qc.cp(-0.39269908169872414,[3], [6])
qc.cp(-0.19634954084936207,[2], [6])
qc.cp(-0.09817477042468103,[1], [6])
qc.cp(-0.04908738521234052,[0], [6])
qc.h([5])
qc.cp(-1.5707963267948966,[4], [5])
qc.cp(-0.7853981633974483,[3], [5])
qc.cp(-0.39269908169872414,[2], [5])
qc.cp(-0.19634954084936207,[1], [5])
qc.cp(-0.09817477042468103,[0], [5])
qc.h([4])
qc.cp(-1.5707963267948966,[3], [4])
qc.cp(-0.7853981633974483,[2], [4])
qc.cp(-0.39269908169872414,[1], [4])
qc.cp(-0.19634954084936207,[0], [4])
qc.h([3])
qc.cp(-1.5707963267948966,[2], [3])
qc.cp(-0.7853981633974483,[1], [3])
qc.cp(-0.39269908169872414,[0], [3])
qc.h([2])
qc.cp(-1.5707963267948966,[1], [2])
qc.cp(-0.7853981633974483,[0], [2])
qc.h([1])
qc.cp(-1.5707963267948966,[0], [1])
qc.h([0])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19])