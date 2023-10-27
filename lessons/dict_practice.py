name: dict[str, float]
dict()

#Creates new dictionary
ice_cream: dict[str, float] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print(ice_cream)

#Added mint
ice_cream["mint"] = 3
print(ice_cream)

#Deletes mint
ice_cream.pop("mint")
print(ice_cream)

#Access value to print one flavor
print(ice_cream["chocolate"])

#Update vanilla orders
ice_cream["vanilla"] += 2
print(ice_cream)

#Print length
print(len(ice_cream))

#Check if values in dictionary
print("chocolate" in ice_cream)
print("mint" in ice_cream)

if("mint" in ice_cream):
    print(ice_cream["mint"])
else:
    print("no orders of mint")

#Loop through dictionary
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders")

