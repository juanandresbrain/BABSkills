# dbo.PostGresDiscountFactsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transactionkey | nvarchar | 510 | 1 |  |  |  |
| device_id | varchar | 128 | 1 |  |  |  |
| storeid | int | 4 | 1 |  |  |  |
| business_date | datetime | 8 | 1 |  |  |  |
| transactionnumber | int | 4 | 1 |  |  |  |
| registernumber | int | 4 | 1 |  |  |  |
| barcode | varchar | 128 | 1 |  |  |  |
| entity | nvarchar | 510 | 1 |  |  |  |
| promotion_id | varchar | 128 | 1 |  |  |  |
| campaignId | varchar | 128 | 1 |  |  |  |
| description | varchar | 128 | 1 |  |  |  |
| discountamount | numeric | 9 | 1 |  |  |  |
| loyaltycertificateid | varchar | 128 | 1 |  |  |  |
