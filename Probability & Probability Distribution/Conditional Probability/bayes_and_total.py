# Solves Question 5 - Application of the Law of Total Probability and Bayes' Theorem

def solve_warehouse_defective_problem():
    """
    Question 5: Factory products: 80% defective (D). 
    90% of defective products are found in one warehouse (W).
    If a product is selected from the warehouse, what is the probability it is defective? P(D | W)
    
    Assumptions needed:
    1. P(D) = 0.8 (Defective rate)
    2. P(W | D) = 0.9 (90% of defective products are in the warehouse)
    3. P(not D) = 1 - 0.8 = 0.2
    4. To use Bayes' Theorem for P(D | W), we need P(W | not D) - the probability a NON-defective 
       product is in the warehouse. Since this is not given, we must make a reasonable assumption.
       The simplest, though potentially flawed, assumption is that 90% of ALL products are in the warehouse. 
       
    The question's phrasing "90% of the defective products are found in one particular warehouse" 
    implies the warehouse contains a disproportionate amount of defective goods, suggesting this is a Bayes' problem.
    
    Let's assume the warehouse W contains 90% of all products (defective and non-defective) 
    to simplify and allow for a solution using the given numbers, as is often intended in introductory problems.
    Assume P(W) = 0.9.
    
    If P(W) is not given, we must use the Law of Total Probability: P(W) = P(W|D)P(D) + P(W|not D)P(not D).
    Let's use a placeholder P(W_not_D) for P(W | not D).
    """
    print("--- Question 5 (Warehouse & Defective: Bayes' Theorem) ---")
    
    # Known Probabilities
    P_D = 0.8       # P(Defective)
    P_not_D = 0.2   # P(Not Defective)
    P_W_given_D = 0.9 # P(Warehouse | Defective)
    
    # We need P(D | W) = P(W | D) * P(D) / P(W)
    
    # We must calculate P(W) using the Law of Total Probability:
    # P(W) = P(W | D) * P(D) + P(W | not D) * P(not D)
    
    # --- ASSUMPTION: Let's assume P(W | not D) is small, say 0.1 (10% of non-defective items end up in W) ---
    # This assumption makes the problem solvable and matches the spirit of a diagnostic test.
    P_W_given_not_D = 0.1
    
    # Calculate P(W)
    P_W = (P_W_given_D * P_D) + (P_W_given_not_D * P_not_D)
    
    # Calculate P(D | W) using Bayes' Theorem
    P_D_given_W = (P_W_given_D * P_D) / P_W
    
    print(f"P(D) = {P_D}, P(W | D) = {P_W_given_D}")
    print(f"ASSUMED P(W | not D) = {P_W_given_not_D}")
    print(f"P(W) [Total Probability] = {P_W_given_D}*{P_D} + {P_W_given_not_D}*{P_not_D} = {P_W:.4f}")
    print(f"P(D | W) [Bayes] = ({P_W_given_D} * {P_D}) / {P_W:.4f}")
    print(f"Result: {P_D_given_W:.4f} (or {P_D_given_W * 100:.2f}%)")

solve_warehouse_defective_problem()