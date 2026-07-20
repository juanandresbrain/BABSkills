# dbo.whsloadline

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| invalid | bigint | 8 | 1 |  |  |  |
| inventtranstype | bigint | 8 | 1 |  |  |  |
| loaddirection | bigint | 8 | 1 |  |  |  |
| parentinventtranstype | bigint | 8 | 1 |  |  |  |
| transportrequest | bigint | 8 | 1 |  |  |  |
| babvalidationstatus | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| inventdimid | varchar | 8000 | 1 |  |  |  |
| inventqty | decimal | 17 | 1 |  |  |  |
| inventtransid | varchar | 8000 | 1 |  |  |  |
| itemid | varchar | 8000 | 1 |  |  |  |
| loadclosedutcdatetime | datetime2 | 8 | 1 |  |  |  |
| loadid | varchar | 8000 | 1 |  |  |  |
| loadinprocessutcdatetime | datetime2 | 8 | 1 |  |  |  |
| loadopenutcdatetime | datetime2 | 8 | 1 |  |  |  |
| loadreadytoshiputcdatetime | datetime2 | 8 | 1 |  |  |  |
| ordernum | varchar | 8000 | 1 |  |  |  |
| overdeliverypct | decimal | 17 | 1 |  |  |  |
| packingqty | decimal | 17 | 1 |  |  |  |
| parentordernum | varchar | 8000 | 1 |  |  |  |
| pickedqty | decimal | 17 | 1 |  |  |  |
| qcqty | decimal | 17 | 1 |  |  |  |
| qty | decimal | 17 | 1 |  |  |  |
| qtylefttostructure | decimal | 17 | 1 |  |  |  |
| releasetowarehouseid | varchar | 8000 | 1 |  |  |  |
| shipmentid | varchar | 8000 | 1 |  |  |  |
| underdeliverypct | decimal | 17 | 1 |  |  |  |
| uom | varchar | 8000 | 1 |  |  |  |
| workcreatedqty | decimal | 17 | 1 |  |  |  |
| volumeqty_br | decimal | 17 | 1 |  |  |  |
| volumetype_br | varchar | 8000 | 1 |  |  |  |
| pickedweight | decimal | 17 | 1 |  |  |  |
| crossdockevaluatedquantity | decimal | 17 | 1 |  |  |  |
| crossdockquantity | decimal | 17 | 1 |  |  |  |
| crossdockreservedphysical | decimal | 17 | 1 |  |  |  |
| shipconsolidationpolicy | bigint | 8 | 1 |  |  |  |
| itemnetweight | decimal | 17 | 1 |  |  |  |
| itemtareweight | decimal | 17 | 1 |  |  |  |
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
