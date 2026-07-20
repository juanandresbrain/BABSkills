# dbo.dimensionattributevalue

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| isblockedformanualentry | bigint | 8 | 1 |  |  |  |
| isdeleted | bigint | 8 | 1 |  |  |  |
| issuspended | bigint | 8 | 1 |  |  |  |
| istotal | bigint | 8 | 1 |  |  |  |
| pendingsuccessfuldeletevalidation | bigint | 8 | 1 |  |  |  |
| isbalancing_psn | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| activefrom | datetime2 | 8 | 1 |  |  |  |
| activeto | datetime2 | 8 | 1 |  |  |  |
| cacheddisplayvalue | varchar | 8000 | 1 |  |  |  |
| dimensionattribute | bigint | 8 | 1 |  |  |  |
| entityinstance | bigint | 8 | 1 |  |  |  |
| groupdimension | varchar | 8000 | 1 |  |  |  |
| hashkey | varchar | 8000 | 1 |  |  |  |
| cachedinvariantname | varchar | 8000 | 1 |  |  |  |
| cachedname | varchar | 8000 | 1 |  |  |  |
| displayvalue | varchar | 8000 | 1 |  |  |  |
| backingrecorddataareaid | varchar | 8000 | 1 |  |  |  |
| originalentityinstance | bigint | 8 | 1 |  |  |  |
| owner | bigint | 8 | 1 |  |  |  |
| modifieddatetime | datetime2 | 8 | 1 |  |  |  |
| modifiedby | varchar | 8000 | 1 |  |  |  |
| modifiedtransactionid | bigint | 8 | 1 |  |  |  |
| createddatetime | datetime2 | 8 | 1 |  |  |  |
| createdby | varchar | 8000 | 1 |  |  |  |
| createdtransactionid | bigint | 8 | 1 |  |  |  |
| dataareaid | varchar | 8000 | 1 |  |  |  |
| recversion | bigint | 8 | 1 |  |  |  |
| partition | bigint | 8 | 1 |  |  |  |
| sysrowversion | bigint | 8 | 1 |  |  |  |
| recid | bigint | 8 | 1 |  |  |  |
| tableid | bigint | 8 | 1 |  |  |  |
| versionnumber | bigint | 8 | 1 |  |  |  |
| createdon | datetime2 | 8 | 1 |  |  |  |
| modifiedon | datetime2 | 8 | 1 |  |  |  |
| IsDelete | bit | 1 | 1 |  |  |  |
| createdonpartition | varchar | 8000 | 1 |  |  |  |
| PartitionId | varchar | 2048 | 1 |  |  |  |
