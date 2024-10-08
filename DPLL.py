import time
from collections import defaultdict

class DPLLSolver:
    def __init__(self):
        self.dpll_count = 0
        self.clauses = []
        self.num_vars = 0
        self.num_clauses = 0
        self.branch_count = 0

    def find_unit_clause(self, formula):
        for clause in formula:
            if len(clause) == 1:
                return clause[0]
        return 0
                        
    def unit_propagate(self, formula, model):
        unit_clause = self.find_unit_clause(formula)
        while unit_clause != 0:
            new_unit_clause = 0
            new_formula = []
            for clause in formula:
                if unit_clause in clause:
                    continue
                elif -unit_clause in clause:
                    clause = [lit for lit in clause if lit != -unit_clause]
                if clause == []:
                    return [[]], []
                if len(clause) == 1:
                    new_unit_clause = clause[0]
                new_formula.append(clause)
            formula = new_formula
            if unit_clause not in model:
                model.append(unit_clause)
            unit_clause = new_unit_clause
        return formula, model

    # def pure_literal_elimination(self, formula, model):
    #     while True:
    #         literals = {literal for clause in formula for literal in clause}
    #         pure_literals = {literal for literal in literals if -literal not in literals}
    #         if not pure_literals:
    #             break
    #         for literal in pure_literals:
    #             if literal not in model:
    #                 model.append(literal)
    #         formula = [clause for clause in formula if not any(literal in clause for literal in pure_literals)]
    #     return formula, model

    def select_literal(self, formula):
        # JW-One Heuristic
        jw_scores = defaultdict(float)
        for clause in formula:
            for literal in clause:
                jw_scores[literal] += 2 ** -len(clause)
        return max(jw_scores, key=jw_scores.get)

    def dpll(self, formula, model = []):
        self.dpll_count += 1
        formula, model = self.unit_propagate(formula, model)
        # formula, model = self.pure_literal_elimination(formula, model)
        if formula == []:
            return True, model
        if formula == [[]]:
            return False, []
        
        literal = self.select_literal(formula)
        pos_formula = formula + [[literal]]
        neg_formula = formula + [[-literal]]
        pos_model = model[:]
        neg_model = model[:]

        self.branch_count += 1

        sat_pos, pos_model = self.dpll(pos_formula, pos_model)
        if sat_pos:
            return True, pos_model

        sat_neg, neg_model = self.dpll(neg_formula, neg_model)
        if sat_neg:
            return True, neg_model

        return False, []

    def check_model_consistency(self, model):
        variables = set()
        for literal in model:
            variable = abs(literal)
            if variable in variables:
                print("Inconsistent")
                return False  # Inconsistent model
            variables.add(variable)
        return True

    def verify_solution(self, model):
        # Verify the solution
        next = self.check_model_consistency(model)
        if not next:
            return False
        for clause in self.clauses :                   # for each clause
            flag = False
            for literal in clause:
                if literal in model:                 # atleast one literal should be true
                    flag = True
                    break
            if not flag:
                print(f"Unsatisfied clause: {clause}")
                return False
        return True

    def solve(self, clauses):
        self.clauses = clauses
        start = time.time()
        sat, model = self.dpll(self.clauses)
        end = time.time()
        solve_time = end - start
        if sat:
            verification_result = self.verify_solution(model)
        else:
            verification_result = True
        return sat, model, verification_result, self.branch_count, solve_time
