# dbo.custom_property

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| custom_property_id | decimal | 9 | 0 | YES |  |  |
| cust_prop_code | nvarchar | 12 | 0 |  |  |  |
| cust_prop_label | nvarchar | 60 | 0 |  |  |  |
| property_type | smallint | 2 | 0 |  |  |  |
| entity_type | smallint | 2 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.spMerchandisingDistroImportValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportValidation.md)
- [me_01: dbo.spMerchandisingOutputBaleCondo](../../StoredProcedures/me_01/dbo.spMerchandisingOutputBaleCondo.md)
- [me_01: dbo.spMerchandisingOutputCNTransfers](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNTransfers.md)
- [me_01: dbo.spMerchandisingSelectPoolPointTransfer](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPoolPointTransfer.md)
- [me_01: dbo.spMerchandisingSelectRpacPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO.md)
- [me_01: dbo.spMerchandisingSelectRpacPO_BAK_02282018](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO_BAK_02282018.md)
- [me_01: dbo.spPBISelectProductCatalogMasterAttributes](../../StoredProcedures/me_01/dbo.spPBISelectProductCatalogMasterAttributes.md)
- [me_01: dbo.spPOSSelectProductCatalogMasterAttributes](../../StoredProcedures/me_01/dbo.spPOSSelectProductCatalogMasterAttributes.md)
- [me_01: dbo.spPOSSelectProductCatalogMasterAttributes_BACKUP20240313](../../StoredProcedures/me_01/dbo.spPOSSelectProductCatalogMasterAttributes_BACKUP20240313.md)
- [me_01: dbo.spWEBSelectProductCatalogMasterAttributes](../../StoredProcedures/me_01/dbo.spWEBSelectProductCatalogMasterAttributes.md)
- [me_01: dbo.spWEBSelectProductCatalogMasterAttributes_BackUp20221101](../../StoredProcedures/me_01/dbo.spWEBSelectProductCatalogMasterAttributes_BackUp20221101.md)
- [me_01: dbo.spWEBSelectProductCatalogMasterAttributes_backup20221102](../../StoredProcedures/me_01/dbo.spWEBSelectProductCatalogMasterAttributes_backup20221102.md)
- [me_01: dbo.spWEBSelectProductCatalogMasterAttributesBAK20171005](../../StoredProcedures/me_01/dbo.spWEBSelectProductCatalogMasterAttributesBAK20171005.md)

