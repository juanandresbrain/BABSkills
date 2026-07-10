# dbo.spExportWebCouponFiles

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spExportWebCouponFiles"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: spExportWebCouponFiles
--
-- Description: Executes spGenerateWebCouponXML for each of the distinct coupons by Country Code, Discount Amount and Ending Date
--
-- Output: XML File containing coupons and their serialized coupon codes
--
-- Revision History
--		Name:			Date:			Comments:
--		Tim Bytnar	   07/13/2017		   Creation
--	    Ian Wallace	   09/06/2022		   copied proc from kodiak and adjusted it to use new SerializedVoucher table as source
-- =============================================================================================================

CREATE PROCEDURE [dbo].[spExportWebCouponFiles] 
			@discountID int,
			--@discountAmount varchar(100) = '9.9999',
			--@endingDate varchar(100) = '1-1-2111',
			@cntryAbbr varchar(100) -- = 'ZZ'
AS
BEGIN
	
	SET NOCOUNT ON;

	IF OBJECT_ID('tempdb..#tmpRankedDiscounts') IS NOT NULL DROP TABLE #tmpRankedDiscounts

	DECLARE @cmd varchar(8000),
			@currentFileName varchar(100) = NULL,
			@timeStamp varchar(30);

		
set @timeStamp =  
(SELECT FORMAT(GETDATE(), 'yy') +  RIGHT('00' + CONVERT(NVARCHAR(2), DATEPART(MONTH, GETDATE())), 2) + RIGHT('00' + CONVERT(NVARCHAR(2), DATEPART(DAY, GETDATE())), 2)
  + REPLACE(CONVERT(varchar(5), GETDATE(), 108), ':', '') + RIGHT('00' + CONVERT(NVARCHAR(2), DATEPART(ss, GETDATE())), 2) + RIGHT('000' + CONVERT(NVARCHAR(3), DATEPART(ms, GETDATE())), 3))


		SET @currentFileName = @cntryAbbr + '_' + 
							   --@discountAmount + '_' +
							   --CAST(CAST(@endingDate as Date) as varchar(20)) + '_' 
							   --+ 
							     CAST(@discountID as varchar(100)) + '_' + 'CouponExport' + @timeStamp + '.xml'

		SET @cmd = 'bcp.exe "EXEC [DW].[dbo].[spGenerateWebCouponsXML] @discountID = ' + CAST(@discountID as varchar) + ' ,@cntryAbbr = ''' + @cntryAbbr + ''' " queryout \\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Coupons\' + @currentFileName + ' -c -T -C RAW'
		--PRINT @cmd
		EXEC xp_cmdshell @cmd;
END
```

