# dbo.IHpublishers

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_id | smallint | 2 | 0 |  |  |  |
| vendor | sysname | 256 | 0 |  |  |  |
| publisher_guid | uniqueidentifier | 16 | 0 |  |  |  |
| flush_request_time | datetime | 8 | 1 |  |  |  |
| version | sysname | 256 | 1 |  |  |  |
