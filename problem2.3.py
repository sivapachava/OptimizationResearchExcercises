#2.3 Problem
#Unconstraint-Optimization-Problem
import cvxpy as cp

x1 = cp.Variable()
x2 = cp.Variable()
constraints = [-x1 - x2 + 4 <=0, x1>=0, x2 >=0]
obj = cp.Minimize((x1 - 2)**2 + (3*(x2)))
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x1.value, x2.value)

#status: optimal
#optimal value 3.75
#optimal var 3.5 0.5

