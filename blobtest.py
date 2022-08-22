import mysql.connector
import glob
import json
from collections import defaultdict
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import generate_container_sas
from azure.storage.blob import ContainerSasPermissions
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient
import re
import datetime
from datetime import timedelta


def run_sqlfiles_from_s3(bucketName, Inpath, env, dbSchema):
    host_args = {
        "host": "23.100.70.45",
        "user": "core_user",
        "password": "k4w(F<T=4}*[B<7_]csM-H{2k_{>4>d%",
        "database": dbSchema,
        "ssl_ca": "E:\\diwo_code\\ca-cert.pem"
        # "ssl_cert": "C:\\Users\\Prasad\\OneDrive - Diwo Inc\\pmr_databricks_personal\\trial-fullcerts.pem",
        # "ssl_key": "C:\\Users\\Prasad\\OneDrive - Diwo Inc\\pmr_databricks_personal\\convertedkey.pem"

    }

    con = mysql.connector.connect(**host_args)
    print(con)

    cur = con.cursor(dictionary=True)

    sql = "show status like 'Ssl_cipher'"
    cur.execute(sql)

    print(cur.fetchone())
    #     print(cur)

    # if env == "aws":
    #     #         print("entered aws")
    #     session = boto3.Session(
    #         aws_access_key_id=s3_access_key,
    #         aws_secret_access_key=s3_secret_key)
    #     #         print("sessssssssssssssssssss")
    #     # Then use the session to get the resource
    #     s3 = session.resource('s3')
    #     #         print(s3)
    #
    #     my_bucket = s3.Bucket(bucketName)
    #     #         print(type(my_bucket))
    #     # s3://diwo-ma-poc/schema/pmr/pmr_schema_objects/table_ddls.sql
    #     for objects in my_bucket.objects.filter(Prefix=Inpath):
    #         if '.sql' in objects.key:
    #             #                 print(objects.key)
    #             # print(objects.get()['Body'].read())
    #             content = objects.get()['Body'].read()
    #             sqltxt = content.decode("utf-8")
    #             print(sqltxt)
    #             compiled = re.compile(re.escape("delimiter ;"), re.IGNORECASE)
    #             compiled1 = re.compile(re.escape("delimiter //"), re.IGNORECASE)
    #             compiled2 = re.compile(re.escape("end //"), re.IGNORECASE)
    #             res = compiled.sub("", sqltxt)
    #             res1 = compiled1.sub("", res)
    #             sqltxtFinal = compiled2.sub("end", res1)
    #             #                 sqltxtFinal = sqltxt.lower().replace("delimiter //","").replace("delimiter ;","").replace("end //","end")
    #             if (len(sqltxtFinal) > 1):
    #                 result_iterator = cur.execute(sqltxtFinal, multi=True)
    #             # print(type(result_iterator))
    #             for res in result_iterator:
    #                 print("Running query: ", res)  # Will print out a short representation of the query
    #                 print(f"Affected {res.rowcount} rows")
    #
    #             con.commit()
    #     con.close()
    #
    # else:
    #     blob_storage_account = "diwomastg"
    #     blob_storage_container = "diwomaprod"
    #     blob_storage_key = "TCw+lUVpTvHkPlQvy0df9kMB1Vsez3UEteqAefQUlvi2hZgWpq1e6hJ4T/7Vf8y0CoYLTz1e7lZK+AStBI5fag=="
    #
    #     permission = ContainerSasPermissions(read=True, write=True, delete=True,
    #                                          list=True, delete_previous_version=True, tag=True)
    #     sas_token = generate_container_sas(
    #         account_name=blob_storage_account,
    #         container_name=blob_storage_container,
    #         account_key=blob_storage_key,
    #         permission=permission,
    #         expiry=datetime.datetime.utcnow() + timedelta(hours=1)
    #     )
    #     print(sas_token)
    #
    #     url = "https://" + blob_storage_account + ".blob.core.windows.net/" + blob_storage_container
    #     container_client = ContainerClient.from_container_url(
    #         container_url=url,
    #         credential=sas_token
    #     )
    #
    #     print(url)
    #     # print(container_client)
    #
    #     blob_list = container_client.list_blobs(name_starts_with=Inpath)
    #     blob_list = blob_list
    #
    #     for blob in blob_list:
    #         if '.sql' in blob.name:
    #             print(blob.name + '\n')
    #             urlFinal = url + "/" + blob.name
    #             print(urlFinal)
    #             blobClient = BlobClient.from_blob_url(blob_url=urlFinal, credential=sas_token)
    #             with open("./file.txt", "wb") as my_blob:
    #                 blob_data = blobClient.download_blob()
    #                 blob_data.readinto(my_blob)
    #             import codecs
    #             file1 = codecs.open("./file.txt", "r", "utf-8")
    #             sqltext = file1.read()
    #             # sqltext = sqltext.encode("utf-8")
    #             compiled = re.compile(re.escape("delimiter ;"), re.IGNORECASE)
    #             compiled1 = re.compile(re.escape("delimiter //"), re.IGNORECASE)
    #             compiled2 = re.compile(re.escape("end //"), re.IGNORECASE)
    #             res = compiled.sub("", sqltext)
    #             res1 = compiled1.sub("", res)
    #             sqltxtFinal = compiled2.sub("end", res1)
    #             # print(sqltext)
    #             #             sqltxtFinal = sqltext.lower().replace("delimiter //", "").replace("delimiter ;", "").replace("end //", "end")
    #             if (len(sqltxtFinal) > 1):
    #                 result_iterator = cur.execute(sqltxtFinal, multi=True)
    #             # print(type(result_iterator))
    #             for res in result_iterator:
    #                 print("Running query: ", res)  # Will print out a short representation of the query
    #                 print(f"Affected {res.rowcount} rows")
    #
    #             con.commit()
    #             file1.close()
    #     con.close()


run_sqlfiles_from_s3('diwo-ma-poc','diwo/ma/pmr/schema/database_objects/','azure','ma_pmr_db')