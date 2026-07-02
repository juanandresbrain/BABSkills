# dbo.Md_LoadLanguage

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Md_LoadLanguage"]
    dbo_Lg_DependentDesc(["dbo.Lg_DependentDesc"]) --> SP
    dbo_Lg_Identification(["dbo.Lg_Identification"]) --> SP
    dbo_Md_Field(["dbo.Md_Field"]) --> SP
    dbo_Md_FieldGroup(["dbo.Md_FieldGroup"]) --> SP
    dbo_Md_Topic(["dbo.Md_Topic"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Lg_DependentDesc |
| dbo.Lg_Identification |
| dbo.Md_Field |
| dbo.Md_FieldGroup |
| dbo.Md_Topic |

## Stored Procedure Code

```sql

```

