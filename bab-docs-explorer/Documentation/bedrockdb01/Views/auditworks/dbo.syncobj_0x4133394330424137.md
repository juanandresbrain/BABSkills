# dbo.syncobj_0x4133394330424137

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4133394330424137"]
    dbo_ORG_CHN_LOC_HRCHY_LVL_GRP(["dbo.ORG_CHN_LOC_HRCHY_LVL_GRP"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_LOC_HRCHY_LVL_GRP |

## View Code

```sql
create view [dbo].[syncobj_0x4133394330424137]as select  [HRCHY_LVL_GRP_ID],[HRCHY_LVL_GRP_DESC],[GRP_MBR_CHNG],[HRCHY_LVL_ID],[HRCHY_ID],[PRNT_HRCHY_LVL_GRP_ID]  from  [dbo].[ORG_CHN_LOC_HRCHY_LVL_GRP]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_LOC_HRCHY_LVL_GRP]', 'OBJECT', 'SELECT')= 1
```

