# ES.ESToOMSShippingMethodBridge

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ShippingMethodBridgeID | int | 4 | 0 | YES |  |  |
| ESShipMethodCode | varchar | 4 | 0 |  |  |  |
| ESPOSDescription | varchar | 255 | 0 |  |  |  |
| ESDescription | varchar | 255 | 0 |  |  |  |
| ESPrice | decimal | 5 | 1 |  |  |  |
| OMSShipMethod | varchar | 4 | 0 |  |  |  |
| OMSDescription | varchar | 255 | 0 |  |  |  |

