# Python Web Scraping

This project consists of a Python script designed to extract product information, including ID, price, and images, from a store website. The information is based on the HTML structure of the webpage and is exported to an Excel file, storing the images in a specific folder.

## Description

The script has been successfully tested on the website [Autopartes Legazpi](https://autoparteslegazpi.com.mx/products?id=172&per_page=63#search).

## Features

- Extraction of product data (ID, price, image).
- Export of information to an Excel file.
- Storage of images in a specific folder.

## Requirements

- Python 3.x
- Libraries: `requests`, `beautifulsoup4`, `openpyxl`

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/danielmederos2424/python_web_scrap.git
    cd python_web_scrap
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python scrap.py
    ```

2. The data will be exported to an Excel file and the images will be saved in the specified folder.

## Contributions

Contributions are welcome. Please send a pull request for any improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or inquiries, you can contact me through [my GitHub profile](https://github.com/danielmederos2424).
