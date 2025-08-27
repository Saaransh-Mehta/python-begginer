newDict = {
    "name":"Varnit Tyagi",
    "bride":"Bulma",
    "subjects":["DSA, SE, ERP, Python"]
}
print(newDict["subjects"])


twoDict = {
    "name":"varnit Tyagi",
    "college":"CGC",
    "sem":"4th sem",
    "subjects":{
        "dsa":20,
        "maths":25,
        "DAA": 24
    }
}
print(twoDict["subjects"]["dsa"])
twoDict["college"] = "Chitkara University"
print(twoDict)

twoDict["sem"] = "5th sem"
twoDict.pop('sem')
print(twoDict)
twoDict.popitem()
print(twoDict)
twoDict["subjects"] = [20,202,202]
print(twoDict)
del twoDict["name"]
print(twoDict)

for key,values in twoDict.items():
    print(f"{key} = {values}")