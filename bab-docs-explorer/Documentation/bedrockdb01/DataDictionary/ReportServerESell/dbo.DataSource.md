# dbo.DataSource

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DSID | uniqueidentifier | 16 | 0 |  |  |  |
| ItemID | uniqueidentifier | 16 | 1 |  |  |  |
| SubscriptionID | uniqueidentifier | 16 | 1 |  |  |  |
| Name | nvarchar | 520 | 1 |  |  |  |
| Extension | nvarchar | 520 | 1 |  |  |  |
| Link | uniqueidentifier | 16 | 1 |  |  |  |
| CredentialRetrieval | int | 4 | 1 |  |  |  |
| Prompt | ntext | 256 | 1 |  |  |  |
| ConnectionString | image | 256 | 1 |  |  |  |
| OriginalConnectionString | image | 256 | 1 |  |  |  |
| OriginalConnectStringExpressionBased | bit | 1 | 1 |  |  |  |
| UserName | image | 256 | 1 |  |  |  |
| Password | image | 256 | 1 |  |  |  |
| Flags | int | 4 | 1 |  |  |  |
| Version | int | 4 | 0 |  |  |  |
