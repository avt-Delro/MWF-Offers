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


location_df = pd.DataFrame({
    'Location Code': ['V', 'L', 'K', 'F', 'C', 'A', 'W', 'M', 'B'],
    'Location Name':['California','Latrobe','Kentucky','Fort Worth','Carrolton', 'Apopka', 'Winchester', 'Miami', 'Bloomsburg']
})


customers = sorted(
    config["Customer Name"].dropna().unique()
)

st.title("MWF Offers")

selected_customer = st.selectbox(
    "Select Customer",
    customers
)

if selected_customer:

    customer_info = config[
        config["Customer Name"] == selected_customer
    ].iloc[0]

    st.subheader("Configuration")

    send_to = st.text_input(
        "Send To (seperate emails with ;)",
        value=str(customer_info["SEND_TO"])
    )

    cc_s = st.text_input(
        "CC (seperate emails with ;)",
        value=str(customer_info["CC_S"])
    )

    loc_code = st.text_input(
        "Location Code (Accepts a combination of V, L, K, F, C, A, W, M, B)",
        value=str(customer_info["LOC_CODE"]),
        
    )

    # Uses the dictionary for dataframe
    st.dataframe(location_df, 
                 hide_index=True,
                 use_container_width = True)

    hide_pricing = st.checkbox(
        "Hide Pricing",
        value=str(customer_info["HIDE_PRICING"]).upper() == "Y"
    )

    capped = st.checkbox(
        "Capped",
        value=str(customer_info["CAPPED"]).upper() == "Y"
    )

    if st.button("Generate Email"):
        status = st.status("Generating email...", expanded=True)

        odoo_get.get_odoo_data(session_product_file)
        
        status.write("Updating Inventory")

        cust_conf = customer_info.to_dict()

        # Override values from UI
        cust_conf["SEND_TO"] = send_to
        cust_conf["CC_S"] = cc_s
        cust_conf["LOC_CODE"] = loc_code
        cust_conf["HIDE_PRICING"] = "Y" if hide_pricing else "N"
        cust_conf["CAPPED"] = "Y" if capped else "N"

   
        file_to_send = odoo_get.add_data(
            session_product_file,
            cust_conf,
            selected_customer,
            cust_conf["HIDE_PRICING"],
            cust_conf["CAPPED"]
        )
        

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
            label=f"Excel generated and email sent successfully to {send_to}!",
            state="complete")
        
        st.toast('Email was sent', duration = 'long')