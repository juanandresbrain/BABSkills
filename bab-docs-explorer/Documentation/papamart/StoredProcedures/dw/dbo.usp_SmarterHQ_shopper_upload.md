# dbo.usp_SmarterHQ_shopper_upload

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.usp_SmarterHQ_shopper_upload"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[usp_SmarterHQ_shopper_upload]
as
/*
The proc grabs email addresses of shoppers in our stores in the last three days & uploads it to SmarterHQ. We use SmarterHQ to target abandoned online shopping carts.
This data was requested by Donna Mull so we can exclude the guests from the abandoned shopping cart emails that in the meantime have shopped in our store.
The data used is from the Survey reminder job that runs daily.
*/

set nocount on;
declare @bcpsql varchar(500)

SET @bcpsql = 'bcp ' + '"SELECT CAST(''email_addres'' AS VARCHAR(100)) AS email_address UNION ALL select distinct email_address from dw.dbo.tmp_ETEmailOSATUploadForeSee"' + ' queryout ' + '"\\kermode\FileRepository\Responsys\SmarterHQ\BABW_SmarterHQ.txt"' + ' -T -c'
--select @bcpsql
    
EXEC master..xp_cmdshell @bcpsql--, no_output
```

