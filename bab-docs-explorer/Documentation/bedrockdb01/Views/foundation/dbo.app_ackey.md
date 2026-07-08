# dbo.app_ackey

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.app_ackey"]
    dbo_FNDTN_SCRTY_APP_ACS_KEY(["dbo.FNDTN_SCRTY_APP_ACS_KEY"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FNDTN_SCRTY_APP_ACS_KEY |

## View Code

```sql
CREATE VIEW dbo.app_ackey (app_id,ackey, ackey_level, ackey_display_order,ackey_name, ackey_description,  
ackey_data_flag, ackey_data_mask, ackey_data_cliptext, ackey_data_multivalue)
AS SELECT APP_ID,ACS_KEY,ACS_KEY_LVL,ACS_KEY_DSPLY_ORDR,ACS_KEY_NAME, ACS_KEY_DESC, 
ACS_KEY_DATA, ACS_KEY_DATA_MASK,ACS_KEY_DATA_CLIP_TEXT,ACS_KEY_DATA_MLTI_VAL
FROM dbo.FNDTN_SCRTY_APP_ACS_KEY
```

