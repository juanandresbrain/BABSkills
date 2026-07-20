# dbo.web_order_outbound_integration_tracking

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShipDate | date | 3 | 1 |  |  |  |
| ShippedOrder | varchar | 8000 | 1 |  |  |  |
| isShipped | int | 4 | 1 |  |  |  |
| isShippedToday | int | 4 | 1 |  |  |  |
| isShippedBeforeToday | int | 4 | 1 |  |  |  |
| isUS | int | 4 | 1 |  |  |  |
| isUK | int | 4 | 1 |  |  |  |
| isShippedUS | int | 4 | 1 |  |  |  |
| isShippedUK | int | 4 | 1 |  |  |  |
| isInUSIntegration | int | 4 | 1 |  |  |  |
| isInUKIntegration | int | 4 | 1 |  |  |  |
| isWOPShipped | int | 4 | 1 |  |  |  |
| isOMSShipped | int | 4 | 1 |  |  |  |
| isOMSCancelled | int | 4 | 1 |  |  |  |
| isSettled | int | 4 | 1 |  |  |  |
| OMSCurrentStatus | varchar | 8000 | 1 |  |  |  |
| isSalesAuditShipped | int | 4 | 1 |  |  |  |
| isNotShippedInUSIntegration | int | 4 | 1 |  |  |  |
| isNotShippedInUKIntegration | int | 4 | 1 |  |  |  |
| isNotShippedInIntegration | int | 4 | 1 |  |  |  |
| isNotShippedInUSWebOrderProcessing | int | 4 | 1 |  |  |  |
| isNotShippedInUKWebOrderProcessing | int | 4 | 1 |  |  |  |
| isNotShippedInWebOrderProcessing | int | 4 | 1 |  |  |  |
| isNotShippedUSInOMS | int | 4 | 1 |  |  |  |
| isNotShippedUKInOMS | int | 4 | 1 |  |  |  |
| isNotShippedInOMS | int | 4 | 1 |  |  |  |
| isNotSettled | int | 4 | 1 |  |  |  |
| isNotInUSSalesAudit | int | 4 | 1 |  |  |  |
| isNotInUKSalesAudit | int | 4 | 1 |  |  |  |
| isNotInSalesAudit | int | 4 | 1 |  |  |  |
