try:
    subject_marks = []
    num_of_subjects = int(input("Enter number of subjects: "))

    for i in range(num_of_subjects):
        subject = float(input(f"Enter marks for subject {i + 1}: "))
        if subject < 0 or subject > 100:
            raise ValueError("Marks should be between 0 and 100.")
        subject_marks.append(subject)

    # Calculate the average marks
    average_marks = sum(subject_marks) / len(subject_marks)

    # Determine the result based on average marks
    if average_marks >= 80:
        result = "I-Division"
    elif average_marks >= 60:
        result = "II-Division"
    elif average_marks >= 40:
        result = "III-Division"
    else:
        result = "Fail"

    print(f"Result: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
