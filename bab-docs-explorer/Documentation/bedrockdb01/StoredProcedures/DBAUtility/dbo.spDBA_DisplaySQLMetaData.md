# dbo.spDBA_DisplaySQLMetaData

**Database:** DBAUtility  
**Server:** bedrockdb01  

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
```

