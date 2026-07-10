# dbo.spDBA_DisplaySQLMetaData

**Database:** DBAUtility  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_DisplaySQLMetaData"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDBA_DisplaySQLMetaData]
@Database VARCHAR(100)
AS
SET NOCOUNT ON
--this proc is used in the Access Application to display tables with missing meta data
--mike pelikan		7/22/2013		Deployment
DECLARE @SQL VARCHAR(2000)

SET @SQL = '
SELECT  	u.name [Schema], CAST(t.name AS VARCHAR(255)) AS [table], CAST(u.name + ''.'' + t.name  AS VARCHAR(255)) AS [TableName],
            CAST(td.value AS VARCHAR(255)) AS [table_desc],
    		CAST(c.name AS VARCHAR(255)) AS [column],
    		CAST(cd.value AS VARCHAR(255)) AS [column_desc]
FROM    	' + @Database + '.dbo.sysobjects t
INNER JOIN  ' + @Database + '.dbo.sysusers u
    ON		u.uid = t.uid
LEFT OUTER JOIN ' + @Database + '.sys.extended_properties td
    ON		td.major_id = t.id
    AND 	td.minor_id = 0
    AND		td.name = ''MS_Description''
INNER JOIN  ' + @Database + '.dbo.syscolumns c
    ON		c.id = t.id
LEFT OUTER JOIN ' + @Database + '.sys.extended_properties cd
    ON		cd.major_id = c.id
    AND		cd.minor_id = c.colid
    AND		cd.name = ''MS_Description''
WHERE t.type = ''u'' and t.name not like ''asp%'' and t.name not in (''sysdiagrams'')
and (td.value is null or cd.value is null)
ORDER BY    t.name, c.colorder'

EXEC (@SQL)
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
```

