def transform_unordered_semester_data(unordered_module_information, semester_grades, module_name):
    module_information = None  # Initialize to None before the loop starts
    
    for row in unordered_module_information:  # extracted_data contains the cleaned table rows
        if row[0] != "":  # If first element is NOT empty, it's a main entry
            module_information = {
                "module_name": module_name,
                "semester": row[0],
                "exam_type": row[1],
                "date": row[2] if row[2] else None,
                "final_grade": row[3] if row[3] else None,
                "grading_details": []
            }
            semester_grades.append(module_information)
        else:  # If first element IS empty, it's a subset of the last main entry
            if module_information:
                module_information["grading_details"].append({
                    "subject": row[1], 
                    "score": row[3] if row[3] else None
                })
    return