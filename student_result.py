def calculate_student_result(marks):

    if not marks:
        raise ValueError("Marks list cannot be empty")

    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    result = "Pass" if average_marks >= 40 else "Fail"

    return average_marks, result


marks = [65, 72, 38, 80]

average, result = calculate_student_result(marks)

print("Average:", average)
print("Result:", result)
