# dbo.getGrossAmountOverride

**Database:** DWStaging  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** numeric(9)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.getGrossAmountOverride"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @lineAction | tinyint | 1 | NO |
| @lineObject | smallint | 2 | NO |
| @grossAmount | numeric | 9 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
--	G Murrish	11/15/2012	Added 26 as a lineAction to reverse the sign.
-- =============================================
CREATE FUNCTION [dbo].[getGrossAmountOverride]
(
	@lineAction tinyint,
	@lineObject smallint,
	@grossAmount numeric(12,4)
)
RETURNS numeric(12,4)
AS
BEGIN
	RETURN
	   CASE 
		  WHEN @lineAction IN (2,12,19,27,25,18, 26) THEN
			 CASE
				WHEN NOT (@lineAction=12 AND (@lineObject=690 OR @lineObject=633 OR @lineObject=640)) THEN
				    -@grossAmount
				ELSE
				    @grossAmount
			 END
		  ELSE
			 CASE 
				WHEN @lineObject = 1103 AND @lineAction = 13 THEN
				    -@grossAmount
				ELSE
				    @grossAmount
		  END		
	   END
--SELECT dbo.getGrossAmountOverride (13, 1103, 12)
END
```

