# dbo.DiscountFactsReferenceDynamicsStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | datetime | 8 | 1 |  |  |  |
| transaction_id | numeric | 9 | 1 |  |  |  |
| line_id | numeric | 5 | 1 |  |  |  |
| line_sequence | numeric | 5 | 1 |  |  |  |
| SumDiscAmount | numeric | 17 | 1 |  |  |  |
| line_object | smallint | 2 | 1 |  |  |  |
| line_object_description | nvarchar | 510 | 1 |  |  |  |
| line_object_type | tinyint | 1 | 1 |  |  |  |
| object_type_display_descr | nvarchar | 510 | 1 |  |  |  |
| DiscountType | varchar | 20 | 1 |  |  |  |
| LineAction | tinyint | 1 | 1 |  |  |  |
