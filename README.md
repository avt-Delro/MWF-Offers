# MWF-Offers

## Overview
Creates and generate Monday, Wednesday, Friday offers for customers. Gets pricelists and inventory, from our odoo instances. This script connects to an Odoo ERP system, retrieves product and inventory data, processes it, and generates formatted Excel reports. Using Streamlit as UI. 

## Features
- Odoo XML-RPC integration
- Product and inventory data processing
- Excel report generation and formatting
- Logging with rotating files

## Requirements
Install dependencies:

pip install pandas numpy openpyxl python-dotenv

## Configuration
Update environment.py with:
- odoo_api : API Key to connect to WTD Odoo
- odoo_username 
- product_file
- strapping_file

### Data Retrieval
- get_odoo_data(file)
  - Connects to Odoo and retrieves raw data for processing.
  - Run once per scheduled time.

- get_on_hand_quant(file, default_code, loc_key, sheet_name)
  - Extracts on-hand inventory quantities for specified products and locations.

- df_to_qty_map(df, product_col, qty_col)
  - Converts a DataFrame into a dictionary mapping product codes to quantities.

### Data Processing
- identify_prod_to_add(file, config, customer)
  - Reads product data from Excel and determines which products should be added based on configuration rules.
  - Connected function: is_product_allowed().

- is_product_allowed(config, df)
  - Filters products according to business rules (branding, type, etc.).
  - Configuration corresponds to the flags in the config.csv.

### Excel Utilities
- create_sheet(filepath, data_row, sheetname)
  - Creates a new Excel sheet from a list or dictionary of data.
  - If sheet exists, overwrite that sheet.

- copy_template(source, target)
  - Copies formatting and layout from a template Excel file.
  - Templates are: 

- hide_columns(file, column_names)
  - Hides specific columns in the Excel file.

- apply_currency_format(file, columns_names)
  - Applies currency formatting to specified Excel columns.

- delete_first_sheet(file, sheetname)
  - Removes a sheet from the Excel workbook.

### Formatting & Styling
- fill_rows(ws, row, fill, fill_type, location, ps_type)
  - Applies row styling including fills and borders.

- add_data(config, customer, hide_pricing, capped)
  - Main function to populate Excel sheets with processed data and apply formatting.

## Usage
Run the script:
streamlist run streamlit.py

## Output
- Processed Excel files
- Logs stored in logs/ directory

## Author
VJDRIV
