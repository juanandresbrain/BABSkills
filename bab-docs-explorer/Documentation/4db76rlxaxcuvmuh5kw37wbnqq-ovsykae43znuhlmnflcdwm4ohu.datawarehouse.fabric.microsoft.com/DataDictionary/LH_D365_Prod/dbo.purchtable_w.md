# dbo.purchtable_w

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| customsimportorder_in | bigint | 8 | 1 |  |  |  |
| customsinvoiceregistered_in | bigint | 8 | 1 |  |  |  |
| natureofassessee_in | bigint | 8 | 1 |  |  |  |
| invoicetype_my | bigint | 8 | 1 |  |  |  |
| withigstpayment_in | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| emplaccount_ru | varchar | 8000 | 1 |  |  |  |
| purchtable | bigint | 8 | 1 |  |  |  |
| taxbranch | bigint | 8 | 1 |  |  |  |
| tcsgroup_in | varchar | 8000 | 1 |  |  |  |
| tdsgroup_in | varchar | 8000 | 1 |  |  |  |
| gstapprovalnumber_my | varchar | 8000 | 1 |  |  |  |
| invoicepostaladdress_th | bigint | 8 | 1 |  |  |  |
| taxgstimportdeclarationno_my | varchar | 8000 | 1 |  |  |  |
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
