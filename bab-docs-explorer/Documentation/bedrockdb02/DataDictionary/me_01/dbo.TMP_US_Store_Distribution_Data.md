# dbo.TMP_US_Store_Distribution_Data_

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Store | varchar | 20 | 0 |  |  |  |
| RecTypeLabel | nvarchar | 510 | 1 |  |  |  |
| StyleCode | varchar | 20 | 0 |  |  |  |
| StyleShortDescription | varchar | 20 | 1 |  |  |  |
| Quantity | int | 4 | 1 |  |  |  |
| Category | varchar | 40 | 0 |  |  |  |
| Type | varchar | 8 | 0 |  |  |  |
| custom_property_value | varchar | 30 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |

