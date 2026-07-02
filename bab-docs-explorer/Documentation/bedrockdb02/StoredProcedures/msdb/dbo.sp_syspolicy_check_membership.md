# dbo.sp_syspolicy_check_membership

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_syspolicy_check_membership"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_syspolicy_check_membership]
@role sysname,
@raiserror bit = 1
AS
BEGIN
	-- make sure that the caller is dbo or @role
	IF ( IS_MEMBER(@role) != 1 AND USER_ID() != 1)
	BEGIN
		IF (@raiserror = 1)
		BEGIN
			RAISERROR(15003, -1, -1, @role);
		END
		RETURN 15003;
	END
	
	RETURN 0;
END
```

