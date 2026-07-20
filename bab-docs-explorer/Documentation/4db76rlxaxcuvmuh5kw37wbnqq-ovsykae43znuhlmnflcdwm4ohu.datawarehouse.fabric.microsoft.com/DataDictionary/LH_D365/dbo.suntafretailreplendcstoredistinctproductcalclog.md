# dbo.suntafretailreplendcstoredistinctproductcalclog

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| ordertype | bigint | 8 | 1 |  |  |  |
| firmed | bigint | 8 | 1 |  |  |  |
| reftype | bigint | 8 | 1 |  |  |  |
| babadjustmentstatus | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| parmid | varchar | 8000 | 1 |  |  |  |
| inventlocationdataareaid | varchar | 8000 | 1 |  |  |  |
| inventlocationid | varchar | 8000 | 1 |  |  |  |
| inventlocationpriority | bigint | 8 | 1 |  |  |  |
| storenumber | varchar | 8000 | 1 |  |  |  |
| distinctproduct | bigint | 8 | 1 |  |  |  |
| suggestedreplenishment | decimal | 17 | 1 |  |  |  |
| actualreplenishment | decimal | 17 | 1 |  |  |  |
| vendaccount | varchar | 8000 | 1 |  |  |  |
| refid | varchar | 8000 | 1 |  |  |  |
| inventtransid | varchar | 8000 | 1 |  |  |  |
| firmingkey | varchar | 8000 | 1 |  |  |  |
| babadjustedorderquantity | decimal | 17 | 1 |  |  |  |
| babfirmedcartoncount | bigint | 8 | 1 |  |  |  |
| baborderreleaseddate | datetime2 | 8 | 1 |  |  |  |
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
