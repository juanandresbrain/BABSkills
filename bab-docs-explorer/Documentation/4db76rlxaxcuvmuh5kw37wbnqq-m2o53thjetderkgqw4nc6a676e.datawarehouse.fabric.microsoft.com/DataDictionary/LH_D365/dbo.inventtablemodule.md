# dbo.inventtablemodule

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| allocatemarkup | bigint | 8 | 1 |  |  |  |
| enddisc | bigint | 8 | 1 |  |  |  |
| intercompanyblocked | bigint | 8 | 1 |  |  |  |
| moduletype | bigint | 8 | 1 |  |  |  |
| taxwithholdcalculate_th | bigint | 8 | 1 |  |  |  |
| basepricepurchase | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| itemid | varchar | 8000 | 1 |  |  |  |
| linedisc | varchar | 8000 | 1 |  |  |  |
| markup | decimal | 17 | 1 |  |  |  |
| markupgroupid | varchar | 8000 | 1 |  |  |  |
| markupseccur_ru | decimal | 17 | 1 |  |  |  |
| maximumretailprice_in | decimal | 17 | 1 |  |  |  |
| multilinedisc | varchar | 8000 | 1 |  |  |  |
| overdeliverypct | decimal | 17 | 1 |  |  |  |
| pdspricingprecision | bigint | 8 | 1 |  |  |  |
| price | decimal | 17 | 1 |  |  |  |
| pricedate | datetime2 | 8 | 1 |  |  |  |
| priceqty | decimal | 17 | 1 |  |  |  |
| priceseccur_ru | decimal | 17 | 1 |  |  |  |
| priceunit | decimal | 17 | 1 |  |  |  |
| suppitemgroupid | varchar | 8000 | 1 |  |  |  |
| taxitemgroupid | varchar | 8000 | 1 |  |  |  |
| taxwithholditemgroupheading_th | bigint | 8 | 1 |  |  |  |
| underdeliverypct | decimal | 17 | 1 |  |  |  |
| unitid | varchar | 8000 | 1 |  |  |  |
| taxgstreliefcategory_my | bigint | 8 | 1 |  |  |  |
| emptystring | varchar | 8000 | 1 |  |  |  |
| retailinventoryavailabilitybuffer | decimal | 17 | 1 |  |  |  |
| retailinventoryavailabilitylevelprofile | varchar | 8000 | 1 |  |  |  |
| babieretail | decimal | 17 | 1 |  |  |  |
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
