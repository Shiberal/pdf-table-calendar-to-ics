import csv

def prune_rows_without_hours(input_csv, output_csv='pruned.csv'):
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)


        for row in reader:
            # Check if the row contains numeric values in columns representing hours
            if any(field.replace(',', '').replace('.', '').isdigit() for field in row[2:]):
                # Write the row to the output CSV
                writer.writerow(row)


    print(f"Pruned CSV saved to {output_csv}")

if __name__ == "__main__":
    # Replace 'input.csv' with the path to your CSV file
    input_csv = './_table_1.csv'
    
    # Call the function with only the input CSV file, output_csv will default to 'pruned.csv'
    prune_rows_without_hours(input_csv)
