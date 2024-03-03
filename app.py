import streamlit as st
from nbconvert import HTMLExporter, PDFExporter
from nbformat import read

st.title("IPython Notebook Converter")

# Function to convert IPython Notebook to HTML
def convert_to_html(notebook):
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook)
    return body

# Function to convert IPython Notebook to PDF
def convert_to_pdf(notebook):
    pdf_exporter = PDFExporter()
    (body, resources) = pdf_exporter.from_notebook_node(notebook)
    return body

# Main function
def main():
    uploaded_file = st.file_uploader("Upload an IPython Notebook (.ipynb) file", type='.ipynb')

    if uploaded_file is not None:
        notebook = read(uploaded_file, as_version=4)

        if st.button("Convert to HTML"):
            html_content = convert_to_html(notebook)
            # st.markdown(html_content, unsafe_allow_html=True)
            st.markdown(get_download_link(html_content, 'html', 'Download HTML'), unsafe_allow_html=True)

        if st.button("Convert to PDF"):
            pdf_content = convert_to_pdf(notebook)
            # st.markdown(pdf_content, unsafe_allow_html=True)
            st.markdown(get_download_link(pdf_content, 'pdf', 'Download PDF'), unsafe_allow_html=True)

# Function to create download link
def get_download_link(content, file_format, text):
    href = f'<a href="data:file/{file_format};base64,{content}" download="output.{file_format}">{text}</a>'
    return href

if __name__ == "__main__":
    main()
