# dbo.Keys

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| MachineName | nvarchar | 512 | 1 |  |  |  |
| InstallationID | uniqueidentifier | 16 | 0 |  |  |  |
| InstanceName | nvarchar | 64 | 1 |  |  |  |
| Client | int | 4 | 0 |  |  |  |
| PublicKey | image | 16 | 1 |  |  |  |
| SymmetricKey | image | 16 | 1 |  |  |  |
