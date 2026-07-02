# WM.spGetGiftCardInfo

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.spGetGiftCardInfo"]
    WEB_ProductCatalogMasterAttributes(["WEB.ProductCatalogMasterAttributes"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.ProductCatalogMasterAttributes |

## Stored Procedure Code

```sql
CREATE PROCEDURE [WM].[spGetGiftCardInfo]

-- =============================================================================================================
-- Name: spGetGiftCardInfo
--
-- Description:	Get Gift Card information for SalesAudit Transalate.
--
-- Output: 
--	
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		12/18/2017		Initial Creation
-- =============================================================================================================

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	SELECT [Style_Code]
	      ,[giftCardType]
    FROM [STL-SSIS-P-01].[IntegrationStaging].[WEB].[ProductCatalogMasterAttributes]
    WHERE giftCardType IS NOT NULL
END
```

