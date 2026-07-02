# dbo.tmpSSISParamsBak

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_id | bigint | 8 | 0 |  |  |  |
| ProjectName | sysname | 256 | 0 |  |  |  |
| PackageName | nvarchar | 520 | 0 |  |  |  |
| last_deployed_time | datetimeoffset | 10 | 0 |  |  |  |
| parameter_name | sysname | 256 | 0 |  |  |  |
| ParameterValue | sql_variant | 8016 | 1 |  |  |  |
| design_default_value_NEW | sql_variant | 8016 | 1 |  |  |  |

