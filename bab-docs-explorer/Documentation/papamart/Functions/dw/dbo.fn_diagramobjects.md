# dbo.fn_diagramobjects

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** int(4)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_diagramobjects"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

_No parameters._

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION dbo.fn_diagramobjects() 
	RETURNS int
	WITH EXECUTE AS N'dbo'
	AS
	BEGIN
		declare @id_upgraddiagrams		int
		declare @id_sysdiagrams			int
		declare @id_helpdiagrams		int
		declare @id_helpdiagramdefinition	int
		declare @id_creatediagram	int
		declare @id_renamediagram	int
		declare @id_alterdiagram 	int 
		declare @id_dropdiagram		int
		declare @InstalledObjects	int

		select @InstalledObjects = 0

		select 	@id_upgraddiagrams = object_id(N'dbo.sp_upgraddiagrams'),
			@id_sysdiagrams = object_id(N'dbo.sysdiagrams'),
			@id_helpdiagrams = object_id(N'dbo.sp_helpdiagrams'),
			@id_helpdiagramdefinition = object_id(N'dbo.sp_helpdiagramdefinition'),
			@id_creatediagram = object_id(N'dbo.sp_creatediagram'),
			@id_renamediagram = object_id(N'dbo.sp_renamediagram'),
			@id_alterdiagram = object_id(N'dbo.sp_alterdiagram'), 
			@id_dropdiagram = object_id(N'dbo.sp_dropdiagram')

		if @id_upgraddiagrams is not null
			select @InstalledObjects = @InstalledObjects + 1
		if @id_sysdiagrams is not null
			select @InstalledObjects = @InstalledObjects + 2
		if @id_helpdiagrams is not null
			select @InstalledObjects = @InstalledObjects + 4
		if @id_helpdiagramdefinition is not null
			select @InstalledObjects = @InstalledObjects + 8
		if @id_creatediagram is not null
			select @InstalledObjects = @InstalledObjects + 16
		if @id_renamediagram is not null
			select @InstalledObjects = @InstalledObjects + 32
		if @id_alterdiagram  is not null
			select @InstalledObjects = @InstalledObjects + 64
		if @id_dropdiagram is not null
			select @InstalledObjects = @InstalledObjects + 128
		
		return @InstalledObjects 
	END
	
dbo,fn_wbi_trans,SQL_TABLE_VALUED_FUNCTION,-- =============================================================================================================
-- Name: fn_wbi_trans
--
-- Description:	Used with nightly load process for Workbrain
--
-- Input: N/A
--
-- Output: returns transactions for each store, date, and 1/2 hour time increment 
--
-- Dependencies: Must be run from stored procedure xxxx
--
-- Revision History
--		Name:			Date:			Comments:
--		Keith Missey	9/7/2007		Created
--		Keith Missey	10/15/2007		made "trans" all upper case
--		Keith Missey	6/10/2009		remove dino and dolls from CASE statement
--		Keith Missey	8/26/2009		removed RZ from CASE statement and product division parameter
-- =============================================================================================================
CREATE FUNCTION dbo.fn_wbi_trans()
RETURNS @transoutput TABLE
    (
      SKDGRP_NAME varchar(40),
      INVTYP_ID smallint,
      RESDET_DATE char(10),
      RESDET_TIME char(8),
      RESDET_VOLUME money,
      INPUT_INVTYP_ID smallint,
      OLD_SKDGRP_NAME varchar(40),
      VOLTYPE_NAME varchar(200)
    )
AS BEGIN
        INSERT  @transoutput
            SELECT  RTRIM(CAST(store_id AS char)) + '-BAB TRANS',
                    3,
                    CONVERT(varchar(10), actual_date, 101),
                    CONVERT(varchar(2), hour) + ':'
                    + CASE WHEN half_hour_id = 1 THEN '00:00'
                           WHEN half_hour_id = 2 THEN '30:00'
                      END,
                    COUNT(DISTINCT transaction_id),
                    NULL,
                    NULL,
                    NULL
            FROM    dbo.tmp_wbi_rawdata_summary
            WHERE   partyflag = 0 AND [gaapsales] <> 0
            GROUP BY store_id,
                    actual_date,
                    hour,
                    half_hour_id

RETURN 
END
```

