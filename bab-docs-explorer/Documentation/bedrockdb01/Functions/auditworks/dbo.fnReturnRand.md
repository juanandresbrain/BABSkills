# dbo.fnReturnRand

**Database:** auditworks  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** real(4)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnReturnRand"]
    vwReturnRand(["vwReturnRand"]) --> FUNC
```

## Parameters

_No parameters._

## Table Dependencies

| Referenced Table |
|---|
| vwReturnRand |

## Function Code

```sql
CREATE FUNCTION [dbo].[fnReturnRand] ()
	RETURNS REAL
AS
BEGIN
	DECLARE @r REAL
	SET @r = (SELECT r FROM vwReturnRand)
	RETURN @r
END
```

