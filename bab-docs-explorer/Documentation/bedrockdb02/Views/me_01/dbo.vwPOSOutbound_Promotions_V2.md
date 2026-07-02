# dbo.vwPOSOutbound_Promotions_V2

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOSOutbound_Promotions_V2"]
    dbo_deal(["dbo.deal"]) --> VIEW
    dbo_deal_discount(["dbo.deal_discount"]) --> VIEW
    dbo_deal_item_disc_spec(["dbo.deal_item_disc_spec"]) --> VIEW
    dbo_deal_item_req(["dbo.deal_item_req"]) --> VIEW
    dbo_deal_location(["dbo.deal_location"]) --> VIEW
    dbo_deal_tier_definition(["dbo.deal_tier_definition"]) --> VIEW
    dbo_enum_price_chg_doc_status(["dbo.enum_price_chg_doc_status"]) --> VIEW
    dbo_item_group(["dbo.item_group"]) --> VIEW
    dbo_jurisdiction(["dbo.jurisdiction"]) --> VIEW
    dbo_location(["dbo.location"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.deal |
| dbo.deal_discount |
| dbo.deal_item_disc_spec |
| dbo.deal_item_req |
| dbo.deal_location |
| dbo.deal_tier_definition |
| dbo.enum_price_chg_doc_status |
| dbo.item_group |
| dbo.jurisdiction |
| dbo.location |

## View Code

```sql
CREATE view [dbo].[vwPOSOutbound_Promotions_V2]

--------------------------------------------------------------------------------------------------------------------------------------
--	Ian Wallace		2022-12-11	-- Created view for Jumpmind POS postgres Promotions table  
--	Tim Callahan	2023-12-07	-- Official Remark that this View  is used for QA Jumpmind 
--	Tim Callahan	2023-12-18	-- Added Handling for Ad Hoc  Docs to Force Through
--	Tim Callahan	2024-01-04	-- Added Handling to DateAdd 1 day for all promotions so they expire at Midnight the next day
--								-- Example Documents on Jan Support Issue ('012021','012022','012023','012024')
--------------------------------------------------------------------------------------------------------------------------------------
as

with PromoDataStage as
(
select distinct
	isnull(dd.deal_discount_id, d.deal_id) deal_discount_id,
	d.deal_id, 
	d.deal_no, 
	d.name deal_name, 
	d.description deal_description, 
	--case when d.deal_id in (4442,4443,4444,4445) then '2023-07-24' else cast(d.effective_from_date as date) end as DealStartDate,  
	--case when d.deal_id in (4438,4439,4440,4441) then '2023-07-24' else cast(d.effective_to_date as date) end as DealEndDate,
	case when d.deal_no in ('012025')
			then '2023-12-18'
		when d.deal_no in ('012058','012059','012060','012061')
			then '2023-02-13'
		when d.deal_no in ('012072','012073','012074','012075') -- Added 4/2/2024
			then '2024-04-02'
		when d.deal_no in ('012076','012077','012078','012079') -- Added 4/12/2024
			then '2024-04-12'
		when d.deal_no in ('012084','012085','012086','012087') -- Added 5/1/2024
			then '2024-05-01'
		when d.deal_no in ('012088','012089','012090','012091') -- Added 5/21/2024
			then '2024-05-21'
		when d.deal_no in ('012100','012099','012098','012097') -- Added 6/10/2024
			then '2024-06-10'
		when d.deal_no in ('012102','012103','012104','012105') -- Added 6/10/2024
			then '2024-06-11'
		when d.deal_no in ('012124','012125','012126','012127') -- Added 7/16/2024
			then '2024-07-16'
		when d.deal_no in ('012138','012139','012140') -- Added 8/28/2024
			then '2024-08-28'
		when d.deal_no in ('012148','012149','012150') -- Added 9/11/2024
			then '2024-09-11'
		when d.deal_no in ('012166','012167') -- Added 10/09/2024
			then '2024-10-09'
		when d.deal_no in ('012179') -- Added 10/31/2024
			then '2024-10-05'
		else cast(d.effective_from_date as date) end as DealStartDate, -- Add Case Statements For TESTING Specific Date Forward deals 
	--cast(d.effective_from_date as date) as DealStartDate,  
	--case when d.deal_no in ('012025') 
	--	then '2023-12-18'
	--	else cast(d.effective_to_date as date) end as DealEndDate, -- For Testing Specific Date Forward deals and terminating deals that would be ended by now 
	--cast(d.effective_to_date as date) as DealEndDate, 
	cast(dateadd(dd,1,d.effective_to_date) as date) as DealEndDate, -- Replaced Above on 1/4/2024

	dd.type deal_discount_type, 
	dd.name deal_discount_name,  
	dtd.disc_type as DealTierDef_DiscType,
	dtd.disc_pct as DealTierDef_DiscPct,
	dtd.disc_amt as DealTierDef_DiscAmt,
	dtd.disc_applies_to as DealTierDef_DiscAppliesTo,
	dtd.disc_qty as DealTierDef_DiscQty,
	dtd.add_info as DealTierDef_AddlInfo,
	dtd.threshold_type as DealTierDef_ThresholdType,
	dtd.threshold_qty as DealTierDef_ThresholdQty,
	dtd.threshold_amt as DealTierDef_ThresholdAmt,
	isnull(ig.item_group_id,0) as DealItemRequired_ItemGroup,
	dir.quantity DealItemReqQty,
	j.jurisdiction_code DealLocationJurisdictionCode,
	l.gl_location_number as DealLocation,
	dids.identity_type as DealItemDiscSpec_IdentityType,
	dids.quantity as DealItemDiscSpec_Qty,
	dids.disc_type as DealItemDiscSpec_DiscType,
	dids.disc_pct as DealItemDiscSpec_DiscPct,
	dids.disc_amt as DealItemDiscSpec_DiscAmt,
	--dids.disc_applies_to as DealItemDiscSpec_DiscAppliesTo
	case 
		when d.deal_id in 
			(
				4438,
				4439,
				4440,
				4441,
				4442,
				4443,
				4444,
				4445
			) then 'DMTX' ---special handling for specific 'xmas in july promotion' that otherwise will not work correctly in Jump Mind
		else dids.disc_applies_to
	end as DealItemDiscSpec_DiscAppliesTo
from [dbo].[deal] d
join jurisdiction j 
	on d.jurisdiction_id=j.jurisdiction_id
	and j.jurisdiction_code in ('CA','UK','HOME','IE')
join [dbo].[deal_discount] dd on d.deal_id = dd.deal_id
join [dbo].[deal_tier_definition] dtd 
	on d.deal_id=dtd.deal_id
	and dtd.deal_discount_id = dd.deal_discount_id
left join [dbo].[deal_item_req] dir 
	on d.deal_id=dir.deal_id
	and dir.deal_discount_id = dd.deal_discount_id
left join item_group ig on dir.item_group_num=ig.item_group_id
left join deal_item_disc_spec dids 
	on d.deal_id=dids.deal_id
	and dd.deal_discount_id=dids.deal_discount_id
	and dir.item_group_num=dids.item_group_num      
left join deal_location dl on d.deal_id=dl.deal_id
left join location l on dl.location_id=l.location_id 
join enum_price_chg_doc_status s2 on s2.enum=d.document_status -- Added 12/07/2023

where 1=1
--and d.deal_no in ('012166','012167')
--and (dd.deal_discount_id is not null or d.name like '%party%')
and d.name not like '%party%'
and (
		s2.enum not in ('0','1','5') -- Exclude Documents in New, Preliminary and Canceled Statuses -- Query for all statuses here:  select * from enum_price_chg_doc_status -- Added 12/07/2023
	or 
		d.deal_no  in ('012025','012138','012139','012140') -- Allows Test Documents to flow despite status - Added 12/18/2023
	)
and 
	(
		( --current promotions only
			getdate() between cast(dateadd(dd,-7,d.effective_from_date) as date)
			and
			--cast(isnull(d.effective_to_date,'3030-12-31') as date)			
			cast(isnull(cast(dateadd(dd,1,d.effective_to_date) as date) ,'3030-12-31') as date) -- Replaced Above on 1/4/2024
		)
		OR
		d.deal_no in ('012124','012125','012126','012127','012138','012139','012140','012166','012167') -- Added 7/16/2024
	)

),  


MinDealDiscountId as  (

select 
deal_no, 
deal_id,
min (deal_discount_id) as MinDealDiscountId
from PromoDataStage pds
where 1=1 
group by 
deal_no, 
deal_id, 
deal_no 

)


,Summary1 as (

select 
m.deal_no as Min_Deal_no, 
pds.deal_discount_id, 
pds.deal_id, 
pds.deal_no, 
pds.deal_name, 
pds.deal_description, 
pds.DealStartDate, 
pds.DealEndDate, 
pds.deal_discount_type, 
pds.deal_discount_name, 
pds.DealTierDef_DiscType, 
pds.DealTierDef_DiscPct, 
pds.DealTierDef_DiscAmt, 
pds.DealTierDef_DiscAppliesTo, 
pds.DealTierDef_DiscQty, 
pds.DealTierDef_AddlInfo, 
pds.DealTierDef_ThresholdType, 
pds.DealTierDef_ThresholdQty, 
pds.DealTierDef_ThresholdAmt, 
pds.DealItemRequired_ItemGroup, 
pds.DealItemReqQty, 
pds.DealLocationJurisdictionCode, 
pds.DealLocation, 
pds.DealItemDiscSpec_IdentityType, 
pds.DealItemDiscSpec_Qty, 
pds.DealItemDiscSpec_DiscType, 
pds.DealItemDiscSpec_DiscPct, 
pds.DealItemDiscSpec_DiscAmt, 
pds.DealItemDiscSpec_DiscAppliesTo
From PromoDataStage pds 
left join MinDealDiscountId m on m.deal_no = pds.deal_no 
						and m.deal_id=pds.deal_id 
						and m.MinDealDiscountId=pds.deal_discount_id		
where 1=1
and (
			getdate() between
			cast(dateadd(dd,-7,pds.DealStartDate) as date)
			and
			cast(isnull(pds.DealEndDate,'3030-12-31') as date)

	)


), 


FinalSummary as (

select *
from Summary1 s
where  1=1
and s.Min_Deal_no is not null  -- This will capture all Deal Documents where there are single configurations in document
union 
select *
from Summary1 s
where  1=1
and (
		s.Min_Deal_no is null 
			and 
		s.deal_discount_name not like '%BOGO%'
	)   -- This will capture all Deal Documents where there are multiple configurations in document but not BOGO referenced

) 



select
pds.deal_discount_id, 
pds.deal_id, 
pds.deal_no, 
pds.deal_name, 
pds.deal_description, 
pds.DealStartDate, 
--case when pds.deal_no in ('012088','012089','012090','012091')  -- This was to temporarily end date 2fur45 promo while TSYL promo was active 
--	then '2024-07-15'
--		else pds.DealEndDate 
--end as DealEndDate,
pds.DealEndDate, 
pds.deal_discount_type, 
pds.deal_discount_name, 
--pds.DealTierDef_DiscType, -- Replaced with Below on 7/20/2023 
case when pds.DealItemReqQty =1 and pds.DealTierDef_DiscType is null and pds.deal_discount_name like '%BOGO%' then 'BOGOQTY1'
else pds.DealTierDef_DiscType end as DealTierDef_DiscType, 
pds.DealTierDef_DiscPct, 
pds.DealTierDef_DiscAmt, 
pds.DealTierDef_DiscAppliesTo, 
pds.DealTierDef_DiscQty, 
pds.DealTierDef_AddlInfo, 
pds.DealTierDef_ThresholdType, 
pds.DealTierDef_ThresholdQty, 
pds.DealTierDef_ThresholdAmt, 
pds.DealItemRequired_ItemGroup, 
pds.DealItemReqQty, 
pds.DealLocationJurisdictionCode, 
pds.DealLocation, 
pds.DealItemDiscSpec_IdentityType, 
pds.DealItemDiscSpec_Qty, 
pds.DealItemDiscSpec_DiscType, 
pds.DealItemDiscSpec_DiscPct, 
pds.DealItemDiscSpec_DiscAmt, 
pds.DealItemDiscSpec_DiscAppliesTo
from FinalSummary pds
where 1=1
and pds.Deal_no not in ('012089','012091','012133') -- Docs We need to end date early for testing 
--order by 3, 1 











-- Dan T - Test Cases below 
--where d.deal_no=011899 --- 2 for xx
	---deal_discount type='MIPK'
	---DealTierDef_DiscType='PRCH'
	---DealTierDef_DiscAmt=45.00
	---DealTierDef_DiscAppliesTo=ALL_
	---DealItemRequired_ItemGroup=1428
	---DealItemReqQty=2
	---DealLocationJurisdictionCode=HOME
	---DealLocation=xxxx
	---

--where d.deal_no=011911 --bogo % off 
--	---deal_discount_type='MXMH'
--	---DealTierDef_DiscAppliesTo=ITEM
--	---DealItemRequired_ItemGroup=2034
--	---DealItemReqQty=2
--	---DealLocationJurisdictionCode=UK
--	---DealLocation=xxxx
--	---DealItemDiscSpec_IdentityType=IGRP
--	---DealItemDiscSpec_Qty=1
--	---DealItemDiscSpec_DiscType=PCT_
--	---DealItemDiscSpec_DiscPct=50.00
--	---DealItemDiscSpec_DiscAppliesTo=ELST

--where d.deal_no=011914 --purchase with purchase
	---deal_discount_type=MXMH
	---DealTierDef_DiscType=AMT_
	---DealTierDef_DiscAmt=11.00
	---DealTierDef_DiscAppliesTo=ITEM
	---DealItemRequired_ItemGroup=1986 and 1983 (multiple rows)
	---DealItemReqQty=1
	---DealLocationJurisdictionCode=HOME
	---DealLocation=xxxx
	---DealItemDiscSpec_IdentityType=NULL and IGRP (ItemGroup 1986 = NULL, 1983=IGRP)
	---DealItemDiscSpec_Qty=NULL and 1
	---DealItemDiscSpec_DiscType=NULL and AMT_
	---DealItemDiscSpec_DiscAmt=NULL and 9.00
	---DealItemDiscSpec_DiscAppliesTo=NULL and ELST



--- d.deal_no=011903 --bogo setup by juan --- not in aptos, but in the pos??
---d.deal_no=011874 --party package setup by juan --- not in aptos, but in the pos??
--order by d.deal_no



--select *
--from deal 
--where deal_no=011437

--select *
--from deal_discount
--where deal_id=3889

--select d.deal_no, dd.name, dd.description
--from deal d
--join deal_discount dd on d.deal_id=dd.deal_id
--order by d.deal_no

--with Multis as (
--select deal_discount_id, dealLocation
--from #xx
--group by deal_discount_id,dealLocation
--having count(*) >1
--)
--select d.deal_no, dd.name, dd.description
--from deal d
--join deal_discount dd on d.deal_id=dd.deal_id
--where deal_no in (select deal_no from Multis)
--and ( --current promotions only
--			cast(effective_from_date as date)<=getdate()
--			and
--			cast(isnull(effective_to_date,'3030-12-31') as date) > cast(getdate() as date)
--		)
--order by deal_no



--select count(*) 
--from deal d
--join deal_discount dd on d.deal_id=dd.deal_id



--select *
--from #xx
--where deal_discount_id=42980001
```

