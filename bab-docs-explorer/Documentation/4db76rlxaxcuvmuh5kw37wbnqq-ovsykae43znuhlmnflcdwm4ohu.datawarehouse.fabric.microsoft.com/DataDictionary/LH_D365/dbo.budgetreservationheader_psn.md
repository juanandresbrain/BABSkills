# dbo.budgetreservationheader_psn

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| documentstatus | bigint | 8 | 1 |  |  |  |
| relievingdocumenttype | bigint | 8 | 1 |  |  |  |
| workflowstatus | bigint | 8 | 1 |  |  |  |
| psniscorrection | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| accountingdate | datetime2 | 8 | 1 |  |  |  |
| accountingdistributiontemplate | bigint | 8 | 1 |  |  |  |
| budgetreservationtype_psn | bigint | 8 | 1 |  |  |  |
| canceldate | datetime2 | 8 | 1 |  |  |  |
| carriedforwardbudgettransactionheader | bigint | 8 | 1 |  |  |  |
| departmentreference | varchar | 8000 | 1 |  |  |  |
| documentnumber | varchar | 8000 | 1 |  |  |  |
| documenttitle | varchar | 8000 | 1 |  |  |  |
| enddate | datetime2 | 8 | 1 |  |  |  |
| externalreference | varchar | 8000 | 1 |  |  |  |
| finalizeclosingdate | datetime2 | 8 | 1 |  |  |  |
| ledgervoucher | varchar | 8000 | 1 |  |  |  |
| reasontableref | bigint | 8 | 1 |  |  |  |
| sourcedocumentheader | bigint | 8 | 1 |  |  |  |
| startdate | datetime2 | 8 | 1 |  |  |  |
| lastsavedaccountingdate | datetime2 | 8 | 1 |  |  |  |
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
