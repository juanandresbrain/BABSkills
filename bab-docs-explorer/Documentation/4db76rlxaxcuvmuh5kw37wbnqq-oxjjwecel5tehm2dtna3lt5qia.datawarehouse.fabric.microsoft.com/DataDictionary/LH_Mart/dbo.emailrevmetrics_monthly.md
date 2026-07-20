# dbo.emailrevmetrics_monthly

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AzureMonthly__Id__c | int | 4 | 1 |  |  |  |
| Date | varchar | 8000 | 1 |  |  |  |
| EmailType | varchar | 8000 | 1 |  |  |  |
| EmailSentCount | int | 4 | 1 |  |  |  |
| AvgSegmentCount | int | 4 | 1 |  |  |  |
| AvgOpenRate | decimal | 17 | 1 |  |  |  |
| AvgClickThroughRate | decimal | 17 | 1 |  |  |  |
| TotalGuestsMarketed | int | 4 | 1 |  |  |  |
| AvgSendPerDay | decimal | 17 | 1 |  |  |  |
| AvgTrafficVolumne | int | 4 | 1 |  |  |  |
| RetRevenue | decimal | 17 | 1 |  |  |  |
| WebRevenue | decimal | 17 | 1 |  |  |  |
| TotalRevenue | decimal | 17 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
