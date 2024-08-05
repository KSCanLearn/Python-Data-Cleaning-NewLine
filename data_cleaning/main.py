import datetime
import common_vars as common_variable
import data_cleaning as dc

### BEGIN ###
print(f'Starting at {datetime.datetime.now()}')

# Call the function to clean the CSV
dc.clean_csv(common_variable.input_file, common_variable.output_location)

print(f'Ended at {datetime.datetime.now()}')
print(f'Cleaned CSV file has been saved to {common_variable.output_location}')