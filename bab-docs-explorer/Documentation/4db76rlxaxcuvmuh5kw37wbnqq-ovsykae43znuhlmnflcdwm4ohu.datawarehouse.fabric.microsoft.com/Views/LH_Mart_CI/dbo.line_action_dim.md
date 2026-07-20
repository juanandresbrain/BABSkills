# dbo.line_action_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
; CREATE   VIEW [dbo].[line_action_dim] AS     SELECT [Line_Action_Key], [Line_Action], [Line_Action_Description] COLLATE Latin1_General_CI_AS AS [Line_Action_Description], [INS_DT], [UPDT_DT]     FROM LH_Mart.[dbo].[line_action_dim]
```

