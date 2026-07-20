# dbo.budgetreservationline_psn

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| doupdateaccountingdistributions | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| accountingdistributiontemplate | bigint | 8 | 1 |  |  |  |
| activitynumber | varchar | 8000 | 1 |  |  |  |
| budgetreservationheader_psn | bigint | 8 | 1 |  |  |  |
| currency | varchar | 8000 | 1 |  |  |  |
| ledgerdimension | bigint | 8 | 1 |  |  |  |
| lineamount | decimal | 17 | 1 |  |  |  |
| linenumber | bigint | 8 | 1 |  |  |  |
| procurementcategory | bigint | 8 | 1 |  |  |  |
| projcategoryid | varchar | 8000 | 1 |  |  |  |
| projid | varchar | 8000 | 1 |  |  |  |
| projlinepropertyid | varchar | 8000 | 1 |  |  |  |
| projsalescurrencyid | varchar | 8000 | 1 |  |  |  |
| projsalesprice | decimal | 17 | 1 |  |  |  |
| projsalesunitid | varchar | 8000 | 1 |  |  |  |
| projtaxgroupid | varchar | 8000 | 1 |  |  |  |
| projtaxitemgroupid | varchar | 8000 | 1 |  |  |  |
| projtransid | varchar | 8000 | 1 |  |  |  |
| projworker | bigint | 8 | 1 |  |  |  |
| purchreqline | bigint | 8 | 1 |  |  |  |
| quantity | decimal | 17 | 1 |  |  |  |
| sourcedocumentline | bigint | 8 | 1 |  |  |  |
| transactiontext | varchar | 8000 | 1 |  |  |  |
| unitprice | decimal | 17 | 1 |  |  |  |
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
