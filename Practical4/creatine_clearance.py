# 1. Input variables: age (years), weight (kg), gender (string), creatinine (Cr, μmol/L)
# 2. Validate each input against the specified ranges
#     Age must be less than 100 years
#     Weight must be greater than 20 kg and less than 80 kg
#     Creatinine (Cr) must be greater than 0 μmol/L and less than 100 μmol/L
#     Gender must be either "male" or "female" (case-insensitive)
# 3. If any input is invalid, print a message identifying the incorrect variable
# 4. If all inputs are valid, calculate CrCl using the Cockcroft-Gault equation:
#    CrCl = (140 - age) * weight / (72 * Cr) * (0.85 if female else 1)
# 5. Print the final CrCl value with a descriptive message

#Define input variables
# 1.input and validate age
age = float(input("Enter patient age (years): "))
while age >= 100 or age <0:
    print("Error: Age must be < 100! Please re-enter.")
    age = float(input("Enter patient age (years): "))

# 2. input and validate weight
weight = float(input("Enter patient weight (kg): "))
while weight <= 20 or weight >= 80:
    print("Error: Weight must be >20 and <80 kg! Please re-enter.")
    weight = float(input("Enter patient weight (kg): "))

# 3. input and validate gender
gender = input("Enter patient gender (male/female): ").lower()
while gender not in ["male", "female"]:
    print("Error: Gender must be 'male' or 'female'! Please re-enter.")
    gender = input("Enter patient gender (male/female): ").lower()

# 4. input and validate creatinie
cr = float(input("Enter creatinine level (μmol/L): "))
while cr <= 0 or cr >= 100:
    print("Error: Creatinine must be >0 and <100 μmol/L! Please re-enter.")
    cr = float(input("Enter creatinine level (μmol/L): "))

# 5.calculate CrCl using the Cockcroft-Gault equation
if gender == "female":
    crcl = (140 - age) * weight / (72 * cr) * 0.85
else:
    crcl = (140 - age) * weight / (72 * cr)

# 6.print the final CrCl value
print("Creatine Clearance rate (CrCl) is: " + str(round(crcl, 2)) + "µmol/l")
