# dbo.ledgerjournaltrans_asset

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| budgetpostingstatus | bigint | 8 | 1 |  |  |  |
| documenttype_jp | bigint | 8 | 1 |  |  |  |
| isadjusteddepreciation | bigint | 8 | 1 |  |  |  |
| isprioryear | bigint | 8 | 1 |  |  |  |
| lowvaluepooltype_au | bigint | 8 | 1 |  |  |  |
| revaluationtrans | bigint | 8 | 1 |  |  |  |
| transtype | bigint | 8 | 1 |  |  |  |
| candisposal_ru | bigint | 8 | 1 |  |  |  |
| postvalue_ru | bigint | 8 | 1 |  |  |  |
| assettranssubtype | bigint | 8 | 1 |  |  |  |
| originalisprioryear | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| assetdocumententry_jp | bigint | 8 | 1 |  |  |  |
| assetgroup_in | varchar | 8000 | 1 |  |  |  |
| assetid | varchar | 8000 | 1 |  |  |  |
| bookid | varchar | 8000 | 1 |  |  |  |
| budgetmodel | varchar | 8000 | 1 |  |  |  |
| company | varchar | 8000 | 1 |  |  |  |
| consumptionquantity | decimal | 17 | 1 |  |  |  |
| depreciationstartdate | datetime2 | 8 | 1 |  |  |  |
| depreciationtime | decimal | 17 | 1 |  |  |  |
| lvptransferid_au | varchar | 8000 | 1 |  |  |  |
| refassetid | varchar | 8000 | 1 |  |  |  |
| refrecid | bigint | 8 | 1 |  |  |  |
| reservetransid | bigint | 8 | 1 |  |  |  |
| revaluationamount | decimal | 17 | 1 |  |  |  |
| salefactor_pl | decimal | 17 | 1 |  |  |  |
| ledgerdimension_ru | bigint | 8 | 1 |  |  |  |
| depreciationbonusid_ru | varchar | 8000 | 1 |  |  |  |
| depreciationperiod_ru | datetime2 | 8 | 1 |  |  |  |
| linkedtransrecid_ru | bigint | 8 | 1 |  |  |  |
| stornorecid_ru | bigint | 8 | 1 |  |  |  |
| correctedperiod_ru | datetime2 | 8 | 1 |  |  |  |
| assetgroup_lt | varchar | 8000 | 1 |  |  |  |
| amountcreditreportingcurrency | decimal | 17 | 1 |  |  |  |
| amountdebitreportingcurrency | decimal | 17 | 1 |  |  |  |
| periodfromdate | datetime2 | 8 | 1 |  |  |  |
| periodtodate | datetime2 | 8 | 1 |  |  |  |
| originaltransdate | datetime2 | 8 | 1 |  |  |  |
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
| vendinvoiceinfoline | bigint | 8 | 1 |  |  |  |
