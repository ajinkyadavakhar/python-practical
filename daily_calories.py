def calculate_calories(carbs , fats , protein ):
    total = carbs * 4 + fats * 9 + protein * 4
    return total

c = float(input("enter carbs:"))
f = float(input("enter fats:"))
p = float(input("enter protein:"))

result = calculate_calories(c,f,p)
print("total calories : ", result)