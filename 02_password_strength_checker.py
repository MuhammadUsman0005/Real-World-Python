def check_password(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "digit": any(char.isdigit() for char in password),
        "special": any(char in '!@#$%&*()' for char in password)
    }

    if all(criteria.values()):
        return "Strong Password!"
    else:
        weak_points = [k for k,v in criteria.items() if not v]
        return f"Weak! Missing: {','.join(weak_points)}"

print(check_password(input("Enter password: ")))