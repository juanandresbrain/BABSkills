# dbo.syncobj_0x4231453642344341

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4231453642344341"]
    dbo_CLNDR_TMPLT_INSTNC_DFNTN(["dbo.CLNDR_TMPLT_INSTNC_DFNTN"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNDR_TMPLT_INSTNC_DFNTN |

## View Code

```sql
create view [dbo].[syncobj_0x4231453642344341]as select  [CLNDR_TMPLT_ID],[PRNT_CLNDR_LVL_TYPE_ID],[CHLD_CLNDR_LVL_TYPE_ID],[CLNDR_TMPLT_INSTNC_SEQ],[LBL_TEXT],[CHLD_CNT],[CHLD_CNT_ALGRTHM_ID]  from  [dbo].[CLNDR_TMPLT_INSTNC_DFNTN]  where HAS_PERMS_BY_NAME('[dbo].[CLNDR_TMPLT_INSTNC_DFNTN]', 'OBJECT', 'SELECT')= 1
```

