import datetime
from datetime import timedelta
import os, glob
from azure.storage.blob import BlobClient
from azure.storage.blob import ContainerSasPermissions
from azure.storage.blob import generate_container_sas


def upload_file_to_directory(schemaName,localschemaName):
    try:
        blob_storage_account = ""
        blob_storage_container = ""
        blob_storage_key = ""

        permission = ContainerSasPermissions(read=True, write=True, delete=True,
                                             list=True, delete_previous_version=True, tag=True)
        sas_token = generate_container_sas(
            account_name=blob_storage_account,
            container_name=blob_storage_container,
            account_key=blob_storage_key,
            permission=permission,
            expiry=datetime.datetime.utcnow() + timedelta(hours=1)
        )
        print(sas_token)

        parent_folder = "/diwo/ma/pmr/"
        dirPath = parent_folder + "schema/database_objects/"+schemaName+"/"

        path = 'C:\\Users\\Prasad\\OneDrive - Diwo Inc\\mapmr\\schemas\\'+localschemaName
        for filename in glob.glob(os.path.join(path, '*.sql')):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                # open in readonly mode

                filename = os.path.basename(filename)

                # local_file = open("E:\\de_diwo\\populate_experiment_cal_tbl.sql", 'r')
                file_contents = f.read()
                print(filename)
                # C:\Users\Prasad\OneDrive - Diwo Inc\mapmr\schemas\evidence
                url = "https://" + blob_storage_account + ".blob.core.windows.net/" + blob_storage_container
                sas_url = url + dirPath + filename + "?" + sas_token
                blob_client = BlobClient.from_blob_url(sas_url)
                blob_client.upload_blob(file_contents, overwrite=True, blob_type="AppendBlob")
    except Exception as e:
        print(e)


# schemalist = ["diwo_das", "evidence", "kdm_db", "kmm_db", "ma_pmr_db", "smm", "uam_db", "udf", "umm_db","views"]
schemalist = ["diwo_das", "kmm_db", "ma_pmr_db", "udf"]
# schemalist = ["smm"]

for shema in schemalist:
    az_schema = shema
    l_schema = shema

    if shema == "udf":
        az_schema = "ddudf"
        l_schema = shema

    upload_file_to_directory(az_schema, l_schema)
