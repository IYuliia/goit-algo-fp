import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)} 
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        
        total_sum = die1 + die2
        
        sum_counts[total_sum] += 1
 
    probabilities = {sum_: count / num_rolls for sum_, count in sum_counts.items()}
    
    return probabilities, sum_counts

num_rolls = 1000000
probabilities, sum_counts = monte_carlo_simulation(num_rolls)

print("Ймовірності, отримані методом Монте-Карло:")
for total_sum, probability in probabilities.items():
    print(f"Сума {total_sum}: {probability:.4f}")


analytic_probabilities = {
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


print("Аналітичні ймовірності:")
for total_sum, analytic_prob in analytic_probabilities.items():
    print(f"Сума {total_sum}: {analytic_prob:.4f}")
    

x_positions = range(2, 13)

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35

ax.bar([x - bar_width/2 for x in x_positions], probabilities.values(), width=bar_width, alpha=0.8, label='Метод Монте-Карло', color='#1f77b4', edgecolor='black')
ax.bar([x + bar_width/2 for x in x_positions], analytic_probabilities.values(), width=bar_width, alpha=0.8, label='Аналітичні ймовірності', color='#ff7f0e', edgecolor='black')

ax.set_xlabel('Сума')
ax.set_ylabel('Ймовірність')
ax.set_title('Порівняння ймовірностей (Метод Монте-Карло vs Аналітичні)')
ax.legend()

plt.show()
