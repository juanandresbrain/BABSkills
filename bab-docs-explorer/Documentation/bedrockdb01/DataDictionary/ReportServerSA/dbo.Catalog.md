# dbo.Catalog

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ItemID | uniqueidentifier | 16 | 0 |  |  |  |
| Path | nvarchar | 850 | 0 |  |  |  |
| Name | nvarchar | 850 | 0 |  |  |  |
| ParentID | uniqueidentifier | 16 | 1 |  |  |  |
| Type | int | 4 | 0 |  |  |  |
| Content | image | 256 | 1 |  |  |  |
| Intermediate | uniqueidentifier | 16 | 1 |  |  |  |
| SnapshotDataID | uniqueidentifier | 16 | 1 |  |  |  |
| LinkSourceID | uniqueidentifier | 16 | 1 |  |  |  |
| Property | ntext | 256 | 1 |  |  |  |
| Description | nvarchar | 1024 | 1 |  |  |  |
| Hidden | bit | 1 | 1 |  |  |  |
| CreatedByID | uniqueidentifier | 16 | 0 |  |  |  |
| CreationDate | datetime | 8 | 0 |  |  |  |
| ModifiedByID | uniqueidentifier | 16 | 0 |  |  |  |
| ModifiedDate | datetime | 8 | 0 |  |  |  |
| MimeType | nvarchar | 520 | 1 |  |  |  |
| SnapshotLimit | int | 4 | 1 |  |  |  |
| Parameter | ntext | 256 | 1 |  |  |  |
| PolicyID | uniqueidentifier | 16 | 0 |  |  |  |
| PolicyRoot | bit | 1 | 0 |  |  |  |
| ExecutionFlag | int | 4 | 0 |  |  |  |
| ExecutionTime | datetime | 8 | 1 |  |  |  |
| SubType | nvarchar | 256 | 1 |  |  |  |
| ComponentID | uniqueidentifier | 16 | 1 |  |  |  |
