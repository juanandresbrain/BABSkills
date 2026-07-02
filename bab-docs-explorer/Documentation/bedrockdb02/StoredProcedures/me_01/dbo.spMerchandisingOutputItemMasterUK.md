# dbo.spMerchandisingOutputItemMasterUK

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputItemMasterUK"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputItemMasterUK]

as

-- =====================================================================================================
-- Name: spMerchandisingOutputItemMasterUK
--
-- Description:	Outputs CSV file for UK Item Master
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		03/31/2015		Created proc
-- =====================================================================================================

set nocount on


declare @query varchar(1000),
		@date varchar(52),
		@filename varchar(100),
		@file_location varchar(100),
		@server varchar(20),
		@database varchar(20),
		@bcp varchar(1000)

		set @query = 'set nocount on select * from me_01.dbo.VW_UKItemMaster order by style_code'
		select @date = cast(datepart(yyyy, getdate()) as varchar) + cast(datepart(mm, getdate()) as varchar) + cast(datepart(dd, getdate()) as varchar)
		set @file_location = '\\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\ItemMaster\'
		set @filename = 'STOCK_FILE' + @date + '.csv'
		set @server = 'bedrockdb02'
		set @database = 'me_01'
		set @bcp = 'bcp "' + @query + '" queryout "' + @file_location + @filename + '"  -T -w -S' + @server 

		exec master..xp_cmdshell @bcp
```

