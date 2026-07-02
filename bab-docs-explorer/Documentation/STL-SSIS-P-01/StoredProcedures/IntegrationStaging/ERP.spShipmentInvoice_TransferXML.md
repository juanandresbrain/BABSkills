# ERP.spShipmentInvoice_TransferXML

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["ERP.spShipmentInvoice_TransferXML"]
    ERP_ShipmentInvoice(["ERP.ShipmentInvoice"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ERP.ShipmentInvoice |

## Stored Procedure Code

```sql
CREATE proc [ERP].[spShipmentInvoice_TransferXML]
@Entity varchar(10)

as

-- =====================================================================================================
-- Name:  ERP.spShipmentInvoice_TransferXML
--
-- Description:	Outputs Shipment Invoice XML 
--				 
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		2017-12-14		Created proc
-- =====================================================================================================

set nocount on;

with 
XMLStage (XML) as
	(
		select 
			DlvMode,
			InventLocationId,
			ItemId,
			--Null as LineNum, NULL,
			OrderRef,
			cast(sum(Qty) as int) as Qty,
			convert(varchar, ShipDate, 101) as ShipDate
			--NULL as UnitOfMeasure, NULL
		from ERP.ShipmentInvoice with (nolock)
		where Transmitted = 0
		and left(OrderRef,2) = 'TO'
		and Entity = @Entity 
		group by DlvMode, InventLocationId, ItemId, OrderRef, convert(varchar, ShipDate, 101)
		for xml path('rsmBABWMShipmentEntity'), root('Document'), Type
	)
select XML as XMLData
from XMLStage

ERP,spWarehouseInventoryAdjustmentXML_ByEntity,CREATE proc [ERP].[spWarehouseInventoryAdjustmentXML_ByEntity]
@entity nvarchar(4)


as 

set nocount on

;
with 
InventoryMultiple as
	(
		select uom.ProductNumber, uom.InventoryMultiple, uom.entity 
		from ERP.vwItemMasterUOM uom 
		join WMS.ItemMaster im with (nolock) on uom.ProductNumber=im.ItemNumber and uom.Entity=im.Entity
		where im.NecessaryProductionWorkingTimeSchedulingPropertyId = 'Supplies'
	),
InvAdj as
	(
		select 
			concat(
				replace(a.AdjustmentDate, '-', ''),
				a.WarehouseID,
				rank() over(order by a.WarehouseID, a.AdjustmentDate) 
			  )
			as JournalNumber,
			a.AdjustmentDate,
			a.ItemID,
			a.WarehouseID,
			SUM(a.Qty / im.InventoryMultiple) Qty
		from erp.WarehouseInventoryAdjustment a
		join InventoryMultiple im on a.ItemID = im.ProductNumber and a.Entity = im.Entity 
		where datediff(dd, a.InsertDate, getdate()) = 0
		and a.Entity = @Entity 
		group by 
			a.ItemID,
			a.WarehouseID,
			a.AdjustmentDate 
	),
LineNumbers as
	(
		select 
			JournalNumber,
			AdjustmentDate,
			ItemID,
			WarehouseID,
			Qty,
			rank() over(partition by JournalNumber order by AdjustmentDate, WarehouseID, ItemID) as LineNumber
		from InvAdj
		where JournalNumber in (select JournalNumber from erp.tmpInvAdj where exported = 0) --controlled via loop, ensures only working on one Journal at a time
		and Qty <> 0 --excludes qty errors due to inventory multiple conversion issue
	)

select 
	--'' as 'JOURNALNUMBER', 
	0 as 'ARELINESDELETEDAFTERPOSTING',
	--'' AS 'DEFAULTINVENTORYSITEID', 
	--'' AS 'DEFAULTWAREHOUSEID', 
	'Inventory adjustment journal oData' as 'DESCRIPTION',
	0 AS 'ISPOSTED',
	'IADJ' AS 'JOURNALNAMEID',
	getdate() AS 'POSTEDDATETIME',
	--'' AS 'POSTEDUSERID', 
	0 as 'POSTINGDETAILLEVEL',
	0 AS 'RESERVATIONMODE',
	1 AS 'VOUCHERNUMBERALLOCATIONRULE',
	0 AS 'VOUCHERNUMBERSELECTIONRULE',
	'IM-MOV' AS 'VOUCHERNUMBERSEQUENCECODE',
		(
			select 
				JournalNumber as 'JOURNALNUMBER',
				ItemID AS 'ITEMNUMBER',
				--'' AS 'PRODUCTCONFIGURATIONID', 
				--'' AS 'PRODUCTCOLORID', 
				--'' AS 'PRODUCTSIZEID', 
				--'' AS 'PRODUCTSTYLEID', 
				WarehouseID AS 'INVENTORYSITEID',
				WarehouseID as 'INVENTORYWAREHOUSEID',
				--'' AS 'ITEMBATCHNUMBER', 
				--'' AS 'ITEMSERIALNUMBER', 
				'MAIN' AS 'WAREHOUSELOCATIONID',
				--'' AS 'LICENSEPLATENUMBER', 
				--'' AS 'INVENTORYSTATUSID', 
				--'' AS 'CATCHWEIGHTQUANTITY',
				--'' AS 'COSTAMOUNT', 
				concat(WarehouseID, '-9999-19--') AS 'DEFAULTLEDGERDIMENSIONDISPLAYVALUE', 
				--'' AS 'FIXEDCOSTCHARGES', 
				Qty as 'INVENTORYQUANTITY', 
				'IADJ' AS 'JOURNALNAMEID',
				LineNumber AS 'LINENUMBER', 
				--'' AS 'OFFSETMAINACCOUNTIDDISPLAYVALUE', 
				cast(AdjustmentDate as datetime) as 'TRANSACTIONDATE'
				--'' as 'UNITCOST',
				--'' AS 'UNITCOSTQUANTITY'
			from LineNumbers 
			order by LineNumber 
			for xml path('InventInventoryMovementJournalEntryEntity'), Type
		)
for xml path('InventInventoryMovementJournalHeaderEntity'), root('Document'), Type

ES,spEmailEndlessAisleOrdersNotInEsell,CREATE PROC [ES].[spEmailEndlessAisleOrdersNotInEsell]

as

------------------------------------------------------------------------------------------------------------------------------------------------------------
---- [ES].[spEmailEndlessAisleOrdersNotInEsell]
----	Name		Date		Action		Details
----	Lizzy Timm	2023-11-20	Create Proc	Created procedure to identify endless aisle orders missing from Esell.  
----										The missing orders will send to the Develobears in an email and populate the ES.EndlessAisleOrdersNotInEnterpriseSelling table
------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Truncate ES.EndlessAisleOrdersNotInEnterpriseSelling
TRUNCATE TABLE ES.EndlessAisleOrdersNotInEnterpriseSelling

-- Populate EndlessAisle table
IF (Object_ID('tempdb..#EndlessAisle') IS NOT null) DROP TABLE #EndlessAisle
SELECT distinct
			so.[order_id],
			soli.orig_sequence_number,
			so.[create_time],
			cast(so.[business_date] as date) BusinessDate,
			so.[business_unit_id] StoreNumber,
			RIGHT(	'00000' 
					+ SUBSTRING(device_id, 2, 3), 5) 
					+ SUBSTRING(business_date, 3, 2) 
					+ SUBSTRING(business_date, 5, 2) 
					+ RIGHT(device_id, 2) 
					+ RIGHT('00000' 
					+ CAST(soli.orig_sequence_number AS VARCHAR(5)), 5) 
					+ '0101' 
					as 'EnterpriseSellingID',
			so.[total],
			so.[subtotal],
			so.[tax_total],
			so.[discount_total],
			so.[line_item_count],
			so.[order_status_code],
			so.[order_type_code],
			so.[amount_due],
			so.device_id,
			esb.ReferenceNumber,
			esb.OrderNumber
		INTO #EndlessAisle
		FROM papamart.[dw].[dbo].[JMC_sls_order] so
		join papamart.[dw].[dbo].[JMC_sls_order_line_item] soli ON so.order_id = soli.order_id
		left join ES.OMSReferenceNumberBridge (nolock) esb on 
			RIGHT('00000' + SUBSTRING(device_id, 2, 3), 5) + SUBSTRING(business_date, 3, 2) + SUBSTRING(business_date, 5, 2) + RIGHT(device_id, 2) + RIGHT('00000' + CAST(soli.orig_sequence_number AS VARCHAR(5)), 5) + '0101'
			= esb.EnterpriseSellingID
		where datediff(dd, so.create_time, getdate())<=14
		
-- Insert into EndlessAisleOrdersNotInEnterpriseSelling
INSERT INTO ES.EndlessAisleOrdersNotInEnterpriseSelling
SELECT DISTINCT
		ea.order_id,
		ea.orig_sequence_number,
		ea.create_time,
		ea.BusinessDate,
		ea.StoreNumber,
		ea.EnterpriseSellingID,
		ea.total,
		ea.subtotal,
		ea.tax_total,
		ea.discount_total,
		ea.line_item_count,
		ea.order_status_code,
		ea.order_type_code,
		ea.amount_due,
		ea.ReferenceNumber,
		ea.OrderNumber,
		ea.device_id,
		GETDATE() [AlertDate]
	FROM #EndlessAisle ea
	left join bedrockdb02.esell.esell.orders e (nolock) on ea.EnterpriseSellingID = right(e.order_id,20)
	--left join papamart.dw.azure.vwEntepriseSellingFact ef on right(ea.ReferenceNumber,20)=right(ef.ReferenceNumber,20)
	WHERE 1=1
		AND (ea.ReferenceNumber is null	or e.order_id is null)

--  Send email if any result
DECLARE @recipients VARCHAR(8000),
		@alertrecipients VARCHAR(8000),
		@Subject VARCHAR(80),
		@query VARCHAR(8000),
		@text NVARCHAR(MAX)

IF(SELECT COUNT(*) FROM ES.EndlessAisleOrdersNotInEnterpriseSelling) > 0
BEGIN
	SET @Subject = 'WARNING - ' + CONVERT(VARCHAR(4),(SELECT COUNT(DISTINCT EnterpriseSellingID) FROM ES.EndlessAisleOrdersNotInEnterpriseSelling)) + ' Missing Endless Aisle Orders'
	SET @recipients = 'Develobears@buildabear.com'
	SET @text = '<font face =arial size = 2>' +
		'The below Endless Aisle Orders from the last 14 days are not present in esell or the OMSReferenceNumberBridge. <br>' +
		'<br>' +
		'<table border="1" cellpadding="4" cellspacing="0" style="border: 1px solid black; border-collapse: collapse;" >' + 
		'<font face =arial size = 2>' +
		'<tr bgcolor=#D5D5F7 ><th>Business Date</th><th>Deivce ID</th><th>Sequence Num</th><th>EnterpriseSellingID</th><th>Order ID</th></tr>' +
		CAST ( ( SELECT td = BusinessDate,'',
				td = device_id, '', 
				td = orig_sequence_number, '',
				td = EnterpriseSellingID, '',
				td = order_id,''
			FROM ES.EndlessAisleOrdersNotInEnterpriseSelling
			ORDER BY BusinessDate
              FOR XML PATH('tr'), TYPE 
		) AS NVARCHAR(MAX) ) +
		'</table>' +
		'<font face =arial size = 1 color="#C0C0C0">' +
		'<br><br><br><br>' +
		'Server:  STL-SSIS-P-01 <br>' +
		'Job Name:  POS_JumpMindEndlessAisleOrdersNotInEntSelling <br>' +
		'Stored Proc:  [STL-SSIS-P-01].[IntegrationStaging].[ES].[spEmailEndlessAisleOrdersNotInEsell] <br>' +
		'Created by:  Lizzy Timm <br>' +
		'Team Ownership:  BI Admin <br>' +
		'<br><br>' +
		'<font face =arial size = 1><i>The information in this message may be privileged, “confidential” and protected from disclosure and/or intended only for the addressee(s) named above.  If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, please notify us immediately by replying to the message and deleting it from your computer.  Thank you beary much.</i></font>'

	EXEC msdb.dbo.sp_send_dbmail
	@profile_name = 'BIAdmin',
	@recipients = @recipients,
	@body = @text,
	@subject = @Subject,
	@body_format = 'HTML'
END
ES,spES_Sku_Merge,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [ES].[spES_Sku_Merge] 

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	  WITH department (style_code, department_id)
	  AS
	  (
		  SELECT s.style_code, hg2.[pos_merch_group_key] AS 'department_id'
		  FROM [BEDROCKDB02].[me_01].[dbo].[hierarchy_group] hg
		  INNER JOIN [BEDROCKDB02].[me_01].[dbo].[hierarchy_group] hg1 ON hg1.hierarchy_group_id = hg.parent_group_id
		  INNER JOIN [BEDROCKDB02].[me_01].[dbo].[hierarchy_group] hg2 ON hg2.hierarchy_group_id = hg1.parent_group_id
		  --INNER JOIN [me_01].[dbo].[hierarchy_group] hg3 ON hg2.hierarchy_group_id = hg3.parent_group_id
		  INNER JOIN [BEDROCKDB02].[me_01].[dbo].style_group sg ON hg.hierarchy_group_id = sg.hierarchy_group_id
		  INNER JOIN [BEDROCKDB02].[me_01].[dbo].style s ON sg.style_id = s.style_id
	  )
	  SELECT [retailer_id]
		  ,[sku_id]
		  ,[sku_price]
		  ,[product_id]
		  ,[inv_ver_req_cd]
		  ,[barcode]
		  ,[upc]
		  ,[pick_desc]
		  ,[sku_avail_date]
		  ,[sku_unavail_date]
		  ,[search_allowed_cd]
		  ,[rec_update_date]
		  ,[rec_create_date]
		  ,[rec_update_id]
		  ,d.[department_id]
	  INTO #wrk
	  FROM [BEDROCKDB02].[esell].[esell].[sku] s
	  LEFT JOIN department d ON s.product_id = d.style_code
	  UNION
	  SELECT 1 AS [retailer_id]
		  ,v.BaseID [sku_id]
		  ,null [sku_price]
		  ,v.ProductNumber [product_id]
		  ,'Y' [inv_ver_req_cd]
		  ,null [barcode]
		  ,v.UPC [upc]
		  ,v.ItemDescription [pick_desc]
		  ,null [sku_avail_date]
		  ,null [sku_unavail_date]
		  ,'Y' [search_allowed_cd]
		  ,GETDATE() [rec_update_date]
		  ,GETDATE() [rec_create_date]
		  ,1 [rec_update_id]
		  ,d.department_id [department_id] 
	  FROM [IntegrationStaging].[POS].[vwPOSOutbound_Products] v
	  INNER JOIN department d  ON v.StyleCode = d.style_code
	  WHERE style_code in ('035383');

	  MERGE ES.sku s
	  USING #wrk w
	  ON s.[retailer_id] = w.[retailer_id] AND s.sku_id = w.sku_id
	  WHEN MATCHed	
		THEN UPDATE 
			SET s.[sku_price] = w.[sku_price], s.[product_id] = w.[product_id], s.[inv_ver_req_cd] = w.[inv_ver_req_cd], s.[barcode] = w.[barcode], s.[upc] = w.[upc],
				s.[pick_desc] = w.[pick_desc], s.[sku_avail_date] = w.[sku_avail_date], s.[sku_unavail_date] = w.[sku_unavail_date], s.[search_allowed_cd] = w.[search_allowed_cd],
				s.[rec_update_date] = w.[rec_update_date]
				--,s.[rec_create_date] = w.[rec_create_date]
				,s.[rec_update_id] = w.[rec_update_id], s.[department_id] = w.[department_id]
	  WHEN NOT MATCHED BY TARGET
		THEN INSERT ([retailer_id], [sku_id], [sku_price], [product_id], [inv_ver_req_cd], [barcode], [upc], [pick_desc],
				[sku_avail_date], [sku_unavail_date], [search_allowed_cd], [rec_update_date], [rec_create_date], [rec_update_id], [department_id])
			 VALUES (w.[retailer_id], w.[sku_id], w.[sku_price], w.[product_id], w.[inv_ver_req_cd], w.[barcode], w.[upc], w.[pick_desc],
				w.[sku_avail_date], w.[sku_unavail_date], w.[search_allowed_cd], w.[rec_update_date], w.[rec_create_date], w.[rec_update_id], w.[department_id])
	  WHEN NOT MATCHED BY SOURCE
		THEN DELETE;
END
```

