# dbo.fnDW_AuditRowCounts

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** int(4)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnDW_AuditRowCounts"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @SrcCount | int | 4 | NO |
| @DestCount | int | 4 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
-- =============================================
-- Author:		Trista Parmentier
-- Create date: 10/14/2011
-- Description:	Function to compare source and destination row counts for DW Sales SSIS packages 
-- =============================================
CREATE FUNCTION [dbo].[fnDW_AuditRowCounts]
	(@SrcCount INT,
	@DestCount INT)

RETURNS INT
AS
BEGIN

	DECLARE @InvalidCountFlag INT

	SET @InvalidCountFlag = CASE WHEN @SrcCount = @DestCount THEN 0 ELSE 1 END --0 if they match, 1 if invalid, notification required

	RETURN @InvalidCountFlag

END
```

