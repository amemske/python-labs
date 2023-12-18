# In a program, a dictionary contains lists of students and their courses. The teacher is interested
# to have a dictionary that has the courses as key and the students enrolled in each course as values.
# Each key has three different values.
#
# To address this requirement, write a function to invert the dictionary and implement a solution that
# satisfies the teacher’s need. In particular, the function will need to turn each of the list items
# into separate keys in the inverted dictionary. Also provide a technical explanation for the code and its output in minimum 200 words.

# write a function to invert the dictionary
# the function will need to turn each of the list items into separate keys in the inverted dictionary

# Sample input:
student_courses = {'Stud1': ['CS1101', 'CS2402', 'CS2001'], 'Stud2': ['CS2402', 'CS2001', 'CS1102'], }


def invert_dict_func(any_dict):
    inverted_dict = {}

    for student_name, course_codes in any_dict.items():
        for course_code in course_codes:
            if course_code in inverted_dict:
                inverted_dict[course_code].append(student_name)
            else:
                inverted_dict[course_code] = [student_name]

    # Print the original  dictionary
    print(f"Original Dictionary: ${any_dict}")

    # Print the inverted  dictionary
    print(f"Inverted Dictionary: ${inverted_dict}")

    return inverted_dict


invert_dict_func(student_courses)

# Output -------------------------
# Original Dictionary: ${'Stud1': ['CS1101', 'CS2402', 'CS2001'], 'Stud2': ['CS2402', 'CS2001', 'CS1102']}
# Inverted Dictionary: ${'CS1101': ['Stud1'], 'CS2402': ['Stud1', 'Stud2'], 'CS2001': ['Stud1', 'Stud2'], 'CS1102': ['Stud2']}

# Explanation
# This function "invert_dict_func" takes any dictionary as an argument, we pass the "student_courses" variable, which holds the original dictionary we want to invert.
#
# Inside the "invert_dict" function, we create an empty dictionary to store the key-values pairs of the new dictionary .
#
# Next, we loop through the passed dictionary, using "student_names" and "course_codes" as key-value pairs. We also create an inner loop to loop through the list of course codes, if a course_code is already stored in the "invered_dict" as a key, we append student name as it's value, otherwise, we add the "course_code" as a key and the current student name as it's value.Finally, we return the "inverted_dict" with the new dictionary items.
#
# We invoke the "invert_dict_func" and pass the "student_courses" variable
