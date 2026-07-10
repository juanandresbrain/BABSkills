# dbo.tmpGuestSurveyHierarchy

**Database:** SurveyResults  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STORE_ID | varchar | 4 | 0 |  |  |  |
| STORE_NAME | varchar | 58 | 1 |  |  |  |
| CHAIN_ID | int | 4 | 0 |  |  |  |
| CHAIN_NAME | varchar | 4 | 0 |  |  |  |
| FORMAT_ID | int | 4 | 0 |  |  |  |
| FORMAT_NAME | varchar | 100 | 0 |  |  |  |
| ZONE_ID | int | 4 | 0 |  |  |  |
| ZONE_NAME | varchar | 100 | 0 |  |  |  |
| REGION_ID | int | 4 | 0 |  |  |  |
| REGION_NAME | varchar | 100 | 0 |  |  |  |
| DISTRICT_ID | varchar | 5 | 0 |  |  |  |
| DISTRICT_NAME | varchar | 100 | 0 |  |  |  |
| STORE_TYPE | nvarchar | 510 | 1 |  |  |  |
| STORE_SUB_TYPE | varchar | 7 | 0 |  |  |  |
| STORE_AGE | varchar | 7 | 0 |  |  |  |
| CUSTOM_ATTR_1 | varchar | 50 | 1 |  |  |  |
| CUSTOM_ATTR_2 | varchar | 50 | 1 |  |  |  |
| CUSTOM_ATTR_3 | varchar | 100 | 1 |  |  |  |
| CUSTOM_ATTR_4 | varchar | 5 | 1 |  |  |  |
