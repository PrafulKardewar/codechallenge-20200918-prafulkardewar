
from csv import reader,writer,QUOTE_MINIMAL

list_of_rows = []
uncleaned_data=[]
count=0


def clean_and_fix_the_data(table_info):
    global count
    flag = 0
    for row in table_info:
        if flag == 0:
            row.extend(["BMI (Body Mass Index) ", "BMI Range (kg/m2)", "Health risk"])
            flag = 1
            list_of_rows.append(row)
            continue

        try:
            if row[0] not in ['Male','Female','Other']:
                uncleaned_data.append(row)
                continue
            height = int(row[1]) / 100
            mass = int(row[2])

        except ValueError as ve:
            uncleaned_data.append(row)
            continue
        else:
            bmi = mass / height
            if bmi <= 18.4:
                bmi_category = "Underweight"
                bmi_range = bmi
                health_risk = "Malnutrition risk"
            elif bmi >= 18.4 and bmi <=24.9:
                bmi_category = "Normal weight"
                bmi_range = bmi
                health_risk = "Low risk"
            elif bmi >= 25 and bmi <= 29.9:
                count = count+1
                bmi_category = "Overweight"
                bmi_range = bmi
                health_risk = "Enhanced risk"
            elif bmi >= 30 and bmi <= 34.9:
                bmi_category = "Moderately obese"
                bmi_range = bmi
                health_risk = "Medium risk"
            elif bmi >= 35 and bmi <= 39.9:
                bmi_category = "Severely obese"
                bmi_range = bmi
                health_risk = "High risk"
            elif bmi >= 40:
                bmi_category = "Very severely obese"
                bmi_range = bmi
                health_risk = "Very high risk"
            bmi_new_field=[bmi_category, str(round(bmi_range,2)), health_risk]
            row.extend(bmi_new_field)
            list_of_rows.append(row)
    return data

with open(r'Data_for_BMI_Calculator_Height_Weight.csv', 'r') as file:
    data = reader(file)
    clean_and_fix_the_data(data)


with open(r'output_for_BMI_Calculator_Height_Weight.csv', 'w', newline='') as file:
    data = writer(file, delimiter=',')
    for row in list_of_rows:
        data.writerows([row])

for row in uncleaned_data:
    print(row)

print('Total no of overweight people are = ',count)
