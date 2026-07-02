# dbo.sp_ExecResultSet

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_ExecResultSet"]
    mydata_value(["mydata.value"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| mydata.value |

## Stored Procedure Code

```sql
CREATE procedure [dbo].[sp_ExecResultSet]
(
	@cmd	nvarchar(4000),
	@dbname	sysname = NULL
)
as
begin
  SET NOCOUNT ON
	declare @retcode bit,
		    @proc nvarchar(4000)
	
	-- check to ensure that the @dbname provided is neither null or empty
	if isnull(rtrim(@dbname), N'') = N''
	begin
		raiserror('Internal Error : @dbname cannot be null or empty.', 16, -1)
		return 1
	end
   DECLARE @x TABLE
    (
        sql NVARCHAR(MAX),
        num INT IDENTITY(1,1)
    )
	
   DECLARE @input_sql NVARCHAR(355)
    SET @input_sql = N'EXEC ' + @dbname + '..sp_executesql @stmt=@cmd'

    INSERT @x (sql)
    EXEC sp_executesql 
        @input_sql, 
        N'@cmd NVARCHAR(MAX)', 
        @cmd

  
    DECLARE @sql NVARCHAR(MAX)
    
	SELECT @sql = mydata.value('/row[1]/x[1]', 'varchar(max)')
	FROM
	(
		SELECT x
		FROM
		(        
			SELECT sql + ';' AS [data()]
			FROM @x
			ORDER BY num
			FOR XML PATH(''), TYPE
		) y (x)
		FOR XML RAW, TYPE
	) d (mydata)

    exec @retcode = sp_executesql 
        @input_sql, 
        N'@cmd NVARCHAR(MAX)', 
        @sql

	return @retcode
--this function uses some of the original microsoft logic, as well as 
--logic from http://sqlblog.com/blogs/adam_machanic/archive/2006/10/19/replacing-xp-execresultset-in-sql-server-2005.aspx

END
```

