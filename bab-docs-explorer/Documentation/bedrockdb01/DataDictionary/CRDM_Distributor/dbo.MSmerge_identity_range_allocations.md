# dbo.MSmerge_identity_range_allocations

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| publisher_id | smallint | 2 | 0 |  |  |  |
| publisher_db | sysname | 256 | 0 |  |  |  |
| publication | sysname | 256 | 0 |  |  |  |
| article | sysname | 256 | 0 |  |  |  |
| subscriber | sysname | 256 | 1 |  |  |  |
| subscriber_db | sysname | 256 | 1 |  |  |  |
| is_pub_range | bit | 1 | 0 |  |  |  |
| ranges_allocated | tinyint | 1 | 0 |  |  |  |
| range_begin | numeric | 17 | 1 |  |  |  |
| range_end | numeric | 17 | 1 |  |  |  |
| next_range_begin | numeric | 17 | 1 |  |  |  |
| next_range_end | numeric | 17 | 1 |  |  |  |
| max_used | numeric | 17 | 0 |  |  |  |
| time_of_allocation | datetime | 8 | 1 |  |  |  |
