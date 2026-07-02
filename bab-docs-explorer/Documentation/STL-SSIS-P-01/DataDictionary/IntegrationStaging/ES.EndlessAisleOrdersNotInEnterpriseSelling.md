# ES.EndlessAisleOrdersNotInEnterpriseSelling

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 128 | 0 |  |  |  |
| orig_sequence_number | int | 4 | 1 |  |  |  |
| create_time | datetime | 8 | 1 |  |  |  |
| BusinessDate | date | 3 | 1 |  |  |  |
| StoreNumber | varchar | 128 | 1 |  |  |  |
| EnterpriseSellingID | varchar | 20 | 1 |  |  |  |
| total | numeric | 9 | 1 |  |  |  |
| subtotal | numeric | 9 | 1 |  |  |  |
| tax_total | numeric | 9 | 1 |  |  |  |
| discount_total | numeric | 9 | 1 |  |  |  |
| line_item_count | int | 4 | 1 |  |  |  |
| order_status_code | varchar | 128 | 1 |  |  |  |
| order_type_code | varchar | 128 | 1 |  |  |  |
| amount_due | numeric | 9 | 1 |  |  |  |
| ReferenceNumber | varchar | 50 | 1 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| device_id | varchar | 128 | 1 |  |  |  |
| AlertDate | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: ES.spGetEndlessAisleOrdersNotInEsell](../../StoredProcedures/IntegrationStaging/ES.spGetEndlessAisleOrdersNotInEsell.md)

