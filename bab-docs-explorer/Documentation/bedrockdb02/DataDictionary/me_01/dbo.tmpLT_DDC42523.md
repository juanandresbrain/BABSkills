# dbo.tmpLT_DDC42523

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| document_no | nvarchar | 40 | 0 |  |  |  |
| ToLocation | nvarchar | 40 | 0 |  |  |  |
| FromWarehouse | nvarchar | 40 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| distribution_no | nvarchar | 40 | 0 |  |  |  |
| carton_no | nvarchar | 40 | 1 |  |  |  |
| SumUnitsSentAptos | int | 4 | 1 |  |  |  |
| SumUnitsReceivedAptos | int | 4 | 1 |  |  |  |
| ERP | smalldatetime | 4 | 1 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| RawInsertDAte | datetime | 8 | 1 |  |  |  |
| SumRawShippedQty | int | 4 | 1 |  |  |  |
| RawRowCountForGrouping | int | 4 | 1 |  |  |  |
| variance | int | 4 | 1 |  |  |  |

