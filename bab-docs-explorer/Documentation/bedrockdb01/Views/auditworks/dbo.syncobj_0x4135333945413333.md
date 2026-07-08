# dbo.syncobj_0x4135333945413333

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4135333945413333"]
    dbo_ORG_CHN_LOC_FNCTN_LANG(["dbo.ORG_CHN_LOC_FNCTN_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_LOC_FNCTN_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x4135333945413333]as select  [FNCTN_NUM],[LANG_ID],[FNCTN_DESC],[FNCTN_SHRT_DESC]  from  [dbo].[ORG_CHN_LOC_FNCTN_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_LOC_FNCTN_LANG]', 'OBJECT', 'SELECT')= 1
```

