def result(marks):
    t = sum(marks)
    a = t / len(marks)

    if a >= 40:
        print("Pass")
    else:
        print("Fail")

    print("Average:", a)


marks = [65, 72, 38, 80]
result(marks)