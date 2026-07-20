# dbo.ecoresproduct

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| pdscwproduct | bigint | 8 | 1 |  |  |  |
| producttype | bigint | 8 | 1 |  |  |  |
| servicetype | bigint | 8 | 1 |  |  |  |
| sunplmsyncwithplm | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| displayproductnumber | varchar | 8000 | 1 |  |  |  |
| instancerelationtype | bigint | 8 | 1 |  |  |  |
| searchname | varchar | 8000 | 1 |  |  |  |
| engchgproductownerid | varchar | 8000 | 1 |  |  |  |
| engchgproductcategorydetails | bigint | 8 | 1 |  |  |  |
| engchgproductreleasepolicy | bigint | 8 | 1 |  |  |  |
| engchgproductreadinesspolicy | bigint | 8 | 1 |  |  |  |
| babcolordescription | varchar | 8000 | 1 |  |  |  |
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
