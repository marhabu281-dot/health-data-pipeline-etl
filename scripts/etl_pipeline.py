import pandas as pd
from sqlalchemy import create_engine
from anonymizer import hash_identifier

def run_pipeline():
    print("Extracting raw clinical data...")
    patients_df = pd.read_csv('../data/raw/patients.csv')
    encounters_df = pd.read_csv('../data/raw/encounters.csv')

    print("Applying data cleaning and PHI masking...")
    patients_df['patient_hash'] = patients_df['Id'].apply(hash_identifier)
    encounters_df['patient_hash'] = encounters_df['PATIENT'].apply(hash_identifier)

    clean_patients = patients_df[['patient_hash', 'GENDER', 'BIRTHDATE', 'STATE']].rename(
        columns={'GENDER': 'gender', 'BIRTHDATE': 'birth_date', 'STATE': 'state'}
    )

    clean_encounters = encounters_df[['Id', 'patient_hash', 'ENCOUNTERCLASS', 'START', 'STOP', 'REASONCODE', 'REASONDESCRIPTION']].rename(
        columns={
            'Id': 'encounter_id',
            'ENCOUNTERCLASS': 'encounter_class',
            'START': 'start_date',
            'STOP': 'stop_date',
            'REASONCODE': 'reason_code',
            'REASONDESCRIPTION': 'reason_description'
        }
    )

    print("Loading structured metrics into PostgreSQL...")
    engine = create_engine('postgresql://postgres:password@localhost:5432/healthcare_db')

    clean_patients.to_sql('dim_patients', engine, if_exists='append', index=False)
    clean_encounters.to_sql('fact_encounters', engine, if_exists='append', index=False)

    print("ETL Pipeline executed successfully.")

if __name__ == '__main__':
    run_pipeline()