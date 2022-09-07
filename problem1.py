#1 Problem
import cvxpy as cp

x = cp.Variable()
y = cp.Variable()

constraints = [x+y == 1,
               x-y >= 1]

obj = cp.Minimize((x-y)**2)

prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)


#status: optimal
#optimal value 1.0
#optimal var 1.0 1.570086213240983e-22
