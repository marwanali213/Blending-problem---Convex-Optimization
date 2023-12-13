from pulp import *
# section 2 _ link : https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html#problem-description
ingredients = ['chicken', 'beef', 'mutton', 'rice', 'wheat bran','gel']

costs = {
    'chicken':0.013,
    'beef':0.008,
    'mutton':0.01,
    'rice':0.002,
    'wheat bran':0.005,
    'gel':0.001
}

protien = {
    'chicken':0.1,
    'beef':0.2,
    'mutton':0.15,
    'rice':0.0,
    'wheat bran':0.04,
    'gel':0.0
}
fat = {
    'chicken':0.08,
    'beef':0.1,
    'mutton':0.11,
    'rice':0.01,
    'wheat bran':0.01,
    'gel':0.0
}
fibre = {
    'chicken':0.001,
    'beef':0.005,
    'mutton':0.003,
    'rice':0.1,
    'wheat bran':0.15,
    'gel':0.0
}
salt = {
    'chicken':0.002,
    'beef':0.005,
    'mutton':0.007,
    'rice':0.002,
    'wheat bran':0.008,
    'gel':0.0
}

problem = LpProblem("the whiskas problem",LpMinimize)
variables = LpVariable.dicts("ingredients",ingredients,0)

problem += lpSum(costs[i]*variables[i] for i in ingredients)

problem += lpSum(variables[i] for i in ingredients) == 100 , "percentage sum"

problem += lpSum(protien[i]*variables[i] for i in ingredients) >=8.0, "protien constraint"
problem += (lpSum(fibre[i]*variables[i] for i in ingredients)<=2.0 , "fibre constraint")
problem += (lpSum(fat[i]*variables[i] for i in ingredients) <=6.0, "fat constraint")
problem += (lpSum(salt[i]*variables[i] for i in ingredients)<=0.4 , "salt constraint")


problem.solve()

for v in problem.variables():
    print(v.name, "=", v.varValue)

print("overall cost of ingredients per can =", value(problem.objective))