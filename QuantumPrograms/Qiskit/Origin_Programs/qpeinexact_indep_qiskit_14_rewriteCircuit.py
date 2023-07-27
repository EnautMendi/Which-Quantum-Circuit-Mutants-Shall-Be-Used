from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
qc = QuantumCircuit(14, 14)
qc.h([0])
qc.h([1])
qc.h([2])
qc.h([3])
qc.h([4])
qc.h([5])
qc.h([6])
qc.h([7])
qc.h([8])
qc.h([9])
qc.h([10])
qc.h([11])
qc.h([12])
qc.x([13])
qc.cp(-2.6932868,[13], [0])
qc.cp(0.89661177,[13], [1])
qc.cp(1.7932235,[13], [2])
qc.cp(-2.6967382,[13], [3])
qc.cp(0.88970886,[13], [4])
qc.cp(1.7794177,[13], [5])
qc.cp(-2.7243499,[13], [6])
qc.cp(0.83448555,[13], [7])
qc.cp(1.6689711,[13], [8])
qc.cp(-2.945243112740431,[13], [9])
qc.cp(0.39269908169872414,[13], [10])
qc.cp(0.7853981633974483,[13], [11])
qc.cp(1.5707963267948966,[13], [12])
qc.swap([0], [12])
qc.h([0])
qc.swap([1], [11])
qc.cp(-1.5707963267948966,[1], [0])
qc.h([1])
qc.swap([2], [10])
qc.cp(-0.7853981633974483,[2], [0])
qc.cp(-1.5707963267948966,[2], [1])
qc.h([2])
qc.swap([3], [9])
qc.cp(-0.39269908169872414,[3], [0])
qc.cp(-0.7853981633974483,[3], [1])
qc.cp(-1.5707963267948966,[3], [2])
qc.h([3])
qc.swap([4], [8])
qc.cp(-0.19634954084936207,[4], [0])
qc.cp(-0.39269908169872414,[4], [1])
qc.cp(-0.7853981633974483,[4], [2])
qc.cp(-1.5707963267948966,[4], [3])
qc.h([4])
qc.swap([5], [7])
qc.cp(-0.09817477042468103,[5], [0])
qc.cp(-0.19634954084936207,[5], [1])
qc.cp(-0.39269908169872414,[5], [2])
qc.cp(-0.7853981633974483,[5], [3])
qc.cp(-1.5707963267948966,[5], [4])
qc.h([5])
qc.cp(-0.04908738521234052,[6], [0])
qc.cp(-0.09817477042468103,[6], [1])
qc.cp(-0.19634954084936207,[6], [2])
qc.cp(-0.39269908169872414,[6], [3])
qc.cp(-0.7853981633974483,[6], [4])
qc.cp(-1.5707963267948966,[6], [5])
qc.h([6])
qc.cp(-0.02454369260617026,[7], [0])
qc.cp(-0.04908738521234052,[7], [1])
qc.cp(-0.09817477042468103,[7], [2])
qc.cp(-0.19634954084936207,[7], [3])
qc.cp(-0.39269908169872414,[7], [4])
qc.cp(-0.7853981633974483,[7], [5])
qc.cp(-1.5707963267948966,[7], [6])
qc.h([7])
qc.cp(-0.01227184630308513,[8], [0])
qc.cp(-0.02454369260617026,[8], [1])
qc.cp(-0.04908738521234052,[8], [2])
qc.cp(-0.09817477042468103,[8], [3])
qc.cp(-0.19634954084936207,[8], [4])
qc.cp(-0.39269908169872414,[8], [5])
qc.cp(-0.7853981633974483,[8], [6])
qc.cp(-1.5707963267948966,[8], [7])
qc.h([8])
qc.cp(-0.006135923151542565,[9], [0])
qc.cp(-0.0030679615757712823,[10], [0])
qc.cp(-0.0015339807878856412,[11], [0])
qc.cp(-0.0007669903939428206,[12], [0])
qc.cp(-0.01227184630308513,[9], [1])
qc.cp(-0.006135923151542565,[10], [1])
qc.cp(-0.0030679615757712823,[11], [1])
qc.cp(-0.0015339807878856412,[12], [1])
qc.cp(-0.02454369260617026,[9], [2])
qc.cp(-0.01227184630308513,[10], [2])
qc.cp(-0.006135923151542565,[11], [2])
qc.cp(-0.0030679615757712823,[12], [2])
qc.cp(-0.04908738521234052,[9], [3])
qc.cp(-0.02454369260617026,[10], [3])
qc.cp(-0.01227184630308513,[11], [3])
qc.cp(-0.006135923151542565,[12], [3])
qc.cp(-0.09817477042468103,[9], [4])
qc.cp(-0.04908738521234052,[10], [4])
qc.cp(-0.02454369260617026,[11], [4])
qc.cp(-0.01227184630308513,[12], [4])
qc.cp(-0.19634954084936207,[9], [5])
qc.cp(-0.09817477042468103,[10], [5])
qc.cp(-0.04908738521234052,[11], [5])
qc.cp(-0.02454369260617026,[12], [5])
qc.cp(-0.39269908169872414,[9], [6])
qc.cp(-0.19634954084936207,[10], [6])
qc.cp(-0.09817477042468103,[11], [6])
qc.cp(-0.04908738521234052,[12], [6])
qc.cp(-0.7853981633974483,[9], [7])
qc.cp(-0.39269908169872414,[10], [7])
qc.cp(-0.19634954084936207,[11], [7])
qc.cp(-0.09817477042468103,[12], [7])
qc.cp(-1.5707963267948966,[9], [8])
qc.cp(-0.7853981633974483,[10], [8])
qc.cp(-0.39269908169872414,[11], [8])
qc.cp(-0.19634954084936207,[12], [8])
qc.h([9])
qc.cp(-1.5707963267948966,[10], [9])
qc.h([10])
qc.cp(-0.7853981633974483,[11], [9])
qc.cp(-1.5707963267948966,[11], [10])
qc.h([11])
qc.cp(-0.39269908169872414,[12], [9])
qc.cp(-0.7853981633974483,[12], [10])
qc.cp(-1.5707963267948966,[12], [11])
qc.h([12])
qc.barrier([0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13])
