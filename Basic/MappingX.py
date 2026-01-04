# Key Value and its called as Mapping    
# Duplication of key is not allowed but the last value will be considered as final
# Values are mutable in Dictionary

Information = {"Name" : "Rahul", "Age" : 25, "City" : "Pune", "Marks" : 89.32, "City" : "Mumbai"} 

print(Information)

print(Information["City"])
Information["Age"] = 26

print(Information)