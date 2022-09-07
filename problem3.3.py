#3.3 Problem
from numpy import log
import cvxpy as cp

x1 = cp.Variable()
x2 = cp.Variable()

constraints = [x1 + x2 == 200]

obj = cp.Maximize((7000*cp.log(1 + x1)) + (5000*cp.log(1 + x2)) - x1 - x2)

prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("Rural Projects", x1.value, "Orban Projects", x2.value)

#status: optimal
#optimal value 55348.89310673721
#Rural Projects 116.83330317505175 Orban Projects 83.1666963297482