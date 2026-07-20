# dbo.journeyactivation

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Journey_Name | varchar | 8000 | 1 |  |  |  |
| Version | int | 4 | 1 |  |  |  |
| Activity_Name | varchar | 8000 | 1 |  |  |  |
| Date | varchar | 8000 | 1 |  |  |  |
| Email_Name | varchar | 8000 | 1 |  |  |  |
| Email_Subject | varchar | 8000 | 1 |  |  |  |
| Total_Sent | int | 4 | 1 |  |  |  |
| Total_Delivered | int | 4 | 1 |  |  |  |
| Delivery_Rate | varchar | 8000 | 1 |  |  |  |
| Total_Bounces | int | 4 | 1 |  |  |  |
| Bounce_Rate | varchar | 8000 | 1 |  |  |  |
| Total_Soft_Bounces | int | 4 | 1 |  |  |  |
| Soft_Bounce_Rate | varchar | 8000 | 1 |  |  |  |
| Total_Hard_Bounces | int | 4 | 1 |  |  |  |
| Hard_Bounce_Rate | varchar | 8000 | 1 |  |  |  |
| Total_Block_Bounces | int | 4 | 1 |  |  |  |
| Block_Bounce_Rate | varchar | 8000 | 1 |  |  |  |
| Total_Opens | int | 4 | 1 |  |  |  |
| Unique_Opens | int | 4 | 1 |  |  |  |
| Unique_Open_Rate | varchar | 8000 | 1 |  |  |  |
| Unique_Mobile_Opens | int | 4 | 1 |  |  |  |
| Unique_Mobile_Open_Rate | varchar | 8000 | 1 |  |  |  |
| Total_Clicks | int | 4 | 1 |  |  |  |
| Unique_Clicks | int | 4 | 1 |  |  |  |
| Unique_Click_Rate | varchar | 8000 | 1 |  |  |  |
| Total_Unsubscribes | int | 4 | 1 |  |  |  |
| Total_Unsubscribe_Rate | varchar | 8000 | 1 |  |  |  |
| Total_Conversions | int | 4 | 1 |  |  |  |
| Conversion_Rate | varchar | 8000 | 1 |  |  |  |
