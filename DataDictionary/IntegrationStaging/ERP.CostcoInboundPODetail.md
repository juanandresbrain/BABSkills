# ERP.CostcoInboundPODetail

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PurchaseOrderID | int | 4 | 1 |  |  |  |
| CUSTOMERREQUISITIONNUMBER | varchar | 50 | 1 |  |  |  |
| CUSTOMERSLINENUMBER | int | 4 | 1 |  |  |  |
| ITEMNUMBER | varchar | 7 | 1 |  |  |  |
| ORDEREDSALESQUANTITY | numeric | 5 | 1 |  |  |  |
| SALESPRICE | numeric | 5 | 1 |  |  |  |
| SALESUNITSYMBOL | varchar | 50 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ERP.spMergeCostcoInboundPODetail](../../StoredProcedures/IntegrationStaging/ERP.spMergeCostcoInboundPODetail.md)
- [IntegrationStaging: ERP.spOutputCostcoPOxml](../../StoredProcedures/IntegrationStaging/ERP.spOutputCostcoPOxml.md)

