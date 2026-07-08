# dbo.syncobj_0x4442464636374534

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4442464636374534"]
    dbo_ORG_CHN_HRCHY_LVL(["dbo.ORG_CHN_HRCHY_LVL"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_HRCHY_LVL |

## View Code

```sql
create view [dbo].[syncobj_0x4442464636374534]as select  [HRCHY_LVL_ID],[HRCHY_LVL_DESC],[SEQ_NUM],[AFLTN_PRMTD],[HRCHY_ID],[PRNT_HRCHY_LVL_ID],[ACTV],[GRP_CODE_MSK]  from  [dbo].[ORG_CHN_HRCHY_LVL]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_HRCHY_LVL]', 'OBJECT', 'SELECT')= 1
```

