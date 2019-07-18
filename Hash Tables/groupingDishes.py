def groupingDishes(dishes):
    out = {}
    for dish in dishes:
        for ingredient in dish[1:]:
            if ingredient in out.keys():
                out[ingredient].append(dish[0])
            else:
                out[ingredient] = [dish[0]]
    for key in list(out):
        if len(out[key]) < 2:
            del out[key]
        else:
            out[key] = sorted(out[key])
    ingredients = sorted(out.keys())
   
    for i in range(len(ingredients)):
        ingredients[i] = [ingredients[i]]
        for j in out[ingredients[i][0]]:
            ingredients[i].append(j)
    return ingredients

# Input:
# dishes: [["Salad","Tomato","Cucumber","Salad","Sauce"], 
#  ["Pizza","Tomato","Sausage","Sauce","Dough"], 
#  ["Quesadilla","Chicken","Cheese","Sauce"], 
#  ["Sandwich","Salad","Bread","Tomato","Cheese"]]
# Expected Output:
# [["Cheese","Quesadilla","Sandwich"], 
#  ["Salad","Salad","Sandwich"], 
#  ["Sauce","Pizza","Quesadilla","Salad"], 
#  ["Tomato","Pizza","Salad","Sandwich"]]


dishes= [["Salad","Tomato","Cucumber","Salad","Sauce"],
 ["Pizza","Tomato","Sausage","Sauce","Dough"], 
 ["Quesadilla","Chicken","Cheese","Sauce"], 
 ["Sandwich","Salad","Bread","Tomato","Cheese"]]


print(groupingDishes(dishes))