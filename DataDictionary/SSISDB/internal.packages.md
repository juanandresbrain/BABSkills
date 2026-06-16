# internal.packages

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| package_id | bigint | 8 | 0 | YES |  |  |
| project_version_lsn | bigint | 8 | 0 |  | YES |  |
| name | nvarchar | 520 | 0 |  |  |  |
| package_guid | uniqueidentifier | 16 | 0 |  |  |  |
| description | nvarchar | 2048 | 1 |  |  |  |
| package_format_version | int | 4 | 0 |  |  |  |
| version_major | int | 4 | 0 |  |  |  |
| version_minor | int | 4 | 0 |  |  |  |
| version_build | int | 4 | 0 |  |  |  |
| version_comments | nvarchar | 2048 | 1 |  |  |  |
| version_guid | uniqueidentifier | 16 | 0 |  |  |  |
| project_id | bigint | 8 | 0 |  | YES |  |
| entry_point | bit | 1 | 0 |  |  |  |
| validation_status | char | 1 | 0 |  |  |  |
| last_validation_time | datetimeoffset | 10 | 1 |  |  |  |
| package_data | varbinary | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: internal.clean_update_packages](../../StoredProcedures/SSISDB/internal.clean_update_packages.md)
- [SSISDB: internal.prepare_packages_deploy](../../StoredProcedures/SSISDB/internal.prepare_packages_deploy.md)

