import streamlit as st
from nbconvert import HTMLExporter, PDFExporter
from nbformat import read
import os

st.title("IPython Notebook Converter")

# Function to convert IPython Notebook to HTML
def convert_to_html(notebook, filename):
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook)
    html_filename = f"{filename}.html"
    with open(html_filename, "w") as html_file:
        html_file.write(body)
    return html_filename

# Function to convert IPython Notebook to PDF
def convert_to_pdf(notebook, filename):
    pdf_exporter = PDFExporter()
    (body, resources) = pdf_exporter.from_notebook_node(notebook)
    pdf_filename = f"{filename}.pdf"
    with open(pdf_filename, "wb") as pdf_file:
        pdf_file.write(body)
    return pdf_filename

# Main function
def main():
    uploaded_file = st.file_uploader("Upload an IPython Notebook (.ipynb) file", type='.ipynb')

    if uploaded_file is not None:
        notebook = read(uploaded_file, as_version=4)
        filename = os.path.splitext(uploaded_file.name)[0]

        if st.button("Convert to HTML"):
            html_filename = convert_to_html(notebook, filename)
            st.download_button(label="Download HTML", data=open(html_filename, 'rb'), file_name=os.path.basename(html_filename), mime="text/html")

        if st.button("Convert to PDF"):
            pdf_filename = convert_to_pdf(notebook, filename)
            st.download_button(label="Download PDF", data=open(pdf_filename, 'rb'), file_name=os.path.basename(pdf_filename), mime="application/pdf")

if __name__ == "__main__":
    main()
