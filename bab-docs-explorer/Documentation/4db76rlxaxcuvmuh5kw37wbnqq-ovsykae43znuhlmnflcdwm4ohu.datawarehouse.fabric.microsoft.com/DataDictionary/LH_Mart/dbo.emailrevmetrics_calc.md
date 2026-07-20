# dbo.emailrevmetrics_calc

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AzureDaily__Id__c | int | 4 | 1 |  |  |  |
| SendType | varchar | 8000 | 1 |  |  |  |
| JourneyName | varchar | 8000 | 1 |  |  |  |
| Campaign | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| SendDate | date | 3 | 1 |  |  |  |
| SegmentCount | int | 4 | 1 |  |  |  |
| OpenRate | decimal | 17 | 1 |  |  |  |
| ClickRate | decimal | 17 | 1 |  |  |  |
| TrafficVolume | int | 4 | 1 |  |  |  |
| retRev | decimal | 17 | 1 |  |  |  |
| webRev | decimal | 17 | 1 |  |  |  |
| TotalRev | decimal | 17 | 1 |  |  |  |
| JourneyActivation | varchar | 8000 | 1 |  |  |  |
| FirstEmailSent | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
