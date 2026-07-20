# dbo.inventclosing

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| active | bigint | 8 | 1 |  |  |  |
| adjustmentspec | bigint | 8 | 1 |  |  |  |
| adjustmenttype | bigint | 8 | 1 |  |  |  |
| cancellation | bigint | 8 | 1 |  |  |  |
| cancelrecalculation | bigint | 8 | 1 |  |  |  |
| helperscreated | bigint | 8 | 1 |  |  |  |
| inventcoststatus | bigint | 8 | 1 |  |  |  |
| inventsumdatefinancialcalcfinished_ru | bigint | 8 | 1 |  |  |  |
| inventtranscurrency_ru | bigint | 8 | 1 |  |  |  |
| ledger | bigint | 8 | 1 |  |  |  |
| ledgercorrection | bigint | 8 | 1 |  |  |  |
| prodjournal | bigint | 8 | 1 |  |  |  |
| runrecalculation | bigint | 8 | 1 |  |  |  |
| stoprunning | bigint | 8 | 1 |  |  |  |
| stoponerror | bigint | 8 | 1 |  |  |  |
| stornoadjustment_ru | bigint | 8 | 1 |  |  |  |
| shouldsummarizeinfolog | bigint | 8 | 1 |  |  |  |
| itmadjustment | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| bomlevel | bigint | 8 | 1 |  |  |  |
| cancelclosingrefrecid | bigint | 8 | 1 |  |  |  |
| end | bigint | 8 | 1 |  |  |  |
| executed | datetime2 | 8 | 1 |  |  |  |
| maxiterations | bigint | 8 | 1 |  |  |  |
| mintransfervalue | decimal | 17 | 1 |  |  |  |
| nextrunnum | bigint | 8 | 1 |  |  |  |
| notes | varchar | 8000 | 1 |  |  |  |
| numofiteration | bigint | 8 | 1 |  |  |  |
| periodcode | varchar | 8000 | 1 |  |  |  |
| runnum | bigint | 8 | 1 |  |  |  |
| start | bigint | 8 | 1 |  |  |  |
| transdate | datetime2 | 8 | 1 |  |  |  |
| voucher | varchar | 8000 | 1 |  |  |  |
| ledgerpostingbatch | bigint | 8 | 1 |  |  |  |
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
