# My own Problem
import cvxpy as cp
x = cp.Variable()
y = cp.Variable()
z = cp.Variable()


constraints = [10*x + 2*y + 2*z >= 100,
                 2*x + 6*y >= 100,
                 8*y + 10*z >=300,
                8*y + 10*z <=600]

obj = cp.Minimize((30*x) + (50*y) + (20*z))

prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value , y.value, z.value) 

#status: optimal
#optimal value 1229.7297299032412
#optimal var 3.378378382114954 15.540540541034668 17.567567569402957
