# dbo.MStracer_tokens

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tracer_id | int | 4 | 0 | YES |  |  |
| publication_id | int | 4 | 0 |  |  |  |
| publisher_commit | datetime | 8 | 0 |  |  |  |
| distributor_commit | datetime | 8 | 1 |  |  |  |
