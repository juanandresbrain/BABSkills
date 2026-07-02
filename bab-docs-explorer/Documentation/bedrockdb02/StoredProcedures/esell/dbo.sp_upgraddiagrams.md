# dbo.sp_upgraddiagrams

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_upgraddiagrams"]
    dbo_dtproperties(["dbo.dtproperties"]) --> SP
    dbo_sysdiagrams(["dbo.sysdiagrams"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dtproperties |
| dbo.sysdiagrams |

## Stored Procedure Code

```sql

```

