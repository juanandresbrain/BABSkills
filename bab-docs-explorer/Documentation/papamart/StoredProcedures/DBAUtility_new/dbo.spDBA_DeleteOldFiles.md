# dbo.spDBA_DeleteOldFiles

**Database:** DBAUtility_new  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_DeleteOldFiles"]
    dbo_xp_cmdshell(["dbo.xp_cmdshell"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.xp_cmdshell |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[spDBA_DeleteOldFiles] 
	@path VARCHAR(100), @filemask VARCHAR(20), @retention INT = 2
AS


-- =============================================================================================================
-- Name: spDBA_DeleteOldFiles
--
-- Description:	Deletes files 
--
-- @path: directory location of files to delete.
-- @filemask: file extension of files to delete.
-- @retention: number of days of files to keep.
--
-- Output: 
--
-- Available actions: delete files
--
-- Dependency: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Mike Pelikan	01/08/2014		Changed Name and added comment block

DECLARE @Revision DATETIME
SET @Revision = '01/08/2014'
 	
/*

*/
-- =============================================================================================================
SET NOCOUNT ON 

declare @cmd varchar(1000)
declare @rowcnt int	--stores @@rowcount
declare @WhichFile VARCHAR(1000)

--declare @path varchar(100)
--declare @filemask varchar(20)
--declare @retention int
--
--select @path = 'i:\postfuture\uploaded\'
--select @filemask = '*.zip'
--select @retention = 7

-- Stores the name of the file to be deleted
CREATE TABLE #DeleteOldFiles
 (
  DirInfo VARCHAR(7000)
 )

-- Build the command that will list out all of the files in a directory
SELECT @cmd = 'dir ' + @path + @filemask + ' /OD'

  -- Run the dir command and put the results into a temp table
  INSERT INTO #DeleteOldFiles
  EXEC master.dbo.xp_cmdshell @cmd

  -- Delete all rows from the temp table except the ones that correspond to the files to be deleted
  DELETE
  FROM #DeleteOldFiles
  WHERE ISDATE(SUBSTRING(DirInfo, 1, 10)) = 0 OR DirInfo LIKE '%
%' OR SUBSTRING(DirInfo, 25, 5) = '<DIR>'
	OR SUBSTRING(DirInfo, 1, 10) >= GETDATE() - @retention

  -- Get the file name portion of the row that corresponds to the file to be deleted
  SELECT TOP 1 @WhichFile = SUBSTRING(DirInfo, LEN(DirInfo) -  PATINDEX('% %', REVERSE(DirInfo)) + 2, LEN(DirInfo))
  FROM #DeleteOldFiles
  
  SET @rowcnt = @@ROWCOUNT
  
  -- Interate through the temp table until there are no more files to delete
  WHILE @rowcnt <> 0
  BEGIN
  
   -- Build the del command
   SELECT @cmd = 'del ' + @path + @WhichFile + ' /Q /F'
   
   -- Delete the file
   EXEC master.dbo.xp_cmdshell @cmd, NO_OUTPUT
   
   -- To move to the next file, the current file name needs to be deleted from the temp table
   DELETE
   FROM #DeleteOldFiles
   WHERE SUBSTRING(DirInfo, LEN(DirInfo) -  PATINDEX('% %', REVERSE(DirInfo)) + 2, LEN(DirInfo))  = @WhichFile

   -- Get the file name portion of the row that corresponds to the file to be deleted
   SELECT TOP 1 @WhichFile = SUBSTRING(DirInfo, LEN(DirInfo) -  PATINDEX('% %', REVERSE(DirInfo)) + 2, LEN(DirInfo))
   FROM #DeleteOldFiles
  
   SET @rowcnt = @@ROWCOUNT
  
  END
  
  DROP TABLE #DeleteOldFiles
```

