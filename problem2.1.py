#2.1 Problem
#Unconstraint-Optimization-Problem
import cvxpy as cp

x1 = cp.Variable()
x2 = cp.Variable()

constraints = [x2 >=0, x1 >=0]

obj = cp.Minimize((x1-4)**2 + 7*(x2-4)**2 + 4*(x2))

prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x1.value, x2.value)

#status: optimal
#optimal value 15.428571428571429
#optimal var 4.0 3.7142857142857144