# dbo.azure_weborders_ssk

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SourceSite | varchar | 8000 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| OrderNum | varchar | 8000 | 1 |  |  |  |
| OrderDate | date | 3 | 1 |  |  |  |
| ShippingAmount | decimal | 9 | 1 |  |  |  |
| OrderStatus | varchar | 8000 | 1 |  |  |  |
| StatusDate | datetime2 | 8 | 1 |  |  |  |
| Physical | varchar | 8000 | 1 |  |  |  |
| StatusSortOrder | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| ShipToPostalCode | varchar | 8000 | 1 |  |  |  |
| ShipToState | varchar | 8000 | 1 |  |  |  |
| ShipToCountry | varchar | 8000 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| ESFlag | int | 4 | 1 |  |  |  |
