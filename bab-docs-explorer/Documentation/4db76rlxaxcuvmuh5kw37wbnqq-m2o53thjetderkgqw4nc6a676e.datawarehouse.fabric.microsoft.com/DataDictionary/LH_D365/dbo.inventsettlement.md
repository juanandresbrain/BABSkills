# dbo.inventsettlement

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| balancesheetposting | bigint | 8 | 1 |  |  |  |
| cancelled | bigint | 8 | 1 |  |  |  |
| inventtranscurrency_ru | bigint | 8 | 1 |  |  |  |
| operationsposting | bigint | 8 | 1 |  |  |  |
| posted | bigint | 8 | 1 |  |  |  |
| settlemodel | bigint | 8 | 1 |  |  |  |
| settletype | bigint | 8 | 1 |  |  |  |
| itmisstdcostadjustment | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| balancesheetledgerdimension | bigint | 8 | 1 |  |  |  |
| costamountadjustment | decimal | 17 | 1 |  |  |  |
| costamountsettled | decimal | 17 | 1 |  |  |  |
| defaultdimension | bigint | 8 | 1 |  |  |  |
| inventtransid | varchar | 8000 | 1 |  |  |  |
| itemgroupid | varchar | 8000 | 1 |  |  |  |
| itemid | varchar | 8000 | 1 |  |  |  |
| markupcode_ru | varchar | 8000 | 1 |  |  |  |
| operationsledgerdimension | bigint | 8 | 1 |  |  |  |
| pdscwsettled | decimal | 17 | 1 |  |  |  |
| qtysettled | decimal | 17 | 1 |  |  |  |
| settletransid | varchar | 8000 | 1 |  |  |  |
| transbegintime | datetime2 | 8 | 1 |  |  |  |
| transdate | datetime2 | 8 | 1 |  |  |  |
| transrecid | bigint | 8 | 1 |  |  |  |
| vendaccountmarkup_ru | varchar | 8000 | 1 |  |  |  |
| vendinvoiceidmarkup_ru | varchar | 8000 | 1 |  |  |  |
| voucher | varchar | 8000 | 1 |  |  |  |
| itmcosttransrecid | bigint | 8 | 1 |  |  |  |
| itmcosttypeid | varchar | 8000 | 1 |  |  |  |
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
