# dbo.aba_lockinfo

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 | YES |  |  |
| last | bit | 1 | 0 |  |  |  |
| cnt | int | 4 | 0 |  |  |  |
| active | bit | 1 | 0 |  |  |  |
| spid | smallint | 2 | 0 |  |  |  |
| ecid | smallint | 2 | 0 |  |  |  |
| login | sysname | 256 | 1 |  |  |  |
| status | nvarchar | 60 | 1 |  |  |  |
| dbname | sysname | 256 | 1 |  |  |  |
| host | nvarchar | 256 | 1 |  |  |  |
| command | nvarchar | 32 | 1 |  |  |  |
| appl | nvarchar | 256 | 1 |  |  |  |
| opntrn | smallint | 2 | 1 |  |  |  |
| blking | smallint | 2 | 0 |  |  |  |
| blkby | smallint | 2 | 1 |  |  |  |
| blklvl | smallint | 2 | 0 |  |  |  |
| waittime | int | 4 | 1 |  |  |  |
| req_mode | tinyint | 1 | 1 |  |  |  |
| rsc_type | tinyint | 1 | 1 |  |  |  |
| req_status | tinyint | 1 | 1 |  |  |  |
| req_ownertype | smallint | 2 | 1 |  |  |  |
| refcnt | smallint | 2 | 1 |  |  |  |
| locktype | nvarchar | 60 | 0 |  |  |  |
| waittype | binary | 2 | 1 |  |  |  |
| lkdbid | smallint | 2 | 1 |  |  |  |
| lkobjid | int | 4 | 1 |  |  |  |
| lkindid | int | 4 | 1 |  |  |  |
| lkobj | nvarchar | 340 | 0 |  |  |  |
| restype | nvarchar | 40 | 0 |  |  |  |
| lkstatus | nvarchar | 40 | 0 |  |  |  |
| lkowntype | nvarchar | 10 | 0 |  |  |  |
| cpu | int | 4 | 1 |  |  |  |
| physio | int | 4 | 1 |  |  |  |
| memusage | int | 4 | 1 |  |  |  |
| now | char | 23 | 0 |  |  |  |
| login_time | char | 16 | 1 |  |  |  |
| last_batch | char | 16 | 1 |  |  |  |
| last_since | numeric | 9 | 1 |  |  |  |
| delay | int | 4 | 0 |  |  |  |
| inputbuffer | nchar | 510 | 0 |  |  |  |
| currentdate | datetime | 8 | 0 |  |  |  |
