# MerchandisingPlanning.spTXTDataLoad_CleanseFailedMeasures

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_CleanseFailedMeasures"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Author,,Brian Byas>
-- Create date: <12/11/2015>
-- Description:	<Remove any data in each TXT measure where there is no corresponding store in the store dimension>
-- =============================================
CREATE PROCEDURE [MerchandisingPlanning].[spTXTDataLoad_CleanseFailedMeasures] 
@ServerName NVARCHAR(40)
AS

SET NOCOUNT ON;

DECLARE  @SQL NVARCHAR(4000)

SET @SQL = '
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv Ch Tfr Unit] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))

DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv Ch Tfr Cost Value] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv Ch Tfr Value]
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv EOP Cost Value] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv EOP Unit] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Inv EOP Value]
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA. [dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Markdown Perm Value]
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Markdown POS Value] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK)) 
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs On Order Cost Value] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs On Order Unit]
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs On Order Value] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Receipts Cost Value]
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Receipts Unit]
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Receipts Value]
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Sales Value Base] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Sales Value Local] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Sales Cost Value Base] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Shrink Cost Value] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Shrink Unit] 
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))
--
DELETE FROM '+@ServerName+'.BABW_ARCA.[dbo].[AMB_hs Shrink Value]
WHERE STORE NOT IN (SELECT [STORE] FROM '+@ServerName+'.BABW_ARCA.[dbo].[ADB_LOCATION] WITH(NOLOCK))'

EXEC (@SQL)
```

