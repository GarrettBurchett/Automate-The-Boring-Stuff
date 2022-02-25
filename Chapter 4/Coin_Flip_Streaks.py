# Coin Flip Streaks
import random

numberOfStreaks = 0
tosses = [random.choice(('H', 'T')) for _ in range(10000)]
for idx,toss in enumerate(tosses):
    try:
        if (tosses[idx:idx+6] == ['H', 'H', 'H', 'H', 'H', 'H']) or (
        tosses[idx:idx+6] == ['T', 'T', 'T', 'T', 'T', 'T']):
            numberOfStreaks += 1
    except IndexError:
        break

print(f"Number of 6 Heads or Tails in a row: {numberOfStreaks}")
print(f"Chance of streak: {round(numberOfStreaks / 10000, 2)}")