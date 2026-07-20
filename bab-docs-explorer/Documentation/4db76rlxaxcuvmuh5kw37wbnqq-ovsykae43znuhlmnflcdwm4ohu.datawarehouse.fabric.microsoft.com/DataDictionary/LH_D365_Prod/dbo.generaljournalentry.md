# dbo.generaljournalentry

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| journalcategory | bigint | 8 | 1 |  |  |  |
| postinglayer | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| accountingdate | datetime2 | 8 | 1 |  |  |  |
| acknowledgementdate | datetime2 | 8 | 1 |  |  |  |
| documentdate | datetime2 | 8 | 1 |  |  |  |
| documentnumber | varchar | 8000 | 1 |  |  |  |
| fiscalcalendarperiod | bigint | 8 | 1 |  |  |  |
| fiscalcalendaryear | bigint | 8 | 1 |  |  |  |
| journalnumber | varchar | 8000 | 1 |  |  |  |
| ledger | bigint | 8 | 1 |  |  |  |
| subledgerjournalentry | bigint | 8 | 1 |  |  |  |
| transferid | bigint | 8 | 1 |  |  |  |
| subledgervoucher | varchar | 8000 | 1 |  |  |  |
| subledgervoucherdataareaid | varchar | 8000 | 1 |  |  |  |
| ledgerentryjournal | bigint | 8 | 1 |  |  |  |
| ledgerpostingjournal | varchar | 8000 | 1 |  |  |  |
| ledgerpostingjournaldataareaid | varchar | 8000 | 1 |  |  |  |
| budgetsourceledgerentryposted | bigint | 8 | 1 |  |  |  |
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
