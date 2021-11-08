#!/usr/bin/python
"""For running Process 1"""
# change dates/times (if needed)
# change code for necessary process
# change names! FN, LN, recordID

import csv
import random
import string
import datetime
import sys
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


records=int(sys.argv[1])
print("Making %d records\n" % records)

fieldnames=['record_id', 'client', 'patient_id', 'first_name', 'last_name', 'sex', 
            'dob', 'race', 'ethnicity', 'email', 'confirm_email', 'primary_phone', 'address', 'city', 'state', 
            'county', 'zipcode', 'has_traveled', 'travel_location', 'has_close_contact', 
            'has_any_symptoms', 'has_any_further_symptoms', 'has_symptoms_throat', 
            'has_preexisting_conditions', 'has_conditions_detail', 'ordering_provider_name', 'ordering_provider_phone', 'ordering_provider_address',
            'ordering_provider_npi', 'language', 'verbal_consent',
            'specimen_type', 'collection_datetime','specimen_id', 'specimen_tube_barcode']

clients=['bcmcl', 'coh', 'acadian']
emails=['mahiraj@tamu.edu', '']
travel_locations=['Japan', 'China', 'Korea', 'Italy', 'UK', 'Brazil', 'Peru', '']
primary_phones=['7137988322', '5555555555', '9999999999', '7137981000', '7137984103', '(713) 942-0110']

start_dt_collection= datetime.datetime.strptime('2020/06/15 1:00 PM', '%Y/%m/%d %I:%M %p')
end_dt_collection = datetime.datetime.strptime('2020/06/19 10:30 AM', '%Y/%m/%d %I:%M %p')

start_date_dob = datetime.datetime.strptime('1920/01/01','%Y/%m/%d').date()
end_date_dob = datetime.datetime.strptime('2020/01/01','%Y/%m/%d').date()

start_dt_email= datetime.datetime.strptime('2020/06/23 1:00 PM', '%Y/%m/%d %I:%M %p')
end_dt_email = datetime.datetime.strptime('2020/06/24 1:00 PM', '%Y/%m/%d %I:%M %p')

start_date_report = datetime.datetime.strptime('2020/06/19','%Y/%m/%d').date()
end_date_report = datetime.datetime.strptime('2020/06/23','%Y/%m/%d').date()

right_now = datetime.datetime.now()

writer = csv.DictWriter(open(sys.argv[2], "w"), fieldnames=fieldnames)
writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
    mail = random.choice(emails)
    run_ver = sys.argv[3] # 4 digits change per upload
    spid = 'SPID{}{}'.format(run_ver, random.randrange(10000, 99999))
    writer.writerow(dict([
        ('record_id', 'test_p1{}{}'.format(run_ver, i+1)),
        ('client', random.choice(clients)),
        ('patient_id', 'PI{}{}'.format(run_ver, i+1)),
        ('first_name', '{}FN{}'.format(run_ver, i+1)),
        ('last_name', '{}LN{}'.format(run_ver, i+1)),
        ('sex', str(random.randint(1,3))),
        ('dob', random_date(start_date_dob, end_date_dob)),
        ('race', str(random.randint(1,18))),
        ('ethnicity', str(random.randint(1,12))),
        ('email', mail),
        ('confirm_email', mail),
        ('primary_phone', random.choice(primary_phones)),
        ('address', '1235 Demo Lane'),
        ('city', 'Houston'),
        ('state', 'TX'),
        ('county','Harris'),
        ('zipcode', '77030'),
        ('has_traveled', str(random.randint(1,3))),
        ('travel_location', random.choice(travel_locations)),
        ('has_close_contact', str(random.randint(1,3))),
        ('has_any_symptoms', str(random.randint(1,3))),
        ('has_any_further_symptoms', str(random.randint(1,3))),
        ('has_symptoms_throat', str(random.randint(1,3))),
        ('has_preexisting_conditions', str(random.randint(1,3))),
    ]))
    