# Azure.vwDynamicsPOReceiptVarianceVsAptos

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwDynamicsPOReceiptVarianceVsAptos"]
    Azure_DynamicsPOReceiptVariances(["Azure.DynamicsPOReceiptVariances"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.DynamicsPOReceiptVariances |

## View Code

```sql
CREATE view [Azure].[vwDynamicsPOReceiptVarianceVsAptos]

as


select [ReceiptDate],[PurchaseOrderNumber],[ItemNumber],[ProductDescription],[Quantity],[AptosReceiptQty],[VarianceQty],[ReceivingWarehouseID]
from Azure.DynamicsPOReceiptVariances with (nolock)
```

