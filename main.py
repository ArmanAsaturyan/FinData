import analyze_data
import calculation

# Read data from text files
file_names = ['CompanyA_Quarter1.txt', 'CompanyA_Quarter2.txt', 'CompanyB_Quarter1.txt', 'CompanyB_Quarter2.txt']

file_data = {}

for file_name in file_names:
    with open(file_name , 'r') as file:
        data = file.read()
        file_data[file_name] = data
        

# Analyze the data and store in dictionary
analyzed_data = {}
for file_name, data in file_data.items():
    company_data = analyze_data.analyze__data(data)
    analyzed_data[company_data['Company'] + '_' + company_data['Quarter']] = company_data
    

# Allow the user to input the name of the organization
user_input = input("Enter the name of the organization (Company A or Company B): ").strip()

# Check if the user input corresponds to any of the analyzed companies
for key, company_data in analyzed_data.items():
    if user_input.lower() in key.lower():
        print(f"Difference between Q2 and Q1 for {company_data['Company']} ({company_data['Quarter']}):")
        difference = calculation.calculate_difference(analyzed_data[company_data['Company'] + '_Q1'], analyzed_data[company_data['Company'] + '_Q2'])
        for metric, value in difference.items():
            print(f"{metric}: {value}")
        break
else:
    print("Organization not found in the analyzed data.")
















