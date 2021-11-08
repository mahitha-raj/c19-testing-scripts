/* Dynamic SQL query to pull Ordering Provider name. */
SELECT DISTINCT op_names.value
FROM redcap_data AS op_names
INNER JOIN redcap_data AS subc_codes
INNER JOIN redcap_data AS subc_names
INNER JOIN redcap_data as c_codes
INNER JOIN redcap_data AS current_record
ON  op_names.project_id = {{project_id}}
AND subc_codes.project_id = {{project_id}}
AND subc_names.project_id = {{project_id}}
AND c_codes.project_id = {{project_id}}
AND subc_names.record = op_names.record
AND subc_codes.record = subc_names.record
AND c_codes.record = subc_codes.record
AND op_names.field_name = 'ordering_provider_name'
AND subc_codes.field_name = 'sub_client_code'
AND subc_names.field_name = 'sub_client'
AND c_codes.field_name = 'client'
AND current_record.project_id = [project-id]
AND current_record.record = [record-name]
AND current_record.field_name = 'sub_client'
AND current_record.value = subc_codes.value

/* Dynamic SQL query to pull OP NPI information. */
SELECT DISTINCT op_npis.value
FROM redcap_data AS op_npis
INNER JOIN redcap_data AS op_names
INNER JOIN redcap_data AS subc_codes
INNER JOIN redcap_data AS subc_names
INNER JOIN redcap_data as c_codes
INNER JOIN redcap_data AS current_record
ON op_npis.project_id = {{project_id}}
AND op_names.project_id = {{project_id}}
AND subc_codes.project_id = {{project_id}}
AND subc_names.project_id = {{project_id}}
AND c_codes.project_id = {{project_id}}
AND op_npis.record = op_names.record
AND subc_names.record = op_names.record
AND subc_codes.record = subc_names.record
AND c_codes.record = subc_codes.record
AND op_npis.field_name = 'ordering_provider_npi'
AND op_names.field_name = 'ordering_provider_name'
AND subc_codes.field_name = 'sub_client_code'
AND subc_names.field_name = 'sub_client'
AND c_codes.field_name = 'client'
AND current_record.project_id = [project-id]
AND current_record.record = [record-name]
AND current_record.field_name = 'ordering_provider_name'
AND current_record.value = op_names.value

/* Dynamic SQL query to pull OP ICD-10 code. */
SELECT DISTINCT op_icds.value
FROM redcap_data AS op_icds
INNER JOIN redcap_data AS op_names
INNER JOIN redcap_data AS subc_codes
INNER JOIN redcap_data AS subc_names
INNER JOIN redcap_data as c_codes
INNER JOIN redcap_data AS current_record
ON op_icds.project_id = {{project_id}}
AND op_names.project_id = {{project_id}}
AND subc_codes.project_id = {{project_id}}
AND subc_names.project_id = {{project_id}}
AND c_codes.project_id = {{project_id}}
AND op_icds.record = op_names.record
AND subc_names.record = op_names.record
AND subc_codes.record = subc_names.record
AND c_codes.record = subc_codes.record
AND op_icds.field_name = 'icd_10_code'
AND op_names.field_name = 'ordering_provider_name'
AND subc_codes.field_name = 'sub_client_code'
AND subc_names.field_name = 'sub_client'
AND c_codes.field_name = 'client'
AND current_record.project_id = [project-id]
AND current_record.record = [record-name]
AND current_record.field_name = 'ordering_provider_name'
AND current_record.value = op_names.value