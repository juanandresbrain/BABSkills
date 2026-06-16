# WM.PrintFiles

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WM.PrintFiles"]
    SP --> NoRefs(["No table dependencies detected"])
```

## Table Dependencies

_No table references detected automatically._

## Stored Procedure Code

```sql
-- =============================================
-- Author:		John Eck
-- Create date: 9/28/17
-- Description:	allows passing parameters to print command for ssis printing of pickslips
-- =============================================
create PROCEDURE [WM].[PrintFiles] 
	-- Add the parameters for the stored procedure here
	
	@Filename varchar(200),
	@Printer varchar(100)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	Declare @PrintString varchar(500) = 'Print ' + @FileName + ' /d:' + @Printer

exec xp_cmdshell @PrintString
END


WMS,AptosToDynamicsResetForAPI,CREATE proc [WMS].[AptosToDynamicsResetForAPI]

as 
---------------------------------------------------------------------------------------------------------------------
--Dan Tweedie 2020-09-24 - Create proc to reset PO's to export again to Dynamics if they meet these conditions:
--							1) Failed in API due to item number does not exist
--							3) PO has still not successfully passed API
--							2) Item Number now does exist
---------------------------------------------------------------------------------------------------------------------


set nocount on 
;

with 
PO as
	(
		select 
			api.AptosDocumentNumber PONumber, 
			substring(api.ResponseBody, charindex('Item Number ', api.ResponseBody, 1)+12, 6) ItemNumber
		from wms.DynamicsAPILog api with (nolock)
		where IntegrationName='WMS_PurchaseOrderToDynamics'
		and ResponseBody like '%Item number%does not exist%'
		and not exists ( 
							select x.AptosDocumentNumber
							from wms.DynamicsAPILog x with (nolock)
							where x.IntegrationName='WMS_PurchaseOrderToDynamics' 
							and x.ResponseBody like '%"hasErrors":false%'
							and x.AptosDocumentNumber=api.AptosDocumentNumber
							and x.InsertDate > api.InsertDate
						) 
		group by api.AptosDocumentNumber, substring(api.ResponseBody, charindex('Item Number ', api.ResponseBody, 1)+12, 6)
		having max(api.InsertDate) <= 30
	)
update x
set x.ExportedToDynamicsDate=NULL
from wms.PurchaseOrderMerchToDynamics x
join PO on x.PONumber=PO.PONumber
where exists (
				select 
					im.ProductNumber 
				from wms.ItemMasterProducts im 
				where im.ProductNumber=po.ItemNumber
				group by 
					im.ProductNumber
			 )
;

WMS,archive,CREATE proc [WMS].[archive]
as 
begin 
EXEC master..xp_cmdshell 'move \\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\* \\kermode\FileRepository\MERCHANDISING\UK_Distro\OUTBOUND\done'
end 

WMS,ASNToDynamicsResetForAPI,CREATE proc [WMS].[ASNToDynamicsResetForAPI]

as 
---------------------------------------------------------------------------------------------------------------------
--Dan Tweedie 2020-09-24 - Create proc to reset ASN's to export again to Dynamics if they meet these conditions:
--							1) Failed in API due to Aptos PO Not Found
--							2) ASN is still not in Dynamics
--							3) PO is now in Dynamics
---------------------------------------------------------------------------------------------------------------------


			--stage ASNs which successsfully created in Dynamics
			select 
				ASNShipmentNumber,
				max(EnqueuedTimeCST) MaxQueue
			into #NoFail
			from wms.ASN_CreateConfirmation
			where Message like '%Aptos PO%successfully assigned to ASN%'
			group by ASNShipmentNumber
			
			--stage ASNs which failed in Dynamics due to Deadlock
			select 
				ASNShipmentNumber,
				max(EnqueuedTimeCST) MaxQueue
			into #Fail
			from wms.ASN_CreateConfirmation 
			where Errormessage like '%Deadlock%'
			or ErrorMessage like '%An update conflict occurred due to another user%'
			group by ASNShipmentNumber

			----stage ASNs successfully logged in API log
			--select x.TPMShipmentNumber ASN
			--into #ASNCreated
			--from wms.DynamicsAPILog x with (nolock)
			--where x.IntegrationName='WMS_ASNCreate'
			--and x.ResponseBody like '%"hasErrors":false%'

			----stage Aptos PO's successfully logged in API log
			--select xx.AptosDocumentNumber
			--into #POCreated
			--from wms.DynamicsAPILog xx with (nolock)
			--where xx.IntegrationName='WMS_PurchaseOrderToDynamics' 
			--and xx.ResponseBody like '%"hasErrors":false%'

			--stage ASNs with error in API log due to PO not found in Dynamics, when the PO is now in Dynamics, but the ASN is not
			--select 
			--	api.TPMShipmentNumber ASN
			--into #ASN
			--from wms.DynamicsAPILog api with (nolock)
			--where IntegrationName='WMS_ASNCreate'
			--and ResponseBody like '%hasErrors":true%'
			--and ResponseBody like '%Purchase Order not found with Aptos PO Ref Number%'
			--and not exists ( 
			--					select ASN, ResponseBody
			--					from #ASNCreated x
			--					where x.ASN=api.TPMShipmentNumber
			--				) 
			--and exists ( 
			--				select xx.AptosDocumentNumber
			--				from #POCreated xx
			--				where xx.AptosDocumentNumber=substring(api.ResponseBody, charindex('Purchase Order not found with Aptos PO Ref Number ', api.ResponseBody, 1)+50, 7)
			--			) 
			--UNION --stage ASNs that failed in Dynamics due to deadlock, which are not in the ASN confirmation
			select f.ASNShipmentNumber ASN
			into #ASN
			from #Fail f
			where not exists 
				(
					select nf.ASNShipmentNumber 
					from #NoFail nf
					where nf.ASNShipmentNumber=f.ASNShipmentNumber
					and nf.MaxQueue>f.MaxQueue
				)
	
	update a
	set a.SentTo365=NULL
	from wms.ASN_TPMToDynamics a
	where exists (select x.ASN from #ASN x where x.ASN=a.Shipment)
	and datediff(dd, a.InsertDate, getdate()) <= 1
	and Shipment<>'SH0000035497'
;





;
/*
	with 
	NoFail as
		(
			select 
				ASNShipmentNumber,
				max(EnqueuedTimeCST) MaxQueue
			from wms.ASN_CreateConfirmation
			where Message like '%Aptos PO%successfully assigned to ASN%'
			group by ASNShipmentNumber
		),
	Fail as
		(
			select 
				ASNShipmentNumber,
				max(EnqueuedTimeCST) MaxQueue
			from wms.ASN_CreateConfirmation 
			where Errormessage like '%Deadlock%'
			or ErrorMessage like '%An update conflict occurred due to another user%'
			group by ASNShipmentNumber
		),
	ASN as
		( 
			select 
				api.TPMShipmentNumber ASN
			--	substring(api.ResponseBody, charindex('Purchase Order not found with Aptos PO Ref Number ', api.ResponseBody, 1)+50, 7) PONumber
			from wms.DynamicsAPILog api with (nolock)
			where IntegrationName='WMS_ASNCreate'
			and ResponseBody like '%hasErrors":true%'
			and ResponseBody like '%Purchase Order not found with Aptos PO Ref Number%'
			and not exists ( 
								select x.TPMShipmentNumber ASN, ResponseBody
								from wms.DynamicsAPILog x with (nolock)
								where x.IntegrationName='WMS_ASNCreate'
								and x.ResponseBody like '%"hasErrors":false%'
								and x.TPMShipmentNumber=api.TPMShipmentNumber
							) 
			and exists ( 
							select xx.AptosDocumentNumber
							from wms.DynamicsAPILog xx with (nolock)
							where xx.IntegrationName='WMS_PurchaseOrderToDynamics' 
							and xx.ResponseBody like '%"hasErrors":false%'
							and xx.AptosDocumentNumber=substring(api.ResponseBody, charindex('Purchase Order not found with Aptos PO Ref Number ', api.ResponseBody, 1)+50, 7)
						) 
			UNION 
			select f.ASNShipmentNumber
			from Fail f
			where not exists 
				(
					select nf.ASNShipmentNumber 
					from NoFail nf
					where nf.ASNShipmentNumber=f.ASNShipmentNumber
					and nf.MaxQueue>f.MaxQueue
				)
		)
	update a
	set a.SentTo365=NULL
	from wms.ASN_TPMToDynamics a
	where exists (select x.ASN from ASN x where x.ASN=a.Shipment)
	and datediff(dd, a.InsertDate, getdate()) <= 90
	and Shipment<>'SH0000035497'
;
*/
```

