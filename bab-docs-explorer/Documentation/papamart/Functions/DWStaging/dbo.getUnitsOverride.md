# dbo.getUnitsOverride

**Database:** DWStaging  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** numeric(9)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.getUnitsOverride"]
    dbo_getHighPartyCode(["dbo.getHighPartyCode"]) --> FUNC
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @lineObject | smallint | 2 | NO |
| @units | numeric | 9 | NO |
| @grossAmount | numeric | 9 | NO |
| @lineAction | tinyint | 1 | NO |

## Table Dependencies

| Referenced Table |
|---|
| dbo.getHighPartyCode |

## Function Code

```sql
-- =============================================
-- Author:		Rick Caminiti
-- Create date:	9/20/2011
-- Description:	Used in SSIS package to load Sales data
-- =============================================
CREATE FUNCTION [dbo].[getUnitsOverride]
(
	@lineObject smallint,
	@units numeric(15,4),
	@grossAmount numeric(12,4),
	@lineAction tinyint
)
RETURNS numeric(15,4)
AS
BEGIN
    DECLARE @highPartyCode smallint,
		  @unitsOverride numeric(15,4);

    SET @highPartyCode = dbo.getHighPartyCode()
    SET @unitsOverride = 
	   CASE 
		  WHEN @units IS NOT NULL THEN
			 @units
		  ELSE
			 CASE 
				WHEN @lineObject >= 3000 AND @lineObject <= @highPartyCode THEN
				    1
				WHEN @lineObject IN (200,202,203,204,205,206,210,250,291,293,296,400,401,402,403,404) THEN
				    1
				WHEN @lineObject = 292 THEN
				    round(@grossAmount, 0)
				ELSE
				    null
		  END		
	   END
	   
    SET @unitsOverride = 
	   CASE
		  WHEN @lineAction IN (2,12,19,27,25) THEN
			 CASE 
				WHEN NOT (@lineAction = 12 AND @lineObject = 690) THEN
				    -@unitsOverride
				ELSE
				    @unitsOverride
			 END
		  ELSE
			 @unitsOverride
	   END
	   
    RETURN @unitsOverride;
--SELECT dbo.getUnitsOverride (292, null, 12)
END


dbo,fnRemoveNonNumericCharacters,SQL_SCALAR_FUNCTION,-- =============================================
-- Author:		Gary Murrish
-- Create date: 2/5/2013
-- Description:	Strip out Non-Numeric Characters
-- =============================================
CREATE FUNCTION [dbo].[fnRemoveNonNumericCharacters] 
(
	-- Add the parameters for the function here
	@strText varchar(1000)
)
RETURNS varchar(1000)
AS
BEGIN
	WHILE PATINDEX('%[^0-9]%',@strText) > 0
	BEGIN
		SET @strText = STUFF(@strText,PATINDEX('%[^0-9]%',@strText),1,'')
	end
	RETURN @strText

END
```

