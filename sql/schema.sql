CREATE TABLE IF NOT EXISTS dim_patients (
    patient_hash VARCHAR(64) PRIMARY KEY,
    gender VARCHAR(10),
    birth_date DATE,
    state VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS fact_encounters (
    encounter_id VARCHAR(50) PRIMARY KEY,
    patient_hash VARCHAR(64) REFERENCES dim_patients(patient_hash),
    encounter_class VARCHAR(50),
    start_date TIMESTAMP,
    stop_date TIMESTAMP,
    reason_code VARCHAR(50),
    reason_description TEXT
);