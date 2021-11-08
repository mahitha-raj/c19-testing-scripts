#!/usr/bin/python
"""For running process 3"""
# change dates/times (if needed)
# change code for necessary process
# change names! FN, LN, recordID

import csv
import random
import string
import sys
import datetime
from datetime import timedelta


def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime('%Y-%m-%d')


def random_datetime(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    rand_dt = start + timedelta(seconds=random_second)
    dt_without_seconds = rand_dt.replace(second=0, microsecond=0)
    return dt_without_seconds.strftime('%Y-%m-%d %H:%M:%S')


def random_datetime_collection(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    rand_dt = start + timedelta(seconds=random_second)
    dt_without_seconds = rand_dt.replace(second=0, microsecond=0)
    return dt_without_seconds.strftime('%Y-%m-%d %H:%M')


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


records=10
print("Making %d records\n" % records)

fieldnames=['record_id', 'client', 'institutional_id', 'first_name', 'last_name', 'sex', 
            'dob', 'race', 'ethnicity', 'email', 'confirm_email', 'primary_phone', 'address',
            'zipcode', 'has_traveled', 'travel_location', 'travel_date', 'has_close_contact', 
            'has_any_symptoms', 'has_any_further_symptoms', 'has_symptoms_throat', 
            'has_preexisting_conditions', 'has_conditions_detail', 
            'consent_signature', 'consent_date', 'requisition_complete', 'ordering_physician',
            'ordering_physician_npi', 'cpt_code', 'icd_10_code', 'language', 'verbal_consent',
            'participant_extra_info_complete', 'specimen_type', 'collection_datetime',
            'specimen_id', 'specimen_tube_barcode', 'specimen_collection_complete', 
            'research_specimen_id', 'research_participant_id', 'anonymous_ids_complete', 
            'result', 'result_summary', 
            'comments','version', 'result_complete', 'pdf_path', 'report_date', 
            'pdf_generation_comments', 'pdf_generation_finished',
            'pdf_generation_complete', 'ror_medium', 'date_time_results_emailed', 'ror_complete']

clients=['bcm', 'hcph', 'other', 'bcmdom']
emails=['mahiraj@tamu.edu']
travel_locations=['Japan', 'China', 'Korea', 'Italy', 'UK', 'Brazil', 'Peru']
results=['Positive', 'Not detected', 'Invalid', 'Inconclusive']

start_dt_collection= datetime.datetime.strptime('2020/04/15 1:00 PM', '%Y/%m/%d %I:%M %p')
end_dt_collection = datetime.datetime.strptime('2020/04/19 10:30 AM', '%Y/%m/%d %I:%M %p')

start_date_dob = datetime.datetime.strptime('1920/01/01','%Y/%m/%d').date()
end_date_dob = datetime.datetime.strptime('2020/01/01','%Y/%m/%d').date()

start_dt_email= datetime.datetime.strptime('2020/04/23 1:00 PM', '%Y/%m/%d %I:%M %p')
end_dt_email = datetime.datetime.strptime('2020/04/24 1:00 PM', '%Y/%m/%d %I:%M %p')

start_date_report = datetime.datetime.strptime('2020/04/19','%Y/%m/%d').date()
end_date_report = datetime.datetime.strptime('2020/04/23','%Y/%m/%d').date()

right_now = datetime.datetime.now()

writer = csv.DictWriter(open(sys.argv[1], "w"), fieldnames=fieldnames)
writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
    mail = random.choice(emails)
    run_ver = sys.argv[2] # change per upload
    spid = 'SPID{}{}'.format(i+1, run_ver)
    fin_result = random.choice(results)
    if fin_result == 'Positive':
        summary = 'This means your test sample is reactive for COVID-19 and needs to be confirmed by FDA certified test.'
    elif fin_result == 'Not detected':
        summary = 'This means that our test could not detect the virus that causes COVID-19.'
    elif fin_result == 'Invalid':
        summary = 'We were unable to make a determination based on the sample provided.'
    else:
        summary = 'We were unable to make a determination based on the sample provided.'
    writer.writerow(dict([
        ('record_id', 'stressload{}{}'.format(run_ver, i+1)),
        ('client', random.choice(clients)),
        ('first_name', '{}FN{}'.format(run_ver, i+1)),
        ('last_name', '{}LN{}'.format(run_ver, i+1)),
        ('sex', str(random.randint(1,3))),
        ('dob', random_date(start_date_dob, end_date_dob)),
        ('race', str(random.randint(1,18))),
        ('ethnicity', str(random.randint(1,12))),
        ('email', mail ),
        ('confirm_email', mail),
        ('primary_phone', '5555555555'),
        ('zipcode', '77030'),
        ('has_traveled', str(random.randint(1,3))),
        ('travel_location', random.choice(travel_locations)),
        ('has_close_contact', str(random.randint(1,3))),
        ('has_any_symptoms', str(random.randint(1,3))),
        ('has_any_further_symptoms', str(random.randint(1,3))),
        ('has_symptoms_throat', str(random.randint(1,3))),
        ('has_preexisting_conditions', str(random.randint(1,3))),
        ('has_conditions_detail', 'Has conditions'),
        ('consent_signature', '[document]'),
        ('consent_date', '2020-04-20'),
        ('requisition_complete', '2'),
        ('participant_extra_info_complete', str(random.randint(0,2))),
        ('specimen_type', '1'),
        ('collection_datetime', random_datetime_collection(start_dt_collection, end_dt_collection)),
        ('specimen_id', spid),
        ('specimen_tube_barcode', 'TBC{}{}'.format(run_ver, i+1)),
        ('specimen_collection_complete', '2'),
        ('research_specimen_id', id_generator()),
        ('research_participant_id', id_generator()),
        ('anonymous_ids_complete', '2'),
        ('result', fin_result),
        ('result_summary', summary),
        ('comments', 'Approve Comment'),
        ('version', '1'),
        ('result_complete', '2'),
        ('pdf_path', ''),
        ('report_date', random_date(start_date_report, end_date_report)),
        ('pdf_generation_comments', 'A comment here and a comment there'),
        ('pdf_generation_finished', right_now.strftime("%Y/%m/%d %H:%M:%S")),
        ('pdf_generation_complete', '0'),
        ('ror_medium', '0'),
        ('ror_complete', '0')
    ]))
    
#Change date times to necessary format
