import os
import pandas as pd
import uuid
import random
from datetime import datetime, timedelta

# Ensure data/raw directory exists
os.makedirs('data/raw', exist_ok=True)

# Generate 50 sample patient records
patients_data = []
genders = ['M', 'F']
states = ['MA', 'NY', 'CA', 'TX', 'FL']

patient_ids = [str(uuid.uuid4()) for _ in range(50)]

for p_id in patient_ids:
    birth_year = random.randint(1950, 2010)
    birth_date = datetime(birth_year, random.randint(1, 12), random.randint(1, 28)).strftime('%Y-%m-%d')
    patients_data.append({
        'Id': p_id,
        'BIRTHDATE': birth_date,
        'GENDER': random.choice(genders),
        'STATE': random.choice(states)
    })

pd.DataFrame(patients_data).to_csv('data/raw/patients.csv', index=False)

# Generate sample encounter records mapped to patients
reasons = [
    ('10509002', 'Acute bronchitis (disorder)'),
    ('444814009', 'Viral upper respiratory tract infection'),
    ('162673000', 'General examination of patient'),
    ('73211009', 'Diabetes mellitus (disorder)')
]
classes = ['ambulatory', 'wellness', 'emergency', 'outpatient']

encounters_data = []
for _ in range(150):
    p_id = random.choice(patient_ids)
    reason_code, reason_desc = random.choice(reasons)
    start = datetime(2025, random.randint(1, 12), random.randint(1, 28), random.randint(8, 17))
    stop = start + timedelta(hours=random.randint(1, 3))
    
    encounters_data.append({
        'Id': str(uuid.uuid4()),
        'PATIENT': p_id,
        'ENCOUNTERCLASS': random.choice(classes),
        'START': start.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'STOP': stop.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'REASONCODE': reason_code,
        'REASONDESCRIPTION': reason_desc
    })

pd.DataFrame(encounters_data).to_csv('data/raw/encounters.csv', index=False)
print("Synthetic patient and encounter datasets generated inside data/raw/")