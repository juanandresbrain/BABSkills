# dbo.SCRTY_CHK_IS_GRP_IN_SET_$SP

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SCRTY_CHK_IS_GRP_IN_SET_$SP"]
    ORG_CHN_HRCHY_LVL_GRP_SET_A(["ORG_CHN_HRCHY_LVL_GRP_SET_A"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ORG_CHN_HRCHY_LVL_GRP_SET_A |

## Stored Procedure Code

```sql
CREATE PROC dbo.SCRTY_CHK_IS_GRP_IN_SET_$SP
/**********************************************************************
	Procedure		: SCRTY_CHK_IS_GRP_IN_SET_$SP
	CRM Version		: 7.0
	Date			: 2009 0428
	Author			: ABida
	Called from		:
	Calls			:
	Description		: Check whether the division (ORG_CHN Group) exists in the division set (ORG_CHN Group set).
***********************************************************************
UPDATES:
2009 0714 ABida		Simplified the query since each set contains divisions its subset contains.
2010 0208 JHardin	CRDM Merge renaming
2012 0613 JHardin	CRDM merge final renaming, cosmetic cleanup

************************************************************************/
	@OC_GRP_IDNTY	int,
	@OCG_SET_ID		int,
	@isInSet		bit OUT
AS
BEGIN
	SET NOCOUNT ON;

	SET @isInSet = 0;

	IF @OCG_SET_ID = -1
	BEGIN
		-- Global set contains all, no need to query
		SET @isInSet = 1;
	END;
	ELSE
	BEGIN
		IF EXISTS(
			SELECT 1
			FROM ORG_CHN_HRCHY_LVL_GRP_SET_A
			WHERE HRCHY_LVL_GRP_SET_ID = @OCG_SET_ID
			AND HRCHY_LVL_GRP_IDNTY = @OC_GRP_IDNTY
		)
		BEGIN
			SET @isInSet = 1;
		END;
	END;

	RETURN @isInSet;

END;
```

