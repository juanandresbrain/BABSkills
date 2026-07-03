# internal.decrypt_binarydata

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  
**Function Type:** CLR Scalar Function  
**Returns:** varbinary  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["internal.decrypt_binarydata"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @algorithmName | nvarchar | 510 | NO |
| @key | varbinary | 8000 | NO |
| @IV | varbinary | 8000 | NO |
| @binary_value | varbinary | -1 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
-- (code not available)
```
