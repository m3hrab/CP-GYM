brand = input("Brand: ")
wheel = input("Wheel: ")
horse_power = int(input("Horse-Power: "))

extra_tax = 0
if brand.lower() == "ferrari":
    extra_tax += 30
elif brand.lower() == "ford":
    extra_tax += 25

if wheel.lower() == "left":
    extra_tax += 10

if horse_power > 2000:
    extra_tax += 10

print("Extra Tax: " + str(extra_tax) + "%")