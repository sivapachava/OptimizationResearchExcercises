#2.2 Problem
#Unconstraint-Optimization-Problem
import cvxpy as cp

x1 = cp.Variable()
x2 = cp.Variable()
x3 = cp.Variable()

constraints = [x3 >=0, x1 >=0, x2 >=0]

obj = cp.Minimize((x1)**3 + (x2-x3)**2 + (x3)**3 + 2)

prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x1.value , x2.value , x3.value)

#status: optimal
#optimal value 1.999999998940935
#optimal var 0.0004827960287620879 0.0003661093880596608 0.0003658179600187619