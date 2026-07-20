# dbo.serializedvoucher

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SerializedNumber | bigint | 8 | 1 |  |  |  |
| StartDate | date | 3 | 1 |  |  |  |
| DiscountAmount | decimal | 5 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| Email | varchar | 8000 | 1 |  |  |  |
| ExpirationDate | date | 3 | 1 |  |  |  |
| isExported | bit | 1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| FirstName | varchar | 8000 | 1 |  |  |  |
| LastName | varchar | 8000 | 1 |  |  |  |
| Address1 | varchar | 8000 | 1 |  |  |  |
| Address2 | varchar | 8000 | 1 |  |  |  |
| City | varchar | 8000 | 1 |  |  |  |
| State | varchar | 8000 | 1 |  |  |  |
| ZipCode | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| ExportedDate | datetime2 | 8 | 1 |  |  |  |
| ExportedDateXML | datetime2 | 8 | 1 |  |  |  |
| CouponID | int | 4 | 1 |  |  |  |
| Description | varchar | 8000 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
| title | varchar | 8000 | 1 |  |  |  |
