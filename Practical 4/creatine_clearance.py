# Set several values of a person's information
age = 30
weight = 75
gender = "male"
creatine_concentration = 25 

# Input validation
valid = True
if age >= 100:
    print("Input variable of age needs corrected.")
    valid = False
if weight <= 20 or weight >= 80:
    print("Input variable of weight needs corrected.")
    valid = False
if creatine_concentration <= 0 or creatine_concentration >= 100:
    print("Input variable of creatinine concentration needs corrected.")
    valid = False
if gender not in ["male", "female"]:
    print("Input variable of gender needs corrected.")
    valid = False

# Calculate creatinine clearance if all inputs are valid
if valid ==  True:
    if gender == "male":
        CrCl = ((140 - age) * weight) / (72 * creatine_concentration)
    if gender == "female":
        CrCl = ((140 - age) * weight) / (72 * creatine_concentration) * 0.85

    # Print the final result
    print("The creatinine clearance rate is " + str(round(CrCl, 2)) + " ml/min")
      # "str()" is used to convert a number into a string
      # "round()" is used to round a number to a specified number of decimal places, in this case 2