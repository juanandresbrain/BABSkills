# dbo.retailsalesline

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| ispriceoverridden | bigint | 8 | 1 |  |  |  |
| fulfillmentstatus | bigint | 8 | 1 |  |  |  |
| ispricekeyedin | bigint | 8 | 1 |  |  |  |
| quantitycolumnsversion | bigint | 8 | 1 |  |  |  |
| ispricelocked | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| catalog | bigint | 8 | 1 |  |  |  |
| linedscamount | decimal | 17 | 1 |  |  |  |
| linemanualdiscountamount | decimal | 17 | 1 |  |  |  |
| linemanualdiscountpercentage | decimal | 17 | 1 |  |  |  |
| linepercentagediscount | decimal | 17 | 1 |  |  |  |
| listingid | varchar | 8000 | 1 |  |  |  |
| periodicdiscount | decimal | 17 | 1 |  |  |  |
| periodicpercentagediscount | decimal | 17 | 1 |  |  |  |
| totaldiscount | decimal | 17 | 1 |  |  |  |
| totalpctdiscount | decimal | 17 | 1 |  |  |  |
| salesline | bigint | 8 | 1 |  |  |  |
| fulfillmentstoreid | varchar | 8000 | 1 |  |  |  |
| inventtransid | varchar | 8000 | 1 |  |  |  |
| returnreasoncodeid | varchar | 8000 | 1 |  |  |  |
| originalprice | decimal | 17 | 1 |  |  |  |
| pickupstarttime | bigint | 8 | 1 |  |  |  |
| pickupendtime | bigint | 8 | 1 |  |  |  |
| priceoverridereasoncode | varchar | 8000 | 1 |  |  |  |
| quantitypicked | decimal | 17 | 1 |  |  |  |
| quantitypacked | decimal | 17 | 1 |  |  |  |
| quantityinvoiced | decimal | 17 | 1 |  |  |  |
| infocodeid | varchar | 8000 | 1 |  |  |  |
| information | varchar | 8000 | 1 |  |  |  |
| subinfocodeid | varchar | 8000 | 1 |  |  |  |
| tenderdiscount | decimal | 17 | 1 |  |  |  |
| tenderdiscountpercentage | decimal | 17 | 1 |  |  |  |
| taxexemptpriceinclusiveoriginalprice | decimal | 17 | 1 |  |  |  |
| taxexemptpriceinclusivereductionamount | decimal | 17 | 1 |  |  |  |
| quantitynotprocessed | decimal | 17 | 1 |  |  |  |
| quantityphysicallyreserved | decimal | 17 | 1 |  |  |  |
| retailproductlistlineupdateid | varchar | 8000 | 1 |  |  |  |
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
