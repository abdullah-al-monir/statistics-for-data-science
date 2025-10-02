# Solves the practice problems using conditional probability and Bayes' Theorem.

# Helper function to perform Bayes' calculation for a single hypothesis E1
def bayes_theorem(P_E1, P_A_given_E1, P_A_given_not_E1):
    """
    Calculates P(E1 | A) using Bayes' Theorem.
    P(E1 | A) = [P(A | E1) * P(E1)] / P(A)
    where P(A) = P(A | E1)*P(E1) + P(A | not E1)*P(not E1)
    """
    P_not_E1 = 1 - P_E1

    # Law of Total Probability: P(A)
    P_A = (P_A_given_E1 * P_E1) + (P_A_given_not_E1 * P_not_E1)

    # Bayes' Theorem
    P_E1_given_A = (P_A_given_E1 * P_E1) / P_A
    return P_E1_given_A, P_A

# --- Question 1: Medical Test Diagnostics (Classic Bayes' Problem) ---


def solve_q1_medical_test():
    """
    P(Disease) = 0.01
    P(Positive | Disease) = 0.95 (True Positive Rate/Sensitivity)
    P(False Positive) = 0.05
    Find P(Disease | Positive).
    """
    print("--- Question 1: Medical Test (Bayes' Theorem) ---")

    # E1 = Disease (D), A = Positive Test (P)
    P_D = 0.01          # Prior Probability: P(D)
    P_P_given_D = 0.95  # Likelihood: P(P | D) - True Positive Rate

    # False Positive Rate is P(Positive | Not Disease)
    P_P_given_not_D = 0.05

    P_D_given_P, P_P = bayes_theorem(P_D, P_P_given_D, P_P_given_not_D)

    print(
        f"P(Disease | Positive) = {P_D_given_P:.4f} (Approx {P_D_given_P * 100:.1f}%)")
    # Expected Answer: 0.161 (16.1%)

# --- Question 2: Dependent Probability (Conditional/Joint) ---


def solve_q2_balls_dependent():
    """
    Bag: 4 Red (R1), 6 Blue (B). Total 10. Two balls drawn without replacement.
    Given first ball was red (A), what is P(Second ball is Red | First was Red)? P(R2 | R1)
    This is a direct conditional probability, NOT requiring the full Bayes' formula.
    """
    print("\n--- Question 2: Balls (Direct Conditional Probability) ---")

    # State after the first draw (R1)
    remaining_total = 9
    remaining_red = 3

    # P(R2 | R1) = remaining_red / remaining_total
    P_R2_given_R1 = remaining_red / remaining_total

    print(
        f"P(Second Red | First Red) = 3 / 9 = {P_R2_given_R1:.4f} (Approx {P_R2_given_R1 * 100:.2f}%)")
    # Expected Answer: 0.3333 (33.33%)

# --- Question 3: Factory Defective (Bayes' Theorem with Partitions) ---


def solve_q3_factory_defective():
    """
    P(Machine A) = 0.80 (E1)
    P(Machine B) = 0.20 (E2)
    P(Defective | A) = 0.02 (P(D | E1))
    P(Defective | B) = 0.05 (P(D | E2))
    Find P(A | Defective).
    """
    print("\n--- Question 3: Factory Defective (Generalized Bayes) ---")

    # Define events and probabilities
    P_A = 0.80  # P(E1)
    P_B = 0.20  # P(E2)
    P_D_given_A = 0.02  # P(A | E1)
    P_D_given_B = 0.05  # P(A | E2)

    # Law of Total Probability: P(Defective) = P(D|A)P(A) + P(D|B)P(B)
    P_D = (P_D_given_A * P_A) + (P_D_given_B * P_B)

    # Bayes' Theorem: P(A | D) = P(D | A) * P(A) / P(D)
    P_A_given_D = (P_D_given_A * P_A) / P_D

    print(f"P(Defective) = {P_D:.4f}")
    print(
        f"P(Machine A | Defective) = {P_A_given_D:.4f} (Approx {P_A_given_D * 100:.1f}%)")
    # Expected Answer: 0.6154 (61.5%)

# --- Question 4: Simple Conditional Probability (Joint/Marginal) ---


def solve_q4_ice_cream_chocolate():
    """
    P(Ice Cream) = 0.70 [P(I)]
    P(Ice Cream AND Chocolate) = 0.40 [P(I ∩ C)]
    Find P(Chocolate | Ice Cream) = P(C | I).
    Formula: P(C | I) = P(I ∩ C) / P(I)
    """
    print("\n--- Question 4: Ice Cream & Chocolate (Conditional Probability) ---")

    P_I = 0.70
    P_I_and_C = 0.40

    P_C_given_I = P_I_and_C / P_I

    print(
        f"P(Chocolate | Ice Cream) = {P_I_and_C} / {P_I} = {P_C_given_I:.4f} (Approx {P_C_given_I * 100:.1f}%)")
    # Expected Answer: 0.5714 (57.1%)


# Run all solutions
solve_q1_medical_test()
solve_q2_balls_dependent()
solve_q3_factory_defective()
solve_q4_ice_cream_chocolate()
