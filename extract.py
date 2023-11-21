import tabula

def extract_table_from_pdf(pdf_path, output_csv_path):
    # Read the PDF file and extract tables
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    # Save each table as a separate CSV file
    for i, table in enumerate(tables):
        csv_path = f"{output_csv_path}_table_{i + 1}.csv"
        table.to_csv(csv_path, index=False)
        print(f"Table {i + 1} extracted and saved to {csv_path}")

if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your PDF file
    pdf_path = 'input.pdf'
    
    # Replace 'output_table' with the desired output CSV file prefix
    output_csv_path = './'
    
    extract_table_from_pdf(pdf_path, output_csv_path)
