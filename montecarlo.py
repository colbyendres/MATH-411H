import numpy as np
from math import comb

TRIALS = 10 ** 6
HAND_SIZE = 7
a,b,c = 0,0,0 # successes for parts a, b, c 

for i in range(TRIALS):
    hand = np.random.permutation(52)[:HAND_SIZE] # Generate HAND_SIZE distinct integers
    num_queens, num_jacks = 0,0
    for card in hand:
        if card < 4: # Label 0,1,2,3 as queens
            num_queens += 1
        elif card < 8: # Label 4,5,6,7 as jacks
            num_jacks += 1
    if num_queens == 3:
        a += 1
    if num_jacks == 2:
        b += 1
    if num_queens == 3 or num_jacks == 2:
        c += 1

total_hands = comb(52,7)
true_a = float(comb(4,3) * comb(48,4) / total_hands)
true_b = float(comb(4,2) * comb(48,5) / total_hands)
true_c = true_a + true_b - float(comb(4,2) * comb(4,3) * comb(44,2) / total_hands)

print("experimental/theoretical P(A):", float(a)/TRIALS, true_a)
print("experimental/theoretical P(B):", float(b)/TRIALS, true_b)
print("experimental/theoretical P(C):", float(c)/TRIALS, true_c)