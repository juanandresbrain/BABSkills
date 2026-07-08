# dbo.nt_map

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.nt_map"]
    dbo_FNDTN_SCRTY_NT_MAP(["dbo.FNDTN_SCRTY_NT_MAP"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_NT_MAP |

## View Code

```sql
CREATE VIEW dbo.nt_map (user_id,computer_name,instance,app_id,comp_id,ackey,nt_map_data,time_stamp)
AS SELECT USER_ID,CMPTR_NAME,INSTNC,APP_ID,CMPNY_ID,ACS_KEY,NT_MAP_DATA,TIME_STMP
FROM dbo.FNDTN_SCRTY_NT_MAP
```

