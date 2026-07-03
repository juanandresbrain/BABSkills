# catalog.get_version_log_size

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  
**Function Type:** Scalar Function  
**Returns:** bigint(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["catalog.get_version_log_size"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

_No parameters._

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [catalog].[get_version_log_size]()
RETURNS bigint
AS 
BEGIN
    DECLARE @value bigint
    SELECT @value = internal.get_space_used('internal.object_versions')
    RETURN @value
END
```
