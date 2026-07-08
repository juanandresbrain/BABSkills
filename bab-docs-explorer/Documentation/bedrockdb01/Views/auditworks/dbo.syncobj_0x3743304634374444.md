# dbo.syncobj_0x3743304634374444

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3743304634374444"]
    dbo_ORG_CHN_HRCHY_LVL_GRP_A(["dbo.ORG_CHN_HRCHY_LVL_GRP_A"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_HRCHY_LVL_GRP_A |

## View Code

```sql
create view [dbo].[syncobj_0x3743304634374444]as select  [HRCHY_LVL_GRP_ID],[ORG_CHN_NUM],[HRCHY_LVL_ID],[HRCHY_ID],[VRTL],[FDN_CSTMZTN_DATA]  from  [dbo].[ORG_CHN_HRCHY_LVL_GRP_A]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_HRCHY_LVL_GRP_A]', 'OBJECT', 'SELECT')= 1
```

