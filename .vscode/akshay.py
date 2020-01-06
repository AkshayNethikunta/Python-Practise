your_weight_is=int(input("your weight please: "))
print("your_weight_is : " + str(your_weight_is))

kg_or_lb=input("enter kg or lb:" )

print(kg_or_lb)

if (kg_or_lb == "kg"):
    weight_in_lbs= your_weight_is * 2.20
    print(weight_in_lbs)
elif (kg_or_lb== "lb"):
    weight_in_lbs= your_weight_is * 0.45
    print(weight_in_lbs)
else:
    print("enter in kgs or lbs")



