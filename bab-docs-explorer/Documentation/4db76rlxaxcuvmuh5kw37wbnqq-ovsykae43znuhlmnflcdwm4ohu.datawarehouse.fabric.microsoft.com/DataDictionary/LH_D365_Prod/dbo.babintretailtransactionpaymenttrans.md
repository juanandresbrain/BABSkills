# dbo.babintretailtransactionpaymenttrans

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| changeline | bigint | 8 | 1 |  |  |  |
| babintretailprocessed | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| amountcur | decimal | 17 | 1 |  |  |  |
| amountmst | decimal | 17 | 1 |  |  |  |
| retailamounttendered | decimal | 17 | 1 |  |  |  |
| retailcardtypeid | varchar | 8000 | 1 |  |  |  |
| linenum | decimal | 17 | 1 |  |  |  |
| retailreceiptid | varchar | 8000 | 1 |  |  |  |
| retailtendertypeid | varchar | 8000 | 1 |  |  |  |
| retailterminalid | varchar | 8000 | 1 |  |  |  |
| retailtransactionid | varchar | 8000 | 1 |  |  |  |
| transdate | datetime2 | 8 | 1 |  |  |  |
| accountnum | varchar | 8000 | 1 |  |  |  |
| retailcardnum | varchar | 8000 | 1 |  |  |  |
| paymentauthorization | varchar | 8000 | 1 |  |  |  |
| currencycode | varchar | 8000 | 1 |  |  |  |
| babintretailoperatingunitnumber | varchar | 8000 | 1 |  |  |  |
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
