# dbo.spGuestLoad_CRM_Get_RecordsProcessedToday

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGuestLoad_CRM_Get_RecordsProcessedToday"]
    dbo_GuestLoad_CRM_RecordsProcessed(["dbo.GuestLoad_CRM_RecordsProcessed"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GuestLoad_CRM_RecordsProcessed |

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: spGuestLoad_CRM_Get_RecordsProcessedToday
--
-- Description:	
--		This procedure Returns the number of records already processed
--		by the CRM_File_Generation processor today
--
-- Input:
--		None
--
-- Output: 
--		The number of records already processed today
--
-- Dependencies: 
--
-- EXAMPLE:
--		? = exec spGuestLoad_CRM_Get_RecordsProcessedToday
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		12/30/2010		created
-- =============================================================================================================
CREATE PROCEDURE [dbo].[spGuestLoad_CRM_Get_RecordsProcessedToday]
	@recordsProcessedToday  INT OUTPUT	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
    SET NOCOUNT ON ;

    --DECLARE @recordsProcessedToday int
    DECLARE @today datetime
    SET @today = CAST(CONVERT(varchar(10), GETDATE(), 120) AS datetime)
    SET @recordsProcessedToday = ISNULL(
    (SELECT
         recordsProcessed
     FROM
         dbo.GuestLoad_CRM_RecordsProcessed WITH (NOLOCK)
     WHERE
     dateProcessed = @today), 0)

    --RETURN @recordsProcessedToday
END
```

