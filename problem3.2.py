#3.2 Problem
import cvxpy as cp

p = cp.Variable()
q = cp.Variable()
r = cp.Variable()
s = cp.Variable()

constraints = [  p >= 0.10, p <= 0.25,  q >= 0.05, q <= 0.2, r >= 0.30, s>=0,
               (0.30*p) + (0.20*q) + (0.40*r) + (0.20*s) <= 0.35,
               (0.35*p) + (0.60*q) + (0.35*r) + (0.40*s) <= 0.50,
               (0.20*p) + (0.15*q) + (0.05*r) + (0.30*s) >= 0.19,
               (0.15*p) + (0.05*q) + (0.20*r) + (0.10*s) >= 0.08,
               (0.15*p) + (0.05*q) + (0.20*r) + (0.10*s) <= 0.13,
               p+q+r+s ==1]

obj = cp.Minimize((55*p) + (65*q) + (35*r) + (85*s))

prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal values for each blend: ")
print("blend1:", p.value ,"blend2:", q.value, "blend3:", r.value, "blend4:", s.value)

#status: optimal
#optimal value 62.99999999853861
#optimal values for each blend: 
#blend1: 0.1399999999863198 blend2: 0.14000000000496018 blend3: 0.3000000000350219 blend4: 0.4199999999734453