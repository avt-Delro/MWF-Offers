import environment as env
from dotenv import load_dotenv
import win32com.client as win32
import os
from datetime import datetime
import calendar
import pandas as pd
from openpyxl import load_workbook
import logging
from logging.handlers import RotatingFileHandler
import os
import traceback

import pythoncom

date_today = datetime.now()

month = date_today.strftime('%B')

#Sends file, send_to:: String, cc_s:: String
def to_send_email(file, flyer_filename, send_to: str, cc_s: str, loc_code: str, cust_name:str):
    pythoncom.CoInitialize()
    outlook =win32.Dispatch("Outlook.Application")

    outlook_ap = outlook.GetNamespace("MAPI")
    mail = outlook.CreateItem(0)

    mail.Attachments.Add(os.path.abspath(file))
    mail.Attachments.Add(os.path.abspath(flyer_filename))
    mail.To = send_to
    mail.CC = cc_s
    

    mail.Subject = f'"{month} SPECIAL" WTD Domestic Floor Stock Available for Full Trailer Loads'


    #Instead of checking if NA just check if it is not a string
    try:
        if not isinstance(cust_name, str):
            cust_name = ''
        else:
            cust_name = cust_name
    except:
        logging.error(f"Cust Name is not valid")
        logging.exception(traceback.format_exc())


    if loc_code == 'V':
        warehouse_str = "California warehouse."
        mail.HTMLBody = f'''
        <html>
        <body>
            Hello {cust_name}
            <br><br>
            Please find attached updated inventory available from our California warehouse.<br>
            This is ALL IN PRICING from our California warehouse.<br><br>
            Let us know what items you could use so we can allocate and prepare a 53\' trailer load for you.<br><br>

            <span style="font-size:12px;color:red;">*Note inventory is on a first come first serve basis.</span>
            <br>
            Thank you, <br><br>WTD
        </body>
        </html>
        '''
    
    elif loc_code == 'VLK':
        warehouse_str = "California, Pennsylvania, Kentucky, Carrolton and Fort Worth warehouses."
        mail.HTMLBody = f'''
        <html>
        <body>
            Hello {cust_name}
            <br><br>
            Please find attached updated inventory available from our California, Pennsylvania, Kentucky, Carrolton and Fort Worth warehouse.
            This is ALL IN PRICING from our California, Pennsylvania, Kentucky, Carrolton and Fort Worth warehouse.<br><br>
            Let us know what items you could use so we can allocate and prepare a 53\' trailer load for you.<br><br>

            <span style="font-size:12px;color:red;">*Note inventory is on a first come first serve basis.</span>
            <br>
            <span style="font-size:14px;color:red;">*FULL LOAD MUST BE FROM ONE LOCATION. CANNOT BE COMBINED. ORDER FROM California, Pennsylvania, Kentucky, Carrolton and Fort Worth MIXED WILL NOT BE PROCESSED.</span>
            <br><br>
            Thank you, <br><br>WTD
        </body>
        </html>
        '''

    elif loc_code == 'PS':
        mail.HTMLBody = f"""
            <html>
                <body>
                    Hello
                        <br><br>
                    Please find attached updated inventory available from our {location_str}.
                        This is ALL IN PRICING from our California, Pennsylvania, Kentucky, Carrolton and Fort Worth warehouses.<br><br>
                    Let us know what items you could use so we can allocate and prepare a 53\' trailer load and 40HQ LTL for you.<br><br>

                    <span style="font-size:12px;color:red;">*Note inventory is on a first come first serve basis.</span>
                    <br>
                    <span style="font-size:14px;color:red;">*FULL LOAD AND LTL MUST BE FROM ONE LOCATION. CANNOT BE COMBINED. ORDER FROM California, Pennsylvania, Kentucky and Texas MIXED WILL NOT BE PROCESSED.</span>
                    <br>
                    <span style="font-size:14px;color:red;">*Orders to be submitted to Point-S via purchasing@pointstire.com. Please copy your WTD Account Manager to ensure the fastest processing of your order. </span>
                    <br>
                    <span style="font-size:14px;color:red;">*Note: All purchases are processed through and invoiced by Point-S Tire Inc. to the Point-S Member. All pertinent patronage benefits and/or volume bonuses will be accrued to your Point-S account. </span>

                    <br><br>
                </body>
            </html>
        """
    
    else:
        #For location list
        location_list = list(loc_code.upper())
        location_list_str = []

        for loc in location_list:
            if loc == 'V':
                location_list_str.append("California")
            elif loc == 'L':
                location_list_str.append("Pennsylvania")
            elif loc == 'K':
                location_list_str.append("Kentucky")
            elif loc == 'F':
                location_list_str.append("Fort Worth")
            elif loc == 'C':
                location_list_str.append("Carrolton") 
            elif loc == 'A':
                location_list_str.append("Apopka")
            elif loc == 'W':
                location_list_str.append("Winchester")
            elif loc == 'M':
                location_list_str.append("Miami")
            elif loc == 'B':
                location_list_str.append("Bloomsburg") 
            
        location_str = ', '.join(location_list_str)

        mail.HTMLBody = f"""
    <html>
        <body>
            Hello {cust_name}
            <br><br>
            Please find attached updated inventory available from our {location_str} warehouse.
            This is ALL IN PRICING from our {location_str} warehouse.<br><br>
            Let us know what items you could use so we can allocate and prepare a 53\' trailer load for you.<br><br>

            <span style="font-size:12px;color:red;">*Note inventory is on a first come first serve basis.</span>
            <br>
            <span style="font-size:14px;color:red;">*FULL LOAD MUST BE FROM ONE LOCATION. CANNOT BE COMBINED. ORDER FROM {location_str} MIXED WILL NOT BE PROCESSED.</span>
            <br><br>
            Thank you, <br><br>WTD
        </body>
        </html>
        """
    
    mail.Send()


    logging.info(f'File {file}, sent to Customer:{send_to} with CCs:{cc_s}')



    
