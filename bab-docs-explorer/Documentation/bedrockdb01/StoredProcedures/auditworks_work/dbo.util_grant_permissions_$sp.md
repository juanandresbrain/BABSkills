# dbo.util_grant_permissions_$sp

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_grant_permissions_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
create proc dbo.util_grant_permissions_$sp ( 
  @preview_only tinyint = 1,
  @grptype nvarchar(30) = 'FULL',  --FULL or BROWSER
  @grp nvarchar(30) = 'awusers')   --normally awusers or awbrowsers
AS

/* Proc Name: util_grant permissions_$sp
  Description: grant permissions
        CALLED by release_no_$upgr for FULL/awusers,  BROWSER/awbrowsers
        proc must be manually executed for other groups
	Adds group/role specified if it does not already exist (requires create role permission).
	Grants all permissions if group-type specified is 'FULL', otherwise
	only grants select permissions.
	The awusers group should not normally have insert, delete permission on table security_user.
	
	Note: this version can be the same for SA5 and SA5.1

HISTORY:
10Jun2015 Vicci   125486  support custom objects with large names or names with special characters.
25May2011 Paul    125883  avoid compilation error and use create role in a SQL 2008 environment 
11Nov2010 Paul    121798  exclude security_user table when granting insert/delete permissions except for initial install.
28Oct2010 Paul    121798  avoid error in SQL2008, added order by to cursor
08Jul2009 Paul    109078  check for sql2000 environment to avoid error due to using 'CONTROL'
26May2009 Vicci   109078  Add 'CONTROL' to permissions granted to allow for TRUNCATE.
13Dec2006 Daphna   81180  Modify GRANT ALL to explicit permissions (UPDATE,INSERT,DELETE,SELECT and EXECUTE)
19Dec2005 Vicci           Author
	
*/
	
DECLARE	@exists		tinyint,
	@grant_string nvarchar(255),
	@group_existed	tinyint,
	@object_name nvarchar(255),
	@object_type nvarchar(2),
	@sql_command nvarchar(2000),
	@sql_version  tinyint,
	@warning_msg  nvarchar(120)

SELECT @group_existed = 1

/* will get a compilation warning that the sp_addgroup does not exist on SQL2008 but this is ok
   because the code will not be executed in a 2008 environment.
   Need to create the groups using the gui for SQL2008 */

SELECT @grant_string = N'GRANT'

-- Check whether the SQL environment is SQL 2000 or not

IF @@version NOT LIKE '%2000%'
  SELECT @sql_version = 9

-- check for SQL2008
IF CHARINDEX('2008',@@VERSION) > 0
  SELECT @sql_version = 10

IF @sql_version >= 9
  SELECT @grant_string = N'GRANT CONTROL,'

-- 2005/2008 compatible: Check for existence of group/role in current db.
if not exists( select name from sys.database_principals where name = @grp )
begin
  SELECT @sql_command = N'Creating group/role:  ' + @grp 
  PRINT @sql_command
  IF @preview_only <> 1
	BEGIN
	 /* In SQL 2008 and up, create a role (owned by dbo) under the current db */
	 IF @sql_version > 8
		SELECT @sql_command = N'CREATE ROLE [' + @grp + N'] AUTHORIZATION dbo'
     ELSE
		SELECT @sql_command = N'sp_addgroup ''' + @grp + N''''
	 EXEC sp_executesql @sql_command
	END
  SELECT @group_existed = 0
end


PRINT 'GRANTING ' + @grptype + ' PERMISSIONS TO ' +  @grp
 
DECLARE processing_cursor CURSOR FAST_FORWARD
 FOR
  SELECT name, type
    FROM sysobjects 
   WHERE type IN ( 'U', 'P', 'V' )
     AND uid = 1
   ORDER BY type, name

OPEN processing_cursor

WHILE 1=1 
  BEGIN
    FETCH processing_cursor
     INTO @object_name, @object_type

    IF @@fetch_status <> 0
	BREAK

    SELECT @sql_command = NULL

	-- avoid error when space exists in proc name by mistake
    IF @object_name = 'util_verify_ transl_rejects_$sp'
	SELECT @object_name = 'util_verify_transl_rejects_$sp'

	/* Need to avoid regranting insert, update, delete when upgrading */
    IF @object_name = 'security_user' AND @grptype = 'FULL' AND @group_existed = 1
      CONTINUE

    IF @grptype = 'FULL' 
    BEGIN
      IF @object_type = 'P'  
        SELECT @sql_command = 'GRANT EXECUTE on dbo.[' + @object_name + '] TO ' + @grp
      ELSE   --- U OR V
        SELECT @sql_command = @grant_string + ' SELECT, INSERT, DELETE, UPDATE on dbo.[' + @object_name + '] TO ' + @grp
    END
    ELSE -- BROWSERS
    BEGIN   
      IF (@object_type IN ('U', 'V'))
      BEGIN
        IF @object_name = 'security_user'
           SELECT @sql_command = 'GRANT SELECT, UPDATE on dbo.security_user TO ' + @grp  
        ELSE    
          IF SUBSTRING(@object_name, 1, 5) = 'work_'
            SELECT @sql_command = @grant_string + ' SELECT, INSERT, DELETE, UPDATE on dbo.' + @object_name + ' TO ' + @grp
          ELSE
            SELECT @sql_command = 'GRANT SELECT on dbo.[' + @object_name + '] TO ' + @grp
      END
      ELSE  -- object_type P
      BEGIN
        IF @object_name = 'check_cleanup_$sp'
           SELECT @sql_command = 'GRANT EXECUTE on check_cleanup_$sp TO ' + @grp       
      END  
      
    END -- BROWSERS  

    IF @sql_command IS NOT NULL
    BEGIN   
      IF @preview_only = 1
        PRINT @sql_command
  ELSE
        EXEC sp_executesql @sql_command
    END
   
 END /* while 1=1 */

CLOSE processing_cursor
DEALLOCATE processing_cursor 

SELECT @exists = COUNT(1)
FROM sysobjects
WHERE LOWER(name) = 'security_user'

/* Avoid all users being able to grant access to PB tm */

IF @exists > 0 AND @grptype = 'FULL' AND COALESCE(@preview_only,0) = 0
  BEGIN
	SELECT @sql_command = 'GRANT select, update ON security_user TO ' + @grp
	EXEC sp_executesql @sql_command

	/* If not the initial install, then revoke any existing insert, delete perm */

	SELECT @warning_msg = 'REMINDER: It is recommended to revoke insert, delete on security_user from ' + @grp
	 + '. Then grant to admin login/group/role.'

	SELECT @sql_command = 'REVOKE insert, delete ON security_user FROM ' + @grp
	IF @group_existed = 1
	BEGIN -- upgrades
	  PRINT @warning_msg
--	  PRINT @sql_command
--	  EXEC sp_executesql @sql_command
	END
	ELSE -- new install
	  PRINT @warning_msg
  END


RETURN
```

