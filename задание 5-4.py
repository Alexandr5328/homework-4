def count_xy(string):
    x_count = string.count('x')
    y_count = string.count('y')
    return f"x: {x_count}, y: {y_count}"
    
input_string = "xyxyxyxyy"
result = count_xy(input_string)
print(result)