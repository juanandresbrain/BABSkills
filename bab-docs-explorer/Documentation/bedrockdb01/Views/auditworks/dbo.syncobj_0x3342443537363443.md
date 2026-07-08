# dbo.syncobj_0x3342443537363443

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3342443537363443"]
    dbo_ORG_CAR_SHPMNT_MTHD_LANG(["dbo.ORG_CAR_SHPMNT_MTHD_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CAR_SHPMNT_MTHD_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3342443537363443]as select  [LANG_ID],[SHPMNT_MTHD_CODE],[SHPMNT_MTHD_DESC],[SHPMNT_MTHD_SHRT_DESC]  from  [dbo].[ORG_CAR_SHPMNT_MTHD_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CAR_SHPMNT_MTHD_LANG]', 'OBJECT', 'SELECT')= 1
```

