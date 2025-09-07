prior_arrests = int(input("Prior arrests:"))
loc_ord = input("Prior arrests for local ordinance (Y/N):")
age = int(input("Age at release:"))
score = 0
if prior_arrests >= 2:
    score = score + 1
if prior_arrests >= 5:
    score = score + 1
if loc_ord == "Y":
    score = score + 1
if age >= 18 and age <= 24:
    score = score + 1
if age >= 40:
    score = score -1
print(f"The recidivism risk score is {score}")
