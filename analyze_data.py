def analyze__data(data):

    financial_info = {}

    for line in data.split('\n'): #amboxj datan bajanum enq toxeri

        line = line.strip() # amen toxi aj u dzax maseric hanum enq avel bacatnery

        if not line:  # ete datark e toxy sharunakel
            continue

        key , value = line.split(':') # splity gcum e listi mej ev ':' ov bajanum maseri
        key = key.strip() # maqrum e avel space er@
        value = value.strip()
        
        if key == 'Company':
            financial_info['Company'] = value
        elif key == 'Quarter':
            financial_info['Quarter'] = value
        elif key in ['Revenue', 'Expenses', 'Net Income','EPS', 'Assets', 'Liabilities', 'Equity']:
            financial_info[key] = float(value.strip('$').replace(',' , ''))

    return financial_info








