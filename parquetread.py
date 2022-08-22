import time as T
import datetime
from datetime import timedelta

start_date = datetime.date(2021,10,24)
end_date = datetime.date(2022,1,22)
issuer_id = 1521

def date_range(start, end):
    start = start +timedelta(days=7)
    while start<=end:
        yield start
        start = start + timedelta(days=7)



date_list = [i for i in date_range(start_date,end_date)]
input_path = ",".join(["dbfs:/mnt/diwo-ma-prod/diwo/ma/pmr/data/prepared/fact_data/parquet_files/cs_pmr_fact_clearing_tbl.parquet"+f"/issuer_id={issuer_id}"+"/clear_trxn_dt=%s" % (d) for d in  date_list])

print(input_path)



# for dt in date_list:
#     print(dt)
# input_path = ",".join(["PARTITION_YEAR=2017/PARTITION_MONTH=%02d/PARTITION_DAY=%02d" % (d.month, d.day) for d in  date_list])