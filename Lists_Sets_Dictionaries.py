#Lists
grocery=["apple","banana","orange","watermelon","papaya","cucumber","strawberry","blueberry"]
for i in grocery:
    print(i)

#Append elements in list
grocery.append("spinach")
print(grocery)

#Remove elements from list
grocery.remove("banana")
print(grocery)

#Indexing
print(grocery.index("cucumber"))

#Insert elements at preferred index
grocery.insert(4,"spinach")
print(grocery)
print(grocery.index("cucumber"))

#Print the element present at a particular index
print(grocery[3])

#Sets (No repetitions)
print(set(grocery))

#Dictionary (Keys:Values)
class_record={"name":"Max","surname":"Turner","sex":"Male","class":12,"percentage":97.23}
print(class_record["name"],class_record["sex"],class_record["percentage"])

#Multiple dictionaries in a list
topper_list=[{"name":"Arif","surname":"Hamiid","sex":"Male","class":12,"percentage":92.23},
             {"name":"Tirtha","surname":"Ghosh","sex":"Male","class":11,"percentage":89.45},
             {"name":"Seema","surname":"Sharma","sex":"Female","class":10,"percentage":98.2},
             {"name":"Naseem","surname":"Ali","sex":"Male","class":9,"percentage":88.44}]
print(topper_list[1]["name"])
print(type((topper_list[0]["percentage"])))