# task2_greeting.py

def greet_user():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    full_name = f"{first_name} {last_name}"
    print(f"Hello, {full_name}! Welcome to the Python world.")

if __name__ == "__main__":
    greet_user()
