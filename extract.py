import tabula

def extract_table_from_pdf(pdf_path, output_csv_path):
    # Read the PDF file and extract tables
    tables = tabula.read_pdf(pdf_path, pages='all' )

    # Define the header for the CSV files
    #header = ["Day", "Date", "Start Time", "End Time", "Duration", "Subject", "Empty", "Location", "Instructor"]

    #extract header from the second row in table
    header = tables[0].iloc[0]
    header = header.dropna()
    header = header.tolist()
    
    #replace for each element in header the \r with " " with map
    header = list(map(lambda x: x.replace("\r", " "), header))
    #append to the array from array start "weekday"
    header.insert(0, "Giorno Settimana")

    #remove the first row
    tables[0] = tables[0].iloc[1:]
    tables[0] = tables[0].reset_index(drop=True)

    
    print(f"Header: {header}")

    # Save each table as a separate CSV file with the header
    for i, table in enumerate(tables):
        if not table.empty:
          
            csv_path = f"{output_csv_path}_table_{i + 1}.csv"

            # Add header to the table
            table.columns = header + [f"Column_{j}" for j in range(len(table.columns) - len(header))]

            # Save the table to CSV
            table.to_csv(csv_path, index=False, header=True)
            print(f"Table {i + 1} extracted and saved to {csv_path}")
        else:
            print(f"Table {i + 1} is empty, skipping.")

if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your PDF file
    pdf_path = 'input.pdf'
    
    # Replace 'output_table' with the desired output CSV file prefix
    output_csv_path = './'
    
    extract_table_from_pdf(pdf_path, output_csv_path)
