# dbo.spMerchandisingOutputAsnCN

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingOutputAsnCN"]
    dbo_VW_CN_PO_ASN(["dbo.VW_CN_PO_ASN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.VW_CN_PO_ASN |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingOutputAsnCN]

as

-- =====================================================================================================
-- Name: spMerchandisingOutputShanghaiPO_ASN
--
-- Description:	Creates CSV file to contain PO's shipping to Shanghai warehouses
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		01/20/2016		Created proc.	
--		Tim Callahan	09/11/2018		Remarked out call of FTP within this proc, will have second SQL agent step call the FTP stored proc
--										This is because D365 integrations are dropping the same directory but relying on the existing FTP proc
--										If there are no applicable PO ASNs ready for export for Aptos, the FTP step wouldn't run 
-- =====================================================================================================

set nocount on

if (select count(*) from me_01.dbo.VW_CN_PO_ASN) > 0

begin

	declare @query varchar(1000),
			@date varchar(20),
			@filename varchar(100),
			@filelocation varchar(100),
			@server varchar(20),
			@database varchar(20),
			@sqlcmd varchar(1000),
			@query_text varchar(1000)

	select @query = 'set nocount on select * from VW_CN_PO_ASN'
	select @date = cast(datepart(yyyy, getdate()) as varchar) + cast(datepart(mm, getdate()) as varchar) + cast(datepart(dd, getdate()) as varchar) + cast(datepart(hh, getdate()) as varchar) + cast(datepart(mi, getdate()) as varchar) + cast(datepart(ss, getdate()) as varchar) 
	select @filelocation = '\\kermode\FileRepository\MERCHANDISING\CN_Distro\OUTBOUND\ASN\'
	select @filename = 'CN_PO_ASN_' + @date + '.csv'
	select @server = 'bedrockdb02'
	select @database = 'me_01'
	select @sqlcmd = 'sqlcmd -S' + @server + ' -d' + @database + ' -Q' + '"' + @query + '"' + ' -o' + '"' + @filelocation + @filename + '"' + ' -s"," -W -h-1 -f 65001'-- (-h-1) removes headers - - (-f 65001 sets to unicode (for chinese characters))
	exec master..xp_cmdshell @sqlcmd

	--exec spMerchandisingFtpCN_ASN -- Remarked out on 9/11/2018 see notes

end
```

