default_name="jarvis"
def greet_by_name(n=default_name):
    if(n):
        message = f"Good Morning {n}"
    else:
        message = f"Good Morning {default_name}"

    return message

result = greet_by_name("Saaransh")
print(result)