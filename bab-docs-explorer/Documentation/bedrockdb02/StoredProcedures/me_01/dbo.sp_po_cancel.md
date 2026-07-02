# dbo.sp_po_cancel

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_po_cancel"]
    dbo_color(["dbo.color"]) --> SP
    dbo_currency(["dbo.currency"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_ib_audit_trail(["dbo.ib_audit_trail"]) --> SP
    dbo_keith_country(["dbo.keith_country"]) --> SP
    dbo_keith_ib_audit_trail(["dbo.keith_ib_audit_trail"]) --> SP
    dbo_keith_ib_audit_trail_pointer(["dbo.keith_ib_audit_trail_pointer"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_po(["dbo.po"]) --> SP
    dbo_po_line(["dbo.po_line"]) --> SP
    dbo_po_line_shipment(["dbo.po_line_shipment"]) --> SP
    dbo_po_location(["dbo.po_location"]) --> SP
    dbo_po_shipment(["dbo.po_shipment"]) --> SP
    dbo_po_shipment_udd(["dbo.po_shipment_udd"]) --> SP
    dbo_position(["dbo.position"]) --> SP
    dbo_ship_via(["dbo.ship_via"]) --> SP
    dbo_sku(["dbo.sku"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_color(["dbo.style_color"]) --> SP
    dbo_style_group(["dbo.style_group"]) --> SP
    dbo_style_retail(["dbo.style_retail"]) --> SP
    dbo_style_vendor(["dbo.style_vendor"]) --> SP
    dbo_terms(["dbo.terms"]) --> SP
    dbo_tpm_po_create_line_1(["dbo.tpm_po_create_line_1"]) --> SP
    dbo_upc(["dbo.upc"]) --> SP
    dbo_vendor(["dbo.vendor"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.color |
| dbo.currency |
| dbo.hierarchy_group |
| dbo.ib_audit_trail |
| dbo.keith_country |
| dbo.keith_ib_audit_trail |
| dbo.keith_ib_audit_trail_pointer |
| dbo.location |
| dbo.po |
| dbo.po_line |
| dbo.po_line_shipment |
| dbo.po_location |
| dbo.po_shipment |
| dbo.po_shipment_udd |
| dbo.position |
| dbo.ship_via |
| dbo.sku |
| dbo.style |
| dbo.style_color |
| dbo.style_group |
| dbo.style_retail |
| dbo.style_vendor |
| dbo.terms |
| dbo.tpm_po_create_line_1 |
| dbo.upc |
| dbo.vendor |

## Stored Procedure Code

```sql
CREATE procedure [dbo].[sp_po_cancel]

as
-- =====================================================================================================
-- Name: sp_po_cancel
--
-- Description:	
--
-- Input: 
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Keith Lee		xx/xx/xxx		Created proc.	
--		Tim Callahan	01/22/2016		Modified code to include China Warehouses 3970, 3980		
--		Tim Callahan	01/25/2018		Added China Warehouses 8502 to be included		
--		Tim Callahan	03/13/2018		Added China Warehouses 8502 to be included	
--		Lizzy Timm		01/09/2025		Added bonded China Warehouses 9942 to be included		
--		
-- =====================================================================================================

--- Canceled POs
-- Need to remove from PO Process Table incase PO gets reinstated later on.

select iat.application_identifier as po_no,
	   iat.entry_date as TransactionDate
into #keith_sp_po_cancel
from ib_audit_trail iat with (nolock)
join po po with (nolock) on iat.application_identifier = po.po_no
join po_location ploc  with (nolock) on po.po_id = ploc.po_id
join location l  with (nolock) on ploc.location_id = l.location_id
where iat.application = 'POM' 
and	iat.activity in ('Canceled')
and	po.po_status = 5
and	l.location_code in ('0980','0470','2970','0975','0960','3970','3980','9942','8502','8505','0013','2991') -- Added China Warehouses
and iat.ib_audit_trail_id between (select ib_audit_trail_id from keith_ib_audit_trail_pointer where pointer = 'start')
and (select ib_audit_trail_id from keith_ib_audit_trail_pointer where pointer = 'end')

-- PO by line for Merchandising
insert into tpm_po_create_line_1 (
	po_no,Type,EventCode,EventLocationInternalId,EventSourceLocationInternalId,InternalStatus,FulFillFlag,
	AcceptRqdMode,AcceptedFlag,OwnerID,ShipToldRef,ShipTo,ShipFromId,SupplierId,Hub1Id,BillTold,TypeCode,CurrencyDesc,OrderDate,PayTermsDesc,
	TransportMethodDesc,FOBDesc,COOCode,Rep1Id,OrderLine,AltDetailKey,ItemId,ItemDesc,AcceptedItemFlag,CurrQty,UOMCode,StartShipDate,EndDeliverDateTime,CancelDate,
	UnitCost,RetailPrice,ColorCode,ColorDesc,ItemAttr1,SupplierItemId,SupplierItemDesc,ShipToId,StdPackQty,StdCaseQty,CatchWeightFlag,Rep2Id,InternalStatusDetail,line_no,TransactionDate,TransactionType
)



--- US POs by line (Supplies and Merch)

select 	po.po_no as po_no,
	1 as "Type", --1= PO 4= transfer
	'1110' as "EventCode",
	'HostHQ' as "EventLocationInternalId",
	'HostHQ' as "EventSourceLocationInternalId",
	case when po.cancellation_reason = 3
	then
		'90'
	else
		'99' 
	end as "InternalStatus", -- 1=Planning,10=Open,85= Completed, 90=Closed,99=Cancelled
	1 as "FulFillFlag",
	1 as "AcceptRqdMode",
	1 as "AcceptedFlag",  -- 5 = Pending Partner Accept 1= Auto Accept	'Host' as "OwnerID",
	'Host' as "OwnerID",
	cast(l.location_code as int) as "ShipToldRef",
	cast(l.location_code as int) as "ShipTo",
	v.vendor_code as "ShipFromId",
	v.vendor_code as "SupplierId",
	'' as "Hub1Id",
	'HostHQ' as "BillTold",
	'1' as "TypeCode",
	cy.currency_description as "CurrencyDesc",
	po.order_date as "OrderDate",
	replace(t.terms_description,',',' ') as "PayTermsDesc",
	isnull(sv.ship_via_description,'Ocean') as "TransportMethodDesc",
	replace(po.fob_description,',',' ') as "FOBDesc",
	cty.country_code as "COOCode",
	p.position_label as "Rep1Id",
	pls.po_line_shipment_id as "OrderLine", --- VALID???? 09-19-20 - CONFIRMED with Roger
	0 as "AltDetailKey",
	s.style_code as "ItemId",
	replace(s.short_desc,',',' ') as "ItemDesc",
	1 as "AcceptedItemFlag",  -- 0 = Pending Parter Accept 1 = Auto Accept
	pls.quantity as "CurrQty",
	'' as "UOMCode",
	udd1.user_defined_date as "StartShipDate",
	ps.expected_receipt_date as "EndDeliverDateTime",
	udd2.user_defined_date as "CancelDate",
	'0' as "UnitCost",
	sr.current_selling_retail as "RetailPrice", 
	clr.color_code as "ColorCode",
	clr.color_short_description as "ColorDesc",
	u.upc_number as "ItemAttr1",
	substring(replace(stv.vendor_style,',',' '),1,25) as "SupplierItemId", -- limit it to 25
	replace(stv.vendor_style,',',' ') as "SupplierItemDesc",
	cast(l.location_code as int) as "ShipToId", 
 	s.distribution_multiple	as "StdPackQty",
 	s.order_multiple as "StdCaseQty",
	0 as "CatchWeightFlag",
	lower(left(iat.employee_first_name,1) + iat.employee_last_name) as "Rep2Id",
	case when po.cancellation_reason = 3
	then
		'90'
	when  po.cancellation_reason = 4
	then 
		'99' 
	end as "InternalStatusDetail",
	pl.line_no,
	(select max(TransactionDate) from #keith_sp_po_cancel where po.po_no = po_no) as TransactionDate,
	'Cancelled' as TransactionType
from po po with (nolock)
join position p with (nolock) on po.position_id = p.position_id
join vendor v with (nolock) on po.vendor_id = v.vendor_id
join currency cy with (nolock) on po.currency_id = cy.currency_id
left join ship_via sv with (nolock) on po.ship_via_id = sv.ship_via_id
left join terms t with (nolock) on po.terms_id = t.terms_id
join po_line pl with (nolock) on po.po_id = pl.po_id 
join keith_country cty with (nolock) on v.country_id = cty.country_id
join keith_ib_audit_trail iat with (nolock) on iat.po_no= po.po_no
join po_shipment ps with (nolock) on po.po_id = ps.po_id
join po_line_shipment pls with (nolock) on pl.po_line_id = pls.po_line_id
	and pl.po_id = pls.po_id
	and ps.po_shipment_id = pls.po_shipment_id
join po_location ploc with (nolock) on po.po_id = ploc.po_id
join location l with (nolock) on ploc.location_id = l.location_id
join po_shipment_udd udd1 with (nolock) on ps.po_shipment_id = udd1.po_shipment_id
	and ps.po_id = udd1.po_id
join po_shipment_udd udd2 with (nolock) on ps.po_shipment_id = udd2.po_shipment_id
	and ps.po_id = udd2.po_id
join style_vendor stv with (nolock) on po.vendor_id = stv.vendor_id
join style s with (nolock) on s.style_id = stv.style_id
join style_group sg with (nolock) on s.style_id = sg.style_id
join hierarchy_group hg with (nolock) on sg.hierarchy_group_id = hg.hierarchy_group_id
join style_retail sr with (nolock) on s.style_id = sr.style_id
join style_color sc with (nolock) on sc.style_id = s.style_id
join color clr with (nolock) on sc.color_id = clr.color_id
join sku sk with (nolock) on pl.style_color_id = sk.style_color_id
	and sk.style_color_id = sc.style_color_id
join upc u with (nolock) on sk.sku_id = u.sku_id
where udd1.po_date_type_id = 2
and	pls.quantity <> 0
and	udd2.po_date_type_id = 3
and	u.upc_number < '000000999999'
and	sr.jurisdiction_id = 1 -- home
and po.po_no in (select po_no from #keith_sp_po_cancel)
```

