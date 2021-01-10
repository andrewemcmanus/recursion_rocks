# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    # Write code here

    if n < 1:
        print('n must be > 0')
    elif n == 1:
        outcome = ['H', 'T']
        return outcome
    else:
        outcome = coin_flips(n - 1)
        new_outcome = []
        for i in range(len(outcome)):
            add_h = outcome[i] + 'H'
            new_outcome.append(add_h)
            add_t = outcome[i] + 'T'
            new_outcome.append(add_t)
            # print(new_outcome)
        return new_outcome
user_input = input('Enter the number of coin flips: ')
n = int(user_input)
print(coin_flips(n))
# => ["HH", "HT", "TH", "TT"]
