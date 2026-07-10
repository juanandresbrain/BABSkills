# dbo.spFranchiseeFilesImportNoFilesEmail

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spFranchiseeFilesImportNoFilesEmail"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spFranchiseeFilesImportNoFilesEmail]
@franchisee varchar(2)

as

-- =====================================================================================================
-- Name: spFranchiseeFilesImportNoFilesEmail
--
--Description: Called from SSIS, sends email when no Franchisee files are found to import 

-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		12/22/2015		Created proc.	
--		Tim Bytnar		11/6/2017		Added the CN recipients in case statements
--		Anuhya Relangi	11/11/2019		Updated the IN recipients in case statment.
--		Anuhya Relangi	11/18/2019		Added new recipients to IN list
--		Anuhya Relangi	4/2/2020		Added new recipients to copy_recipients
-- =====================================================================================================


set nocount on

declare 
	@date varchar(10),
	@subj varchar(1000),
	@recip varchar(1000),
	@text varchar(1000),
	@FranchiseeText varchar(52)

select 
	@date = convert(varchar, getdate(), 101),

	@recip = case @Franchisee 
					when 'AU' then 'duane.roberts@buildabear.com.au'
				   when 'DE' then 'levent.isli@kidsretailgroup.com;Volker.Seitz@kids-fashion-group.com'
				   when 'MX' then 'luis.pena@buildabear.mx;victor.pena@buildabear.mx;'
				   when 'AE' then 'jong@buildabear.ae;mahesh@ajb.ae'
				   when 'TR' then 'nihala@buildabear.com.tr;arzukushan@ozsay.com;tufana@buildabear.com.tr;omerk@buildabear.com.tr'
				   when 'ZA' then 'alex@toykingdom.co.za;kyle@toykingdom.co.za;michelle@buildabear.co.za;Lance@toykingdom.co.za'
				   when 'SG' then 'duane.roberts@buildabear.com.au;Gavin.Port@buildabear.com.au'
				   when 'CN' then 'donald@harrys-kitchen.com;johan@harrys-kitchen.com;frank.lin@harrys-kinderactive.com;KevenXiao@buildabear.com;benjamin@harrys-kinderactive.com;benjamin@harrys-kitchen.com'
				   when 'IN' then 'steve.antony@pearldatadirect.com;raiji.jolly@pearldatadirect.com;tablez.it@pearldatadirect.com;sumanta.guha@in.tablez.com;arun.cs@in.tablez.com'
				   when 'CL' then 'sjerez@ansaldo.cl;alex@ansaldo.cl;jmadera_sistemas@ansaldo.cl'
					else 'biadmin@buildabear.com'
				 end,

	@FranchiseeText = case @Franchisee
						when 'AU' then '(Australia)'
						when 'DE' then '(Germany)'
						when 'MX' then '(Mexico)'
						when 'AE' then '(Gulf States)'
						when 'TR' then '(Turkey)'
						when 'ZA' then '(South Africa)'
						when 'SG' then '(Singapore)'
						when 'CN' then '(China)'
						when 'IN' then '(India)'
						when 'CL' then '(Chile)'
						end,
		
	@subj = 'Franchisee File Summary - ' + @franchisee + ' - ' + @FranchiseeText + ' - ' + @date + ' - No Files Found',
	@text = '<font face = arial size = 2>The franchisee files import procedure has completed for the ' + @franchisee + ' ' + @FranchiseeText + ' franchisee. There were no files on the server to import.</font><br><br>'
	 
exec msdb.dbo.sp_send_dbmail
	@profile_name = 'BIAdmin',
	@recipients = @Recip,
	@copy_recipients = 'biadmin@buildabear.com;victoriak@buildabear.com;GeorgeR@buildabear.co.uk;ColleenMe@buildabear.com',
	@body = @text,
	@subject= @subj,
	@body_format = 'HTML'
```

