from datetime import datetime
import os
from logging_config import logger
import traceback
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

date_today = datetime.now()
month = date_today.strftime('%B')

# SMTP Settings
smtp_server = "smtp.office365.com"
smtp_port = 587

email_user = "sales@wtdus.com"
email_password = "ckwvpzrncjvgqqmh"


def to_send_email(
    file,
    flyer_filename,
    send_to: str,
    cc_s: str,
    loc_code: str,
    cust_name: str
):

    msg = MIMEMultipart()

    msg["From"] = email_user
    msg["To"] = send_to
    msg["CC"] = cc_s
    msg["Subject"] = (
        f'{month} WTD Domestic Floor Stock Available '
        f'for Full Trailer Loads'
    )

    try:
        if not isinstance(cust_name, str):
            cust_name = ""
    except Exception:
        cust_name = ""
        logger.error("Cust Name is not valid")
        logger.exception(traceback.format_exc())

    # Build email body
    if loc_code == "V":

        html_body = f"""
        <html>
        <body>
            Hello {cust_name}
            <br><br>

            Please find attached updated inventory available from our California warehouse.<br>
            This is ALL IN PRICING from our California warehouse.<br><br>

            Let us know what items you could use so we can allocate and prepare a 53' trailer load for you.<br><br>

            <span style="font-size:12px;color:red;">
                *Note inventory is on a first come first serve basis.
            </span>

            <br>
            Thank you,
            <br><br>
            WTD
        </body>
        </html>
        """

    elif loc_code == "VLK":

        html_body = f"""
        <html>
        <body>
            Hello {cust_name}
            <br><br>

            Please find attached updated inventory available from our California, Pennsylvania, Kentucky, Carrolton and Fort Worth warehouses.<br>

            This is ALL IN PRICING from our California, Pennsylvania, Kentucky, Carrolton and Fort Worth warehouses.<br><br>

            Let us know what items you could use so we can allocate and prepare a 53' trailer load for you.<br><br>

            <span style="font-size:12px;color:red;">
                *Note inventory is on a first come first serve basis.
            </span>

            <br>

            <span style="font-size:14px;color:red;">
                *FULL LOAD MUST BE FROM ONE LOCATION. CANNOT BE COMBINED.
                ORDER FROM California, Pennsylvania, Kentucky, Carrolton
                and Fort Worth MIXED WILL NOT BE PROCESSED.
            </span>

            <br><br>

            Thank you,
            <br><br>
            WTD
        </body>
        </html>
        """

    elif loc_code == "PS":

        html_body = """
        <html>
            <body>
                Hello
                <br><br>

                Please find attached updated inventory available from our locations.

                This is ALL IN PRICING from our California, Pennsylvania,
                Kentucky, Carrolton and Fort Worth warehouses.<br><br>

                Let us know what items you could use so we can allocate and prepare
                a 53' trailer load and 40HQ LTL for you.<br><br>

                <span style="font-size:12px;color:red;">
                    *Note inventory is on a first come first serve basis.
                </span>

                <br>

                <span style="font-size:14px;color:red;">
                    *FULL LOAD AND LTL MUST BE FROM ONE LOCATION.
                    CANNOT BE COMBINED.
                </span>

                <br>

                <span style="font-size:14px;color:red;">
                    *Orders to be submitted to Point-S via
                    purchasing@pointstire.com.
                </span>

                <br>

                <span style="font-size:14px;color:red;">
                    *Note: All purchases are processed through and invoiced
                    by Point-S Tire Inc.
                </span>

                <br><br>
            </body>
        </html>
        """

    else:

        location_list = list(loc_code.upper())
        location_list_str = []

        for loc in location_list:

            if loc == "V":
                location_list_str.append("California")
            elif loc == "L":
                location_list_str.append("Pennsylvania")
            elif loc == "K":
                location_list_str.append("Kentucky")
            elif loc == "F":
                location_list_str.append("Fort Worth")
            elif loc == "C":
                location_list_str.append("Carrolton")
            elif loc == "A":
                location_list_str.append("Apopka")
            elif loc == "W":
                location_list_str.append("Winchester")
            elif loc == "M":
                location_list_str.append("Miami")
            elif loc == "B":
                location_list_str.append("Bloomsburg")

        location_str = ", ".join(location_list_str)

        html_body = f"""
        <html>
            <body>

                Hello {cust_name}

                <br><br>

                Please find attached updated inventory available from our {location_str} warehouse.

                This is ALL IN PRICING from our {location_str} warehouse.

                <br><br>

                Let us know what items you could use so we can allocate and prepare a 53' trailer load for you.

                <br><br>

                <span style="font-size:12px;color:red;">
                    *Note inventory is on a first come first serve basis.
                </span>

                <br>

                <span style="font-size:14px;color:red;">
                    *FULL LOAD MUST BE FROM ONE LOCATION.
                    CANNOT BE COMBINED.
                    ORDER FROM {location_str} MIXED WILL NOT BE PROCESSED.
                </span>

                <br><br>

                Thank you,

                <br><br>

                WTD

            </body>
        </html>
        """

    # Add HTML Body
    msg.attach(MIMEText(html_body, "html"))

    # Attach Inventory File
    with open(file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f'attachment; filename="{os.path.basename(file)}"'
    )

    msg.attach(part)

    # Attach Flyer File
    # with open(flyer_filename, "rb") as attachment:
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read())

    # encoders.encode_base64(part)

    # part.add_header(
    #     "Content-Disposition",
    #     f'attachment; filename="{os.path.basename(flyer_filename)}"'
    # )

    # msg.attach(part)

    # Send Email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_user, email_password)

            recipients = [send_to]

            if cc_s:
                recipients.append(cc_s)

            server.sendmail(
                email_user,
                recipients,
                msg.as_string()
            )

            logger.info(
                f"File {file} sent to Customer:{send_to} with CCs:{cc_s}"
            )

    except Exception as e:
        logger.error(f"Email send failed: {e}")
        logger.exception(traceback.format_exc())