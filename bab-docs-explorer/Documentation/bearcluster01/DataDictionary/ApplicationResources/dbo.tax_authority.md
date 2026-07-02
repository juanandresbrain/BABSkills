# dbo.tax_authority

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | smallint | 2 | 1 |  |  |  |
| auth_name | nvarchar | 100 | 1 |  |  |  |
| auth_type_name | nvarchar | 100 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ApplicationResources: dbo.sp_GetJumpMindStateExists](../../StoredProcedures/ApplicationResources/dbo.sp_GetJumpMindStateExists.md)
- [ApplicationResources: dbo.sp_GetJumpMindTaxState](../../StoredProcedures/ApplicationResources/dbo.sp_GetJumpMindTaxState.md)

