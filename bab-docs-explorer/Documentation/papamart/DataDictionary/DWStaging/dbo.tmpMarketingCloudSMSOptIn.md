# dbo.tmpMarketingCloudSMSOptIn

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customer-no | nvarchar | 100 | 1 |  |  |  |
| email | nvarchar | 510 | 1 |  |  |  |
| country-code | nvarchar | 100 | 1 |  |  |  |
| first-name | nvarchar | -1 | 1 |  |  |  |
| last-name | nvarchar | -1 | 1 |  |  |  |
| address1 | nvarchar | 510 | 1 |  |  |  |
| address2 | nvarchar | -1 | 1 |  |  |  |
| city | nvarchar | 200 | 1 |  |  |  |
| state-code | nvarchar | -1 | 1 |  |  |  |
| postal-code | nvarchar | -1 | 1 |  |  |  |
| _RowIndex_Customer | bigint | 8 | 1 |  |  |  |
| _RowIndex_Address | bigint | 8 | 1 |  |  |  |
| phone-mobile | nvarchar | -1 | 1 |  |  |  |
| phone-home | nvarchar | -1 | 1 |  |  |  |
| phone-business | nvarchar | -1 | 1 |  |  |  |
