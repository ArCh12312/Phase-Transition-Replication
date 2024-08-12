from DPLL import DPLLSolver
from SatGen import generate_3sat_instance

# solver = DPLLSolver()
# problem = generate_3sat_instance(20,90)
# solver.solve(problem)
# print(f"Number of Recursive DPLL Calls: {solver.dpll_count}")

def dpll_run_script(num_vars, num_clauses, num_iterations):
    calls_list = []
    for i in range(num_iterations):
        solver = DPLLSolver()
        problem = generate_3sat_instance(num_vars,num_clauses)
        solver.solve(problem)
        calls_list.append(solver.dpll_count)
    return calls_list

num_vars = 20
num_clauses = 90
num_iterations = 10

calls_list = dpll_run_script(num_vars, num_clauses, num_iterations)
print(calls_list)