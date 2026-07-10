# dbo.spINFA_household_keys

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spINFA_household_keys"]
    household_dim(["household_dim"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| household_dim |

## Stored Procedure Code

```sql
Create procedure spINFA_household_keys
as



select max(household_key) from household_dim
```

