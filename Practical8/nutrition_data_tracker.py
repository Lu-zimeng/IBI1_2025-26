class food_item:
    def __init__(self,name,calories,protein,carbohydrates,fat):
        self.name=name
        self.calories=calories
        self.protein=protein
        self.carbohydrates=carbohydrates
        self.fat=fat
def calculate_total_nutrition(consumed_items):
    total_calories=0
    total_protein=0
    total_carbohydrates=0
    total_fat=0
    for food in consumed_items:
        total_calories+=food.calories
        total_protein+=food.protein
        total_carbohydrates+=food.carbohydrates
        total_fat+=food.fat
    return total_calories,total_protein,total_carbohydrates,total_fat

print("Please type in the nutrition of the food as: food_name calories protein carbohydrates fat")
print("Input q to end inputing food")

food_list = []

while True:
    line = input("Type in food:")
    if line.strip().lower() == "q":
        break
    parts = line.split()
    name = parts[0]
    cal = float(parts[1])
    pro = float(parts[2])
    carb = float(parts[3])
    fat = float(parts[4])

    food = food_item(name, cal, pro, carb, fat)
    food_list.append(food)
    print("✅Added")

print("Total nutrition intake:")
total_cal, total_pro, total_carb, total_fat = calculate_total_nutrition(food_list)

print("Total calories: "+str(total_cal))
print("Total protein: "+str(total_pro))
print("Total carbohydrates: "+str(total_carb))
print("Total fat: "+str(total_fat))
if total_cal>2500:
    print("⚠️ Warning: You have consumed more than 2500 calories!")
if total_fat>90:
    print("⚠️ Warning: You have consumed more than 90g fat!")