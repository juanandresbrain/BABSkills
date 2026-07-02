# dbo.FDS_REMOTE_REGISTRY

**Database:** FDS  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| REMOTE_ID | uniqueidentifier | 16 | 0 | YES |  |  |
| STATUS | char | 10 | 1 |  |  |  |
| HOST_NAME | char | 32 | 0 |  |  |  |
| LOCATION | char | 32 | 0 |  |  |  |
| IP_ADDR | char | 15 | 1 |  |  |  |
| SERVER | bit | 1 | 1 |  |  |  |
| LAST_UPDATED | datetime | 8 | 0 |  |  |  |
| REGISTER | bit | 1 | 1 |  |  |  |
| PARENT_HOST_NAME | char | 32 | 1 |  |  |  |
| PARENT_IP_ADDR | char | 15 | 1 |  |  |  |
| GROUP | char | 32 | 1 |  |  |  |
| SERVER_ORDER | smallint | 2 | 1 |  |  |  |

