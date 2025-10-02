# Solves Question 2 and 4 - Conditional Probability using Proportions/Set Theory

def solve_ice_cream_cake_problem():
    """
    Question 2: In a survey of 100 people, 50 like ice cream (I), 20 like both (I ∩ C). 
    If a person likes ice cream, what is the probability they also like cake (C)?
    P(C | I)
    """
    print("--- Question 2 (Ice Cream & Cake: Set Theory) ---")

    # Given data (using counts/proportions)
    n_total = 100
    n_ice_cream = 50
    n_both = 20

    # The probability is the ratio of people who like BOTH, among those who like ICE CREAM.
    # P(C | I) = P(C ∩ I) / P(I) = n(C ∩ I) / n(I)

    prob_c_given_i = n_both / n_ice_cream

    print(f"Favorable (Both): {n_both}")
    print(f"Given Set (Ice Cream): {n_ice_cream}")
    print(
        f"P(Cake | Ice Cream) = {n_both} / {n_ice_cream} = {prob_c_given_i:.4f}")
    print(f"Result: {prob_c_given_i:.4f} (or {prob_c_given_i * 100:.2f}%)")


def solve_glasses_male_problem():
    """
    Question 4: 30 students total. 12 wear glasses (G). 8 males (M) wear glasses.
    What is P(Male | Glasses)?
    """
    print("\n--- Question 4 (Glasses & Gender: Set Theory) ---")

    # Given data (counts)
    n_total = 30
    n_glasses = 12
    n_male_and_glasses = 8  # This is n(M ∩ G)

    # We want P(M | G) = n(M ∩ G) / n(G)

    prob_m_given_g = n_male_and_glasses / n_glasses

    print(f"Favorable (Male AND Glasses): {n_male_and_glasses}")
    print(f"Given Set (Glasses): {n_glasses}")
    print(
        f"P(Male | Glasses) = {n_male_and_glasses} / {n_glasses} = {prob_m_given_g:.4f}")
    print(f"Result: {prob_m_given_g:.4f} (or {prob_m_given_g * 100:.2f}%)")


solve_ice_cream_cake_problem()
solve_glasses_male_problem()
