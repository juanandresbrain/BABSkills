# dbo.syncobj_0x3346363137453331

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syncobj_0x3346363137453331"]
    dbo_ORG_CHN_FCLTY_CNTNR_TYPE_LANG(["dbo.ORG_CHN_FCLTY_CNTNR_TYPE_LANG"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_FCLTY_CNTNR_TYPE_LANG |

## View Code

```sql
create view [dbo].[syncobj_0x3346363137453331]as select  [CNTNR_TYPE_CODE],[LANG_ID],[CNTNR_TYPE_DESC],[CNTNR_TYPE_SHRT_DESC]  from  [dbo].[ORG_CHN_FCLTY_CNTNR_TYPE_LANG]  where HAS_PERMS_BY_NAME('[dbo].[ORG_CHN_FCLTY_CNTNR_TYPE_LANG]', 'OBJECT', 'SELECT')= 1
```

