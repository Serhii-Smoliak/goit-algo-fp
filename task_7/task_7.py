import random
import matplotlib.pyplot as plt
from tabulate import tabulate

num_simulations = 1000000
sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    sum_counts[dice_sum] += 1

sum_probabilities = {sum_value: count / num_simulations for sum_value, count in sum_counts.items()}

theoretical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

theoretical_probabilities_percentage = {k: v * 100 for k, v in theoretical_probabilities.items()}
simulated_probabilities_percentage = {k: v * 100 for k, v in sum_probabilities.items()}

table_data = []

for sum_value in range(2, 13):
    table_data.append([
        sum_value,
        f"{simulated_probabilities_percentage[sum_value]:.2f}",
        f"{theoretical_probabilities_percentage[sum_value]:.2f}"
    ])

print(tabulate(table_data, headers=["Сума", "Симульована імовірність (%)", "Теоретична імовірність (%)"], tablefmt="pretty"))

sums = list(range(2, 13))
simulated_probs = [simulated_probabilities_percentage[sum_value] for sum_value in sums]
theoretical_probs = [theoretical_probabilities_percentage[sum_value] for sum_value in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, simulated_probs, width=0.4, label='Симульована імовірність (%)', align='center')
plt.bar([x + 0.4 for x in sums], theoretical_probs, width=0.4, label='Теоретична імовірність (%)', align='center')
plt.xlabel('Сума')
plt.ylabel('Імовірність (%)')
plt.title('Ймовірність сум при киданні двох кубиків')
plt.xticks(sums, [str(sum_value) for sum_value in sums])
plt.legend()
plt.grid(True)
plt.show()
