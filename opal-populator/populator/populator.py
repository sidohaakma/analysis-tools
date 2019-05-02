#!python

import click
import Opal

@click.command()
@click.option(
    '--host',
    '-h', 
    default='localhost:8080',
    help='Opal host; only yhe dns name, without protocol and port number.')
@click.option(
    '--administrator-password',
    '-p', 
    prompt=True,
    help='Administrator password of Opal host')
@click.option(
    '--cohort',
    '-c', 
    prompt=True,
    help='Cohort name; lowercase for example "gecko".')
@click.option(
    '--version',
    '-v', 
    default='1_0',
    help='Version of data dictionary; can be x_x, for example 1_0.')
@click.option(
    '--status',
    '-s', 
    default='beta',
    help='Status of data dictionary; can be beta or released.')        
def populate(host, administrator_password, cohort, version, status): 
    """
    This script will bootstrap the data dictionary version of the LifeCycle variables into Opal.
    """
    print("")
    print("############################################")
    print("")
    opal -o host -u 'administrator' -p administrator_password --content-type 'application/json' -m POST /projects 
    # echo "{\"name\":\"lifecycle_${COHORT}\",\"title\":\"lifecycle_${COHORT}\", \"database\": \"opal_data\"}" | 

    # echo "Create table ${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_monthly_repeated_measures" 2>&1
    # sed s/@table_name@/${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_monthly_repeated_measurements/g /opt/opal/data/table_template.json | \
    #   opal rest -o http://${OPAL_HOST}:8080 -u administrator -p ${OPAL_ADMINISTRATOR_PASSWORD} -m POST -ct 'application/json' /datasource/lifecycle_${COHORT}/tables
    # echo "Create table ${DATA_DICTIONARY_VERSION}_yearly_repeated_measures" 2>&1
    # sed s/@table_name@/${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_yearly_repeated_measurements/g /opt/opal/data/table_template.json | \
    #   opal rest -o http://${OPAL_HOST}:8080 -u administrator -p ${OPAL_ADMINISTRATOR_PASSWORD} -m POST -ct 'application/json' /datasource/lifecycle_${COHORT}/tables
    # echo "Create table ${DATA_DICTIONARY_VERSION}_non_repeated_measures" 2>&1
    # sed s/@table_name@/${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_non_repeated_measurements/g /opt/opal/data/table_template.json | \
    #   opal rest -o http://${OPAL_HOST}:8080 -u administrator -p ${OPAL_ADMINISTRATOR_PASSWORD} -m POST -ct 'application/json' /datasource/lifecycle_${COHORT}/tables

    # echo "Upload variables for ${DATA_DICTIONARY_VERSION}_monthly_repeated_measures" 2>&1
    # opal file -o http://${OPAL_HOST}:8080 -u administrator -p ${OPAL_ADMINISTRATOR_PASSWORD} -up /opt/opal/data/dictionary/${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_monthly_repeated_measurements.csv /home/administrator/
    # echo "Upload variables for ${DATA_DICTIONARY_VERSION}_yearly_repeated_measures" 2>&1
    # opal file -o http://${OPAL_HOST}:8080 -u administrator -p ${OPAL_ADMINISTRATOR_PASSWORD} -up /opt/opal/data/dictionary/${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_yearly_repeated_measurements.csv /home/administrator/
    # echo "Upload variables for ${DATA_DICTIONARY_VERSION}_non_repeated_measures" 2>&1
    # opal file -o http://${OPAL_HOST}:8080 -u administrator -p ${OPAL_ADMINISTRATOR_PASSWORD} -up /opt/opal/data/dictionary/${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_non_repeated_measurements.csv /home/administrator/

    # echo "Import variables for ${DATA_DICTIONARY_VERSION}_monthly_repeated_measures" 2>&1
    # opal import-csv -o http://${OPAL_HOST}:8080 -u administrator -p ${OPAL_ADMINISTRATOR_PASSWORD} --path /home/administrator/${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_monthly_repeated_measurements.csv --destination lifecycle_${COHORT} --tables ${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_monthly_repeated_measurements --separator , --type Participant
    # echo "Import variables for ${DATA_DICTIONARY_VERSION}_monthly_repeated_measures" 2>&1
    # opal import-csv -o http://${OPAL_HOST}:8080 -u administrator -p ${OPAL_ADMINISTRATOR_PASSWORD} --path /home/administrator/${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_yearly_repeated_measurements.csv --destination lifecycle_${COHORT} --tables ${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_yearly_repeated_measurements --separator , --type Participant
    # echo "Import variables for ${DATA_DICTIONARY_VERSION}_monthly_repeated_measures" 2>&1
    # opal import-csv -o http://${OPAL_HOST}:8080 -u administrator -p ${OPAL_ADMINISTRATOR_PASSWORD} --path /home/administrator/${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_non_repeated_measurements.csv --destination lifecycle_${COHORT} --tables ${DATA_DICTIONARY_VERSION}_${DATA_DICTIONARY_STATE}_non_repeated_measurem --separator , --type Participant
    