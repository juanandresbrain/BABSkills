# dbo.sp_syspolicy_delete_policy

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_syspolicy_delete_policy"]
    dbo_sp_syspolicy_check_membership(["dbo.sp_syspolicy_check_membership"]) --> SP
    dbo_sp_syspolicy_verify_policy_identifiers(["dbo.sp_syspolicy_verify_policy_identifiers"]) --> SP
    dbo_syspolicy_policies_internal(["dbo.syspolicy_policies_internal"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_syspolicy_check_membership |
| dbo.sp_syspolicy_verify_policy_identifiers |
| dbo.syspolicy_policies_internal |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_syspolicy_delete_policy] 
@name sysname = NULL,
@policy_id int = NULL
WITH EXECUTE AS OWNER
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF ( 0!= @retval_check)
	BEGIN
		RETURN @retval_check
	END

	DECLARE @retval              INT

    EXEC @retval = sp_syspolicy_verify_policy_identifiers @name, @policy_id OUTPUT
    IF (@retval <> 0)
        RETURN (1)

    DELETE msdb.dbo.syspolicy_policies_internal 
        WHERE policy_id = @policy_id

    RETURN (0)
END
```

