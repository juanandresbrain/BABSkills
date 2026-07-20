# dbo.mcrinventtable

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| allowpriceadjust | bigint | 8 | 1 |  |  |  |
| allowreturn | bigint | 8 | 1 |  |  |  |
| couponuse | bigint | 8 | 1 |  |  |  |
| dropshipment | bigint | 8 | 1 |  |  |  |
| ftcexempt | bigint | 8 | 1 |  |  |  |
| installmenteligible | bigint | 8 | 1 |  |  |  |
| ispackingboxable | bigint | 8 | 1 |  |  |  |
| shipalone | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| conteventduration | bigint | 8 | 1 |  |  |  |
| continuityscheduleid | varchar | 8000 | 1 |  |  |  |
| defaultdropshipmentwarehouse | varchar | 8000 | 1 |  |  |  |
| inventtable | bigint | 8 | 1 |  |  |  |
| itemvendrebategroupid | varchar | 8000 | 1 |  |  |  |
| sellenddate | datetime2 | 8 | 1 |  |  |  |
| sellstartdate | datetime2 | 8 | 1 |  |  |  |
| shipstartdate | datetime2 | 8 | 1 |  |  |  |
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
