# dbo.generaljournalaccountentry

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| iscorrection | bigint | 8 | 1 |  |  |  |
| iscredit | bigint | 8 | 1 |  |  |  |
| postingtype | bigint | 8 | 1 |  |  |  |
| skipcreditcalculation | bigint | 8 | 1 |  |  |  |
| assetleasepostingtypes | bigint | 8 | 1 |  |  |  |
| assetleasetransactiontype | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| accountingcurrencyamount | decimal | 17 | 1 |  |  |  |
| allocationlevel | bigint | 8 | 1 |  |  |  |
| generaljournalentry | bigint | 8 | 1 |  |  |  |
| historicalexchangeratedate | datetime2 | 8 | 1 |  |  |  |
| ledgeraccount | varchar | 8000 | 1 |  |  |  |
| ledgerdimension | bigint | 8 | 1 |  |  |  |
| quantity | decimal | 17 | 1 |  |  |  |
| reportingcurrencyamount | decimal | 17 | 1 |  |  |  |
| subledgerjournalentry | bigint | 8 | 1 |  |  |  |
| text | varchar | 8000 | 1 |  |  |  |
| transactioncurrencyamount | decimal | 17 | 1 |  |  |  |
| transactioncurrencycode | varchar | 8000 | 1 |  |  |  |
| mainaccount | bigint | 8 | 1 |  |  |  |
| fintag | bigint | 8 | 1 |  |  |  |
| projid_sa | varchar | 8000 | 1 |  |  |  |
| projtabledataareaid | varchar | 8000 | 1 |  |  |  |
| reasonref | bigint | 8 | 1 |  |  |  |
| paymentreference | varchar | 8000 | 1 |  |  |  |
| originalaccountentry | bigint | 8 | 1 |  |  |  |
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
