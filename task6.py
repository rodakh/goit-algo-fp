def greedy_algorithm(food_items, max_budget):
    # Sort the items based on the ratio of calories to cost
    sorted_items = sorted(food_items.keys(), key=lambda x: food_items[x]["calories"] / food_items[x]["cost"],
                          reverse=True)
    selected_items = {}
    total_calories = 0
    total_cost = 0

    # Go through the sorted items and add them to the selection if they fit the budget
    for item in sorted_items:
        if total_cost + food_items[item]["cost"] <= max_budget:
            selected_items[item] = food_items[item]
            total_cost += food_items[item]["cost"]
            total_calories += food_items[item]["calories"]

    return selected_items, total_calories


def dynamic_programming(food_items, max_budget):
    item_list = list(food_items.keys())
    dp = [[0 for _ in range(max_budget + 1)] for _ in range(len(food_items) + 1)]

    for i in range(1, len(food_items) + 1):
        for w in range(1, max_budget + 1):
            if food_items[item_list[i - 1]]["cost"] <= w:
                dp[i][w] = max(
                    food_items[item_list[i - 1]]["calories"] + dp[i - 1][w - food_items[item_list[i - 1]]["cost"]],
                    dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = {}
    w = max_budget
    for i in range(len(food_items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = item_list[i - 1]
            selected_items[item] = food_items[item]
            w -= food_items[item]["cost"]

    # The last entry in the table is the total calories
    total_calories = dp[len(food_items)][max_budget]
    return selected_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 50

greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm:", greedy_result, "Total Calories:", greedy_calories)

dp_result, dp_calories = dynamic_programming(items, budget)
print("Dynamic Programming:", dp_result, "Total Calories:", dp_calories)
