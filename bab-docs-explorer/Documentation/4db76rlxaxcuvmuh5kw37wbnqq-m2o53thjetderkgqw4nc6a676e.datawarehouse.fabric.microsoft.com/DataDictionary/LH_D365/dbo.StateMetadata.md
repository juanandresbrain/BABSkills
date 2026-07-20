# dbo.StateMetadata

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EntityName | varchar | 8000 | 1 |  |  |  |
| State | bigint | 8 | 1 |  |  |  |
| IsUserLocalizedLabel | bit | 1 | 1 |  |  |  |
| LocalizedLabelLanguageCode | bigint | 8 | 1 |  |  |  |
| LocalizedLabel | varchar | 8000 | 1 |  |  |  |
| ExternalValue | varchar | 8000 | 1 |  |  |  |
| createdonpartition | varchar | 8000 | 1 |  |  |  |
