# dbo.CRM_bday_UK_guest_export

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tmpId | int | 4 | 0 | YES |  |  |
| emailAddress | nvarchar | 508 | 0 |  |  |  |
| subscriberKey | varchar | 50 | 0 |  |  |  |
| firstName | nvarchar | 510 | 1 |  |  |  |
| lastName | nvarchar | 510 | 1 |  |  |  |
| address | nvarchar | 510 | 1 |  |  |  |
| address2 | nvarchar | 510 | 1 |  |  |  |
| city | nvarchar | 510 | 1 |  |  |  |
| state | nvarchar | 510 | 1 |  |  |  |
| zipCode | nvarchar | 40 | 1 |  |  |  |
| carrierRoute | nvarchar | 20 | 1 |  |  |  |

