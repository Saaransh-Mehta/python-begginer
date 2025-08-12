newDict = {
    "name":"Saaransh",
    "Batch":2027
}

print(newDict)
print(newDict["name"])

name = newDict.get("name")
print(name)

for values in newDict:
    print(newDict[values])

for key, values in newDict.items():
    print(key, values)

if "name" in newDict:
    print("What's your name")

newDict["Address"] = "Haryana"
print(newDict)
print(len(newDict))

newDict.popitem()
print(newDict)

newDict.pop("name")
print(newDict)

newDict["name"] = "Varnit"
print(newDict)

bigDict = {
    "names":{
        "1":"Yudhvir",
        "2":"Rana"
    },
    "batch":"2027"
}


print(bigDict)

print(bigDict["names"]["1"])
newWord = bigDict.get("names")
print(newWord)

squared_num = {x:x**2 for x in range(6) }
print(squared_num)


keys = ["name","name2","name3"]
default_values = ["varnit","tyagi","raman"]
megaDict = dict.fromkeys(keys,default_values)
print(megaDict)