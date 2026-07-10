# dbo.SerializedVoucherStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SerializedNumber | bigint | 8 | 1 |  |  |  |
| StartDate | date | 3 | 1 |  |  |  |
| DiscountAmount | numeric | 5 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| Email | varchar | 255 | 1 |  |  |  |
| ExpirationDate | date | 3 | 1 |  |  |  |
| FirstName | varchar | 255 | 1 |  |  |  |
| LastName | varchar | 255 | 1 |  |  |  |
| Address1 | varchar | 255 | 1 |  |  |  |
| Address2 | varchar | 255 | 1 |  |  |  |
| City | varchar | 255 | 1 |  |  |  |
| State | varchar | 255 | 1 |  |  |  |
| ZipCode | varchar | 20 | 1 |  |  |  |
| Country | varchar | 255 | 1 |  |  |  |
| CouponID | int | 4 | 1 |  |  |  |
| Description | nvarchar | 200 | 1 |  |  |  |
| Status | nvarchar | 510 | 1 |  |  |  |
| title | nvarchar | 20 | 1 |  |  |  |
