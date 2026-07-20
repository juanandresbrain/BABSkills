# dbo.globaloptionsetmetadata

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OptionSetName | varchar | 8000 | 1 |  |  |  |
| Option | bigint | 8 | 1 |  |  |  |
| IsUserLocalizedLabel | bit | 1 | 1 |  |  |  |
| LocalizedLabelLanguageCode | bigint | 8 | 1 |  |  |  |
| LocalizedLabel | varchar | 8000 | 1 |  |  |  |
| GlobalOptionSetName | varchar | 8000 | 1 |  |  |  |
| EntityName | varchar | 8000 | 1 |  |  |  |
| ExternalValue | varchar | 8000 | 1 |  |  |  |
| createdonpartition | varchar | 8000 | 1 |  |  |  |
