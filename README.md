# Python Web Scraping

Este proyecto consiste en un script en Python diseñado para extraer información de productos, incluyendo ID, precio y imágenes, desde un sitio web de tienda. La información se basa en la estructura HTML de la página web y se exporta a un archivo Excel, almacenando las imágenes en una carpeta específica.

## Descripción

El script ha sido probado con éxito en el sitio web [Autopartes Legazpi](https://autoparteslegazpi.com.mx/products?id=172&per_page=63#search).

## Características

- Extracción de datos de productos (ID, precio, imagen).
- Exportación de la información a un archivo Excel.
- Almacenamiento de imágenes en una carpeta específica.

## Requisitos

- Python 3.x
- Librerías: `requests`, `beautifulsoup4`, `openpyxl`

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/danielmederos2424/python_web_scrap.git
    cd python_web_scrap
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script:
    ```bash
    python scrap.py
    ```

2. Los datos se exportarán a un archivo Excel y las imágenes se guardarán en la carpeta especificada.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, envía un pull request para cualquier mejora.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para cualquier duda o consulta, puedes contactarme a través de [mi perfil de GitHub](https://github.com/danielmederos2424).
