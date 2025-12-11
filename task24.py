email = input('email: ')

result = (not email.startswith("@")) and email.endswith(".com")

print(result)