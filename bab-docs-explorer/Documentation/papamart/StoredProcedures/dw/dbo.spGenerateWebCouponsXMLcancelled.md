# dbo.spGenerateWebCouponsXMLcancelled

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGenerateWebCouponsXMLcancelled"]
    SerializedVoucherCancelled(["SerializedVoucherCancelled"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| SerializedVoucherCancelled |

## Stored Procedure Code

```sql
-- =============================================
--     Ian Wallace	   09/06/2022		   copied proc from kodiak and adjusted it to use new SerializedVoucher table as source
-- =============================================
CREATE PROCEDURE [dbo].[spGenerateWebCouponsXMLcancelled] 
	@discountID int,
	--@discountAmount decimal(9,4) -- varchar(10) --
	--@endingDate  varchar(20)
	@cntryAbbr varchar(2)

AS
BEGIN

    DECLARE @Data TABLE (couponNumber bigint, serializedNum bigint, Description varchar(100))
	
	declare	@description varchar(100)
	
	INSERT INTO @Data
	select CouponID as couponNumber, SerializedNumber as SerializedNum, Description 
	from SerializedVoucherCancelled
	where 1=1 
	--and cast(ExportedDate as date) = cast(getdate()-1 as date) and ExportedDateXML is null
	and CouponID = @discountID
	--and Country = @cntryAbbr
	and case when Country in ('US','CA','MX') then 'US' 
	when Country in ('UK' ,'GB') then 'UK' end = @cntryAbbr
	and ExportedDateXML is null
	


	-- one time run for all redeemed voucher sin sales audit since 8/1/22
--	INSERT INTO @Data
--	select CouponID as couponNumber, SerializedNumber as SerializedNum, Description 
--	from SerializedVoucher
--	where 1=1 
--	--and cast(ExportedDate as date) = cast(getdate()-1 as date) and ExportedDateXML is null
--	and CouponID = @discountID
--	--and Country = @cntryAbbr
--	and case when Country in ('US','CA','MX') then 'US' 
--	when Country in ('UK' ,'GB') then 'UK' end = @cntryAbbr
--	and SerializedNumber in 
--(select reference_no from  bedrockdb01.auditworks.dbo.cust_liability where cast(date_issued as date) >= '08/01/2022'  and liability_amount = 0 and reference_type = 35 and issuing_store_no = 990  and email_address <>  'BECKYJ@buildabear.com' )


-- one time run for DM vouchers already redeemed in SA
--INSERT INTO @Data
--	select d.couponNumber as couponNumber, sdd.[serializedNum] as SerializedNum, 'No Description'
--	from kodiak.DiscountMstrData.[dbo].[SerializationDiscountDetail] sdd
--	join kodiak.DiscountMstrData.[dbo].[SerializationDiscount] sd on sdd.serializationID =   sd.serializationID
--	join kodiak.DiscountMstrData.[dbo].[Discount]d on sd.discountID = d.discountID 
--	where 1=1 
--	--and cast(ExportedDate as date) = cast(getdate()-1 as date) and ExportedDateXML is null
--	and d.couponNumber = @discountID
--	--and d.couponNumber = 2005278
--	--and Country = 'US'
--	--and case when Country in ('US','CA','MX') then 'US' 
--	----when Country in ('UK' ,'GB') then 'UK' end = @cntryAbbr
--	--when Country in ('UK' ,'GB') then 'UK' end = 'US'
--	and sdd.[serializedNum] in 
--(select reference_no from  bedrockdb01.auditworks.dbo.cust_liability where cast(date_issued as date) >= '08/01/2022'  and liability_amount = 0 and reference_type = 35 and issuing_store_no = 990  and email_address =  'BECKYJ@buildabear.com' )





	--Hacky way to add the version and encoding tags
	SELECT '<?xml version="1.0" encoding="UTF-8"?>
			<coupons xmlns="http://www.demandware.com/xml/impex/coupon/2008-06-17">' + 
			CAST(
	--		(
	--SELECT 
	--(
	----coupon node
	--SELECT
	--	@discountID as '@coupon-id',
	--	(
	--		SELECT
	--			--@description as 'description',
	--			'true' as 'enabled-flag',
	--			'true' as 'case-insensitive',
	--			(
	--			SELECT '1' as 'limit-per-code',
	--				   'false' as 'allow-multiple-codes-per-order'
					   
	--			FOR XML PATH ('redemption-limits'), TYPE
	--			),
	--			'' as 'multiple-codes'
	--		FOR XML PATH (''),TYPE	  
	--	)
	--FROM @Data as t1
	--GROUP BY t1.couponNumber
	--FOR XML PATH ('coupon'), TYPE
	--),

	--coupon-codes node
	(
		SELECT
			@discountID as '@coupon-id',
			(
				SELECT
				t2.serializedNum as 'code'
				FROM @Data as t2
				WHERE t2.couponNumber = t1.couponNumber
				FOR XML PATH (''), TYPE, ELEMENTS
			)
		FROM @Data as t1
		GROUP BY t1.couponNumber
		FOR XML PATH ('coupon-codes'), TYPE
	)
	--FOR XML PATH (''))


	AS nvarchar(max)
	)+ '</coupons>'
END
```

