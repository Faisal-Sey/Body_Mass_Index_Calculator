import re
print("*******************Adult Body Mass Index (BMI) Calculator********************")

m = input("Enter weight(kilograms/kg): ")
h = input("Enter height(meters/m): ")

def bmi(m, h):
    mass = re.findall(r"\d+", m)[0]
    height = re.findall(r"\d+", h)[0]
    BMI = int(mass) / (int(height) ** 2)
    if BMI < 18.5:
        print(" ")
        print(f"Body Mass Index: {BMI} kg/m^2\nWeight Status: Underweight")
        print(" ")
        print("******Health Tips********:\nEat five to six smaller meals during the day rather than two or three large meals."
              "Choose nutrient-rich foods.\nAs part of an overall healthy diet, choose whole-grain breads, "
              "pastas and cereals; fruits and vegetables;\ndairy products; lean protein sources; and nuts and seeds. "
              "Try smoothies and shakes.")

        print(" ")
        print("Disease risk: ----")
    elif 18.5 <= BMI <= 24.9:
        print(" ")
        print(f"Body Mass Index: {BMI}kg/m^2\nWeight Status: Normal")
        print(" ")
        print("******Health Tips********:\nYour weight is okay for a normal adult. Continue Exercising")

        print(" ")
        print("Disease risk: ----")
    elif 25.0 <= BMI <= 29.9:
        print(" ")
        print(f"Body Mass Index: {BMI}kg/m^2\nWeight Status: Overweight")
        print(" ")
        print("******Health Tips********:\nYou are overweight so you should start regular physical activity when you begin your healthy eating plan.\n"
              "Being active may help you use calories. Regular physical activity may help you stay at a healthy weight.\n"
              "Learn more about healthy eating and physical activity to lose or maintain weight.")

        print(" ")
        print("Disease risk: Increased/High")
    elif BMI >= 30:
        print(" ")
        print(f"Body Mass Index: {BMI}kg/m^2\nWeight Status: obese")
        print(" ")
        print("******Health Tips********:\nCommon treatments for obesity include losing weight through healthy eating, being more physically active, and making other changes to your usual habits.\n"
              "Weight-management programs may help some people lose weight or keep from regaining lost weight.\n"
              "Some people who have obesity are unable to lose enough weight to improve their health or are unable to keep from regaining weight.\n"
              "In such cases, a doctor may consider adding other treatments, including weight-loss medicines, weight-loss devices, or bariatric surgery.")

        print(" ")
        print("Disease risk: Very High")

bmi(m, h)