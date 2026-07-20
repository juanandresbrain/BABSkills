# dbo.test123

**Database:** Temp_Lakehouse  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.test123"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE  procedure dbo.test123 (@param varchar(100) )
AS
SELECT @param as col2
```

