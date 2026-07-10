# dbo.spSurveyResults_JD

**Database:** DBAUtility_new  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spSurveyResults_JD"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE spSurveyResults_JD
	@FileName VARCHAR(1000)
AS
IF DATALENGTH(@FileName ) > 0
DECLARE @SQL VARCHAR(2000)
SET @SQL = '"d:\ETL Executables\GuestSurvey\SurveyResults\jd.exe" "' + @FileName  + '"'
PRINT @SQL
EXEC xp_cmdshell @SQL
```

