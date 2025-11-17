# Implements the simple Spam Detection calculation using Bayes' Theorem.

# Sample Data Analysis (from the provided table)
# EmailID | Contains "Offer" | Spam
# 001     | Yes              | Yes
# 002     | Yes              | No
# 003     | No               | No
# 004     | Yes              | Yes

# --- 1. Define Probabilities from Sample Data ---

# Total number of emails in the sample
N = 4

# P(Spam): Prior probability of an email being spam
count_spam = 2
P_Spam = count_spam / N
print(f"P(Spam) (Prior) = {P_Spam:.2f}")

# P(Offer): Marginal probability of an email containing "Offer"
count_offer = 3
P_Offer = count_offer / N
print(f"P(Offer) = {P_Offer:.2f}")

# P(Offer | Spam): Likelihood of "Offer" given it is Spam
count_offer_AND_spam = 2 # Emails 001, 004
count_is_spam = 2
P_Offer_given_Spam = count_offer_AND_spam / count_is_spam
print(f"P(Offer | Spam) (Likelihood) = {P_Offer_given_Spam:.2f}")

# --- 2. Apply Bayes' Theorem ---

# P(Spam | Offer) = [P(Offer | Spam) * P(Spam)] / P(Offer)

P_Spam_given_Offer = (P_Offer_given_Spam * P_Spam) / P_Offer

print("\n--- Bayes' Theorem Calculation ---")
print(f"P(Spam | Offer) = ({P_Offer_given_Spam:.2f} * {P_Spam:.2f}) / {P_Offer:.2f}")
print(f"P(Spam | Offer) = {P_Spam_given_Offer:.4f} (or {P_Spam_given_Offer * 100:.2f}%)")

# Conclusion: There is a 66.67% chance the email is spam given it contains "offer".