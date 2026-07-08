# dbo.TempCatalog

**Database:** ReportServerSATempDB  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EditSessionID | varchar | 32 | 0 |  |  |  |
| TempCatalogID | uniqueidentifier | 16 | 0 |  |  |  |
| ContextPath | nvarchar | 850 | 0 |  |  |  |
| Name | nvarchar | 850 | 0 |  |  |  |
| Content | varbinary | -1 | 1 |  |  |  |
| Description | nvarchar | -1 | 1 |  |  |  |
| Intermediate | uniqueidentifier | 16 | 1 |  |  |  |
| IntermediateIsPermanent | bit | 1 | 0 |  |  |  |
| Property | nvarchar | -1 | 1 |  |  |  |
| Parameter | nvarchar | -1 | 1 |  |  |  |
| OwnerID | uniqueidentifier | 16 | 0 |  |  |  |
| CreationTime | datetime | 8 | 0 |  |  |  |
| ExpirationTime | datetime | 8 | 0 |  |  |  |
| DataCacheHash | varbinary | 64 | 1 |  |  |  |
