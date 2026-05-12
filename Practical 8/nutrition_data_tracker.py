# Define a class (A class can be understood as a template for batch-creating food objects with the same structure.)
class food_item:
    # __init__() is a special function used aligning with "class"
      # "self" must be placed as the first parameter, referring to "the food object itself that is currently being created".
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = float(calories) # float() is applied to avoid only integer arithmetic problem
        self.protein = float(protein)
        self.carbohydrates = float(carbohydrates)
        self.fat = float(fat)

# Define a function that calculates the total nutrient intake
def calculate_daily_nutrition(food_list): # "food_list" here is only a placeholder not a variable
    # Set variables for further calculation
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0
    
    # When running "calculate_daily_nutrition(unhealthy_diet)" (line 67), "unhealthy_diet" is considered "food_list"
      # This helps to understand why "unhealthy_diet" is input as a list using []
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbohydrates
        total_fat += food.fat
    
    print("24-hour nutrient intake summary:")
    print(f"Total calories: {total_calories:.1f} kcal")
    print(f"Total protein: {total_protein:.1f} g")
    print(f"Total carbohydrates: {total_carbs:.1f} g")
    print(f"Total fat: {total_fat:.1f} g")
    # ".1f" means keeping one decimal place
    
    # Examine whether the warning should be issued
    warning_issued = False
    
    if total_calories > 2500:
        print(f"Warning: Calorie intake exceeds the limit! Recommended daily intake is no more than 2500 kcal. Current intake: {total_calories:.1f} kcal.")
        warning_issued = True
    
    if total_fat > 90:
        print(f"Warning: Fat intake exceeds the limit! Recommended daily intake is no more than 90 g. Current intake: {total_fat:.1f} g.")
        warning_issued = True
    
    if warning_issued == False:
        print("Nutrient intake is within the recommended range.")
    
    return {
        "total_calories": total_calories,
        "total_protein": total_protein,
        "total_carbohydrates": total_carbs,
        "total_fat": total_fat
    }

if __name__ == "__main__":
    
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    banana = food_item("Banana", 105, 1.3, 27, 0.4)
    chicken_breast = food_item("Chicken Breast (100g)", 165, 31, 0, 3.6)
    rice = food_item("White Rice (1 cup)", 206, 4.3, 45, 0.4)
    egg = food_item("Egg", 78, 6.3, 0.6, 5.3)
    burger = food_item("Cheeseburger", 550, 25, 40, 30)
    fries = food_item("French Fries (medium)", 380, 4, 48, 19)

    print("-- Example: Unhealthy diet --")
    unhealthy_diet = [burger, fries, burger, fries]
    calculate_daily_nutrition(unhealthy_diet)