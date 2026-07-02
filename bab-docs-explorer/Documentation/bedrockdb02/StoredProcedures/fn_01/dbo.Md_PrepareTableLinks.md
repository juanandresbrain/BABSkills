# dbo.Md_PrepareTableLinks

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Md_PrepareTableLinks"]
    dbo_Md_Table(["dbo.Md_Table"]) --> SP
    dbo_Md_TableExclusive(["dbo.Md_TableExclusive"]) --> SP
    dbo_Md_TableLink(["dbo.Md_TableLink"]) --> SP
    dbo_Md_TableLink3Ways(["dbo.Md_TableLink3Ways"]) --> SP
    dbo_Md_TableLink4Ways(["dbo.Md_TableLink4Ways"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_Table |
| dbo.Md_TableExclusive |
| dbo.Md_TableLink |
| dbo.Md_TableLink3Ways |
| dbo.Md_TableLink4Ways |

## Stored Procedure Code

```sql

```

