# dbo.getHighPartyCode

**Database:** DWStaging  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** smallint(2)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.getHighPartyCode"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

_No parameters._

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
create FUNCTION [dbo].[getHighPartyCode]()
RETURNS smallint
AS
BEGIN
	RETURN 6999
--SELECT dbo.getHighPartyCode 
END
```

