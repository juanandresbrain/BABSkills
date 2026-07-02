# dbo.Keys

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Client | int | 4 | 0 | YES |  |  |
| InstallationID | uniqueidentifier | 16 | 0 | YES |  |  |
| InstanceName | nvarchar | 64 | 1 |  |  |  |
| MachineName | nvarchar | 512 | 1 |  |  |  |
| PublicKey | image | 16 | 1 |  |  |  |
| SymmetricKey | image | 16 | 1 |  |  |  |