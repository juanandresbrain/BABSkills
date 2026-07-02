# dbo.spMerchandisingOutputStoreMasterCN

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputStoreMasterCN"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputStoreMasterCN]


as

-- =====================================================================================================
-- Name: spMerchandisingOutputStoreMasterCN
--
-- Description:	Outputs CSV file for CN Store Master
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/18/2016		Created proc
-- =====================================================================================================

set nocount on


declare @query varchar(1000),
		@date varchar(20),
		@filename varchar(100),
		@filelocation varchar(100),
		@server varchar(20),
		@database varchar(20),
		@sqlcmd varchar(1000)

select @query = 'set nocount on select * from me_01.dbo.VW_CNStoreMaster order by store_nbr'
select @date = cast(datepart(yyyy, getdate()) as varchar) + cast(datepart(mm, getdate()) as varchar) + cast(datepart(dd, getdate()) as varchar) + cast(datepart(hh, getdate()) as varchar) + cast(datepart(mi, getdate()) as varchar) + cast(datepart(ss, getdate()) as varchar)
select @filelocation = '\\kermode\FileRepository\MERCHANDISING\CN_Distro\OUTBOUND\StoreMaster\'
select @filename = 'CN_STORE_MASTER_' + @date + '.csv'
select @server = 'bedrockdb02'
select @database = 'me_01'
select @sqlcmd = 'sqlcmd -S' + @server + ' -d' + @database + ' -Q' + '"' + @query + '"' + ' -o' + '"' + @filelocation + @filename + '"' + ' -s"," -W -h-1 -f 65001' -- (-h-1) removes headers - - (-f 65001 sets to unicode (for chinese characters))
exec master..xp_cmdshell @sqlcmd
```

