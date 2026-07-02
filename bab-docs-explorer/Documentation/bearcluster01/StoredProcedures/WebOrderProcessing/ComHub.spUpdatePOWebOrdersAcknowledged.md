# ComHub.spUpdatePOWebOrdersAcknowledged

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["ComHub.spUpdatePOWebOrdersAcknowledged"]
    ComHub_ComhubFTPLog(["ComHub.ComhubFTPLog"]) --> SP
    ComHub_POWebOrder(["ComHub.POWebOrder"]) --> SP
    ComHub_POWebOrderStatus(["ComHub.POWebOrderStatus"]) --> SP
    ComHub_Status(["ComHub.Status"]) --> SP
    ComHub_vwPOWebOrderCurrentStatus(["ComHub.vwPOWebOrderCurrentStatus"]) --> SP
    ComHub_xmlFile(["ComHub.xmlFile"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ComHub.ComhubFTPLog |
| ComHub.POWebOrder |
| ComHub.POWebOrderStatus |
| ComHub.Status |
| ComHub.vwPOWebOrderCurrentStatus |
| ComHub.xmlFile |

## Stored Procedure Code

```sql
CREATE PROCEDURE [ComHub].[spUpdatePOWebOrdersAcknowledged]

AS

-- =============================================================================================================
-- Name: spUpdatePOWebOrdersAcknowledged
--
-- Description:	PowebOrders to Functional Acknowledged
--
-- Output: 
-- 
-- Available actions:
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		2020-10-09		Initial Creation
--		

BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @poPlaceStatusId INT, @poAcknowledged INT
    SELECT @poPlaceStatusId = StatusId FROM WebOrderProcessing.ComHub.[Status] WHERE Keyword = 'POPLACED'
	SELECT @poAcknowledged = StatusId FROM WebOrderProcessing.ComHub.[Status] WHERE Keyword = 'POACKNOWLEDGED'

    IF OBJECT_ID('tempdb..#tmpComhubFTPLog') IS NOT NULL
		DROP TABLE #tmpComhubFTPLog

	SELECT [ComhubFileName]
      ,[UploadDateTime]
      ,[Success]
	  ,xmlTypeId
	INTO #tmpComhubFTPLog
    FROM [STL-SSIS-P-01].[IntegrationStaging].[ComHub].[ComhubFTPLog]
	WHERE xmlTypeId = 1 AND Success = 1
	AND [UploadDateTime] > GETDATE() -1

	INSERT INTO [WebOrderProcessing].[ComHub].[POWebOrderStatus] ([POWebOrderId]
        ,[StatusId]
        ,[CreatedBy]
      ,[CreatedOn])
    SELECT v.POWebOrderId
          ,@poAcknowledged
		  ,SYSTEM_USER
		  ,GETDATE()
    FROM [ComHub].[vwPOWebOrderCurrentStatus] v
	INNER JOIN [ComHub].POWebOrder p ON v.POWebOrderId = p.POWebOrderId
	INNER JOIN [ComHub].xmlFile f ON p.FAxmlId = f.xmlFileId
	INNER JOIN #tmpComhubFTPLog t ON f.xmlFileName = t.ComhubFileName
    WHERE StatusId = @poPlaceStatusId

END
```

