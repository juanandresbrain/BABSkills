# dbo.retailstatementjour

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| closingmethod | bigint | 8 | 1 |  |  |  |
| skipconfirmation | bigint | 8 | 1 |  |  |  |
| statementmethod | bigint | 8 | 1 |  |  |  |
| eodcodeversion | bigint | 8 | 1 |  |  |  |
| ignorereturnlink | bigint | 8 | 1 |  |  |  |
| statementtype | bigint | 8 | 1 |  |  |  |
| usechannelcashmanagementreconciliation | bigint | 8 | 1 |  |  |  |
| enableparallelpaymentpostingforsales | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| calculateddate | datetime2 | 8 | 1 |  |  |  |
| calculationtime | bigint | 8 | 1 |  |  |  |
| calculatedtime | datetime2 | 8 | 1 |  |  |  |
| defaultdimension | bigint | 8 | 1 |  |  |  |
| expensesamount | decimal | 17 | 1 |  |  |  |
| incomeamount | decimal | 17 | 1 |  |  |  |
| linediscamount | decimal | 17 | 1 |  |  |  |
| loyaltydiscamount_ru | decimal | 17 | 1 |  |  |  |
| numberofblockedcustomers | bigint | 8 | 1 |  |  |  |
| numberofblockeditems | bigint | 8 | 1 |  |  |  |
| numberofitemsbarcodesnotonfile | bigint | 8 | 1 |  |  |  |
| numberofsalespaymentdifferencetrans | bigint | 8 | 1 |  |  |  |
| numberofwrongshifttransactions | bigint | 8 | 1 |  |  |  |
| numbersequencecode | varchar | 8000 | 1 |  |  |  |
| posteddate | datetime2 | 8 | 1 |  |  |  |
| postedtime | bigint | 8 | 1 |  |  |  |
| postingdate | datetime2 | 8 | 1 |  |  |  |
| replicationcounter | bigint | 8 | 1 |  |  |  |
| salesamount | decimal | 17 | 1 |  |  |  |
| shiftdate | datetime2 | 8 | 1 |  |  |  |
| shiftid | varchar | 8000 | 1 |  |  |  |
| staffterminal | varchar | 8000 | 1 |  |  |  |
| statementdate | datetime2 | 8 | 1 |  |  |  |
| statementid | varchar | 8000 | 1 |  |  |  |
| storeid | varchar | 8000 | 1 |  |  |  |
| taxamount | decimal | 17 | 1 |  |  |  |
| totaldiscamount | decimal | 17 | 1 |  |  |  |
| transfromdate | datetime2 | 8 | 1 |  |  |  |
| transfromtime | bigint | 8 | 1 |  |  |  |
| transtodate | datetime2 | 8 | 1 |  |  |  |
| transtotime | bigint | 8 | 1 |  |  |  |
| calculatedlines | bigint | 8 | 1 |  |  |  |
| postingbatchjobid | bigint | 8 | 1 |  |  |  |
| posteddatetime | datetime2 | 8 | 1 |  |  |  |
| calculateddatetime | datetime2 | 8 | 1 |  |  |  |
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
