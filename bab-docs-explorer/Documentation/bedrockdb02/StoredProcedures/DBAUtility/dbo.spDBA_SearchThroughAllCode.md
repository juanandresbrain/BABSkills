# dbo.spDBA_SearchThroughAllCode

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_SearchThroughAllCode"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDBA_SearchThroughAllCode]
	@SearchStringIn varchar(255),
	@Action VARCHAR(20) = 'Process'
AS
-- =============================================================================================================
-- Name: spDBA_SearchThroughAllCode
--
--	Input:		@SearchStringIn VARCHAR(255)
--	Output:		search results
-- 
-- Available actions:
--@SearchStringIn -the search will only return results that match the pattern. It can be an exact string or it can include wildcards (% and _). Default = '%'. 

-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Mike Pelikan	08/27/2012		Added versioning
-- =============================================================================================================
DECLARE @Revision DATETIME
SET @Revision = '08/27/2012'

SET NOCOUNT ON
----------------------------------------------------------------------------------------------------
--// Revision                                                                                  //--
----------------------------------------------------------------------------------------------------
IF @Action = 'ReturnVersion'
BEGIN
	GOTO EndHere
END

BEGIN
  DECLARE @SQL VARCHAR(2000)

  SET @SQL = 'USE ?; 
  SELECT ''?'' AS DATABASE_NAME, 
    sys.schemas.name AS [Schema Name],
    sys.objects.name AS [Object Name] ,
    type_desc AS [Object Type],
    substring(definition,CHARINDEX(''' + @SearchStringIn + ''',
      definition)-30, 60)
    AS [Text Context]
  FROM sys.objects
  JOIN sys.sql_modules
    ON sys.objects.object_id = sys.sql_modules.object_id
  JOIN sys.schemas
    ON sys.objects.schema_id = sys.schemas.schema_id
  WHERE CHARINDEX(''' + @SearchStringIn + ''',definition)>0'

  CREATE TABLE #SEARCH_RESULTS
   ( DATABASE_NAME NVARCHAR(128),
    [SCHEMA_NAME] VARCHAR(128),
    [OBJECT_NAME] VARCHAR(128),
    [OBJECT_TYPE] VARCHAR(20),
    TEXT_CONTEXT VARCHAR(60) )
    
  INSERT INTO #SEARCH_RESULTS EXEC sp_MSforeachdb @SQL
 

  SELECT * FROM #SEARCH_RESULTS
  ORDER BY DATABASE_NAME, [SCHEMA_NAME], [OBJECT_NAME]

END

EndHere:
IF @Action = 'ReturnVersion'
BEGIN
	SELECT @Revision 
END
```

