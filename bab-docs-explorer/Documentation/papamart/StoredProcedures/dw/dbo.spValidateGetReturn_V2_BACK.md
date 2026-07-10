# dbo.spValidateGetReturn_V2_BACK

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spValidateGetReturn_V2_BACK"]
    dbo_GDPR_Customer_Lookup(["dbo.GDPR_Customer_Lookup"]) --> SP
    Item_value(["Item.value"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GDPR_Customer_Lookup |
| Item.value |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spValidateGetReturn_V2]
	@XMLToValidate AS XML

-- =============================================================================================================
-- Name: spValidateGetReturn
--
-- Description:	
--
-- Output: 
--	ds
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		05/07/2018		Initial Creation
-- =============================================================================================================

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	--DECLARE @XMLToValidate AS XML
	--SET @XMLToValidate = '<?xml version="1.0" encoding="utf-8"?><ValidateGetReturn><ValidationID>1</ValidationID><CustomerID>4D5A567F-EF99-4966-B41B-5FD91F627ECB</CustomerID></ValidateGetReturn>'
    DECLARE @ValidationID AS INT, @CustUID AS UNIQUEIDENTIFIER

	--SELECT @ValidationID = T.Item.value('VaidationID[1]', 'INT'),
	--       @guid = T.Item.value('CustUID[1]', 'UNIQUEIDENTIFIER')
	--FROM @XMLToValidate.nodes('/XMLToValid/ValidationID') AS T(Item)
	SELECT @ValidationID = T.Item.value('ValidationID[1]', 'INT')
	FROM @XMLToValidate.nodes('/ValidateGetReturn') AS T(Item)

	IF @ValidationID = 1
	BEGIN
		SELECT @CustUID = T.Item.value('CustomerID[1]', 'UNIQUEIDENTIFIER')
		FROM @XMLToValidate.nodes('/ValidateGetReturn') AS T(Item)

		PRINT CAST(@XMLToValidate AS VARCHAR(MAX))
		PRINT @ValidationID
		PRINT @CustUID

		SELECT '<?xml version="1.0" encoding="UTF-8"?>' + 
		CAST((
		SELECT @ValidationID AS 'ValidationID', [CustomerNo]
        FROM [CRMDB02].[crm].[dbo].[GDPR_Customer_Lookup]
		WHERE CustUID = @CustUID
		FOR XML PATH ('ValidateGetReturn'), type
		) AS VARCHAR(MAX))
	END
	IF @ValidationID = 2
	BEGIN
		SELECT @CustUID = T.Item.value('CustomerID[1]', 'UNIQUEIDENTIFIER')
		FROM @XMLToValidate.nodes('/ValidateGetReturn') AS T(Item)

		SELECT CAST([CustomerNo] AS VARCHAR(20))
        FROM [CRMDB02].[crm].[dbo].[GDPR_Customer_Lookup]
		WHERE CustUID = @CustUID
	END
END
```

