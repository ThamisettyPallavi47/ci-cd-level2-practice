#DOCKER IMAGE BUILD
import os

def calculate_average(marks):
    if not marks:
        raise ValueError("Marks cannot be empty")

    return sum(marks) / len(marks)

if __name__=='__main__':
    app_env = os.getenv("APP_ENV", "development")

    print(f"Application environment: {app_env}")
    print(f"Average marks: {calculate_average([80, 90, 100])}")
