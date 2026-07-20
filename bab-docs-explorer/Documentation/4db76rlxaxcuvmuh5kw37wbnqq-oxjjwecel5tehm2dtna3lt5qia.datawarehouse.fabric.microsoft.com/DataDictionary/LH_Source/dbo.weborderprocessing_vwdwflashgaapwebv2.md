# dbo.weborderprocessing_vwdwflashgaapwebv2

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| TransactionDate | datetime2 | 8 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| FulfillmentLocation | varchar | 8000 | 1 |  |  |  |
| FulfillmentLocationName | varchar | 8000 | 1 |  |  |  |
| TransactionType | varchar | 8000 | 1 |  |  |  |
| Tax | decimal | 17 | 1 |  |  |  |
| TransactionAmount | decimal | 9 | 1 |  |  |  |
| UnitAmount | int | 4 | 1 |  |  |  |
| FlashGaapSales | decimal | 17 | 1 |  |  |  |
| isBOSISorBOPIS | int | 4 | 1 |  |  |  |
| ReturnsRegister | int | 4 | 1 |  |  |  |
