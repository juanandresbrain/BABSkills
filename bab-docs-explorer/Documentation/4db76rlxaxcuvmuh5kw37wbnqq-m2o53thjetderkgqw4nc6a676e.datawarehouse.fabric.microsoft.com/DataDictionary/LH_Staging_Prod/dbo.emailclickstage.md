# dbo.emailclickstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| SubscriberKey | varchar | 8000 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| ClickDate | datetime2 | 8 | 1 |  |  |  |
| clickCount | int | 4 | 1 |  |  |  |
