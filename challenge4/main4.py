import pdfplumber
import json

def extract_information_and_tables(pdf_path: str) -> dict:
    """Extract both text and table data from each page of the PDF document."""
    extracted_data = {
        "text": [],  
        "tables": []  
    }
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            extracted_data["text"].append(page_text)
            
            
            tables = page.extract_tables()
            for table in tables:
                header_row = table[0]  
                for row in table[1:]:
                    table_dict = {header: cell for header, cell in zip(header_row, row)}
                    extracted_data["tables"].append(table_dict)
                
    return extracted_data

def save_extracted_data(data: dict, output_file: str):
    """Save the extracted data to a JSON file."""
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    pdf_path = 'challenge4\input.pdf' 
    output_file = 'output.json' 
    
    extracted_data = extract_information_and_tables(pdf_path)
    
    save_extracted_data(extracted_data, output_file)
    
    print(f"Extracted data has been saved to {output_file}")

if __name__ == "__main__":
    main()

print("hii")
