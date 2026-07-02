# dbo.factory_address

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| attribute_set_code | nvarchar | 510 | 1 |  |  |  |
| address_name | nvarchar | 510 | 1 |  |  |  |
| port | nvarchar | 510 | 1 |  |  |  |
| vendor_code | nvarchar | 510 | 1 |  |  |  |
| address | nvarchar | 510 | 1 |  |  |  |
| city | nvarchar | 510 | 1 |  |  |  |
| province | nvarchar | 510 | 1 |  |  |  |
| country | nvarchar | 4 | 1 |  |  |  |
| phone_number | nvarchar | 510 | 1 |  |  |  |
| container_stuffing | nvarchar | 510 | 1 |  |  |  |
| mod_date | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702.md)
- [me_01: dbo.spMerchandisingOutputItemMasterHTS](../../StoredProcedures/me_01/dbo.spMerchandisingOutputItemMasterHTS.md)
- [me_01: dbo.spMerchandisingSelectRpacPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO.md)
- [me_01: dbo.spMerchandisingSelectRpacPO_BAK_02282018](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO_BAK_02282018.md)

