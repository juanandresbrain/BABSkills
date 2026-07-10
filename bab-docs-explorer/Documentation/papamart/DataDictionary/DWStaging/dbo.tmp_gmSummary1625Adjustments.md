# dbo.tmp_gmSummary1625Adjustments

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_period | int | 4 | 1 |  |  |  |
| country | varchar | 50 | 1 |  |  |  |
| Line_Object | smallint | 2 | 0 |  |  |  |
| Line_Object_Description | varchar | 50 | 1 |  |  |  |
| isGCCoupon | int | 4 | 0 |  |  |  |
| numRecs | int | 4 | 1 |  |  |  |
| discAmount | numeric | 17 | 1 |  |  |  |
| minDate | datetime | 8 | 1 |  |  |  |
| maxDate | datetime | 8 | 1 |  |  |  |
