# dbo.address

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| address_id | decimal | 9 | 0 | YES |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| parent_type | smallint | 2 | 0 |  |  |  |
| address_type_id | smallint | 2 | 0 |  |  |  |
| address_name | nvarchar | 120 | 0 |  |  |  |
| address_line1 | nvarchar | 100 | 0 |  |  |  |
| address_line2 | nvarchar | 100 | 1 |  |  |  |
| address_city | nvarchar | 40 | 1 |  |  |  |
| address_state | nvarchar | 40 | 1 |  |  |  |
| address_zip_code | nvarchar | 30 | 1 |  |  |  |
| country_id | decimal | 9 | 0 |  |  |  |
| address_email | nvarchar | 120 | 1 |  |  |  |
| document_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.rpt_get_address_for_po_$sp](../../StoredProcedures/me_01/dbo.rpt_get_address_for_po_$sp.md)
- [me_01: dbo.spBABW_GoogleGetValidLocationList](../../StoredProcedures/me_01/dbo.spBABW_GoogleGetValidLocationList.md)
- [me_01: dbo.spMerchandisingSelectCBRSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCBRSummary.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CN](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CN.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CNBAK20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CNBAK20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CNWIP20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CNWIP20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributions](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributions.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsBAK20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsBAK20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsWIP20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsWIP20220406.md)
- [me_01: dbo.spMerchandisingSelectUKCartonSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectUKCartonSummary.md)

