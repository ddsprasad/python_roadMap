import datetime
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# print(getCohortDate(202202, 1 , 'Trigger' , 'start'))

def getCohortDate(reportMonth, cohortID , period , boundary):
    year = int(reportMonth[:4])
    month = int(reportMonth[len(str(reportMonth))-2:])

    reportDate = datetime.datetime(year, month, 1)
    exp_date = reportDate.date()

    exp_start_date = exp_date - relativedelta(months=6)

    # exp_sunday_start_date =
    datetime_object = datetime.datetime.strptime(str(exp_start_date), '%Y-%m-%d')
    dayofweek = datetime_object.weekday()
    if dayofweek !=6:
        exp_sunday_start_date = exp_start_date + timedelta(days=(6 - dayofweek))
    else:
        exp_sunday_start_date = exp_start_date

    exp_cohort_start_date = exp_sunday_start_date + timedelta(days=(7*(cohortID-1)))
    exp_trigger_start_date = exp_cohort_start_date
    exp_trigger_end_date = exp_trigger_start_date + timedelta(days=6)
    exp_baseline_start_date = exp_trigger_start_date + timedelta(weeks=-26)
    exp_baseline_end_date = exp_trigger_start_date + timedelta(days=-1)
    exp_analysis_start_date = exp_trigger_end_date + timedelta(days=1)
    exp_analysis_end_date = ((exp_analysis_start_date + timedelta(weeks=13)) + timedelta(days=-1))

    perBoundery = (period+boundary).upper()
    if perBoundery == "TRIGGERSTART":
        return_date = exp_trigger_start_date
    elif perBoundery =="TRIGGEREND":
        return_date = exp_trigger_end_date
    elif perBoundery =="BASELINESTART":
        return_date = exp_baseline_start_date
    elif perBoundery =="BASELINEEND":
        return_date = exp_baseline_end_date
    elif perBoundery =="ANALYSISSTART":
        return_date=exp_analysis_start_date
    else:
        return_date = exp_analysis_end_date

    return return_date

def current_report_process(cur_report_month):
    year = int(cur_report_month[:4])
    month = int(cur_report_month[len(str(cur_report_month))-2:])
    # print(month)
    reportDate = datetime.datetime(year, month, 1)
    exp_date = reportDate.date()
    # print(exp_date)

    pre_exp_date = exp_date - relativedelta(months=1)
    # print(pre_exp_date)
    pre_year = pre_exp_date.year
    pre_month = pre_exp_date.month

    if(len(str(pre_month))==1):
        pre_month = "0"+str(pre_month)

    pre_report_month = str(pre_year)+""+str(pre_month)
    print(f"previous report_month: {pre_report_month}")


    cur_mnth_base_dt = getCohortDate(cur_report_month, 1, 'BASELINE', 'START')
    # print(cur_mnth_base_dt)

    for chrt in range(1,13):
        prev_mnth_base_dt = getCohortDate(pre_report_month, chrt, 'BASELINE', 'START')
        # print(prev_mnth_base_dt, cur_mnth_base_dt)
        if cur_mnth_base_dt == prev_mnth_base_dt:
            processStart_Cohort = ( (12 - chrt + 2))
            # print(processStart_Cohort)
            processEnd_Cohort = 12

            processStart_Date = getCohortDate(cur_report_month, processStart_Cohort, 'BASELINE', 'START')
            processEnd_Date = getCohortDate(cur_report_month, processEnd_Cohort, 'ANALYSIS', 'END')

            return processStart_Date, processEnd_Date, processStart_Cohort, processEnd_Cohort


# startdt, enddate = current_report_cohorts_process('202202','202203')
#
# print(startdt)
# print(enddate)

def previous_report_copy(cur_report_month):
    year = int(cur_report_month[:4])
    month = int(cur_report_month[len(str(cur_report_month)) - 2:])
    # print(month)
    reportDate = datetime.datetime(year, month, 1)
    exp_date = reportDate.date()
    # print(exp_date)

    pre_exp_date = exp_date - relativedelta(months=1)
    # print(pre_exp_date)
    pre_year = pre_exp_date.year
    pre_month = pre_exp_date.month

    if (len(str(pre_month)) == 1):
        pre_month = "0" + str(pre_month)

    pre_report_month = str(pre_year) + "" + str(pre_month)
    print(f"previous report_month: {pre_report_month}")

    cur_mnth_base_dt = getCohortDate(cur_report_month, 1, 'BASELINE', 'START')
    # print(cur_mnth_base_dt)

    for chrt in range(1,13):
        prev_mnth_base_dt = getCohortDate(pre_report_month, chrt, 'BASELINE', 'START')
        # print(prev_mnth_base_dt, cur_mnth_base_dt)
        if cur_mnth_base_dt == prev_mnth_base_dt:
            copyStart_Cohort = chrt
            copyEnd_Cohort = 12

            copyStart_Date = getCohortDate(cur_report_month, copyStart_Cohort, 'BASELINE', 'START')
            copyEnd_Date = getCohortDate(cur_report_month, copyEnd_Cohort, 'ANALYSIS', 'END')

            return copyStart_Date, copyEnd_Date, copyStart_Cohort, copyEnd_Cohort

def previous_report_paste(cur_report_month):
    year = int(cur_report_month[:4])
    month = int(cur_report_month[len(str(cur_report_month)) - 2:])
    # print(month)
    reportDate = datetime.datetime(year, month, 1)
    exp_date = reportDate.date()
    # print(exp_date)

    pre_exp_date = exp_date - relativedelta(months=1)
    # print(pre_exp_date)
    pre_year = pre_exp_date.year
    pre_month = pre_exp_date.month

    if (len(str(pre_month)) == 1):
        pre_month = "0" + str(pre_month)

    pre_report_month = str(pre_year) + "" + str(pre_month)
    print(f"previous report_month: {pre_report_month}")

    cur_mnth_base_dt = getCohortDate(cur_report_month, 1, 'BASELINE', 'START')
    # print(cur_mnth_base_dt)

    for chrt in range(1,13):
        prev_mnth_base_dt = getCohortDate(pre_report_month, chrt, 'BASELINE', 'START')
        # print(prev_mnth_base_dt, cur_mnth_base_dt)
        if cur_mnth_base_dt == prev_mnth_base_dt:
            pasteStart_Cohort = 1
            pasteEnd_Cohort = (12-chrt+1)

            pasteStart_Date = getCohortDate(cur_report_month, pasteStart_Cohort, 'BASELINE', 'START')
            pasteEnd_Date = getCohortDate(cur_report_month, pasteEnd_Cohort, 'ANALYSIS', 'END')

            return pasteStart_Date, pasteEnd_Date, pasteStart_Cohort, pasteEnd_Cohort

process_start_dt, process_end_dt, process_cohort_start, process_cohort_end = current_report_process('202202')

print(process_start_dt)
print(process_end_dt)
print(process_cohort_start)
print(process_cohort_end)