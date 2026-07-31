def calculate_bmi(weight, height):
    return weight / (height ** 2)


print("===== Patient Health Risk Assessment =====\n")

name = input("Patient Name: ")

age = int(input("Age: "))
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

smoker = input("Smoker? (yes/no): ").lower()
diabetes = input("Diabetes? (yes/no): ").lower()
blood_pressure = int(input("Systolic Blood Pressure: "))
heart_rate = int(input("Resting Heart Rate: "))

bmi = calculate_bmi(weight, height)

risk = 0

if age >= 60:
    risk += 2
elif age >= 45:
    risk += 1

if bmi >= 30:
    risk += 2
elif bmi >= 25:
    risk += 1

if smoker == "yes":
    risk += 2

if diabetes == "yes":
    risk += 2

if blood_pressure >= 140:
    risk += 2
elif blood_pressure >= 130:
    risk += 1

if heart_rate > 100:
    risk += 1

print("\n========== REPORT ==========")
print(f"Patient: {name}")
print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    bmi_status = "Underweight"
elif bmi < 25:
    bmi_status = "Normal"
elif bmi < 30:
    bmi_status = "Overweight"
else:
    bmi_status = "Obese"

print(f"BMI Category: {bmi_status}")

print("\nRisk Level:")

if risk <= 2:
    print("🟢 Low Risk")
elif risk <= 5:
    print("🟡 Moderate Risk")
elif risk <= 8:
    print("🟠 High Risk")
else:
    print("🔴 Very High Risk")

print("\nHealth Summary:")

if smoker == "yes":
    print("- Smoking is a major cardiovascular risk factor.")

if diabetes == "yes":
    print("- Diabetes increases the risk of heart and kidney disease.")

if blood_pressure >= 130:
    print("- Blood pressure is above the normal range.")

if bmi >= 25:
    print("- Maintaining a healthy weight may reduce health risks.")

if heart_rate > 100:
    print("- Resting heart rate is elevated.")

print("\nThis program is for educational purposes only and is not a medical diagnosis.")
