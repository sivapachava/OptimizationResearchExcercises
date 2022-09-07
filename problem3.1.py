#3.1 Problem
import cvxpy as cp

x1 = cp.Variable()
x2 = cp.Variable()

constraints = [x1 + x2 == 500000, x1 <= 100000, ((50*x2/500000) + (250*x1/500000) <=100)]

obj = cp.Minimize(x2*0.1 + x1*0.05)

prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("From Reservoir", x2.value , "From Stream", x1.value)

#status: optimal
#optimal value 44999.9999984417
#From Reservoir 399999.9999688338 From Stream 100000.00003116619