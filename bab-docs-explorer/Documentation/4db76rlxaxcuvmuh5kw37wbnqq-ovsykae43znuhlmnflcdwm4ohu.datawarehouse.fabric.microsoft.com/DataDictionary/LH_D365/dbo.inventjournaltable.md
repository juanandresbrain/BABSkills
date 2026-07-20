# dbo.inventjournaltable

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| deletepostedlines | bigint | 8 | 1 |  |  |  |
| detailsummary | bigint | 8 | 1 |  |  |  |
| inventdoctype_pl | bigint | 8 | 1 |  |  |  |
| journaltype | bigint | 8 | 1 |  |  |  |
| posted | bigint | 8 | 1 |  |  |  |
| reservation | bigint | 8 | 1 |  |  |  |
| retailreplenishmenttype | bigint | 8 | 1 |  |  |  |
| retailretailstatustype | bigint | 8 | 1 |  |  |  |
| storno_ru | bigint | 8 | 1 |  |  |  |
| systemblocked | bigint | 8 | 1 |  |  |  |
| voucherchange | bigint | 8 | 1 |  |  |  |
| voucherdraw | bigint | 8 | 1 |  |  |  |
| isretailcommitted | bigint | 8 | 1 |  |  |  |
| countingstatusregistrationpolicy | bigint | 8 | 1 |  |  |  |
| journalorigintype | bigint | 8 | 1 |  |  |  |
| workflowapprovalstatus | bigint | 8 | 1 |  |  |  |
| inventoryservicejournalexpectedstatus | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| blockusergroupid | varchar | 8000 | 1 |  |  |  |
| blockuserid | varchar | 8000 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| fshreplenishmentref | varchar | 8000 | 1 |  |  |  |
| inventdimfixed | bigint | 8 | 1 |  |  |  |
| inventlocationid | varchar | 8000 | 1 |  |  |  |
| inventsiteid | varchar | 8000 | 1 |  |  |  |
| journalid | varchar | 8000 | 1 |  |  |  |
| journalidorignal | varchar | 8000 | 1 |  |  |  |
| journalnameid | varchar | 8000 | 1 |  |  |  |
| ledgerdimension | bigint | 8 | 1 |  |  |  |
| numoflines | bigint | 8 | 1 |  |  |  |
| offsessionid_ru | varchar | 8000 | 1 |  |  |  |
| posteddatetime | datetime2 | 8 | 1 |  |  |  |
| posteduserid | varchar | 8000 | 1 |  |  |  |
| sessionid | bigint | 8 | 1 |  |  |  |
| sessionlogindatetime | datetime2 | 8 | 1 |  |  |  |
| source | varchar | 8000 | 1 |  |  |  |
| vouchernumbersequencetable | bigint | 8 | 1 |  |  |  |
| worker | bigint | 8 | 1 |  |  |  |
| itmoverundertransid | varchar | 8000 | 1 |  |  |  |
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
| fintag | bigint | 8 | 1 |  |  |  |
| rentaltransferrequest | bigint | 8 | 1 |  |  |  |
