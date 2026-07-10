# dbo.spGuestLoad_CRM_Set_RecordsProcessedToday

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGuestLoad_CRM_Set_RecordsProcessedToday"]
    dbo_GuestLoad_CRM_RecordsProcessed(["dbo.GuestLoad_CRM_RecordsProcessed"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GuestLoad_CRM_RecordsProcessed |

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: spGuestLoad_CRM_Set_RecordsProcessedToday
--
-- Description:	
--		This procedure save the number of records already processed
--		by the CRM_File_Generation processor today
--
-- Input:
--		@numberOfRecordsProcessed The number of records already processed today
--
-- Output: 
--		None
--
-- Dependencies: 
--
-- EXAMPLE:
--		exec spGuestLoad_CRM_Set_RecordsProcessedToday @numberOfRecordsProcessed = 500
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		12/30/2010		created
-- =============================================================================================================
CREATE PROCEDURE [dbo].[spGuestLoad_CRM_Set_RecordsProcessedToday] @numberOfRecordsProcessed int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
    SET NOCOUNT ON ;

    DECLARE @today datetime
    SET @today = CAST(CONVERT(varchar(10), GETDATE(), 120) AS datetime)
    IF EXISTS (SELECT
                   *
               FROM
                   dbo.GuestLoad_CRM_RecordsProcessed WITH (NOLOCK)
               WHERE
               dateProcessed = @today)

        BEGIN
            UPDATE
                dbo.GuestLoad_CRM_RecordsProcessed
            SET
                recordsProcessed = @numberOfRecordsProcessed
            WHERE
            dateProcessed = @today
            AND @numberOfRecordsProcessed IS NOT NULL
        END
    ELSE
        BEGIN
            INSERT INTO
                dbo.GuestLoad_CRM_RecordsProcessed
                (
                 dateProcessed
                ,recordsProcessed)
            VALUES
                (
                 @today
                ,@numberOfRecordsProcessed)
        END

END
```

