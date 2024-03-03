# IPython Notebook Converter

This Streamlit app allows users to convert IPython Notebook (.ipynb) files into HTML or PDF format.

## How to Use

1. **Upload an IPython Notebook file**: Click on the "Upload an IPython Notebook (.ipynb) file" button and select the desired `.ipynb` file.

2. **Convert to HTML**: Once the file is uploaded, click the "Convert to HTML" button to convert the IPython Notebook to HTML format. A download button labeled "Download HTML" will appear. Clicking on it will download the generated HTML file.

3. **Convert to PDF**: Similarly, you can convert the IPython Notebook to PDF format by clicking the "Convert to PDF" button. A download button labeled "Download PDF" will appear. Clicking on it will download the generated PDF file.

## How to Run

To run the app locally:

1. Install the required dependencies:

    - From `packages.txt`:
        ```
        sudo apt-get install texlive texlive-xetex texlive-latex-extra pandoc
        ```

    - From `requirements.txt`:
        ```
        pip install -r requirements.txt
        ```

2. Clone the repository:
    ```
    git clone https://github.com/astro215/ipynb-to-pdf-html.git
    ```

3. Navigate to the directory containing the app file (`app.py`).

4. Run the Streamlit app:
    ```
    streamlit run app.py
    ```

## Requirements

### `packages.txt`
- texlive
- texlive-xetex
- texlive-latex-extra
- pandoc

### `requirements.txt`
- jupyter
- streamlit
- nbconvert

## Deployed App

The deployed app can be accessed [ipynb-to-pdf-html](https://ipynb-to-pdf-html.streamlit.app/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
