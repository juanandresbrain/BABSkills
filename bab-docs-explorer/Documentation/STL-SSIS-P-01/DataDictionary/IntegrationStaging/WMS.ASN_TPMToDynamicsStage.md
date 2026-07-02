# WMS.ASN_TPMToDynamicsStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| shipment | nvarchar | 30 | 1 |  |  |  |
| lpn | nvarchar | 40 | 1 |  |  |  |
| ItemId | nvarchar | 50 | 1 |  |  |  |
| PO_nbr | nvarchar | 50 | 1 |  |  |  |
| Po_Shipment_Line_nbr | numeric | 9 | 1 |  |  |  |
| Qty | numeric | 9 | 1 |  |  |  |
| Unit | varchar | 10 | 1 |  |  |  |
| Vehicle | nvarchar | 200 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeASN_TPMToDynamics](../../StoredProcedures/IntegrationStaging/WMS.spMergeASN_TPMToDynamics.md)
- [IntegrationStaging: WMS.spMergeASN_TPMToDynamics_Bak20231208](../../StoredProcedures/IntegrationStaging/WMS.spMergeASN_TPMToDynamics_Bak20231208.md)

