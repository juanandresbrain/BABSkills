# dbo.util_load_logins_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.util_load_logins_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
create proc dbo.util_load_logins_$sp   
  @password nvarchar(256) = NULL,	  --if not passed, no logins are created, just creates as users in database if not already there
  @one_user_only tinyint = 1, 		  --1=do not create the old standard list of users, just the one specified below
  @username sysname = 'RetSqlSys'  --specify the name of a user to be created
  		
as

/*
NAME: util_load_logins_sp
DESC: for use by TPLs to create standard users
HIST: 

DATE		NAME	DEF	DESC
Mar26,12        Vicci   134079  remove clear text default password and don't create logins if it is not passed (since TPLs now install with only one login this proc is no longer really required).
Jul08,11        Vicci           Remove sp_addalias for smartview_user since does not exist in SQL2008.  Prompt for password.
Jan07.10        Vicci           Modify default password to be strong/complex (caps and numbers);  remove 
				auditworks_interface1 login no longer used in S/A 5.0
Aug03.06 	Daphna		Include in SA repo, remove references to sysxlogins to be compatible with MSSQL2005
                                Data now located in syslogins view, no join necessary.
*/


begin

declare @login_exists bit

IF LTRIM(RTRIM(@password)) = ''
  SELECT @password = NULL
IF LTRIM(RTRIM(@username)) = ''
  SELECT @username = NULL

	create table #results(resulttext nvarchar(512))

-- add logins if they don't exist
-- add users if they don't exist
	
	IF @username IS NOT NULL
	BEGIN
	  SELECT @login_exists = 0
	
	  select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	  if @login_exists = 0 and @password IS NOT NULL
	  begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, @password
		select @login_exists = 1
	  end
	  IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	  begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	  end
	END

	IF @one_user_only = 1
	BEGIN
	insert #results 
		select 'No logins, database users, or aliases added since they already exist.' where not exists (select * from #results)
		select * from #results
		drop table #results
		RETURN
	END
		
	select @username='auditworks_export', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	
	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, @password
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end

		
	select @username='auditworks_dayend', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	
	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, @password
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end

		
	select @username='auditworks_edit', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	
	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, @password
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end
		
	select @username='auditworks_flash_interface', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	
	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, @password
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end
	
	select @username='auditworks_import', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	
	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, @password
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end
		
	select @username='smartview_user', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	
	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, @password
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end

	select @username='VOUCHER_SUPPORT', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	
	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, @password
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end

	select @username='SUPPORT', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	
	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, @password
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end

	select @username='AUDITOR1', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)

	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, Auditor1
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end
	
	select @username='FLUSER', @login_exists = 0
	select @login_exists = 1 where exists (select 1 from master.sys.syslogins s where isntname=0 and name=@username)
	
	if @login_exists = 0 and @password IS NOT NULL
	begin
		insert #results select 'Adding login for '+ @username
		exec sp_addlogin @username, Fluser1
		select @login_exists = 1
	end
	IF @login_exists = 1 and not exists (select 1 from sysusers where name=@username) 
	begin
		insert #results select 'Adding user '+ @username+' to database'
		insert #results select 'Adding user '+ @username+' to ''db_owner'' role'
		exec sp_adduser @username
		exec sp_addrolemember 'db_owner', @username
	end

insert #results 
select 'No logins, database users, or aliases added since they already exist.' where not exists (select * from #results)
select * from #results
drop table #results

end

RETURN
```

