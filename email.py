from pyspark.sql import SparkSession
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def NotifyInEmail(df, sql, tbl):
    df.createOrReplaceTempView(tbl)
    monthly_rpt = spark.sql(sql).collect()
    print(monthly_rpt)
    fromAddr = "ddunga@diwo.ai"
    recipients = "ddunga@diwo.ai"
    cc = "ddunga@diwo.ai"
    subject = "PMR Data Valition Report RAW vs FACT"

    # Create body of the email message
    body = "<html><head><style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style></head>"
    footer = " <br/><br/> **This is an auto generated mail <br/><br/>"
    strTable = "<table><tr><th>report_month</th><th>table_name</th><th>total_records</th><th>unique_trxn_records</th><th>unique_cardholder_records</th></tr>"
    strTable = body + strTable

    #         report_month, issuer_id, table_name, total_records, unique_trxn_records, unique_cardholder_records

    # Create dynamic HTML table with data
    for row in monthly_rpt:
        report_month = str(row["report_month"])
        issuer_id = str(row["issuer_id"])
        table_name = str(row["table_name"])
        total_records = str(row["total_records"])
        unique_trxn_records = str(row["unique_trxn_records"])
        unique_cardholder_records = str(row["unique_cardholder_records"])
        strRW = "<tr><td>" + report_month + "</td><td>" + issuer_id + "</td><td>" + table_name + "</td><td>" + total_records + "</td><td>" + unique_trxn_records + "</td><td>" + unique_cardholder_records + "</td>" + "</tr>"
        strTable = strTable + strRW

    strTable = strTable + "</table></html>"
    # print HTML table
    print(strTable)

    # Create the root message and fill in the from,to,cc and subject
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = fromAddr
    msgRoot['To'] = recipients
    msgRoot['Cc'] = cc

    # Set type of MIMEText as HTML
    msgText = MIMEText(strTable, 'html')

    # Attach body of the message as HTML table
    msgRoot.attach(msgText)

    # Create SMTP object to send email
    server = SMTP('smtp.office365.com', 587)
    #         smtp.connect('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.login("ddunga@getdiwo.ai", "Skoda@99")
    # Connect specific mail server with the input of server address and its port

    # Send email
    smtp.sendmail(fromAddr, recipients.split(','), msgRoot.as_string())
    smtp.quit()

    print("Report Sent successfully")
# custom function to access Hive Table
# def FetchHiveTable():
#         fetch_sql = "select * from hospital_db.patient_report"
#         df = spark.sql(fetch_sql)
#         df.show()
#         #Call next custom function NotifyInEmail() to prepare HTML table and send email
#         NotifyInEmail(df)
# Main program starts here