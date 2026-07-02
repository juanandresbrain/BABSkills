# dbo.tmpDMTProd

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| ean | nvarchar | -1 | 1 |  |  |  |
| upc | nvarchar | -1 | 1 |  |  |  |
| unit | nvarchar | -1 | 1 |  |  |  |
| min-order-quantity | nvarchar | 100 | 1 |  |  |  |
| step-quantity | nvarchar | 100 | 1 |  |  |  |
| store-force-price-flag | nvarchar | 100 | 1 |  |  |  |
| store-non-inventory-flag | nvarchar | 100 | 1 |  |  |  |
| store-non-revenue-flag | nvarchar | 100 | 1 |  |  |  |
| store-non-discountable-flag | nvarchar | 100 | 1 |  |  |  |
| available-flag | nvarchar | 100 | 1 |  |  |  |
| tax-class-id | nvarchar | 100 | 1 |  |  |  |
| sitemap-included-flag | nvarchar | 100 | 1 |  |  |  |
| unit-quantity | nvarchar | 100 | 1 |  |  |  |
| sitemap-changefrequency | nvarchar | 100 | 1 |  |  |  |
| sitemap-priority | nvarchar | 100 | 1 |  |  |  |
| thumbnail | nvarchar | 100 | 1 |  |  |  |
| image | nvarchar | 8000 | 1 |  |  |  |

