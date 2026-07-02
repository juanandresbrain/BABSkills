# dbo.sp_syspolicy_update_policy_category

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_syspolicy_update_policy_category"]
    dbo_sp_syspolicy_check_membership(["dbo.sp_syspolicy_check_membership"]) --> SP
    dbo_sp_syspolicy_verify_policy_category_identifiers(["dbo.sp_syspolicy_verify_policy_category_identifiers"]) --> SP
    dbo_syspolicy_policy_categories_internal_(["dbo.syspolicy_policy_categories_internal "]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_syspolicy_check_membership |
| dbo.sp_syspolicy_verify_policy_category_identifiers |
| dbo.syspolicy_policy_categories_internal  |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_syspolicy_update_policy_category] 
@name sysname = NULL,
@policy_category_id int = NULL,
@mandate_database_subscriptions bit = NULL
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF ( 0!= @retval_check)
	BEGIN
		RETURN @retval_check
	END

    DECLARE @retval              INT

    EXEC @retval = sp_syspolicy_verify_policy_category_identifiers @name, @policy_category_id OUTPUT
    IF (@retval <> 0)
        RETURN (1)

    UPDATE msdb.[dbo].[syspolicy_policy_categories_internal ]
    SET mandate_database_subscriptions = ISNULL(@mandate_database_subscriptions, mandate_database_subscriptions)
    WHERE policy_category_id = @policy_category_id

    SELECT @retval = @@error
    RETURN(@retval)
END
```

