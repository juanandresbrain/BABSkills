# dbo.tmpPFTStyleRollingCountsAndAttributes

**Database:** DBAUtility  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Style Code | nvarchar | 40 | 1 |  |  |  |
| Style Long Desc | nvarchar | 240 | 1 |  |  |  |
| Sub-Class Code | nvarchar | 40 | 1 |  |  |  |
| Sub-Class Label | nvarchar | 80 | 1 |  |  |  |
| NUMBER OF UNITS PER PACK | nvarchar | 60 | 1 |  |  |  |
| Style Last PO Cost | decimal | 9 | 1 |  |  |  |
| BOP OH WH Units:InvStatus[Available] ( 1 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 2 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 3 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 4 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 5 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 6 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 7 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 8 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 9 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 10 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 11 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus  ( 12 Periods(s) Ago ) | int | 4 | 1 |  |  |  |
| BOP OH WH Units:InvStatus[Available] ( This Period ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 1 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 2 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 3 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 4 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 5 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 6 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 7 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 8 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 9 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 10 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 11 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( 12 Period(s) Ago ) | int | 4 | 1 |  |  |  |
| Net Receipts Units ( This Period ) | int | 4 | 1 |  |  |  |
| On Order Units ( Last 3 Period(s) ) | int | 4 | 1 |  |  |  |
| On Order Units ( This Period ) | int | 4 | 1 |  |  |  |
| On Order Units ( Next 1 Periods ) | int | 4 | 1 |  |  |  |
| On Order Units ( Next 2 Periods ) | int | 4 | 1 |  |  |  |
| On Order Units ( Next 3 Periods ) | int | 4 | 1 |  |  |  |
| On Order Units ( Next 4 Periods ) | int | 4 | 1 |  |  |  |
| On Order Units ( Next 5 Periods ) | int | 4 | 1 |  |  |  |
| On Order Units ( Next 6 Periods ) | int | 4 | 1 |  |  |  |
| EOP OH WH Units:InvStatus[Available] ( Current ) | int | 4 | 1 |  |  |  |
| Style Custom Property Value O[SUPPLY STYLE CATEGORY] | nvarchar | 60 | 1 |  |  |  |
| Style Attribute Set Code O[MEG'S INVENTOR STATUS BY STYLE] | nvarchar | 12 | 1 |  |  |  |
| EOP OH Cost:Total ( Current ) | decimal | 17 | 1 |  |  |  |
| Style Custom Property Value O[OUT DATE] | nvarchar | 60 | 1 |  |  |  |
| Style Attribute Set Label O[FACTORY] | nvarchar | 60 | 1 |  |  |  |
| Merchandising Style_ID | decimal | 9 | 1 |  |  |  |
| JurisdictionCode | varchar | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [DBAUtility: dbo.spPFTGetOpenToByRollingCountsAndAttributes](../../StoredProcedures/DBAUtility/dbo.spPFTGetOpenToByRollingCountsAndAttributes.md)

