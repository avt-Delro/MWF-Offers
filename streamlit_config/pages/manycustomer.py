import streamlit as st
import pandas as pd
import odoo_get
import send_email
import environment as env
from dotenv import load_dotenv
import uuid
import shutil
import os
from pathlib import Path
import time

config = pd.read_csv("config/config - new concept.csv")
flyer = env.flyer_file

product_file = env.product_file

# For temporary files - copying excel from the main configuration
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

temp_dir = Path('temp')
os.makedirs("temp", exist_ok=True)

# Get the created session file
session_product_file = (temp_dir/f"product_{st.session_state.session_id}.xlsx")

# Creates a copy if file is not found
if not os.path.exists(session_product_file):
    shutil.copy2(product_file, session_product_file)



customers = sorted(config["Customer Name"].dropna().unique())

st.title("MWF Offers")

selected_customers = st.multiselect("Customers to Send To",
                                    customers,
                                    default=[customers[0]])

if len(selected_customers) > 0:
    hide_pricing = st.checkbox(
        "Hide Pricing",
        value=False
    )

    capped = st.checkbox(
        "Capped",
        value=False
    )
    if st.button('Generate Emails'):
        for customer in selected_customers:
            status = st.status("Generating email...", expanded=True)

            customer_info = config[config["Customer Name"] == customer].iloc[0]
            cust_conf = customer_info.to_dict()
            cust_conf["HIDE_PRICING"] = "Y" if hide_pricing else "N"
            cust_conf["CAPPED"] = "Y" if capped else "N"
            
            file_to_send = odoo_get.add_data(session_product_file,
                                             cust_conf,
                                             customer,
                                             cust_conf["HIDE_PRICING"],
                                             cust_conf["CAPPED"])
            
            status.write("Sending Email")

            send_email.to_send_email(
                file_to_send,
                flyer,
                cust_conf["SEND_TO"],
                cust_conf["CC_S"],
                cust_conf["LOC_CODE"],
                cust_conf["NAME"]
            )
            status.update(
                label=f"Email generated and sent successfully to {customer}!",
                state="complete")
            
            st.toast('Email was sent', duration = 'long')
            



    
