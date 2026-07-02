# ERP.CostcoInboundPOHeaderStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderID | int | 4 | 1 |  |  |  |
| CUSTOMERREQUISITIONNUMBER | varchar | 50 | 1 |  |  |  |
| CUSTOMERSORDERREFERENCE | varchar | 50 | 1 |  |  |  |
| INVOICECUSTOMERACCOUNTNUMBER | varchar | 20 | 1 |  |  |  |
| ORDERINGCUSTOMERACCOUNTNUMBER | varchar | 20 | 1 |  |  |  |
| REQUESTEDSHIPPINGDATE | date | 3 | 1 |  |  |  |
| DELIVERYADDRESSDESCRIPTION | varchar | 50 | 1 |  |  |  |
| DELIVERYADDRESSNAME | varchar | 50 | 1 |  |  |  |
| DELIVERYADDRESSSTREET | varchar | 50 | 1 |  |  |  |
| DELIVERYADDRESSCITY | varchar | 50 | 1 |  |  |  |
| DELIVERYADDRESSSTATEID | varchar | 50 | 1 |  |  |  |
| DELIVERYADDRESSZIPCODE | varchar | 50 | 1 |  |  |  |
| DELIVERYADDRESSCOUNTRYREGIONID | varchar | 5 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergeCostcoInboundPOHeader](../../StoredProcedures/IntegrationStaging/ERP.spMergeCostcoInboundPOHeader.md)

