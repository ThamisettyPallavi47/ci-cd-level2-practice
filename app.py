def calculate_average(marks):
    if not marks:
        raise ValueError("Marks cannot be empty")

    return sum(marks) / len(marks)
