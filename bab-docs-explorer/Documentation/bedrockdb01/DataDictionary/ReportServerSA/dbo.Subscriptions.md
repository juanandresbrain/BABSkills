# dbo.Subscriptions

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SubscriptionID | uniqueidentifier | 16 | 0 |  |  |  |
| OwnerID | uniqueidentifier | 16 | 0 |  |  |  |
| Report_OID | uniqueidentifier | 16 | 0 |  |  |  |
| Locale | nvarchar | 256 | 0 |  |  |  |
| InactiveFlags | int | 4 | 0 |  |  |  |
| ExtensionSettings | ntext | 16 | 1 |  |  |  |
| ModifiedByID | uniqueidentifier | 16 | 0 |  |  |  |
| ModifiedDate | datetime | 8 | 0 |  |  |  |
| Description | nvarchar | 1024 | 1 |  |  |  |
| LastStatus | nvarchar | 520 | 1 |  |  |  |
| EventType | nvarchar | 520 | 0 |  |  |  |
| MatchData | ntext | 16 | 1 |  |  |  |
| LastRunTime | datetime | 8 | 1 |  |  |  |
| Parameters | ntext | 16 | 1 |  |  |  |
| DataSettings | ntext | 16 | 1 |  |  |  |
| DeliveryExtension | nvarchar | 520 | 1 |  |  |  |
| Version | int | 4 | 0 |  |  |  |
| ReportZone | int | 4 | 0 |  |  |  |
