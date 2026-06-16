# ERP.spOutputXMLFile

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["ERP.spOutputXMLFile"]
    SP --> NoRefs(["No table dependencies detected"])
```

## Table Dependencies

_No table references detected automatically._

## Stored Procedure Code

```sql
CREATE proc [ERP].[spOutputXMLFile]
	@Query varchar(1000),
    @FileLocation varchar(5000),
	@FileName varchar(100)

as

-- =====================================================================================================
-- Name: WEB.spOutputXMLFile
--
-- Description:	Outputs XML file in UTF-8 format, accepts Query, FileLocation and FileName parameters
--		
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		05-15-2017		Created proc.	
-- =====================================================================================================

set nocount on


declare 
	@bcp varchar(5000)

set @bcp = 'bcp "' + @query + '" queryout "' + @FileLocation + @FileName + '"  -T -c -C65001' ----c -C65001 means to use UTF-8, otherwise -w means Unicode

exec master..xp_cmdshell @bcp
```

