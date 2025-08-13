def cm_to_inches(cm):
    return cm / 2.54

cm_value = float(input("Enter length in centimeters: "))
inches = cm_to_inches(cm_value)
print(f"{cm_value} cm is {inches:.3f} inches")