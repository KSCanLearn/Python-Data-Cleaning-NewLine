import pandas as pd
import numpy as np

# Function to clean a single field
def clean_field(field):
    if isinstance(field, str): 
        return field.replace('\n', '')
    else: 
        return field

def clean_csv(input_file, output_location):
    # Read the CSV file into a DataFrame
    
    df = pd.read_csv(input_file, dtype=str)
    df["Content"] = df["Content"].apply(clean_field)
    df["Summary"] = df["Summary"].apply(clean_field)

    chunk_size = 100
    num_chunks = len(df) // chunk_size + 1

    for i, chunk in enumerate(np.array_split(df, num_chunks)):
        chunk.to_csv(f"{output_location}\\test_output_cleaned_chunk_{i}.csv", index=False, header=False)
    
