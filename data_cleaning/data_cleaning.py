import csv

csv.field_size_limit(10**9)

def clean_csv(input_file, output_location, chunk_size=1000):
    # Referred: https://stackoverflow.com/questions/19699367/for-line-in-results-in-unicodedecodeerror-utf-8-codec-cant-decode-byte
    encoding_type = 'ISO-8859-1'

    # Read the CSV file into a list of rows
    def clean_field(field):
        return field.replace('\n', '')
    
    with open(input_file, 'r', newline='', encoding=encoding_type) as infile:
        reader = csv.reader(infile)

        chunk_count = 0
        cleaned_rows = []

        for row in reader:
            cleaned_row = []
            for ind, field in enumerate(row):
                if ind == 2 or ind == 3:
                    cleaned_row.append(clean_field(field))
                else:
                    cleaned_row.append(field)
            cleaned_rows.append(cleaned_row)
            
            # When reach the threshold, then save in split csv
            if len(cleaned_rows) == chunk_size:
                chunk_count += 1
                output_to_csv_by_chunk(chunk_count, output_location, cleaned_rows, encoding_type)
                cleaned_rows = []

        # If cleaned_rows still have remainings, then just save
        if cleaned_rows:
            chunk_count += 1
            output_to_csv_by_chunk(chunk_count, output_location, cleaned_rows, encoding_type)

def output_to_csv_by_chunk(chunk_count, output_location, cleaned_rows, encoding_type):
    chunk_output_file = f"{output_location}\\output_chunk_{chunk_count}.csv"
    with open(chunk_output_file, 'w', newline='', encoding=encoding_type) as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)


