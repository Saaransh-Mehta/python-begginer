def print_kwargs(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}:{values}")
    
print_kwargs(name="Happy Stark",role="Superhero",assets="23Billion")
