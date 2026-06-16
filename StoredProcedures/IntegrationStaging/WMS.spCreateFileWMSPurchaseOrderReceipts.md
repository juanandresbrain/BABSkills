# WMS.spCreateFileWMSPurchaseOrderReceipts

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spCreateFileWMSPurchaseOrderReceipts"]
    WMS_PurchaseOrderReceipt(["WMS.PurchaseOrderReceipt"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.PurchaseOrderReceipt |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spCreateFileWMSPurchaseOrderReceipts]
@FilePath varchar(500) 



---------------------------------------------------------------------------------------------------------
--	Dan Tweedie	2019-07-02	Created proc to push PO Receipts from Dynamics WMS to Aptos / Merchandising. 
---------------------------------------------------------------------------------------------------------


as

set nocount on 

if (select count(*) from WMS.PurchaseOrderReceipt where Warehouse in ('9980','0980', '1013','0013', '2991', '8010') and PostedToAptosDate is NULL) > 0

begin
		declare @query varchar(1000),
				@date varchar(200),
				@file_name varchar(100),
				@file_location varchar(100),
				@sqlcmd varchar(1000),
				@query_text varchar(1000)

		select @query_text = 'exec IntegrationStaging.WMS.spSelectWMSPurchaseOrderReceipts'

		--set @date = convert(varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate())) -- Replaced on 2/21/2022 with below which includes TimeStamp
		set @date =  convert (varchar, datepart(yyyy, getdate())) + convert(varchar, datepart(mm, getdate())) + convert(varchar, datepart(dd, getdate()))+convert (varchar, datepart(hh, getdate())) +convert (varchar, datepart(Mi, getdate())) +convert (varchar, datepart(ss, getdate()))
		set @query = @query_text
		set @file_location = @FilePath
		set @file_name = 'STSIMPORECEIPT.WM' + convert(varchar, @date) +'.GO'
		set @sqlcmd = 'sqlcmd ' + ' -Q' + '"' + @query + '"' + ' -o' + '"' + @file_location + @file_name + '"' + ' -s"," -w100 -W'
		exec master..xp_cmdshell @sqlcmd

		update WMS.PurchaseOrderReceipt
		set PostedToAptosDate = getdate()
		where PostedToAptosDate is NULL 


end
```

