# Solves Question 1 (Cards) and Question 5 (Balls) - Dependent Events

def solve_card_problem():
    """
    Question 1: Two cards are drawn without replacement. 
    What is the probability that the second card drawn is a heart, 
    given that the first card drawn was a heart?
    """
    print("--- Question 1 (Cards: Dependent Event) ---")
    
    # Initial state
    total_cards = 52
    hearts = 13
    
    # State after the first card (Heart) is drawn without replacement
    remaining_cards = total_cards - 1
    remaining_hearts = hearts - 1
    
    # P(Second Heart | First Heart)
    prob_b_given_a = remaining_hearts / remaining_cards
    
    print(f"Given: First card was a Heart. Remaining cards: {remaining_cards}")
    print(f"P(Second Heart | First Heart) = {remaining_hearts} / {remaining_cards}")
    print(f"Result: {prob_b_given_a:.4f} (or {prob_b_given_a * 100:.2f}%)")


def solve_ball_problem_3():
    """
    Question 3: A box contains 6 red balls and 4 green balls. Two balls are drawn 
    without replacement. What is the probability that the second ball is green, 
    given that first ball drawn was red?
    """
    print("\n--- Question 3 (Balls: Dependent Event) ---")
    
    # Initial state
    initial_total = 6 + 4
    
    # State after the first ball (Red) is drawn without replacement
    remaining_total = initial_total - 1
    remaining_green = 4  # The number of green balls is unchanged
    
    # P(Second Green | First Red)
    prob_b_given_a = remaining_green / remaining_total
    
    print(f"Given: First ball was Red. Remaining total: {remaining_total}")
    print(f"P(Second Green | First Red) = {remaining_green} / {remaining_total}")
    print(f"Result: {prob_b_given_a:.4f} (or {prob_b_given_a * 100:.2f}%)")

solve_card_problem()
solve_ball_problem_3()