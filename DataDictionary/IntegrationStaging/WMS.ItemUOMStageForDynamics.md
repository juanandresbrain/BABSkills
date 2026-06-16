# WMS.ItemUOMStageForDynamics

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | nvarchar | 40 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| FromUnitSymbol | varchar | 2 | 1 |  |  |  |
| ToUnitSymbol | varchar | 4 | 1 |  |  |  |
| Denominator | int | 4 | 1 |  |  |  |
| Factor | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spQueryItemCreateEcoResProductSpecificUOMXML](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateEcoResProductSpecificUOMXML.md)
- [IntegrationStaging: WMS.spQueryItemCreateXMLBAK20230327](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateXMLBAK20230327.md)
- [IntegrationStaging: WMS.spQueryItemCreateXMLBAK20231113](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateXMLBAK20231113.md)
- [IntegrationStaging: WMS.spQueryItemCreateXMLPreRetailInventory20221027](../../StoredProcedures/IntegrationStaging/WMS.spQueryItemCreateXMLPreRetailInventory20221027.md)

