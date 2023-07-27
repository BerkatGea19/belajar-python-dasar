#Beajar Tipe Data Dictionary

customer = {"Name":"Berkat", "Age":20, "Address":"Yogyakarta"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "X"
customer["Name"] = "Berkat Gea"

del customer["Address"]

for key, value in customer.items():
    print(f"{key}:{value}")