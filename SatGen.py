import random

def generate_clause(num_vars):
    """Generates a single 3-SAT clause with 3 literals."""
    clause = []
    for _ in range(3):
        # Randomly pick a variable and decide if it's negated or not
        var = random.randint(1, num_vars)
        if random.choice([True, False]):
            var = -var
        clause.append(var)
    return clause

def generate_3sat_instance(num_vars, num_clauses):
    """Generates a 3-SAT instance with the given number of variables and clauses."""
    clauses = []
    for _ in range(num_clauses):
        clause = generate_clause(num_vars)
        clauses.append(clause)
    return clauses