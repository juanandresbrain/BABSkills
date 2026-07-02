# dbo.Md_UpdateExtendedField

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Md_UpdateExtendedField"]
    dbo_Md_Field(["dbo.Md_Field"]) --> SP
    dbo_Md_FieldGrouping(["dbo.Md_FieldGrouping"]) --> SP
    dbo_Md_Table(["dbo.Md_Table"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_Field |
| dbo.Md_FieldGrouping |
| dbo.Md_Table |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[Md_UpdateExtendedField]
```

