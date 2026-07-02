# dbo.sysutility_ucp_databases_stub

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| urn | nvarchar | 1024 | 1 |  |  |  |
| powershell_path | nvarchar | -1 | 1 |  |  |  |
| processing_time | datetimeoffset | 10 | 1 |  |  |  |
| batch_time | datetimeoffset | 10 | 1 |  |  |  |
| server_instance_name | sysname | 256 | 0 |  |  |  |
| parent_urn | nvarchar | 640 | 1 |  |  |  |
| Collation | nvarchar | 256 | 1 |  |  |  |
| CompatibilityLevel | smallint | 2 | 1 |  |  |  |
| CreateDate | datetime | 8 | 1 |  |  |  |
| EncryptionEnabled | bit | 1 | 1 |  |  |  |
| Name | nvarchar | 256 | 1 |  |  |  |
| RecoveryModel | smallint | 2 | 1 |  |  |  |
| Trustworthy | bit | 1 | 1 |  |  |  |
| state | tinyint | 1 | 1 |  |  |  |

