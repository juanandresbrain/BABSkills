# dbo.hcmpersonprivatedetails

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| gender | bigint | 8 | 1 |  |  |  |
| isdisabled | bigint | 8 | 1 |  |  |  |
| isfulltimestudent | bigint | 8 | 1 |  |  |  |
| benefitbeneficiarydefault | bigint | 8 | 1 |  |  |  |
| benefitdocumentationstatus | bigint | 8 | 1 |  |  |  |
| benefitemployed | bigint | 8 | 1 |  |  |  |
| benefitemployeeaddress | bigint | 8 | 1 |  |  |  |
| benefithasdocumentation | bigint | 8 | 1 |  |  |  |
| benefitotherinsurance | bigint | 8 | 1 |  |  |  |
| benefitoverageddependent | bigint | 8 | 1 |  |  |  |
| benefitsmoker | bigint | 8 | 1 |  |  |  |
| benefitisloc | bigint | 8 | 1 |  |  |  |
| benefitisloa | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| personbirthcountryregion | varchar | 8000 | 1 |  |  |  |
| personbirthcity | varchar | 8000 | 1 |  |  |  |
| birthdate | datetime2 | 8 | 1 |  |  |  |
| citizenshipcountryregion | varchar | 8000 | 1 |  |  |  |
| deceaseddate | datetime2 | 8 | 1 |  |  |  |
| disabledverificationdate | datetime2 | 8 | 1 |  |  |  |
| education | varchar | 8000 | 1 |  |  |  |
| ethnicorigin | bigint | 8 | 1 |  |  |  |
| fatherbirthcountryregion | varchar | 8000 | 1 |  |  |  |
| motherbirthcountryregion | varchar | 8000 | 1 |  |  |  |
| nativelanguage | bigint | 8 | 1 |  |  |  |
| person | bigint | 8 | 1 |  |  |  |
| nationalitycountryregion | varchar | 8000 | 1 |  |  |  |
| benefitadoptiondate | datetime2 | 8 | 1 |  |  |  |
| benefitdesigneenickname | varchar | 8000 | 1 |  |  |  |
| benefitdivorcedate | datetime2 | 8 | 1 |  |  |  |
| benefitdocumentationdate | datetime2 | 8 | 1 |  |  |  |
| benefitvalidfromdatetime | datetime2 | 8 | 1 |  |  |  |
| benefitvalidtodatetime | datetime2 | 8 | 1 |  |  |  |
| benefitweddingdate | datetime2 | 8 | 1 |  |  |  |
| benefitmedicareeligibilitydate | datetime2 | 8 | 1 |  |  |  |
| benefitloceffectivedate | datetime2 | 8 | 1 |  |  |  |
| benefitloaeffectivedate | datetime2 | 8 | 1 |  |  |  |
| benefitloaexpirationdate | datetime2 | 8 | 1 |  |  |  |
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
