# dbo.emailengagementsummary

**Database:** LH_Temp  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SendType | varchar | 8000 | 1 |  |  |  |
| JourneyName | varchar | 8000 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| SendDate | date | 3 | 1 |  |  |  |
| SegmentCount | int | 4 | 1 |  |  |  |
| UniqueOpens | int | 4 | 1 |  |  |  |
| DeliveredEmails | int | 4 | 1 |  |  |  |
| TotalClicks | int | 4 | 1 |  |  |  |
