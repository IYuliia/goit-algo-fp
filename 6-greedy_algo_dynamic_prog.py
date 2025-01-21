def greedy_algorithm(items, budget):
    items_sorted = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, details in items_sorted:
        cost = details["cost"]
        calories = details["calories"]
        
        if total_cost + cost <= budget:
            selected_items.append(item)
            total_calories += calories
            total_cost += cost

    return selected_items, total_calories

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    for item, details in items.items():
        cost = details["cost"]
        calories = details["calories"]
       
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                selected_items[current_budget] = selected_items[current_budget - cost] + [item]

    return dp[budget], selected_items[budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_items, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Вибрані страви: {greedy_items}")
print(f"Максимальна калорійність: {greedy_calories}")

max_calories, selected_items = dynamic_programming(items, budget)
print("Динамічне програмування:")
print(f"Максимальна калорійність при бюджеті {budget}: {max_calories}")
print(f"Вибрані страви: {selected_items}")



