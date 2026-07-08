# dbo.syncobj_0x4134324634314139

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x4134324634314139"]
    dbo_ORG_CHN_STR_TRAY_LANG(["dbo.ORG_CHN_STR_TRAY_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_STR_TRAY_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x4134324634314139]as select  [TRAY_ID],[LANG_ID],[TRAY_DESC]  from  [dbo].[ORG_CHN_STR_TRAY_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_STR_TRAY_LANG]', 'OBJECT', 'SELECT')= 1
```

