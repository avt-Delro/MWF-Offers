import streamlit as st
import pandas as pd
import odoo_get
import environment as env
from dotenv import load_dotenv
import uuid
import shutil
import os
from pathlib import Path
import time
import logging

temp_dir = Path('temp')

def cleanup_temp_files(max_age_hours=24):

    if not temp_dir.exists():
        os.makedirs("temp", exist_ok=True)
        

    now = time.time()

    for file in temp_dir.glob("product_*.xlsx"):
        try:
            age_hours = (now - file.stat().st_mtime) / 3600

            if age_hours > max_age_hours:
                file.unlink()
                logging.info(f"Deleted old temp file: {file}")

        except Exception as e:
            logging.warning(f"Could not delete {file}: {e}")
        
# Clean temporary file with age more than 24 hours
cleanup_temp_files()

one_customer_page = st.Page('streamlit_config/pages/onecustomer.py', title = 'Send to One Customer')
many_customer_page = st.Page('streamlit_config/pages/manycustomer.py', title = 'Send to Many Customer')

pg = st.navigation({'Send Email':[one_customer_page, many_customer_page]})
pg.run()












        