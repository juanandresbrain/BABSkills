# dbo.dimensionattribute

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| type | bigint | 8 | 1 |  |  |  |
| usetranslationnamemethod | bigint | 8 | 1 |  |  |  |
| copyvaluesoncreate | bigint | 8 | 1 |  |  |  |
| givederiveddimensionsprecedence | bigint | 8 | 1 |  |  |  |
| backingentitypercompanytype | bigint | 8 | 1 |  |  |  |
| isbalancing_psn | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| backingentitykeyfieldid | bigint | 8 | 1 |  |  |  |
| backingentitykeyfieldname | varchar | 8000 | 1 |  |  |  |
| backingentitytableid | bigint | 8 | 1 |  |  |  |
| backingentitytablename | varchar | 8000 | 1 |  |  |  |
| backingentitytype | bigint | 8 | 1 |  |  |  |
| backingentityvaluefieldid | bigint | 8 | 1 |  |  |  |
| backingentityvaluefieldname | varchar | 8000 | 1 |  |  |  |
| hashkey | varchar | 8000 | 1 |  |  |  |
| keyattribute | bigint | 8 | 1 |  |  |  |
| name | varchar | 8000 | 1 |  |  |  |
| nameattribute | bigint | 8 | 1 |  |  |  |
| reportcolumnname | varchar | 8000 | 1 |  |  |  |
| translationkeyfieldid | bigint | 8 | 1 |  |  |  |
| translationkeyfieldname | varchar | 8000 | 1 |  |  |  |
| translationlanguageidfieldid | bigint | 8 | 1 |  |  |  |
| translationlanguageidfieldname | varchar | 8000 | 1 |  |  |  |
| translationnamefieldid | bigint | 8 | 1 |  |  |  |
| translationnamefieldname | varchar | 8000 | 1 |  |  |  |
| translationtableid | bigint | 8 | 1 |  |  |  |
| translationtablename | varchar | 8000 | 1 |  |  |  |
| valueattribute | bigint | 8 | 1 |  |  |  |
| viewname | varchar | 8000 | 1 |  |  |  |
| translationviewkeyfieldname | varchar | 8000 | 1 |  |  |  |
| translationviewlanguageidfieldname | varchar | 8000 | 1 |  |  |  |
| translationviewname | varchar | 8000 | 1 |  |  |  |
| translationviewnamefieldname | varchar | 8000 | 1 |  |  |  |
| translationviewsystemlanguageidfieldname | varchar | 8000 | 1 |  |  |  |
| translationviewtranslatednamefieldname | varchar | 8000 | 1 |  |  |  |
| translationviewvaluefieldname | varchar | 8000 | 1 |  |  |  |
| translationviewid | bigint | 8 | 1 |  |  |  |
| translationviewkeyfieldid | bigint | 8 | 1 |  |  |  |
| translationviewlanguageidfieldid | bigint | 8 | 1 |  |  |  |
| translationviewnamefieldid | bigint | 8 | 1 |  |  |  |
| translationviewsystemlanguageidfieldid | bigint | 8 | 1 |  |  |  |
| translationviewtranslatednamefieldid | bigint | 8 | 1 |  |  |  |
| translationviewvaluefieldid | bigint | 8 | 1 |  |  |  |
| dimensionkeycolumnname | varchar | 8000 | 1 |  |  |  |
| dimensionvaluecolumnname | varchar | 8000 | 1 |  |  |  |
| balancingdimension_psn | bigint | 8 | 1 |  |  |  |
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
