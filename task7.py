import random
import matplotlib.pyplot as plt


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def monte_carlo_dice_simulation(rolls):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(rolls):
        dice_sum = roll_dice()
        sum_counts[dice_sum] += 1

    probabilities = {sum: count / rolls for sum, count in sum_counts.items()}

    return probabilities, sum_counts


number_of_rolls = 1000000

probabilities, sum_counts = monte_carlo_dice_simulation(number_of_rolls)

print("Monte Carlo Probabilities:")
for sum, probability in probabilities.items():
    print(f"Sum {sum}: {probability:.2%}")

print("\nAnalytical Probabilities:")
analytical_probabilities = {
    2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36,
    7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36, 11: 2 / 36, 12: 1 / 36
}
for sum, probability in analytical_probabilities.items():
    print(f"Sum {sum}: {probability:.2%}")

plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), color='blue', alpha=0.7, label='Monte Carlo')
plt.bar(analytical_probabilities.keys(), analytical_probabilities.values(),
        color='red', alpha=0.5, width=0.4, label='Analytical')
plt.xlabel('Sum of dice')
plt.ylabel('Probability')
plt.title('Probability Distribution of Dice Rolls - Monte Carlo vs Analytical')
plt.xticks(range(2, 13))
plt.legend()
plt.show()
