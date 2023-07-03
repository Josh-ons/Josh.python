# list datastructure, its ordered and changable
cars = ["BMW", "Audi", "Mercedes", "dodge"]
cars[1] = "Subaru"
cars.append("Skoda")
cars.insert(2, "vw")
cars.pop(1)
cars.reverse()
cars.copy()
print(cars)
# this is a tuple, its is unchangable
fruits = ("Mangoes", "Oranges", "Pineapple", "Apples", "Oranges")
print(fruits)
x = fruits.count("Oranges")
for k in fruits:
    print(k)
# sets datastructure, unordered

countries = {"Kenya", "Uganda", "Tanzania", "Burundi", "Ethiopia"}
print(countries)

# dictionaries
matunda = {
    "amount": 40,
    "jina": "Ndizi",
    "rangi": "Yellow",
    "Age": "2_Months"
}
matunda["size"] = "large"
matunda.pop("jina")
print(matunda)
