# Azure.POHeader

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_no | varchar | 20 | 0 |  |  |  |
| po_description | varchar | 60 | 1 |  |  |  |
| CreateDate | date | 3 | 1 |  |  |  |
| FreightOnBoard | varchar | 20 | 1 |  |  |  |
| PoAttributeCode | varchar | 6 | 1 |  |  |  |
| PoAttributeLabel | varchar | 30 | 1 |  |  |  |
| TotalFirstCost | numeric | 17 | 1 |  |  |  |
| VendorCode | varchar | 20 | 0 |  |  |  |
| VendorName | varchar | 50 | 0 |  |  |  |
| LocationCode | varchar | 20 | 1 |  |  |  |
