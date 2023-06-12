# Importing modules
import pandas as pd
# Read datasets/yearly_deaths_by_clinic.csv into yearly
yearly = pd.read_csv('yearly_deaths_by_clinic.csv')
# Print out yearly
print(yearly)

# Calculate proportion of deaths per no. births
yearly['proportion_deaths'] = yearly['deaths'] / yearly['births']
# Extract Clinic 1 data into clinic_1 and Clinic 2 data into clinic_2
clinic_1 = yearly[yearly["clinic"] == "clinic 1"]
clinic_2 = yearly[yearly['clinic'] == 'clinic 2']
# Print out clinic_1
print(clinic_1)

# Import matplotlib
import matplotlib.pyplot as plt