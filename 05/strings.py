username = "Saaransh"
sliced_name = username[0:3]
print(sliced_name)  

# negative Slcing

neg_slice = username[-1:-5:-1]
print(neg_slice)


chai = "       Masala Chai        "
print(chai.strip())
print(chai.replace("Masala","Lemon").strip())

chai_types = "Lemon,Ginger,Masala,Cardmon"
print(chai_types.split(","))

name = "Varnit"
age = 23

formatted_string = "This is {1} and he is {0} years old".format(age,name)
print(formatted_string)

top_singers = ["seedhe maut", "Krishna", "Raftaar","Honey Singh"]
print(", ".join(top_singers))

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))


raw_string = r"c:/Users/varnit"
print(raw_string)