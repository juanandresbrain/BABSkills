# dbo.spGetvwOutputData

**Database:** BABWForgetMe_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGetvwOutputData"]
    dbo_vwOutputData(["dbo.vwOutputData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwOutputData |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spGetvwOutputData] 
	@recordKey AS VARCHAR(30)
AS

-- =============================================================================================================
-- Name: spGetvwOutputData
--
-- Description:	
--
-- Output: 
--	ds
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		06/11/2018		Initial Creation
-- =============================================================================================================

BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	WITH _vwOutputDataEmail(EmailAddress)
	AS
	(
	SELECT DISTINCT EmailAddress
	FROM [BABWForgetMe].[dbo].[vwOutputData]
	WHERE RecordKey = @recordKey AND EmailAddress IS NOT NULL
	),
	_vwOutputData([AppName], [RecordKey], [FirstName], [LastName], [Phone1], [Phone2], [Address1], [Address2], [Address3]
	    		 ,[City], [State], [PostalCode], [Country], [OuputKey], [Notes])
	AS
	(
	SELECT [AppName], [RecordKey], [FirstName], [LastName], [Phone1], [Phone2], [Address1], [Address2], [Address3]
		  ,[City], [State], [PostalCode], [Country], [OuputKey], [Notes]
	FROM [BABWForgetMe].[dbo].[vwOutputData]
	  WHERE RecordKey = @recordKey
	)
	  SELECT '<?xml version="1.0" encoding="UTF-8"?>' +
		CAST(( SELECT EmailAddress
			 ,(SELECT [AppName] AS '@app-name'
			         ,[RecordKey]
					 ,ISNULL([FirstName], '') AS 'FirstName'
					 ,ISNULL([LastName], '') AS 'LastName'
					 ,ISNULL([Phone1], '') AS 'Phone1'
					 ,ISNULL([Phone2], '') AS 'Phone2'
					 ,ISNULL([Address1], '') AS 'Address1'
					 ,ISNULL([Address2], '') AS 'Address2'
					 ,ISNULL([Address3], '') AS 'Address3'
					 ,ISNULL([City], '') AS 'City'
					 ,ISNULL([State], '') AS 'State'
					 ,ISNULL([PostalCode], '') AS 'PostalCode'
					 ,ISNULL([Country], '') AS 'Country'
					 ,ISNULL([OuputKey], '') AS 'OutputKey'
					 ,ISNULL([Notes], '') AS 'Notes'
				FROM _vwOutputData 
				FOR XML PATH ('vwOutputData'), type)
	  FROM _vwOutputDataEmail
	  --WHERE RecordKey = '9897d8dbd99869e8a71cc161e8'
	  FOR XML PATH (''), ROOT('OutputData'), type
		) AS VARCHAR(MAX))
END
```

