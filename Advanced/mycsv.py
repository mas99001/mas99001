import csv
from tomlkit import item
'''
data = open('data\\NewEstimates.csv', encoding="utf-8", mode='r')
reader = csv.reader(data)
data_list = list(reader)
for row in data_list:
    row = row[1:] + row[:1]
    print("\t\t\t\t".join(row))
'''
# CSV Writing
'''
file_path = open('data\\New.csv', mode='w', encoding="utf-8", newline='')
csv_writer = csv.writer(file_path, delimiter=',')
csv_writer.writerow(['Name', 'Age', 'City'])
csv_writer.writerow(['Alice', 30, 'New York'])
file_path.close()
'''
# PDF Writing
import os
from pypdf import PdfWriter
from pypdf import PdfReader

f = open('data\\RFE.06_FATHER-CHK-eStmt_2025-08.pdf', mode='rb')
pdf_reader = PdfReader(f)
print(len(pdf_reader.pages)) 
page = pdf_reader.pages[0]
page_text = page.extract_text()
print(page_text)
pdf_writer = PdfWriter()
pdf_writer.add_page(page)
pdf_output_path = os.path.join('data', 'output.pdf')
with open(pdf_output_path, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)
    output_pdf.close()
f.close()