# dbo.MSpublicationthresholds

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publication_id | int | 4 | 0 |  |  |  |
| metric_id | int | 4 | 0 |  |  |  |
| value | sql_variant | 8016 | 1 |  |  |  |
| shouldalert | bit | 1 | 0 |  |  |  |
| isenabled | bit | 1 | 0 |  |  |  |
