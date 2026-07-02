# dbo.POSProductHardLaunchItems

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StyleCode | varchar | 6 | 1 |  |  |  |
| CountryCode | varchar | 10 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMergePOSProductHardLaunchItems](../../StoredProcedures/me_01/dbo.spMergePOSProductHardLaunchItems.md)
- [me_01: dbo.spMergePOSProductHardLaunchItems_BAK20231018](../../StoredProcedures/me_01/dbo.spMergePOSProductHardLaunchItems_BAK20231018.md)

