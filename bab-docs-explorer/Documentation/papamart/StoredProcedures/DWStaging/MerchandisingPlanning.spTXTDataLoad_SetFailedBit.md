# MerchandisingPlanning.spTXTDataLoad_SetFailedBit

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_SetFailedBit"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Author,,Brian Byas>
-- Create date: <12/28/2015>
-- Description:	<Set bit for validation failure>
-- =============================================
CREATE PROCEDURE [MerchandisingPlanning].[spTXTDataLoad_SetFailedBit] 
@ServerName NVARCHAR(40),
@FailBit BIT OUTPUT
AS

SET NOCOUNT ON;

DECLARE  @SQL NVARCHAR(MAX)

--DECLARE @Count INT

SET @SQL = 'SET @Count = (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv Ch Tfr Unit] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv Ch Tfr Cost Value] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv Ch Tfr Value]
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv EOP Cost Value] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv EOP Unit] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv EOP Value]
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA. [dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Markdown Perm Value]
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Markdown POS Value] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs On Order Cost Value] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs On Order Unit]
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs On Order Value] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Receipts Cost Value]
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Receipts Unit]
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Receipts Value]
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Sales Value Base] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Sales Value Local] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Sales Cost Value Base] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Shrink Cost Value] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Shrink Unit] 
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SET @Count = @Count + (SELECT Count(*) FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Shrink Value]
	WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION]))
SELECT @Count'

 EXEC sp_executesql @SQL,N'@Count int OUTPUT',@FailBit OUTPUT

IF @FailBit > 0 
BEGIN
		SET @FailBit = 1
END
	ELSE	
		SET @FailBit = 0
```

