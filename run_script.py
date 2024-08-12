from DPLL import DPLLSolver
from SatGen import generate_3sat_instance

# solver = DPLLSolver()
# problem = generate_3sat_instance(20,90)
# solver.solve(problem)
# print(f"Number of Recursive DPLL Calls: {solver.dpll_count}")

def dpll_run_script(num_vars, num_clauses, num_iterations):
    num_calls = []
    for i in range(num_iterations):
        solver = DPLLSolver()
        problem = generate_3sat_instance(num_vars,num_clauses)
        solver.solve(problem)
        num_calls.append(solver.dpll_count)
    return num_calls

num_vars = 20
num_iterations = 100

calls_list = []
for i in range(2,9):
    num_clauses = num_vars*i
    num_calls = dpll_run_script(num_vars, num_clauses, num_iterations)
    calls_list.append(num_calls)

print(calls_list)
    