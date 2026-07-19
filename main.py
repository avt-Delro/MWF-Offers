import traceback

import environment as env
from dotenv import load_dotenv
import os
import odoo_get
import pandas as pd
import numpy as np
import logging
import odoo_get
import send_email
from itertools import islice

#################################################
#Start of main code
#################################################

api_key = env.odoo_api
username = env.odoo_username
product_file = env.product_file
flyer = env.flyer_file

#Configuration code
config = pd.read_csv(r'config/config - new concept.csv', encoding='cp1252')

config.columns = config.columns.str.strip().str.upper()

config_lookup = (
            config
            .set_index("CUSTOMER NAME")
            .to_dict(orient="index")
        )


'''
The main functions that the system runs
get_odoo_data: fetch odoo data from production using xmlrpc calls
add_data: generate a file that uses bunch of function calls inside odoo_get.py
'''
def main():
    odoo_get.get_odoo_data(product_file)
    
    for customer, cust_conf in config_lookup.items():
        try:
            logging.info(f'Processing Customer: {customer}')
            file_to_send = odoo_get.add_data(product_file, cust_conf, cust_conf.get('PRICELIST'), cust_conf.get('HIDE_PRICING'), cust_conf.get('CAPPED'))
            #send_email.to_send_email(file_to_send, flyer, cust_conf.get('SEND_TO'), cust_conf.get('CC_S'), cust_conf.get('LOC_CODE'), cust_conf.get('NAME'))
            
        except Exception as e:
            logging.error(f"Error occurred while processing customer: {customer}")
            logging.exception(e)
            logging.exception(traceback.format_exc())
            continue
        
        
def try_test():
    odoo_get.get_odoo_data(product_file)
    for customer, cust_conf in islice(config_lookup.items(), 2):
        logging.info(f'Processing Customer: {customer}')
        file_to_send = odoo_get.add_data(cust_conf, customer)
        send_email.to_send_email(file_to_send, flyer, cust_conf.get('SEND_TO'), cust_conf.get('CC_S'), cust_conf.get('LOC_CODE'), cust_conf.get('NAME'))

def selective_trigger(vendors_to_be_processed):
    odoo_get.get_odoo_data(product_file)

    for customer, cust_conf in config_lookup.items():
        try:
            if customer not in vendors_to_be_processed:
                continue

            logging.info(f'Processing Customer: {customer}')
            file_to_send = odoo_get.add_data(product_file, cust_conf, cust_conf.get('PRICELIST'), cust_conf.get('HIDE_PRICING'), cust_conf.get('CAPPED'))
            send_email.to_send_email(file_to_send, flyer, cust_conf.get('SEND_TO'), cust_conf.get('CC_S'), cust_conf.get('LOC_CODE'), cust_conf.get('NAME'))
            
        except Exception as e:
            logging.error(f"Error occurred while processing customer: {customer}")
            logging.exception(e)
            logging.exception(traceback.format_exc())
            continue
        


if __name__ == "__main__":
    main()