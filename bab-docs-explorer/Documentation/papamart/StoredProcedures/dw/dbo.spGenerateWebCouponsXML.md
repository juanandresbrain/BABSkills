# dbo.spGenerateWebCouponsXML

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGenerateWebCouponsXML"]
    SerializedVoucher(["SerializedVoucher"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| SerializedVoucher |

## Stored Procedure Code

```sql
-- =============================================
--     Ian Wallace	   09/06/2022		   copied proc from kodiak and adjusted it to use new SerializedVoucher table as source
-- =============================================
CREATE PROCEDURE [dbo].[spGenerateWebCouponsXML] 
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
	from SerializedVoucher 
	where 1=1 
	--and cast(ExportedDate as date) = cast(getdate()-1 as date) and ExportedDateXML is null
	and CouponID = @discountID
	--and Country = @cntryAbbr
	and case when Country in ('US','CA','MX') then 'US' 
	when Country in ('UK' ,'GB') then 'UK' end = @cntryAbbr
	and ExportedDateXML is null
	and ExportedDate is not null
	--and cast(ExportedDate as date) = '11/26/2022'
	--and cast(ExportedDate as date) = cast(getdate() as date)
	--and cast(ExportedDate as date) between cast(getdate()-11 as date) and cast(getdate()-4 as date)
	set @description = (select max(d.Description) from  @Data d)
	
	--set @description = 'testing currency symbols: dollar $10 and pound £5 pounds'


	--Hacky way to add the version and encoding tags
	SELECT '<?xml version="1.0" encoding="UTF-8"?>
			<coupons xmlns="http://www.demandware.com/xml/impex/coupon/2008-06-17">' + 
			CAST((
	SELECT 
	(
	--coupon node
	SELECT
		@discountID as '@coupon-id',
		(
			SELECT
				@description as 'description',
				'true' as 'enabled-flag',
				'true' as 'case-insensitive',
				(
				SELECT '1' as 'limit-per-code',
					   'false' as 'allow-multiple-codes-per-order'
					   
				FOR XML PATH ('redemption-limits'), TYPE
				),
				'' as 'multiple-codes'
			FOR XML PATH (''),TYPE	  
		)
	FROM @Data as t1
	GROUP BY t1.couponNumber
	FOR XML PATH ('coupon'), TYPE
	),

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
	FOR XML PATH (''))
	AS nvarchar(max)
	)+ '</coupons>'
END
```

