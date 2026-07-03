# internal.get_package_data

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  
**Function Type:** CLR Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["internal.get_package_data"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @key_name | nvarchar | 510 | NO |
| @KEY | varbinary | 8000 | NO |
| @IV | varbinary | 8000 | NO |
| @project_version_lsn | bigint | 8 | NO |
| @project_id | bigint | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
-- (code not available)
```
