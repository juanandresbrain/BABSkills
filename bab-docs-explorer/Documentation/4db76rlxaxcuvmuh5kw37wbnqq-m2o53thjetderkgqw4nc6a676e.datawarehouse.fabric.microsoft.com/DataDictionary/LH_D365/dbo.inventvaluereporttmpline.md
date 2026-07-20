# dbo.inventvaluereporttmpline

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| linetype | bigint | 8 | 1 |  |  |  |
| referencecategory | bigint | 8 | 1 |  |  |  |
| resourcetype | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| cogsfinancialamount | decimal | 17 | 1 |  |  |  |
| cogsfinancialqty | decimal | 17 | 1 |  |  |  |
| configid | varchar | 8000 | 1 |  |  |  |
| deferredcogsphysicalnonpostedamount | decimal | 17 | 1 |  |  |  |
| deferredcogsphysicalnonpostedqty | decimal | 17 | 1 |  |  |  |
| deferredcogsphysicalpostedamount | decimal | 17 | 1 |  |  |  |
| deferredcogsphysicalpostedqty | decimal | 17 | 1 |  |  |  |
| inventbatchid | varchar | 8000 | 1 |  |  |  |
| inventcolorid | varchar | 8000 | 1 |  |  |  |
| inventgtdid_ru | varchar | 8000 | 1 |  |  |  |
| inventlocationid | varchar | 8000 | 1 |  |  |  |
| inventoryfinancialamount | decimal | 17 | 1 |  |  |  |
| inventoryfinancialqty | decimal | 17 | 1 |  |  |  |
| inventoryphysicalnonpostedamount | decimal | 17 | 1 |  |  |  |
| inventoryphysicalnonpostedqty | decimal | 17 | 1 |  |  |  |
| inventoryphysicalpostedamount | decimal | 17 | 1 |  |  |  |
| inventoryphysicalpostedqty | decimal | 17 | 1 |  |  |  |
| inventownerid_ru | varchar | 8000 | 1 |  |  |  |
| inventprofileid_ru | varchar | 8000 | 1 |  |  |  |
| inventserialid | varchar | 8000 | 1 |  |  |  |
| inventsiteid | varchar | 8000 | 1 |  |  |  |
| inventsizeid | varchar | 8000 | 1 |  |  |  |
| inventstatusid | varchar | 8000 | 1 |  |  |  |
| inventstyleid | varchar | 8000 | 1 |  |  |  |
| inventversionid | varchar | 8000 | 1 |  |  |  |
| inventtransid | varchar | 8000 | 1 |  |  |  |
| licenseplateid | varchar | 8000 | 1 |  |  |  |
| plfinancialamount | decimal | 17 | 1 |  |  |  |
| plfinancialqty | decimal | 17 | 1 |  |  |  |
| reference | varchar | 8000 | 1 |  |  |  |
| resourcegroupid | varchar | 8000 | 1 |  |  |  |
| resourceid | varchar | 8000 | 1 |  |  |  |
| transactionid | bigint | 8 | 1 |  |  |  |
| transbegintime | datetime2 | 8 | 1 |  |  |  |
| transdate | datetime2 | 8 | 1 |  |  |  |
| voucher | varchar | 8000 | 1 |  |  |  |
| wipphysicalnonpostedamount | decimal | 17 | 1 |  |  |  |
| wipphysicalnonpostedqty | decimal | 17 | 1 |  |  |  |
| wipphysicalpostedamount | decimal | 17 | 1 |  |  |  |
| wipphysicalpostedqty | decimal | 17 | 1 |  |  |  |
| wmslocationid | varchar | 8000 | 1 |  |  |  |
| wmspalletid | varchar | 8000 | 1 |  |  |  |
| inventdimension1 | varchar | 8000 | 1 |  |  |  |
| inventdimension2 | varchar | 8000 | 1 |  |  |  |
| inventdimension3 | varchar | 8000 | 1 |  |  |  |
| inventdimension4 | varchar | 8000 | 1 |  |  |  |
| inventdimension5 | varchar | 8000 | 1 |  |  |  |
| inventdimension6 | varchar | 8000 | 1 |  |  |  |
| inventdimension7 | varchar | 8000 | 1 |  |  |  |
| inventdimension8 | varchar | 8000 | 1 |  |  |  |
| inventdimension9 | datetime2 | 8 | 1 |  |  |  |
| inventdimension10 | decimal | 17 | 1 |  |  |  |
| inventdimension11 | varchar | 8000 | 1 |  |  |  |
| inventdimension12 | varchar | 8000 | 1 |  |  |  |
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
