import os
from dotenv import load_dotenv

load_dotenv()

odoo_api = os.getenv('ODOO_API_KEY')
odoo_username = os.getenv('ODOO_USERNAME')
odoo_api_jetstar = os.getenv('ODOO_API_KEY_Jetstar')
odoo_username_jetstar = os.getenv('ODOO_USERNAME_Jetstar')
product_file = os.getenv('product_file')
config_file = os.getenv('config_file')
config_streamlit = os.getenv('config_streamlit')
cc_email = os.getenv('cc_email')
flyer_file = os.getenv('flyers')
strapping_file = os.getenv('strapping_file')

