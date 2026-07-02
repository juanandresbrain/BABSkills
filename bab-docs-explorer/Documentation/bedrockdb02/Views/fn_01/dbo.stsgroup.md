# dbo.stsgroup

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.stsgroup"]
    dbo_FNDTN_SCRTY_NSB_GRP(["dbo.FNDTN_SCRTY_NSB_GRP"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_NSB_GRP |

## View Code

```sql
create view  dbo.stsgroup (group_id,group_name,group_description,group_sid,group_guid)
AS SELECT GRP_ID,GRP_NAME,GRP_DESC,GRP_SID,GRP_GUID
FROM dbo.FNDTN_SCRTY_NSB_GRP
```

