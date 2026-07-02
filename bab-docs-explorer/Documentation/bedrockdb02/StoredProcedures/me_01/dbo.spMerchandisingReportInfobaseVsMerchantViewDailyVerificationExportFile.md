# dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationExportFile

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationExportFile"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMerchandisingReportInfobaseVsMerchantViewDailyVerificationExportFile]
	@iohunits_mev_group bigint,
	@iOnhand_MeV_StyleClr bigint,
	@iohunits_ib bigint,
	@iintransit_ib bigint,
	@iintransit_mev_group bigint,
	@ilntransit_Mev_styleclr bigint,
	@dBeginPeriod smalldatetime, 
	@dEndPeriod smalldatetime,
	@maTotalOnOrder bigint,
	@ibTotalOnOrder bigint,
	@iReceipts_Mev_styleclr bigint,
	@iSales_Mev_styleclr bigint,
	@iReturns_Mev_styleclr bigint,
	@iReceipts_mev bigint,
	@iSales_mev bigint,
	@iReturns_mev bigint,
	@iReceipts_ib bigint,
	@iSales_ib bigint,
	@iReturns_ib bigint

as set nocount on

print 'Infobase-MerchantView Daily Verification Results'
print 'Period Begins: ' + cast(@dBeginPeriod as varchar)
print 'Period Ends: ' + cast(@dEndPeriod as varchar)
print ''
print 'MA Total On Order Group: ' + cast(@maTotalOnOrder as varchar)
print 'IB Total On Order : ' + cast(@ibTotalOnOrder as varchar)
print '-------------------------------------'
print 'Difference : ' + cast(@maTotalOnOrder - @ibTotalOnOrder as varchar) 
print ''
print ''
print 'MA On Hand Units Group : ' + cast(@iohunits_mev_group as varchar) 
print 'MA On Hand Units StyleClr: ' + cast(@iOnhand_MeV_StyleClr as varchar) 
print 'IB On Hand Units : ' + cast(@iohunits_ib as varchar) 
print '-------------------------------------' 
print 'Difference : ' + cast(@iohunits_mev_group - @iohunits_ib as varchar) 
print 'Difference : ' + cast(@iOnhand_MeV_StyleClr - @iohunits_ib as varchar) 
print '' 
print '' 
print 'MA Intransit Group: ' + cast(@iintransit_mev_group as varchar) 
print 'MA Intransit StyleClr: ' + cast(@ilntransit_Mev_styleclr as varchar) 
print 'IB Intransit       : ' + cast(@iintransit_ib as varchar) 
print '-------------------------------------' 
print 'Difference Between MA Group and IB: ' + cast(@iintransit_mev_group - @iintransit_ib as varchar) 
print 'Difference Between MA Style and IB: ' + cast(@ilntransit_Mev_styleclr - @iintransit_ib as varchar) 
print '' 
print '' 
print 'MA Receipts Group : ' + cast(@iReceipts_mev as varchar) 
print 'MA Receipts StyleClr: ' + cast(@iReceipts_MeV_styleclr as varchar) 
print 'IB Receipts : ' + cast(@iReceipts_ib as varchar) 
print '-------------------------------------' 
print 'Difference : ' + cast(@iReceipts_mev - @iReceipts_ib as varchar) 
print 'Difference : ' + cast(@iReceipts_MeV_styleclr - @iReceipts_ib as varchar) 
print '' 
print '' 
print 'MA Returns Group: ' + cast(@iReturns_mev as varchar) 
print 'MA Returns StyleClr: ' + cast(@iReturns_Mev_styleclr as varchar) 
print 'IB Returns : ' + cast(@iReturns_ib as varchar) 
print '-------------------------------------' 
print 'Difference : ' + cast(@iReturns_mev - @iReturns_ib as varchar) 
print 'Difference : ' + cast(@iReturns_Mev_styleclr - @iReturns_ib as varchar) 
print '' 
print '' 
print 'MA Sales : ' + cast(@iSales_mev as varchar) 
print 'MA Sales StyleClr: ' + cast(@iSales_MeV_styleclr as varchar) 
print 'IB Sales : ' + cast((@iSales_ib * -1) as varchar) 
print '-------------------------------------' 
print 'Difference : ' + cast(@iSales_mev - (@iSales_ib * -1) as varchar) 
print 'Difference : ' + cast(@iSales_MeV_styleclr - (@iSales_ib * -1) as varchar) 
print '' 
print '' 
print 'Technical Details:' 
print 'SQL Agent Job on Kermode: MERCHANDISING - Report - Infobase-MerchantViewDailyVerification' 
print 'SQL Stored Procedure on Bedrockdb02.me_01: spMerchandisingReportInfobaseVsMerchantViewDailyVerification'
```

