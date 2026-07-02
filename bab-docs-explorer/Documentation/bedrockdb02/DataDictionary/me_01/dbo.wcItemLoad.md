# dbo.wcItemLoad

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| UpdateDate | varchar | 10 | 1 |  |  |  |
| UpdateUserID | varchar | 4 | 1 |  |  |  |
| UpdatePID | varchar | 10 | 1 |  |  |  |
| ActionCode | varchar | 1 | 1 |  |  |  |
| Direction | varchar | 2 | 1 |  |  |  |
| InterfaceStatus | varchar | 3 | 1 |  |  |  |
| SKU | varchar | 10 | 1 |  |  |  |
| Facility | varchar | 2 | 1 |  |  |  |
| Class | varchar | 2 | 1 |  |  |  |
| InternalUse1 | varchar | 1 | 1 |  |  |  |
| InternalUse2 | varchar | 1 | 1 |  |  |  |
| InternalUse3 | varchar | 1 | 1 |  |  |  |
| Description1 | varchar | 50 | 1 |  |  |  |
| Description2 | varchar | 1 | 1 |  |  |  |
| UnitDesc | varchar | 2 | 1 |  |  |  |
| BulkDesc | varchar | 1 | 1 |  |  |  |
| BulkQty | varchar | 1 | 1 |  |  |  |
| InternalUse4 | varchar | 1 | 1 |  |  |  |
| InternalUse5 | varchar | 1 | 1 |  |  |  |
| InternalUse6 | varchar | 1 | 1 |  |  |  |
| Length | varchar | 1 | 1 |  |  |  |
| Width | varchar | 1 | 1 |  |  |  |
| Height | varchar | 1 | 1 |  |  |  |
| Cube | varchar | 1 | 1 |  |  |  |
| Weight | varchar | 1 | 1 |  |  |  |
| SerialTrack | varchar | 1 | 1 |  |  |  |
| LotTrack | varchar | 1 | 1 |  |  |  |
| ExpDateTrack | varchar | 1 | 1 |  |  |  |
| MfgDateTrack | varchar | 1 | 1 |  |  |  |
| HighQty | varchar | 1 | 1 |  |  |  |
| TieQty | varchar | 1 | 1 |  |  |  |
| ShippableUnit | varchar | 1 | 1 |  |  |  |
| AgeControl | varchar | 1 | 1 |  |  |  |
| InternalUse7 | varchar | 1 | 1 |  |  |  |
| InternalUse8 | varchar | 1 | 1 |  |  |  |
| InternalUse9 | varchar | 1 | 1 |  |  |  |
| NMFCode | varchar | 1 | 1 |  |  |  |
| InternalUse10 | varchar | 1 | 1 |  |  |  |
| InternalUse11 | varchar | 1 | 1 |  |  |  |
| InternalUse12 | varchar | 1 | 1 |  |  |  |
| InternalUse13 | varchar | 4 | 1 |  |  |  |
| AltPartNbr | varchar | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandising_Report_wcItemLoad](../../StoredProcedures/me_01/dbo.spMerchandising_Report_wcItemLoad.md)

