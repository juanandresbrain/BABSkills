# WEB.spOutputPricebooks_Bak20220705

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WEB.spOutputPricebooks_Bak20220705"]
    WEB_spOutputXMLFile(["WEB.spOutputXMLFile"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WEB.spOutputXMLFile |

## Stored Procedure Code

```sql
CREATE proc [WEB].[spOutputPricebooks_Bak20220705]
 @FileNameDate datetime = NULL

as

set nocount on

-- =====================================================================================================
-- Name:  WEB.spOutputPricebooks
--
-- Description:	Outputs master catalog XML file for ecommerce integration, runs WEB.spOutputXMLFile (reusable proc for generating xml files)
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		2017-06-15		Created proc
-- =====================================================================================================


declare 
	@dateString varchar(20),
	@file varchar(100)

select @dateString = case when @FileNameDate is NULL 
							then replace(replace(replace(replace(convert(varchar, getdate(), 121), '-', ''), ':', ''), '.', ''),' ', '')
							else replace(replace(replace(replace(convert(varchar, @FileNameDate, 121), '-', ''), ':', ''), '.', ''),' ', '')
					end

select @file = @datestring + '_pricebooks_usd.xml'

	exec WEB.spOutputXMLFile
	 @Query = 'select XMLData from IntegrationStaging.WEB.vwPricebooksUSXML', 
	 @FileLocation = '\\STL-SSIS-P-01\IntegrationStaging\WEB\Outbound\Pricebook\', 
	 @FileName = @file

 select @file = @datestring + '_pricebooks_gbp.xml'

	 exec WEB.spOutputXMLFile
	 @Query = 'select XMLData from IntegrationStaging.WEB.vwPricebooksUKXML', 
	 @FileLocation = '\\STL-SSIS-P-01\IntegrationStaging\WEB\Outbound\Pricebook\', 
	 @FileName = @file
```

