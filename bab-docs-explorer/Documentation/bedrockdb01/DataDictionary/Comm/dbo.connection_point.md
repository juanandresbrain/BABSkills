# dbo.connection_point

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| connection_point_id | int | 4 | 0 | YES |  |  |
| location_id | int | 4 | 0 |  |  |  |
| device_id | int | 4 | 0 |  |  |  |
| application_id | int | 4 | 0 |  |  |  |
| ip_address | nvarchar | 510 | 1 |  |  |  |
| ip_port | int | 4 | 1 |  |  |  |
| channel_type | int | 4 | 0 |  |  |  |
| port_type | int | 4 | 0 |  |  |  |
| authentication_timeout | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| url | nvarchar | 510 | 0 |  |  |  |
| DLL_NAME | varchar | 255 | 0 |  |  |  |
| CLS_NAME | varchar | 255 | 0 |  |  |  |
| USER_ID | nvarchar | 100 | 0 |  |  |  |
| PSWRD | nvarchar | 100 | 0 |  |  |  |
| IS_PRXY | tinyint | 1 | 0 |  |  |  |
| PRXY_ATHNTCTN | tinyint | 1 | 0 |  |  |  |
| USE_SSN_ID | tinyint | 1 | 0 |  |  |  |
| BCKP_IP_ADRS | nvarchar | 510 | 0 |  |  |  |
| BCKP_IP_PORT | int | 4 | 0 |  |  |  |
