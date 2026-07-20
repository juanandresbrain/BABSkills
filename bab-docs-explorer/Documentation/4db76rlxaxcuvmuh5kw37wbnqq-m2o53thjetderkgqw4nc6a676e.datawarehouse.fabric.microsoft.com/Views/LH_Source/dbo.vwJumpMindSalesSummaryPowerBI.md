# dbo.vwJumpMindSalesSummaryPowerBI

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwJumpMindSalesSummaryPowerBI"]
    vwJumpMindSalesSummary(["vwJumpMindSalesSummary"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| vwJumpMindSalesSummary |

## View Code

```sql
CREATE view vwJumpMindSalesSummaryPowerBI 

as

with 
RefundTransactions as 
	(
		select 
			d.StoreID, 
			d.TransactionDate,
			d.ProductNumber,
			count (distinct d.TransactionKey ) as CountRefundTransctions
		from vwJumpMindSalesSummary d
		where 1=1
		and d.RefundTrans  <> 0
		group by  
			d.StoreID, 
			d.TransactionDate,
			d.ProductNumber
	), 
GiftCardOnly as 
(
	select 
		d.StoreID, 
		d.TransactionDate,
		d.ProductNumber,
		count (distinct d.TransactionKey ) as CountGiftCardOnlyTransactions
	from vwJumpMindSalesSummary d
	where 1=1
	and d.GiftCardUnits  > 0
	and d.TransactionKey  not in 
		(
			select distinct d.TransactionKey 
			from vwJumpMindSalesSummary d
			where 1=1
			and d.SaleUnits > 0 
			and d.GiftCardUnits  = 0
			and d.RefundTrans  = 0
		) -- merch sales Transactions 
	group by 
		d.StoreID, 
		d.TransactionDate,
		d.ProductNumber
)

select
	cast(d.StoreCode as varchar(4)) as StoreCode,
	d.TransactionDate,
	d.TransactionHour,
	cast(d.StoreName as varchar(100)) as StoreName,
	cast(d.District as varchar(100)) as District,
	cast(d.Country as varchar(100)) as Country,
	cast(d.ProductNumber as varchar(100)) as ProductNumber,
	cast(d.ProductDescription as varchar(100)) as ProductDescription,
	cast(d.KeyStory as varchar(100)) as KeyStory,
	(case when sum(coalesce(d.SaleTrans,0)) <= 0 then 0	else coalesce(count(distinct d.TransactionKey) - coalesce (max (gc.CountGiftCardOnlyTransactions),0) -coalesce (max (rt.CountRefundTransctions),0),0)end) SaleTrans,
	(sum(coalesce(d.SaleValue,0))) SaleValue,	
	(sum(coalesce(d.SaleUnits,0))) SaleUnits,	
	(case when sum(coalesce(d.RefundTrans,0)) <= 0
		then  0
			else max (rt.CountRefundTransctions) -- Used Max here just because I needed an aggregate function to avoid another group by 
	end )
	RefundTrans,
	(sum(coalesce(d.RefundValue,0))) RefundValue,	
	(sum(coalesce(d.RefundUnits,0))) RefundUnits,
	(sum(coalesce(d.PartySaleValue,0))) PartySaleValue,	
	(case when sum(coalesce(d.PartyTrans,0)) <= 0 then 0 else count(distinct d.TransactionKey) end) PartyTrans,
	cast('0' as int) as PartyBookings, -- from DECK / PARTY VIEW
	(sum(coalesce(d.PartyCount,0))) PartyCount,
	(case when sum(coalesce(d.StufferTrans,0)) <= 0 then 0 else count(distinct d.TransactionKey) end) as StufferTrans, --WILL get LATER from PRODUCT DATA
	(case when sum(coalesce(d.SkinTrans,0)) <= 0 then 0 else count(distinct d.TransactionKey) end) as SkinsTrans, --WILL get LATER from PRODUCT DATA
	(sum(coalesce(d.StufferUnits,0))) as StuffersUnits, --WILL get LATER from PRODUCT DATA
	(sum(coalesce(d.SkinUnits,0))) as SkinsUnits, --WILL get LATER from PRODUCT DATA
	(case when sum(coalesce(d.BackpackTrans,0)) <= 0 then 0 else count(distinct d.TransactionKey) end) BackpackTrans,
	(sum(coalesce(d.BackpackUnits,0))) BackpackUnits,
	--case when sum(coalesce(bcc.CountBonusClubTransactions,0)) < 0 then 0 else sum(coalesce(bcc.CountBonusClubTransactions,0)) end as BonusClubTrans,
	(case when sum(coalesce(d.BonusClubTrans,0)) <= 0 then 0 else count(distinct d.TransactionKey) end) as BonusClubTrans,
	(sum(coalesce(d.GiftCardValue,0))) GiftCardValue,	
	(sum(coalesce(d.GiftCardUnits,0))) GiftCardUnits,
	(sum(coalesce(d.EndlessAisleValue,0))) EnterpriseSellingValue,
	(case when sum(coalesce(d.EndlessAisleTrans,0)) <= 0 then 0 else count(distinct d.TransactionKey) end) EnterpriseSellingTrans,
	(sum(coalesce(d.EndlessAisleUnits,0))) EnterpriseSellingUnits,
	cast('0.00' as numeric(38,2)) as ShipFromStoreSales, --WILL get from Deck 
	cast('0' as int) as ShipFromStoreTransactions, --WILL get from Deck 
	cast('0' as int) as ShipFromStoreUnits, --WILL get from Deck 
	cast('0.00' as numeric(38,2)) as PickupFromStoreSales, --WILL get from Deck 
	cast('0' as int) as PickupFromStoreTransactions, --WILL get from Deck 
	cast('0' as int) as PickupFromStoreUnits, --WILL get from Deck 
	cast('0.00' as numeric(38,2)) as CurbsideSales, --WILL get from Deck
```

