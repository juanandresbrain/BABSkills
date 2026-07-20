# dbo.integrationstaging_wms_cartonssummarytoha

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| shipmentId | varchar | 8000 | 1 |  |  |  |
| deliveryName | varchar | 8000 | 1 |  |  |  |
| street | varchar | 8000 | 1 |  |  |  |
| city | varchar | 8000 | 1 |  |  |  |
| state | varchar | 8000 | 1 |  |  |  |
| zip | varchar | 8000 | 1 |  |  |  |
| country | varchar | 8000 | 1 |  |  |  |
| shipCarrier | varchar | 8000 | 1 |  |  |  |
| modeOfDelivery | varchar | 8000 | 1 |  |  |  |
| waveId | varchar | 8000 | 1 |  |  |  |
| containerId | varchar | 8000 | 1 |  |  |  |
| grossWeight | float | 8 | 1 |  |  |  |
| length | float | 8 | 1 |  |  |  |
| width | float | 8 | 1 |  |  |  |
| height | float | 8 | 1 |  |  |  |
| shipTo | varchar | 8000 | 1 |  |  |  |
| warehouse | varchar | 8000 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| deliveryDescription | varchar | 8000 | 1 |  |  |  |
| totalQuantityContainer | varchar | 8000 | 1 |  |  |  |
| itemNumber | varchar | 8000 | 1 |  |  |  |
| totalQuantity | varchar | 8000 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| CustomerAccount | varchar | 8000 | 1 |  |  |  |
| AptosDistroNumber | varchar | 8000 | 1 |  |  |  |
| MessageDateUTC | datetime2 | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| SentToHa | datetime2 | 8 | 1 |  |  |  |
