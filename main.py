from fpdf import FPDF

def convert_file(file):
    pdf = FPDF()
    pdf.add_page()

    for text in file:
        if len(text) <= 20:
            pdf.set_font("Arial","B",size=18) # For title text
            pdf.cell(w=200,h=10,txt=text,ln=1,align="C")
        else:
            pdf.set_font("Arial",size=15) # For paragraph text
            pdf.multi_cell(w=0,h=10,txt=text,align="L")
    pdf.output("output.pdf")
    print("Successfully converted!")
file = open("sample.txt","r")

convert_file(file)













