# dbo.util_load_logins_$sp

**Database:** auditworks_work  
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

dbo,dt_setpropertybyid,/*
**	If the property already exists, reset the value; otherwise add property
**		id -- the id in sysobjects of the object
**		property -- the name of the property
**		value -- the text value of the property
**		lvalue -- the binary value of the property (image)
*/
create procedure dbo.dt_setpropertybyid
	@id int,
	@property varchar(64),
	@value varchar(255),
	@lvalue image
as
	set nocount on
	declare @uvalue nvarchar(255) 
	set @uvalue = convert(nvarchar(255), @value) 
	if exists (select * from dbo.dtproperties 
			where objectid=@id and property=@property)
	begin
		--
		-- bump the version count for this row as we update it
		--
		update dbo.dtproperties set value=@value, uvalue=@uvalue, lvalue=@lvalue, version=version+1
			where objectid=@id and property=@property
	end
	else
	begin
		--
		-- version count is auto-set to 0 on initial insert
		--
		insert dbo.dtproperties (property, objectid, value, uvalue, lvalue)
			values (@property, @id, @value, @uvalue, @lvalue)
	end


dbo,dt_getobjwithprop,/*
**	Retrieve the owner object(s) of a given property
*/
create procedure dbo.dt_getobjwithprop
	@property varchar(30),
	@value varchar(255)
as
	set nocount on

	if (@property is null) or (@property = '')
	begin
		raiserror('Must specify a property name.',-1,-1)
		return (1)
	end

	if (@value is null)
		select objectid id from dbo.dtproperties
			where property=@property

	else
		select objectid id from dbo.dtproperties
			where property=@property and value=@value

dbo,dt_getpropertiesbyid,/*
**	Retrieve properties by id's
**
**	dt_getproperties objid, null or '' -- retrieve all properties of the object itself
**	dt_getproperties objid, property -- retrieve the property specified
*/
create procedure dbo.dt_getpropertiesbyid
	@id int,
	@property varchar(64)
as
	set nocount on

	if (@property is null) or (@property = '')
		select property, version, value, lvalue
			from dbo.dtproperties
			where  @id=objectid
	else
		select property, version, value, lvalue
			from dbo.dtproperties
			where  @id=objectid and @property=property

dbo,dt_setpropertybyid_u,/*
**	If the property already exists, reset the value; otherwise add property
**		id -- the id in sysobjects of the object
**		property -- the name of the property
**		uvalue -- the text value of the property
**		lvalue -- the binary value of the property (image)
*/
create procedure dbo.dt_setpropertybyid_u
	@id int,
	@property varchar(64),
	@uvalue nvarchar(255),
	@lvalue image
as
	set nocount on
	-- 
	-- If we are writing the name property, find the ansi equivalent. 
	-- If there is no lossless translation, generate an ansi name. 
	-- 
	declare @avalue varchar(255) 
	set @avalue = null 
	if (@uvalue is not null) 
	begin 
		if (convert(nvarchar(255), convert(varchar(255), @uvalue)) = @uvalue) 
		begin 
			set @avalue = convert(varchar(255), @uvalue) 
		end 
		else 
		begin 
			if 'DtgSchemaNAME' = @property 
			begin 
				exec dbo.dt_generateansiname @avalue output 
			end 
		end 
	end 
	if exists (select * from dbo.dtproperties 
			where objectid=@id and property=@property)
	begin
		--
		-- bump the version count for this row as we update it
		--
		update dbo.dtproperties set value=@avalue, uvalue=@uvalue, lvalue=@lvalue, version=version+1
			where objectid=@id and property=@property
	end
	else
	begin
		--
		-- version count is auto-set to 0 on initial insert
		--
		insert dbo.dtproperties (property, objectid, value, uvalue, lvalue)
			values (@property, @id, @avalue, @uvalue, @lvalue)
	end

dbo,dt_getobjwithprop_u,/*
**	Retrieve the owner object(s) of a given property
*/
create procedure dbo.dt_getobjwithprop_u
	@property varchar(30),
	@uvalue nvarchar(255)
as
	set nocount on

	if (@property is null) or (@property = '')
	begin
		raiserror('Must specify a property name.',-1,-1)
		return (1)
	end

	if (@uvalue is null)
		select objectid id from dbo.dtproperties
			where property=@property

	else
		select objectid id from dbo.dtproperties
			where property=@property and uvalue=@uvalue

dbo,dt_getpropertiesbyid_u,/*
**	Retrieve properties by id's
**
**	dt_getproperties objid, null or '' -- retrieve all properties of the object itself
**	dt_getproperties objid, property -- retrieve the property specified
*/
create procedure dbo.dt_getpropertiesbyid_u
	@id int,
	@property varchar(64)
as
	set nocount on

	if (@property is null) or (@property = '')
		select property, version, uvalue, lvalue
			from dbo.dtproperties
			where  @id=objectid
	else
		select property, version, uvalue, lvalue
			from dbo.dtproperties
			where  @id=objectid and @property=property

dbo,dt_dropuserobjectbyid,/*
**	Drop an object from the dbo.dtproperties table
*/
create procedure dbo.dt_dropuserobjectbyid
	@id int
as
	set nocount on
	delete from dbo.dtproperties where objectid=@id

dbo,dt_droppropertiesbyid,/*
**	Drop one or all the associated properties of an object or an attribute 
**
**	dt_dropproperties objid, null or '' -- drop all properties of the object itself
**	dt_dropproperties objid, property -- drop the property
*/
create procedure dbo.dt_droppropertiesbyid
	@id int,
	@property varchar(64)
as
	set nocount on

	if (@property is null) or (@property = '')
		delete from dbo.dtproperties where objectid=@id
	else
		delete from dbo.dtproperties 
			where objectid=@id and property=@property


dbo,dt_verstamp006,/*
**	This procedure returns the version number of the stored
**    procedures used by the Microsoft Visual Database Tools.
**    Current version is 7.0.00.
*/
create procedure dbo.dt_verstamp006
as
	select 7000
```

