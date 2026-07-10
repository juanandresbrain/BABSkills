# dbo.spStoreForceSalesPreStage

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spStoreForceSalesPreStage"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
--exec spStoreForceSalesPreStage 1, 1, '10.0.1.101', 'SA', '5@5t0r3'
CREATE proc [dbo].[spStoreForceSalesPreStage]
@StoreID int,
@StoreKey int,
@IP varchar(15),
@UName varchar(2),
@PWord varchar(10)

as

set nocount on

Declare
	@StoreQuery nvarchar(max)

Select @StoreQuery = 
						'
						select 
							StoreCode,	
							Date,	
							Slot,	
							SaleTrans,	
							SaleValue,	
							SaleUnits,	
							RefundTrans,
							RefundValue,	
							RefundUnits,
							PartySaleValue,	
							PartyTrans,	
							PartyBookings,	
							PartyCount,	
							StufferTrans,	
							SkinsTrans,	
							StuffersUnits,	
							SkinsUnits,	
							BackpackTrans,	
							BackpackUnits,	
							BonusClubTrans,	
							GiftCardValue,	
							GiftCardUnits,	
							EnterpriseSellingValue,	
							EnterpriseSellingTrans,	
							EnterpriseSellingUnits
						from openrowset
						(''SQLNCLI'', ''' + @IP + '''; ''' + @Uname + '''; ''' + @PWord + ''',
						''set nocount on;
						with 
						AllTime (TimeSlot) as
						(
									select ''''00:00''''	UNION	select ''''00:30''''	UNION	select ''''01:00''''	UNION	select ''''01:30''''	UNION	select ''''02:00''''	UNION	select ''''02:30''''	UNION	select ''''03:00''''	UNION	select ''''03:30''''
							UNION	select ''''04:00''''	UNION	select ''''04:30''''	UNION	select ''''05:00''''	UNION	select ''''05:30''''	UNION	select ''''06:00''''	UNION	select ''''06:30''''	UNION	select ''''07:00''''	UNION	select ''''07:30''''
							UNION	select ''''08:00''''	UNION	select ''''08:30''''	UNION	select ''''09:00''''	UNION	select ''''09:30''''	UNION	select ''''10:00''''	UNION	select ''''10:30''''	UNION	select ''''11:00''''	UNION	select ''''11:30''''
							UNION	select ''''12:00''''	UNION	select ''''12:30''''	UNION	select ''''13:00''''	UNION	select ''''13:30''''	UNION	select ''''14:00''''	UNION	select ''''14:30''''	UNION	select ''''15:00''''	UNION	select ''''15:30''''
							UNION	select ''''16:00''''	UNION	select ''''16:30''''	UNION	select ''''17:00''''	UNION	select ''''17:30''''	UNION	select ''''18:00''''	UNION	select ''''18:30''''	UNION	select ''''19:00''''	UNION	select ''''19:30''''
							UNION	select ''''20:00''''	UNION	select ''''20:30''''	UNION	select ''''21:00''''	UNION	select ''''21:30''''	UNION	select ''''22:00''''	UNION	select ''''22:30''''	UNION	select ''''23:00''''	UNION	select ''''23:30''''
						),
						RTL_TRN
							(
								RTL_TRN_ID,
								STORE_NO,
								RTL_TRN_TYPE_CODE,
								END_DATETIME,
								DEPT_NO,
								UPC,
								ITEM_NO,
								SkuDescription,
								QUANTITY,
								EXT_NET_PRICE,
								VOID_FLG,
								Line_Item_No,
								RETURN_FLG,
								PartyID,
								CUSTOMER_NO 
							)
							as
							(
								select
									RT.RTL_TRN_ID,
									RT.STORE_NO,
									RT.RTL_TRN_TYPE_CODE,
									RT.END_DATETIME,
									LI.DEPT_NO,
									LI.Item_POS_No as UPC,
									LI.ITEM_NO,	
									LI.Sale_Item_Comment as SkuDescription,
									LI.QUANTITY,
									LI.EXT_NET_PRICE,
									LI.VOID_FLG,
									LI.Line_Item_No,
									LI.RETURN_FLG,
									p.EXT_VALUE as PartyID,
									RT.CUSTOMER_NO 
								from
									RETAIL_TRANSACTION RT with (nolock)
									join SALE_RTRN_LN_ITEM LI with (nolock)
										on (RT.RTL_TRN_ID = LI.RTL_TRN_ID)
										AND (RT.STORE_NO = LI.STORE_NO)
									left join SALE_RTRN_LN_ITEM_EXT P with (nolock)
										on P.EXT_GROUP_NAME = ''''UserInputs''''
										AND P.EXT_NAME = ''''PARTYID''''
										and RT.rtl_trn_id=p.rtl_trn_id
										and LI.line_item_no=p.line_item_no
										and RT.STORE_NO=p.STORE_NO
								where 1=1
									--datediff(day,@PRM_BEGIN_DT,END_DATETIME) >= 0
									--and datediff(day,END_DATETIME,@PRM_END_DT) >= 0
									and RTL_TRN_TYPE_CODE = ''''SALE''''
									and SUSPENDED_FLG=0
									and TRAINING_FLG=0
									and RT.VOID_FLG=0
									and RT.VOIDED_FLG=0
									and RT.VOIDING_FLG=0
									and LI.VOID_FLG=0
							),

						DataStage1 as
							(
								select
									RT.StoreCode,
									RT.TransactionDate,
									RT.TransactionHour,
									RT.TransactionMinute,
									RT.RTL_TRN_ID,
									RT.Line_Item_No,
									RT.SalesFlag,
									RT.ReturnFlag,
									RT.PartyFlag,
									RT.PartyID,
									RT.PartyBook,
									RT.StuffersFlag,
									RT.SkinsFlag,
									RT.BackpackFlag,
									RT.BonusClubFlag,
									RT.GiftCardFlag,
									RT.EnterpriseSellingFlag,
									RT.DEPT_NO,
									RT.UPC,
									RT.ITEM_NO,
									RT.SkuDescription,
									RT.SaleValue,
									RT.SaleUnits,
									isnull(TN.REDEEMED_AMOUNT,0) REDEEMED_AMOUNT,
									RT.Excluded_Items,
									RT.TranUnits,
									RT.TranValue
								from
									(
									select
										right((cast(''''100'''' as varchar) + cast(STORE_NO as varchar)),4) as StoreCode, 
										convert(varchar, End_DateTime, 103) as TransactionDate,
										right(cast(''''00'''' as varchar) + cast(datepart(hh, End_DateTime) as varchar),2) as TransactionHour,
										right(cast(''''00'''' as varchar) + cast(datepart(mi, End_DateTime) as varchar),2) as TransactionMinute,
										RTL_TRN_ID,
										Line_Item_No,
										case 
											when (
													ITEM_NO IN (''''1'''',''''2'''',''''4'''',''''17'''') 
													or 
													DEPT_NO IN (''''145'''',''''245'''',''''445'''',''''146'''',''''246'''',''''446'''',''''147'''',''''247'''',''''447'''',''''148'''',''''157'''',''''248'''',''''257'''',''''448'''',''''457'''')
												)
											then 0
											else 1
										end as SalesFlag, ---excludes giftcards, donations, etc
										RETURN_FLG as ReturnFlag,
										case 
											when PartyID is null 
											then 0 
											else 1 
										end as PartyFlag,
										PartyID,
										0 as PartyBook, --WILL LOOKUP FROM PARTY DB VIS SSIS
										case 
											when DEPT_NO in (''''905'''',''''914'''',''''923'''',''''932'''',''''355'''',''''364'''',''''373'''',''''382'''')
											then 1
											else 0
										end as StuffersFlag,
										case
											when DEPT_NO IN (''''125'''',''''225'''',''''325'''',''''425'''',''''525'''',''''900'''',''''909'''',''''918'''',''''927'''')
											then 1
											else 0
										end as SkinsFlag,
										0 as BackPackFlag, ---NEED TO DETERMINE HOW TO IDENTIFY BACKPACK
										case 
											when CUSTOMER_NO is NULL
											then 0
											else 1
										end as BonusClubFlag,
										case 
											when ITEM_NO = ''''4''''
											then 1
											else 0
										end as GiftCardFlag,
										0 as EnterpriseSellingFlag ,---NEED TO DETERMINE HOW TO IDENTIFY ENTERPRISE SELLING
										case 
											when (
													ITEM_NO IN (''''1'''',''''2'''',''''4'''',''''17'''') 
													or 
													DEPT_NO IN (''''145'''',''''245'''',''''445'''',''''146'''',''''246'''',''''446'''',''''147'''',''''247'''',''''447'''',''''148'''',''''157'''',''''248'''',''''257'''',''''448'''',''''457'''')
												)
												then 0
											else abs(EXT_NET_PRICE)
										end as SaleValue, ---excludes giftcards, donations, etc
										case 
											when (
													ITEM_NO IN (''''1'''',''''2'''',''''4'''',''''17'''') 
													or 
													DEPT_NO IN (''''145'''',''''245'''',''''445'''',''''146'''',''''246'''',''''446'''',''''147'''',''''247'''',''''447'''',''''148'''',''''157'''',''''248'''',''''257'''',''''448'''',''''457'''')
												)
												then 0
											else abs(QUANTITY)
										end as SaleUnits, ---excludes giftcards, donations, etc
										case	
											when 
												(
													ITEM_NO IN (''''1'''',''''2'''',''''4'''',''''17'''') 
													or 
													DEPT_NO IN (''''145'''',''''245'''',''''445'''',''''146'''',''''246'''',''''446'''',''''147'''',''''247'''',''''447'''',''''148'''',''''157'''',''''248'''',''''257'''',''''448'''',''''457'''')
												)
												then abs(QUANTITY)
											else	0
										end as Excluded_Items,
										abs(QUANTITY) as TranUnits,
										abs(EXT_NET_PRICE) as TranValue,--regardless of if giftcard, donation, merch, etc
										DEPT_NO,
										UPC,
										ITEM_NO,
										SkuDescription
									from
										RTL_TRN
									) RT
								left outer join
									( 
									select
										RTL_TRN_ID,
										sum( case when (TENDER_TYPE_ID IN (''''13'''',''''17''''))
											  then TENDER_AMOUNT
	 											  else 0
											 end
										) as REDEEMED_AMOUNT,
										Line_Item_No
									from				
										TENDER_LINE_ITEM 
									group by RTL_TRN_ID, Line_Item_No	
									) as TN
								on (RT.RTL_TRN_ID = TN.RTL_TRN_ID and RT.Line_Item_No=TN.Line_Item_No)
							),
						DataStage2 as
							(
								select 
									StoreCode,
									TransactionDate as Date,
									TransactionHour + '''':'''' + case when TransactionMinute < 30 then ''''00'''' else ''''30'''' end as Slot,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											then count(distinct RTL_TRN_ID)
										else 0 
									end SaleTrans,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											then sum(SaleValue)
										else 0
									end as SaleValue,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											then sum(SaleUnits)
										else 0
									end as SaleUnits,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 1
										then sum(SaleUnits)
										else 0
									end as RefundTrans,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 1
										then sum(SaleValue)
										else 0
									end as RefundValue,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 1
											then sum(SaleUnits)
										else 0
									end as RefundUnits,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and PartyFlag = 1
											then sum(SaleValue)
										else 0
									end as PartySaleValue,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and PartyFlag = 1
											then count(distinct RTL_TRN_ID)
										else 0 
									end PartyTrans,
									PartyBook as PartyBookings, --need to lookup parties booked in the party database
									count(distinct PartyID) PartyCount,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and StuffersFlag = 1
											then count(distinct RTL_TRN_ID)
										else 0 
									end StufferTrans,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and SkinsFlag = 1
											then count(distinct RTL_TRN_ID)
										else 0 
									end SkinsTrans,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and StuffersFlag = 1
											then sum(SaleUnits)
										else 0
									end as StuffersUnits,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and SkinsFlag = 1
											then sum(SaleUnits)
										else 0
									end as SkinsUnits,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and BackpackFlag = 1
											then count(distinct RTL_TRN_ID)
										else 0 
									end BackpackTrans,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and BackpackFlag = 1
											then sum(SaleUnits)
										else 0
									end as BackpackUnits,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and BonusClubFlag = 1
											then count(distinct RTL_TRN_ID)
										else 0 
									end BonusClubTrans,
									case 
										when 
											GiftCardFlag = 1
											and ReturnFlag = 0
											then sum(TranValue)
										else 0
									end as GiftCardValue,
									case 
										when 
											GiftCardFlag = 1
											and ReturnFlag = 0
											then sum(TranUnits)
										else 0
									end as GiftCardUnits,
	
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and EnterpriseSellingFlag = 1
											then sum(SaleValue)
										else 0
									end as EnterpriseSellingValue,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and EnterpriseSellingFlag = 1
											then count(distinct RTL_TRN_ID)
										else 0 
									end EnterpriseSellingTrans,
									case 
										when 
											SalesFlag = 1
											and ReturnFlag = 0
											and EnterpriseSellingFlag = 1
											then sum(SaleUnits)
										else 0
									end as EnterpriseSellingUnits
								from DataStage1
								group by 
									StoreCode,
									TransactionDate,
									TransactionHour + '''':'''' + case when TransactionMinute < 30 then ''''00'''' else ''''30'''' end,
									SalesFlag,
									ReturnFlag,
									PartyFlag,
									PartyID,
									PartyBook,
									StuffersFlag,
									SkinsFlag,
									BackpackFlag,
									BonusClubFlag,
									GiftCardFlag,
									EnterpriseSellingFlag
							),
						StoreDateTime as
							(
								select distinct
									cast(getdate() as date) as RawDate,
									convert(varchar, getdate(), 103) as Date,
									right((cast(''''100'''' as varchar) + cast(rt.STORE_NO as varchar)),4) as StoreCode,
									alt.TimeSlot
								from RETAIL_TRANSACTION rt with (nolock) --using this table for store no
								cross join AllTime alt
								UNION
								select distinct
									cast(getdate()-1 as date) as RawDate,
									convert(varchar, getdate()-1, 103) as Date,
									right((cast(''''100'''' as varchar) + cast(rt.STORE_NO as varchar)),4) as StoreCode,
									alt.TimeSlot
								from RETAIL_TRANSACTION rt with (nolock) --using this table for store no
								cross join AllTime alt
								UNION
								select distinct
									cast(getdate()-2 as date) as RawDate,
									convert(varchar, getdate()-2, 103) as Date,
									right((cast(''''100'''' as varchar) + cast(rt.STORE_NO as varchar)),4) as StoreCode,
									alt.TimeSlot
								from RETAIL_TRANSACTION rt with (nolock) --using this table for store no
								cross join AllTime alt
							) 

						select 
							sdt.StoreCode,	
							--sdt.RawDate,
							sdt.Date,	
							sdt.TimeSlot as Slot,	
							sum(isnull(d.SaleTrans,0)) SaleTrans,	
							sum(isnull(d.SaleValue,0)) SaleValue,	
							sum(isnull(d.SaleUnits,0)) SaleUnits,	
							sum(isnull(d.RefundTrans,0)) RefundTrans,
							sum(isnull(d.RefundValue,0)) RefundValue,	
							sum(isnull(d.RefundUnits,0)) RefundUnits,
							sum(isnull(d.PartySaleValue,0)) PartySaleValue,	
							sum(isnull(d.PartyTrans,0)) PartyTrans,	
							sum(isnull(d.PartyBookings,0)) PartyBookings,	
							sum(isnull(d.PartyCount,0)) PartyCount,	
							sum(isnull(d.StufferTrans,0)) StufferTrans,	
							sum(isnull(d.SkinsTrans,0)) SkinsTrans,	
							sum(isnull(d.StuffersUnits,0)) StuffersUnits,	
							sum(isnull(d.SkinsUnits,0)) SkinsUnits,	
							sum(isnull(d.BackpackTrans,0)) BackpackTrans,	
							sum(isnull(d.BackpackUnits,0)) BackpackUnits,	
							sum(isnull(d.BonusClubTrans,0)) BonusClubTrans,	
							sum(isnull(d.GiftCardValue,0)) GiftCardValue,	
							sum(isnull(d.GiftCardUnits,0)) GiftCardUnits,	
							sum(isnull(d.EnterpriseSellingValue,0)) EnterpriseSellingValue,	
							sum(isnull(d.EnterpriseSellingTrans,0)) EnterpriseSellingTrans,	
							sum(isnull(d.EnterpriseSellingUnits,0)) EnterpriseSellingUnits
						from StoreDateTime sdt
						left join DataStage2 d 
							on sdt.StoreCode=d.StoreCode
							and sdt.Date=d.date
							and sdt.TimeSlot=d.Slot
						where datediff(dd, sdt.RawDate, getdate()) <= 3
						group by 
							sdt.StoreCode,	
							sdt.RawDate,
							sdt.Date,	
							sdt.TimeSlot
							'') as a'

	exec(@StoreQuery)
	--begin try
	--	insert dwstaging.dbo.FlashGaapSalesPreStage
	--	exec(@StoreQuery)
	--end try

	--begin catch
	--	insert dwstaging.dbo.FlashGaapSalesFailureLog
	--	select @StoreID, @StoreKey, @IP, getdate(), error_message()
	--end catch
```

