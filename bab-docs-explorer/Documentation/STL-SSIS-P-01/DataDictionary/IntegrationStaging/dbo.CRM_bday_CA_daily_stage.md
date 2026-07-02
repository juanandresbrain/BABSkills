# dbo.CRM_bday_CA_daily_stage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| emailAddress | nvarchar | 508 | 0 |  |  |  |
| subscriberKey | varchar | 50 | 0 |  |  |  |
| attributeCode | nvarchar | 100 | 0 |  |  |  |
| attributeComment | nvarchar | 160 | 1 |  |  |  |
| attributeValue | nvarchar | 100 | 0 |  |  |  |
| dayOfMonthAdded | int | 4 | 0 |  |  |  |
| firstName | nvarchar | 510 | 1 |  |  |  |
| lastName | nvarchar | 510 | 1 |  |  |  |
| address | nvarchar | 510 | 1 |  |  |  |
| address2 | nvarchar | 510 | 1 |  |  |  |
| city | nvarchar | 510 | 1 |  |  |  |
| state | nvarchar | 510 | 1 |  |  |  |
| zipCode | nvarchar | 40 | 1 |  |  |  |
| carrierRoute | nvarchar | 20 | 1 |  |  |  |

