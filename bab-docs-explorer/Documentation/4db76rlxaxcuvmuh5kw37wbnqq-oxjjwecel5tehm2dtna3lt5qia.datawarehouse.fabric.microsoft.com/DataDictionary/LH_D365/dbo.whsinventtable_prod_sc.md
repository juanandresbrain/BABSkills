# dbo.whsinventtable_prod_sc

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| allowmaterialoverpick | bigint | 8 | 1 |  |  |  |
| filterchanged | bigint | 8 | 1 |  |  |  |
| pickwcneg | bigint | 8 | 1 |  |  |  |
| salesunitrestricted | bigint | 8 | 1 |  |  |  |
| allowmaterialoverpicknonlp | bigint | 8 | 1 |  |  |  |
| babreceivedstatus | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| filtercode1_ | varchar | 8000 | 1 |  |  |  |
| filtercode2_ | varchar | 8000 | 1 |  |  |  |
| filtercode3_ | varchar | 8000 | 1 |  |  |  |
| filtercode4_ | varchar | 8000 | 1 |  |  |  |
| filtercode5_ | varchar | 8000 | 1 |  |  |  |
| filtercode6_ | varchar | 8000 | 1 |  |  |  |
| filtercode7_ | varchar | 8000 | 1 |  |  |  |
| filtercode8_ | varchar | 8000 | 1 |  |  |  |
| filtercode9_ | varchar | 8000 | 1 |  |  |  |
| filtercode10_ | varchar | 8000 | 1 |  |  |  |
| filtergroup1_ | varchar | 8000 | 1 |  |  |  |
| filtergroup2_ | varchar | 8000 | 1 |  |  |  |
| itemid | varchar | 8000 | 1 |  |  |  |
| maxpickqty | decimal | 17 | 1 |  |  |  |
| packageclassid | varchar | 8000 | 1 |  |  |  |
| packsizecateogryid | varchar | 8000 | 1 |  |  |  |
| physdimid | varchar | 8000 | 1 |  |  |  |
| prodqty | decimal | 17 | 1 |  |  |  |
| rfdescription1 | varchar | 8000 | 1 |  |  |  |
| rfdescription2 | varchar | 8000 | 1 |  |  |  |
| uomseqgroupid | varchar | 8000 | 1 |  |  |  |
| catchweightitemhandlingpolicyname | varchar | 8000 | 1 |  |  |  |
| materialoverpickpercentage | decimal | 17 | 1 |  |  |  |
| batchdetailscapturepolicyid | varchar | 8000 | 1 |  |  |  |
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
| babentityspecifichts | varchar | 8000 | 1 |  |  |  |
