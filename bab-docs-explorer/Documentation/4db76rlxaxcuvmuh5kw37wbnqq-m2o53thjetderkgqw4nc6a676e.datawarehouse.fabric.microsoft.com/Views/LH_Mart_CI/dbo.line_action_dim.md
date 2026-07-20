# dbo.line_action_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.line_action_dim"]
    dbo_line_action_dim(["dbo.line_action_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.line_action_dim |

## View Code

```sql
;

CREATE VIEW dbo.line_action_dim AS SELECT Line_Action_Key, Line_Action, Line_Action_Description COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Line_Action_Description, INS_DT, UPDT_DT FROM LH_Mart.dbo.line_action_dim;
```

