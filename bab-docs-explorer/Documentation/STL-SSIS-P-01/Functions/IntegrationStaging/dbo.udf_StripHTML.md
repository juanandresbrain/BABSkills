# dbo.udf_StripHTML

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  
**Function Type:** Scalar Function  
**Returns:** nvarchar  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.udf_StripHTML"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @HTMLText | nvarchar | -1 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[udf_StripHTML] (@HTMLText nVARCHAR(MAX))
RETURNS nVARCHAR(MAX)
AS
BEGIN
DECLARE @Start INT
DECLARE @End INT
DECLARE @Length INT
SET @Start = CHARINDEX('<',@HTMLText) SET @End = 
CHARINDEX('>',@HTMLText,CHARINDEX('<',@HTMLText)) 
SET @Length = (@End - @Start) + 1 WHILE @Start > 0
AND @End > 0
AND @Length > 0
BEGIN
SET @HTMLText = STUFF(@HTMLText,@Start,@Length,'')
SET @Start = CHARINDEX('<',@HTMLText) SET @End = CHARINDEX('>',@HTMLText,CHARINDEX('<',@HTMLText))
SET @Length = (@End - @Start) + 1
END
RETURN LTRIM(RTRIM(@HTMLText))
END
```
