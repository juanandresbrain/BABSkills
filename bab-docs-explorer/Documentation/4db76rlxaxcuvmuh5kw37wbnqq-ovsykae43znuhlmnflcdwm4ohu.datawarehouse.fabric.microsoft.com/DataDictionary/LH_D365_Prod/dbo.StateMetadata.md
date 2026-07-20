# dbo.StateMetadata

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
