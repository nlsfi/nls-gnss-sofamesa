def grading(value, tolerance_1st_min, tolerance_1st_max, tolerance_2nd_min, tolerance_2nd_max, tolerance_3rd_min, tolerance_3rd_max, tolerance_4th_min, tolerance_4th_max, tolerance_5th_min, weighing):
    
    if tolerance_1st_max < tolerance_1st_min:
        if value <= 100 and value >= tolerance_1st_max:
            grade = 5 * weighing
        elif value < tolerance_2nd_min and value >= tolerance_2nd_max:
            grade = 4 * weighing
        elif value < tolerance_3rd_min and value >= tolerance_3rd_max:
            grade = 3 * weighing
        elif value < tolerance_4th_min and value >= tolerance_4th_max:
            grade = 2 * weighing
        elif value < tolerance_5th_min:
            grade = 1 * weighing
        else:
            grade = 0
        return round(grade, 3)
    else:
        if value >= 0 and value <= tolerance_1st_max:
            grade = 5 * weighing
        elif value > tolerance_2nd_min and value <= tolerance_2nd_max:
            grade = 4 * weighing
        elif value > tolerance_3rd_min and value <= tolerance_3rd_max:
            grade = 3 * weighing
        elif value > tolerance_4th_min and value <= tolerance_4th_max:
            grade = 2 * weighing
        elif value > tolerance_5th_min:
            grade = 1 * weighing
        else:
            grade = 0
        return round(grade, 3)