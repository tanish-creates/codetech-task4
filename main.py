# Install the required library
!pip install fpdf pandas

# Import the libraries
from fpdf import FPDF
import pandas as pd

# Define the PDF class for the report
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Automated Report", align="C", ln=True)
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, content)
        self.ln(10)

# Analyze the data
def analyze_data(file_path):
    # Load the data (assuming it's a CSV file)
    data = pd.read_csv(file_path)
    summary = data.describe()  # Get a statistical summary of the data
    return summary

# Generate the PDF report
def generate_report(data_summary, output_path):
    pdf = PDFReport()
    pdf.add_page()
    
    # Add sections to the report
    pdf.add_section("Report Summary", "This report contains the analysis of the provided dataset.")
    pdf.add_section("Data Analysis", data_summary.to_string())
    
    # Save the PDF
    pdf.output(output_path)

# Upload and process the file in Colab
from google.colab import files

# Ask the user to upload a file
print("Please upload a CSV file:")
uploaded = files.upload()

# Process the uploaded file
for file_name in uploaded.keys():
    summary = analyze_data(file_name)  # Analyze the uploaded data
    output_pdf = "report.pdf"
    generate_report(summary, output_pdf)  # Generate the report
    print(f"Report generated successfully: {output_pdf}")

# Download the generated PDF
files.download(output_pdf)
