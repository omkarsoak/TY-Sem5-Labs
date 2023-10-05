try:
    num_students = int(input("Enter the number of students: "))
    student_results = []

    for student in range(num_students):
        print(f"Student {student + 1}:")
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

        student_results.append(result)
        print(f"Result: {result}")

    # Display the overall results
    print("\nOverall Results:")
    i = 0
    for result in student_results:
        print(f"Student {i + 1}: {result}")
        i = i+1

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
