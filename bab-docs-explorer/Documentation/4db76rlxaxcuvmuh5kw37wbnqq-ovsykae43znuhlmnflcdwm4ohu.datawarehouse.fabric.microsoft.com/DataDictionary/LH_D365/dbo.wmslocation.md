# dbo.wmslocation

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| locationtype | bigint | 8 | 1 |  |  |  |
| manualname | bigint | 8 | 1 |  |  |  |
| manualsortcode | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| absoluteheight | decimal | 17 | 1 |  |  |  |
| aisleid | varchar | 8000 | 1 |  |  |  |
| checktext | varchar | 8000 | 1 |  |  |  |
| depth | decimal | 17 | 1 |  |  |  |
| height | decimal | 17 | 1 |  |  |  |
| inputblockingcauseid | varchar | 8000 | 1 |  |  |  |
| inputlocation | varchar | 8000 | 1 |  |  |  |
| inventlocationid | varchar | 8000 | 1 |  |  |  |
| lastcountedutcdatetime | datetime2 | 8 | 1 |  |  |  |
| level | bigint | 8 | 1 |  |  |  |
| locprofileid | varchar | 8000 | 1 |  |  |  |
| maxpalletcount | bigint | 8 | 1 |  |  |  |
| maxvolume | decimal | 17 | 1 |  |  |  |
| maxweight | decimal | 17 | 1 |  |  |  |
| mcrreservationpriority | bigint | 8 | 1 |  |  |  |
| outputblockingcauseid | varchar | 8000 | 1 |  |  |  |
| pallettypegroupid | varchar | 8000 | 1 |  |  |  |
| pickingareaid | varchar | 8000 | 1 |  |  |  |
| position | bigint | 8 | 1 |  |  |  |
| rack | bigint | 8 | 1 |  |  |  |
| sortcode | bigint | 8 | 1 |  |  |  |
| storeareaid | varchar | 8000 | 1 |  |  |  |
| volume | decimal | 17 | 1 |  |  |  |
| width | decimal | 17 | 1 |  |  |  |
| wmslocationid | varchar | 8000 | 1 |  |  |  |
| zoneid | varchar | 8000 | 1 |  |  |  |
| additionalzone1 | varchar | 8000 | 1 |  |  |  |
| additionalzone2 | varchar | 8000 | 1 |  |  |  |
| additionalzone3 | varchar | 8000 | 1 |  |  |  |
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
| xcoordinate | decimal | 17 | 1 |  |  |  |
| ycoordinate | decimal | 17 | 1 |  |  |  |
| zcoordinate | decimal | 17 | 1 |  |  |  |
