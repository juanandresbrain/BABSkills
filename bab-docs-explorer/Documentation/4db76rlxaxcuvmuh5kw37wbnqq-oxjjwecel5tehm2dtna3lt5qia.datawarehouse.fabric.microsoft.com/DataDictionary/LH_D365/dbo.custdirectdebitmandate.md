# dbo.custdirectdebitmandate

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| isfirst | bigint | 8 | 1 |  |  |  |
| mandatepaymenttype | bigint | 8 | 1 |  |  |  |
| mandatescheme | bigint | 8 | 1 |  |  |  |
| status | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| bankaccount | varchar | 8000 | 1 |  |  |  |
| banksubmissiondaysfirst | bigint | 8 | 1 |  |  |  |
| banksubmissiondaysrecurring | bigint | 8 | 1 |  |  |  |
| cancellationdate | datetime2 | 8 | 1 |  |  |  |
| creditorbankaccount | varchar | 8000 | 1 |  |  |  |
| custaccount | varchar | 8000 | 1 |  |  |  |
| customeraddress | bigint | 8 | 1 |  |  |  |
| expectedusagecount | bigint | 8 | 1 |  |  |  |
| expirationdate | datetime2 | 8 | 1 |  |  |  |
| lastlognum | bigint | 8 | 1 |  |  |  |
| mandatereference | varchar | 8000 | 1 |  |  |  |
| prenotificationdaysfirst | bigint | 8 | 1 |  |  |  |
| prenotificationdaysrecurring | bigint | 8 | 1 |  |  |  |
| previousexpirationdate | datetime2 | 8 | 1 |  |  |  |
| previousiban | varchar | 8000 | 1 |  |  |  |
| signaturedate | datetime2 | 8 | 1 |  |  |  |
| signaturelocation | varchar | 8000 | 1 |  |  |  |
| usagecount | bigint | 8 | 1 |  |  |  |
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
