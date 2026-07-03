# esell.fGetLocationAttributeIds

**Database:** esell  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** varchar(4000)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["esell.fGetLocationAttributeIds"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @AttributeLvl | smallint | 2 | NO |
| @AttributeIdList | varchar | 4000 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
--END fGetDelimitedOrderStatuses


--START fGetLocationAttributeIds
CREATE FUNCTION [esell].[fGetLocationAttributeIds]
(
@AttributeLvl SMALLINT,
@AttributeIdList VARCHAR(4000)
)
RETURNS VARCHAR(4000)
AS


--Function Name: fGetLocationAttributeIds
--
--  Description: --This function prepares a dynamic query for finding the leaf level location attributes using parent child relationships.
--
--  Parameters:
--             IN Parameter(s):
--                 1. AttributeLvl  - Attribute Level of selected location attributes.
--                 2. AttributeIdList - Comma Seperated List of location attributes Ids selected from criteria pages.
--			
--  Returns: Dynamic query for finding leaf level location attributes as Varchar.

--  Author: OBernal
--
--  Date: 22-OCtober-2012
--
--  Revisions:
--
--  Notes: 

BEGIN
DECLARE @baseSQL VARCHAR(4000)
DECLARE @prependSQL VARCHAR(500)
DECLARE @finalSQL VARCHAR(4000)

SET @baseSQL = 'SELECT grp.HRCHY_LVL_GRP_ID FROM ORG_CHN_HRCHY_LVL_GRP grp 
WHERE grp.PRNT_HRCHY_LVL_GRP_ID IN (' + @AttributeIdList + ')'

SET @prependSQL = 'SELECT grp.HRCHY_LVL_GRP_ID from ORG_CHN_HRCHY_LVL_GRP grp 
WHERE grp.PRNT_HRCHY_LVL_GRP_ID IN ' 

SET @finalSQL = ''

IF (@AttributeLvl = 1)
	BEGIN
		set @finalsql = @baseSQL
	END
ELSE
	BEGIN
		while(@AttributeLvl > 1 )
		begin
			set @finalSQL = @prependSQL + '(' + CONVERT(VARCHAR(4000), @baseSQL) + ')'
			set @baseSQL = @finalSQL
			set @AttributeLvl = @AttributeLvl - 1 
		end
	END

RETURN @finalSQL
END
```
