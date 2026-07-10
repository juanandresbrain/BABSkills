# dbo.spShopperTrak_UpdateFileRecord

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spShopperTrak_UpdateFileRecord"]
    dbo_SHPR_TRK_FL_LOG(["dbo.SHPR_TRK_FL_LOG"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SHPR_TRK_FL_LOG |

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: spShopperTrak_UpdateFileRecord
--
-- Description: 
-- Insers a record in SHPR_TRK_FL_LOG to indicate that the file is being imported
--
--
-- 
--
-- Input:
--  @fl_nm   varchar(255)
--      @stat_id     int
--    10  Importing
--    20  Imported
--    30  Loading
--    40  ???
--    900 DONE
--    910 ERROR
--  @row_cnt     int  --logs only the rowcount of the rows imported
--
-- Output: 
--  @fl_id   int
--
-- Dependencies: 
--
-- EXAMPLE:
--  exec dwstaging.dbo.spShopperTrak_UpdateFileRecord 1, 20
--
-- Revision History
--  Name:   Date:      Comments:
--  Rick Caminiti 04/23/2012  created
-- =============================================================================================================

CREATE PROCEDURE [dbo].[spShopperTrak_UpdateFileRecord]
(
    @fl_id  varchar(255) = null,
    @stat_id  int,
    @row_cnt  int = null
)
AS
BEGIN
SET NOCOUNT ON;

DECLARE @UPD_DT datetime,
    @prev_stat_id int;

SELECT  @UPD_DT = getdate(),
	   /*prev_stat_id is the sequential status prior to the status that was passed as a parameter
	   The order currently is 10, 20, 30, 900*/
	   @prev_stat_id = case @stat_id when 900 then 30 when 30 then 20 end;

IF @fl_id is null 
/*If file ID is null, this is being called as a bulk operation, so we need to update all rows
  to the new status that are in the old status.  This is called while moving the data from staging
  to dw.  Set all records that are ready to be processed to processing (from 20 to 30)*/
    BEGIN
    UPDATE [dbo].[SHPR_TRK_FL_LOG]
       SET [STAT_ID] = @stat_id
          ,[UPD_DT] = @UPD_DT
     WHERE [STAT_ID] = @prev_stat_id
    END
ELSE
/*File id is present, so only update the status of this one file to the new status 
  and add the rowcound value if it is passed along (this is passed in when the file 
  is actually processed for the first time*/
    BEGIN
    UPDATE [dbo].[SHPR_TRK_FL_LOG]
       SET [STAT_ID] = @stat_id
		,[ROW_CNT] = ISNULL(@row_cnt, [ROW_CNT])
          ,[UPD_DT] = @UPD_DT
     WHERE [SHPR_TRK_FL_LOG_ID] = @fl_id
    END


SELECT @@ROWCOUNT UPD_CNT

END
```

