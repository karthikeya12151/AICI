def generate_email(name):
    parts = name.strip().split()
    if len(parts) < 2:
        return "Invalid name format"
    first_letter = parts[0][0].lower()
    last_name = parts[-1].lower()
    email = f"{first_letter}{last_name}@sru.edu.in"
    return email

student_names = input("Enter student names separated by commas: ").split(',')

for name in student_names:
    email = generate_email(name)
    print(f"{name.strip()} -> {email}")