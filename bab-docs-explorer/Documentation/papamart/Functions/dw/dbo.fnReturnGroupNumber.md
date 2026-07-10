# dbo.fnReturnGroupNumber

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** int(4)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnReturnGroupNumber"]
    dbo_CRMde1(["dbo.CRMde1"]) --> FUNC
```

## Parameters

_No parameters._

## Table Dependencies

| Referenced Table |
|---|
| dbo.CRMde1 |

## Function Code

```sql
CREATE FUNCTION [dbo].[fnReturnGroupNumber] ()
	RETURNS INT
AS
BEGIN
	DECLARE @currRecordCount INT
	SET @currRecordCount = (select count(*) from DW.dbo.CRMde1)
	DECLARE @groupNumber INT
	SET @groupNumber = @currRecordCount/350000
	SET @groupNumber += 1
	RETURN @groupNumber
END
```

