def calculate_difference(company_data_q1,company_data_q2):
    difference = {}
    for key in company_data_q1:
        if key != 'Company' and key != 'Quarter':
            difference[key] = company_data_q2[key] - company_data_q1[key]

    return difference