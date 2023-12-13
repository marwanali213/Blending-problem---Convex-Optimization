from pulp import *

foods = ['outmeal', 'chicken', 'eggs','milk', 'pecan pie', 'beef and beans']

prices = {
    'outmeal':0.30,
    'chicken':2.4,
    'eggs':1.3,
    'milk':0.9,
    'pecan pie':2.0,
    'beef and beans':1.9
}

protien = {
    'outmeal': 4,
    'chicken':32,
    'eggs':13,
    'milk':8,
    'pecan pie':4,
    'beef and beans':14
}

energy = {
    'outmeal':110,
    'chicken':205,
    'eggs':160,
    'milk':160,
    'pecan pie':420,
    'beef and beans':260
}

calcium = {
    'outmeal': 2,
    'chicken':12,
    'eggs':54,
    'milk':285,
    'pecan pie':22,
    'beef and beans':80
}

problem = LpProblem("diet plan",LpMinimize)

food_vars = LpVariable.dicts("Serving portions",foods,0)

problem += lpSum(prices[i]*food_vars[i] for i in foods)

problem += lpSum(energy[i]*food_vars[i] for i in foods) >= 2000
problem += lpSum(protien[i]*food_vars[i] for i in foods) >= 55
problem += lpSum(calcium[i]*food_vars[i] for i in foods) >= 800

problem.solve()
print("Status:",LpStatus[problem.status])

for v in problem.variables():
    print(v.name,"=",v.varValue)


print("total cost of this meal ", value(problem.objective))


