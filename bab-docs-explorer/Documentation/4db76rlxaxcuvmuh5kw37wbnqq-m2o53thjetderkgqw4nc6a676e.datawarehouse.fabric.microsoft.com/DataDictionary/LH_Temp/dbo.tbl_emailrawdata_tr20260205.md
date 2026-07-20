# dbo.tbl_emailrawdata_tr20260205

**Database:** LH_Temp  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SendDate | date | 3 | 1 |  |  |  |
| ClickDate | datetime2 | 8 | 1 |  |  |  |
| BounceDate | datetime2 | 8 | 1 |  |  |  |
| IsDelivered | int | 4 | 1 |  |  |  |
| OpenDate | datetime2 | 8 | 1 |  |  |  |
| clickCount | int | 4 | 1 |  |  |  |
| EmailName | varchar | 8000 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| ClientID | int | 4 | 1 |  |  |  |
| SendID | int | 4 | 1 |  |  |  |
| SendType | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| SegmentCount | int | 4 | 1 |  |  |  |
| UniqueOpen | int | 4 | 1 |  |  |  |
| RID | int | 4 | 1 |  |  |  |
