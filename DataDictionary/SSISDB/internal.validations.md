# internal.validations

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| validation_id | bigint | 8 | 0 | YES | YES |  |
| environment_scope | char | 1 | 0 |  |  |  |
| validate_type | char | 1 | 0 |  |  |  |
| folder_name | sysname | 256 | 0 |  |  |  |
| project_name | sysname | 256 | 0 |  |  |  |
| project_lsn | bigint | 8 | 1 |  |  |  |
| use32bitruntime | bit | 1 | 1 |  |  |  |
| reference_id | bigint | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: internal.prepare_validate_package](../../StoredProcedures/SSISDB/internal.prepare_validate_package.md)
- [SSISDB: internal.prepare_validate_project](../../StoredProcedures/SSISDB/internal.prepare_validate_project.md)

