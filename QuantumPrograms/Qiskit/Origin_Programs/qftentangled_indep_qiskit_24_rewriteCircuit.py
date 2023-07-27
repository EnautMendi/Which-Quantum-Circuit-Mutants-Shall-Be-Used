from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(24, 24)
qc.h([23])
qc.cx([23], [22])
qc.cx([22], [21])
qc.cx([21], [20])
qc.cx([20], [19])
qc.cx([19], [18])
qc.cx([18], [17])
qc.cx([17], [16])
qc.cx([16], [15])
qc.cx([15], [14])
qc.cx([14], [13])
qc.cx([13], [12])
qc.cx([12], [11])
qc.cx([11], [10])
qc.cx([10], [9])
qc.h([23])
qc.cp(1.5707963267948966,[23], [22])
qc.h([22])
qc.cp(0.7853981633974483,[23], [21])
qc.cp(1.5707963267948966,[22], [21])
qc.h([21])
qc.cp(0.39269908169872414,[23], [20])
qc.cp(0.7853981633974483,[22], [20])
qc.cp(1.5707963267948966,[21], [20])
qc.h([20])
qc.cp(0.19634954084936207,[23], [19])
qc.cp(0.39269908169872414,[22], [19])
qc.cp(0.7853981633974483,[21], [19])
qc.cp(1.5707963267948966,[20], [19])
qc.h([19])
qc.cp(0.09817477042468103,[23], [18])
qc.cp(0.19634954084936207,[22], [18])
qc.cp(0.39269908169872414,[21], [18])
qc.cp(0.7853981633974483,[20], [18])
qc.cp(1.5707963267948966,[19], [18])
qc.h([18])
qc.cp(0.04908738521234052,[23], [17])
qc.cp(0.09817477042468103,[22], [17])
qc.cp(0.19634954084936207,[21], [17])
qc.cp(0.39269908169872414,[20], [17])
qc.cp(0.7853981633974483,[19], [17])
qc.cp(1.5707963267948966,[18], [17])
qc.h([17])
qc.cp(0.02454369260617026,[23], [16])
qc.cp(0.04908738521234052,[22], [16])
qc.cp(0.09817477042468103,[21], [16])
qc.cp(0.19634954084936207,[20], [16])
qc.cp(0.39269908169872414,[19], [16])
qc.cp(0.7853981633974483,[18], [16])
qc.cp(1.5707963267948966,[17], [16])
qc.h([16])
qc.cp(0.01227184630308513,[23], [15])
qc.cp(0.02454369260617026,[22], [15])
qc.cp(0.04908738521234052,[21], [15])
qc.cp(0.09817477042468103,[20], [15])
qc.cp(0.19634954084936207,[19], [15])
qc.cp(0.39269908169872414,[18], [15])
qc.cp(0.7853981633974483,[17], [15])
qc.cp(1.5707963267948966,[16], [15])
qc.h([15])
qc.cp(0.006135923151542565,[23], [14])
qc.cp(0.01227184630308513,[22], [14])
qc.cp(0.02454369260617026,[21], [14])
qc.cp(0.04908738521234052,[20], [14])
qc.cp(0.09817477042468103,[19], [14])
qc.cp(0.19634954084936207,[18], [14])
qc.cp(0.39269908169872414,[17], [14])
qc.cp(0.7853981633974483,[16], [14])
qc.cp(1.5707963267948966,[15], [14])
qc.h([14])
qc.cp(0.0030679615757712823,[23], [13])
qc.cp(0.006135923151542565,[22], [13])
qc.cp(0.01227184630308513,[21], [13])
qc.cp(0.02454369260617026,[20], [13])
qc.cp(0.04908738521234052,[19], [13])
qc.cp(0.09817477042468103,[18], [13])
qc.cp(0.19634954084936207,[17], [13])
qc.cp(0.39269908169872414,[16], [13])
qc.cp(0.7853981633974483,[15], [13])
qc.cp(1.5707963267948966,[14], [13])
qc.h([13])
qc.cp(0.0015339807878856412,[23], [12])
qc.cp(0.0030679615757712823,[22], [12])
qc.cp(0.006135923151542565,[21], [12])
qc.cp(0.01227184630308513,[20], [12])
qc.cp(0.02454369260617026,[19], [12])
qc.cp(0.04908738521234052,[18], [12])
qc.cp(0.09817477042468103,[17], [12])
qc.cp(0.19634954084936207,[16], [12])
qc.cp(0.39269908169872414,[15], [12])
qc.cp(0.7853981633974483,[14], [12])
qc.cp(1.5707963267948966,[13], [12])
qc.h([12])
qc.cp(0.0007669903939428206,[23], [11])
qc.cp(0.0015339807878856412,[22], [11])
qc.cp(0.0030679615757712823,[21], [11])
qc.cp(0.006135923151542565,[20], [11])
qc.cp(0.01227184630308513,[19], [11])
qc.cp(0.02454369260617026,[18], [11])
qc.cp(0.04908738521234052,[17], [11])
qc.cp(0.09817477042468103,[16], [11])
qc.cp(0.19634954084936207,[15], [11])
qc.cp(0.39269908169872414,[14], [11])
qc.cp(0.7853981633974483,[13], [11])
qc.cp(1.5707963267948966,[12], [11])
qc.h([11])
qc.cp(0.0003834951969714103,[23], [10])
qc.cp(0.0007669903939428206,[22], [10])
qc.cp(0.0015339807878856412,[21], [10])
qc.cp(0.0030679615757712823,[20], [10])
qc.cp(0.006135923151542565,[19], [10])
qc.cp(0.01227184630308513,[18], [10])
qc.cp(0.02454369260617026,[17], [10])
qc.cp(0.04908738521234052,[16], [10])
qc.cp(0.09817477042468103,[15], [10])
qc.cp(0.19634954084936207,[14], [10])
qc.cp(0.39269908169872414,[13], [10])
qc.cp(0.7853981633974483,[12], [10])
qc.cp(1.5707963267948966,[11], [10])
qc.h([10])
qc.cx([9], [8])
qc.cp(0.00019174759848570515,[23], [9])
qc.cp(0.0003834951969714103,[22], [9])
qc.cp(0.0007669903939428206,[21], [9])
qc.cp(0.0015339807878856412,[20], [9])
qc.cp(0.0030679615757712823,[19], [9])
qc.cp(0.006135923151542565,[18], [9])
qc.cp(0.01227184630308513,[17], [9])
qc.cp(0.02454369260617026,[16], [9])
qc.cp(0.04908738521234052,[15], [9])
qc.cp(0.09817477042468103,[14], [9])
qc.cp(0.19634954084936207,[13], [9])
qc.cp(0.39269908169872414,[12], [9])
qc.cp(0.7853981633974483,[11], [9])
qc.cp(1.5707963267948966,[10], [9])
qc.cx([8], [7])
qc.cp(9.587379924285257e-05,[23], [8])
qc.cp(0.00019174759848570515,[22], [8])
qc.cp(0.0003834951969714103,[21], [8])
qc.cp(0.0007669903939428206,[20], [8])
qc.cp(0.0015339807878856412,[19], [8])
qc.cp(0.0030679615757712823,[18], [8])
qc.cp(0.006135923151542565,[17], [8])
qc.cp(0.01227184630308513,[16], [8])
qc.cp(0.02454369260617026,[15], [8])
qc.cp(0.04908738521234052,[14], [8])
qc.cp(0.09817477042468103,[13], [8])
qc.cp(0.19634954084936207,[12], [8])
qc.cp(0.39269908169872414,[11], [8])
qc.cp(0.7853981633974483,[10], [8])
qc.cx([7], [6])
qc.cp(4.7936899621426287e-05,[23], [7])
qc.cp(9.587379924285257e-05,[22], [7])
qc.cp(0.00019174759848570515,[21], [7])
qc.cp(0.0003834951969714103,[20], [7])
qc.cp(0.0007669903939428206,[19], [7])
qc.cp(0.0015339807878856412,[18], [7])
qc.cp(0.0030679615757712823,[17], [7])
qc.cp(0.006135923151542565,[16], [7])
qc.cp(0.01227184630308513,[15], [7])
qc.cp(0.02454369260617026,[14], [7])
qc.cp(0.04908738521234052,[13], [7])
qc.cp(0.09817477042468103,[12], [7])
qc.cp(0.19634954084936207,[11], [7])
qc.cp(0.39269908169872414,[10], [7])
qc.cx([6], [5])
qc.cp(2.3968449810713143e-05,[23], [6])
qc.cp(4.7936899621426287e-05,[22], [6])
qc.cp(9.587379924285257e-05,[21], [6])
qc.cp(0.00019174759848570515,[20], [6])
qc.cp(0.0003834951969714103,[19], [6])
qc.cp(0.0007669903939428206,[18], [6])
qc.cp(0.0015339807878856412,[17], [6])
qc.cp(0.0030679615757712823,[16], [6])
qc.cp(0.006135923151542565,[15], [6])
qc.cp(0.01227184630308513,[14], [6])
qc.cp(0.02454369260617026,[13], [6])
qc.cp(0.04908738521234052,[12], [6])
qc.cp(0.09817477042468103,[11], [6])
qc.cp(0.19634954084936207,[10], [6])
qc.cx([5], [4])
qc.cp(1.1984224905356572e-05,[23], [5])
qc.cp(2.3968449810713143e-05,[22], [5])
qc.cp(4.7936899621426287e-05,[21], [5])
qc.cp(9.587379924285257e-05,[20], [5])
qc.cp(0.00019174759848570515,[19], [5])
qc.cp(0.0003834951969714103,[18], [5])
qc.cp(0.0007669903939428206,[17], [5])
qc.cp(0.0015339807878856412,[16], [5])
qc.cp(0.0030679615757712823,[15], [5])
qc.cp(0.006135923151542565,[14], [5])
qc.cp(0.01227184630308513,[13], [5])
qc.cp(0.02454369260617026,[12], [5])
qc.cp(0.04908738521234052,[11], [5])
qc.cp(0.09817477042468103,[10], [5])
qc.cx([4], [3])
qc.cp(5.992112452678286e-06,[23], [4])
qc.cp(1.1984224905356572e-05,[22], [4])
qc.cp(2.3968449810713143e-05,[21], [4])
qc.cp(4.7936899621426287e-05,[20], [4])
qc.cp(9.587379924285257e-05,[19], [4])
qc.cp(0.00019174759848570515,[18], [4])
qc.cp(0.0003834951969714103,[17], [4])
qc.cp(0.0007669903939428206,[16], [4])
qc.cp(0.0015339807878856412,[15], [4])
qc.cp(0.0030679615757712823,[14], [4])
qc.cp(0.006135923151542565,[13], [4])
qc.cp(0.01227184630308513,[12], [4])
qc.cp(0.02454369260617026,[11], [4])
qc.cp(0.04908738521234052,[10], [4])
qc.cx([3], [2])
qc.cx([2], [1])
qc.cx([1], [0])
qc.cp(2.996056226339143e-06,[23], [3])
qc.cp(5.992112452678286e-06,[22], [3])
qc.cp(1.1984224905356572e-05,[21], [3])
qc.cp(2.3968449810713143e-05,[20], [3])
qc.cp(4.7936899621426287e-05,[19], [3])
qc.cp(9.587379924285257e-05,[18], [3])
qc.cp(0.00019174759848570515,[17], [3])
qc.cp(0.0003834951969714103,[16], [3])
qc.cp(0.0007669903939428206,[15], [3])
qc.cp(0.0015339807878856412,[14], [3])
qc.cp(0.0030679615757712823,[13], [3])
qc.cp(0.006135923151542565,[12], [3])
qc.cp(0.01227184630308513,[11], [3])
qc.cp(0.02454369260617026,[10], [3])
qc.cp(1.4980281131695715e-06,[23], [2])
qc.cp(2.996056226339143e-06,[22], [2])
qc.cp(5.992112452678286e-06,[21], [2])
qc.cp(1.1984224905356572e-05,[20], [2])
qc.cp(2.3968449810713143e-05,[19], [2])
qc.cp(4.7936899621426287e-05,[18], [2])
qc.cp(9.587379924285257e-05,[17], [2])
qc.cp(0.00019174759848570515,[16], [2])
qc.cp(0.0003834951969714103,[15], [2])
qc.cp(0.0007669903939428206,[14], [2])
qc.cp(0.0015339807878856412,[13], [2])
qc.cp(0.0030679615757712823,[12], [2])
qc.cp(0.006135923151542565,[11], [2])
qc.cp(0.01227184630308513,[10], [2])
qc.cp(7.490140565847857e-07,[23], [1])
qc.cp(1.4980281131695715e-06,[22], [1])
qc.cp(2.996056226339143e-06,[21], [1])
qc.cp(5.992112452678286e-06,[20], [1])
qc.cp(1.1984224905356572e-05,[19], [1])
qc.cp(2.3968449810713143e-05,[18], [1])
qc.cp(4.7936899621426287e-05,[17], [1])
qc.cp(9.587379924285257e-05,[16], [1])
qc.cp(0.00019174759848570515,[15], [1])
qc.cp(0.0003834951969714103,[14], [1])
qc.cp(0.0007669903939428206,[13], [1])
qc.cp(0.0015339807878856412,[12], [1])
qc.cp(0.0030679615757712823,[11], [1])
qc.cp(0.006135923151542565,[10], [1])
qc.cp(3.7450702829239286e-07,[23], [0])
qc.cp(7.490140565847857e-07,[22], [0])
qc.cp(1.4980281131695715e-06,[21], [0])
qc.cp(2.996056226339143e-06,[20], [0])
qc.cp(5.992112452678286e-06,[19], [0])
qc.cp(1.1984224905356572e-05,[18], [0])
qc.cp(2.3968449810713143e-05,[17], [0])
qc.cp(4.7936899621426287e-05,[16], [0])
qc.cp(9.587379924285257e-05,[15], [0])
qc.cp(0.00019174759848570515,[14], [0])
qc.cp(0.0003834951969714103,[13], [0])
qc.cp(0.0007669903939428206,[12], [0])
qc.cp(0.0015339807878856412,[11], [0])
qc.cp(0.0030679615757712823,[10], [0])
qc.swap([10], [13])
qc.swap([11], [12])
qc.h([9])
qc.cp(1.5707963267948966,[9], [8])
qc.h([8])
qc.cp(0.7853981633974483,[9], [7])
qc.cp(1.5707963267948966,[8], [7])
qc.h([7])
qc.cp(0.39269908169872414,[9], [6])
qc.cp(0.7853981633974483,[8], [6])
qc.cp(1.5707963267948966,[7], [6])
qc.h([6])
qc.cp(0.19634954084936207,[9], [5])
qc.cp(0.39269908169872414,[8], [5])
qc.cp(0.7853981633974483,[7], [5])
qc.cp(1.5707963267948966,[6], [5])
qc.h([5])
qc.cp(0.09817477042468103,[9], [4])
qc.cp(0.19634954084936207,[8], [4])
qc.cp(0.39269908169872414,[7], [4])
qc.cp(0.7853981633974483,[6], [4])
qc.cp(1.5707963267948966,[5], [4])
qc.h([4])
qc.cp(0.04908738521234052,[9], [3])
qc.cp(0.09817477042468103,[8], [3])
qc.cp(0.19634954084936207,[7], [3])
qc.cp(0.39269908169872414,[6], [3])
qc.cp(0.7853981633974483,[5], [3])
qc.cp(1.5707963267948966,[4], [3])
qc.h([3])
qc.cp(0.02454369260617026,[9], [2])
qc.cp(0.04908738521234052,[8], [2])
qc.cp(0.09817477042468103,[7], [2])
qc.cp(0.19634954084936207,[6], [2])
qc.cp(0.39269908169872414,[5], [2])
qc.cp(0.7853981633974483,[4], [2])
qc.cp(1.5707963267948966,[3], [2])
qc.h([2])
qc.cp(0.01227184630308513,[9], [1])
qc.cp(0.02454369260617026,[8], [1])
qc.cp(0.04908738521234052,[7], [1])
qc.cp(0.09817477042468103,[6], [1])
qc.cp(0.19634954084936207,[5], [1])
qc.cp(0.39269908169872414,[4], [1])
qc.cp(0.7853981633974483,[3], [1])
qc.cp(1.5707963267948966,[2], [1])
qc.h([1])
qc.cp(0.006135923151542565,[9], [0])
qc.cp(0.01227184630308513,[8], [0])
qc.cp(0.02454369260617026,[7], [0])
qc.cp(0.04908738521234052,[6], [0])
qc.cp(0.09817477042468103,[5], [0])
qc.cp(0.19634954084936207,[4], [0])
qc.cp(0.39269908169872414,[3], [0])
qc.cp(0.7853981633974483,[2], [0])
qc.cp(1.5707963267948966,[1], [0])
qc.h([0])
qc.swap([0], [23])
qc.swap([1], [22])
qc.swap([2], [21])
qc.swap([3], [20])
qc.swap([4], [19])
qc.swap([5], [18])
qc.swap([6], [17])
qc.swap([7], [16])
qc.swap([8], [15])
qc.swap([9], [14])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23])
