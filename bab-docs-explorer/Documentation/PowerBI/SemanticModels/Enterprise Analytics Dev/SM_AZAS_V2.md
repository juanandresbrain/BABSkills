# SM_AZAS_V2

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** 0d354f73-5a32-4d1d-9be1-e2681297b656  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| CRMCustomerDim | 15 | 0 |  |
| WebOrderItems | 13 | 0 |  |
| TransactionDetailFact | 23 | 13 |  |
| CRMTransactionFact | 22 | 17 |  |
| DiscountFact | 16 | 3 |  |
| Azure vwFcastMonths | 7 | 3 |  |
| AWTransactionPostVoids | 5 | 0 |  |
| PartyFact | 14 | 0 |  |
| WebTransactions | 9 | 0 |  |
| DailyInventory | 12 | 9 |  |
| GiftCardFact | 12 | 0 |  |
| InventoryRollups | 10 | 0 |  |
| CRMcustomerMasterData | 74 | 82 |  |
| WebOrderInboundDemandTrackingFacts | 62 | 258 |  |
| WebOrderInboundIntegrationTracking | 51 | 16 |  |
| WebOrderOutboundIntegrationTracking | 31 | 32 |  |
| Pricebooks | 7 | 0 |  |
| DynamicsTransactionExceptions | 14 | 0 |  |
| CRMemailFactRollupSummary | 2 | 0 |  |
| CRMTransactionKeyStoryRanking | 36 | 928 |  |
| CRMTransactionKeyStoryRankingPurchases | 18 | 14 |  |
| DynamicsPOReceiptVarianceVsAptos | 9 | 0 |  |
| PCHealthChecks | 11 | 2 |  |
| DynamicsTransactionsStuckInStaging | 9 | 0 |  |
| CRMtrendMonths | 4 | 0 |  |
| CRMtrendQuarters | 5 | 0 |  |
| StoreCount | 5 | 0 |  |
| CategoryMap | 8 | 0 |  |
| WMS_cycleCount_accuracy2 | 11 | 2 |  |
| WMS_cycleCount_accuracy | 29 | 2 |  |
| CatalogAttributes | 69 | 0 |  |
| IT_CommWorks | 47 | 3 |  |
| IT_Heat | 67 | 13 |  |
| POSCompareJumpMindStageUnpublishedMessages | 6 | 0 |  |
| FranchiseeTSPA | 40 | 0 |  |
| CRM_Data_Dictionary | 4 | 0 |  |
| WebOrders | 18 | 0 |  |
| WebShippingDiscounts | 8 | 0 |  |
| UKLoyatly | 10 | 4 |  |
| CRMCustomerLeadGeneration | 14 | 16 |  |
| WebOrderTrueAttachmentConcatenatedSkus | 12 | 6 |  |
| ShipFromStoresUnshipped | 29 | 1 |  |
| ServiceDeskClosed | 26 | 1 |  |
| ServiceDeskOpen | 24 | 1 |  |
| CRMsurveyResults | 143 | 0 |  |
| CRMsurveyQuestions | 3 | 0 |  |
| ProductsStyleGroup | 2 | 0 |  |
| StoreOperationalHours | 17 | 0 |  |
| GiftCardLocations | 14 | 0 |  |
| Filter Products | 27 | 23 |  |
| POSCompareJumpMindStageToSalesAudit | 23 | 0 |  |
| Azure vwFcastDays | 4 | 0 |  |
| CurrencyExchangeFact | 8 | 0 |  |
| EntepriseSellingFact | 15 | 0 |  |
| EnterpriseSellingLifecycleFacts | 30 | 0 |  |
| FWOSFactors | 5 | 0 |  |
| merchonOrder | 10 | 7 |  |
| FlashGaapSales | 19 | 5 |  |
| MerchSales | 13 | 53 |  |
| PoOnOrder | 22 | 0 |  |
| NameMeTransactionFact | 22 | 11 |  |
| SalesPlanFact | 8 | 2 |  |
| StoreInventory | 15 | 0 |  |
| StoreCompDim | 26 | 0 |  |
| WHInventory | 19 | 9 |  |
| TrafficFact | 7 | 3 |  |
| Stores | 42 | 0 |  |
| WMS_cycleCount_occurrence | 5 | 0 |  |
| WMS_cycleCount_adjustments | 12 | 0 |  |
| WebOrderShippingFacts | 18 | 1 |  |
| TransactionFact | 115 | 135 |  |
| FranchiseeMonthlyRoyalty | 35 | 20 |  |
| NewDateDim | 48 | 0 |  |
| StoreList | 6 | 0 |  |
| Products | 62 | 44 |  |

## Measures

### TransactionDetailFact.NetSales

```sql
 sum('TransactionDetailFact'[UnitGrossAmount])-sum('TransactionDetailFact'[UnitDiscAmount]) + sum(TransactionDetailFact[UpsellDiscAllocated])

```

### TransactionDetailFact.NetPercOfDeptTotal

```sql
divide('TransactionDetailFact'[NetSales],
				Calculate('TransactionDetailFact'[NetSales],all(Products[Department]))
				,0)
```

### TransactionDetailFact.UnitsPercOfDeptTotal

```sql

    divide( sumx('TransactionDetailFact','TransactionDetailFact'[Units]),
             Calculate(sumx('TransactionDetailFact','TransactionDetailFact'[Units]),all(Products[Department]))
	,0)
```

### TransactionDetailFact.NetPercOfChainTotal

```sql
divide('TransactionDetailFact'[NetSales],
				Calculate('TransactionDetailFact'[NetSales],all(Products[Chain]))
				,0)
```

### TransactionDetailFact.UnitsPercOfChainTotal

```sql

    divide( sumx('TransactionDetailFact','TransactionDetailFact'[Units]),
             Calculate(sumx('TransactionDetailFact','TransactionDetailFact'[Units]),all(Products[Chain]))
	,0)
```

### TransactionDetailFact.NetPercOfStoryTotal

```sql
divide('TransactionDetailFact'[NetSales],
				Calculate('TransactionDetailFact'[NetSales],all(Products[KeyStory]))
				,0)
```

### TransactionDetailFact.NetPercOfStyleTotal

```sql
divide('TransactionDetailFact'[NetSales],
				Calculate('TransactionDetailFact'[NetSales],all(Products[Code-Desc]))
				,0)
```

### TransactionDetailFact.NetPercOfAltStoryTotal

```sql
divide('TransactionDetailFact'[NetSales],
				Calculate('TransactionDetailFact'[NetSales],all(Products[altKeyStory]))
				,0)
```

### TransactionDetailFact.UnitsPercOfStoryTotal

```sql

    divide( sumx('TransactionDetailFact','TransactionDetailFact'[Units]),
             Calculate(sumx('TransactionDetailFact','TransactionDetailFact'[Units]),all(Products[KeyStory]))
	,0)
```

### TransactionDetailFact.UnitsPercOfStyleTotal

```sql

    divide( sumx('TransactionDetailFact','TransactionDetailFact'[Units]),
             Calculate(sumx('TransactionDetailFact','TransactionDetailFact'[Units]),all(Products[Code-Desc]))
	,0)
```

### TransactionDetailFact.UnitsPercOfAltStoryTotal

```sql

    divide( sumx('TransactionDetailFact','TransactionDetailFact'[Units]),
             Calculate(sumx('TransactionDetailFact','TransactionDetailFact'[Units]),all(Products[altKeyStory]))
	,0)
```

### TransactionDetailFact.DeptUPT

```sql
 divide(sum('TransactionDetailFact'[Units]),
		Calculate(sumx('TransactionFact','TransactionFact'[GAAPTransaction]),all('Products'[Department]))
		,0)
```

### TransactionDetailFact.AnimalCount

```sql
Calculate(distinctCOUNT(TransactionDetailFact[ProductKey]),Products[Department]="Unstuffed")
```

### CRMTransactionFact.NewLoyaltyTransactions

```sql
 calculate(counta(CRMTransactionFact[CRMTransactionID]),'CRMTransactionFact'[CRMTransactionType] = "New")
```

### CRMTransactionFact.RepeatLoyaltyTransactions

```sql
 calculate(counta(CRMTransactionFact[CRMTransactionID]),'CRMTransactionFact'[CRMTransactionType] = "Repeat")
```

### CRMTransactionFact.CaptureRate

```sql
 divide(counta(CRMTransactionFact[CRMTransactionID]),sumx('TransactionFact','TransactionFact'[CaptureEligible]),0)


```

### CRMTransactionFact.newCustomer

```sql
 SUM(CRMTransactionFact[isNewCustomer])
```

### CRMTransactionFact.repeatCustomer

```sql
 SUM(CRMTransactionFact[isRepeatCustomer])
```

### CRMTransactionFact.sumLifetimeVisitNumber

```sql
 SUM(CRMTransactionFact[LifeTimeVisitNumber])
```

### CRMTransactionFact.sumLifetimeTransactionNumber

```sql
 SUM(CRMTransactionFact[LifetimeTransactionNumber])
```

### CRMTransactionFact.sumGaapSales

```sql
 SUM(CRMTransactionFact[GaapSales])
```

### CRMTransactionFact.sumGaapUnits

```sql
 SUM(CRMTransactionFact[GaapUnits])
```

### CRMTransactionFact.month1

```sql
 sum(CRMTransactionFact[inMonth1])
```

### CRMTransactionFact.month3

```sql
 sum(CRMTransactionFact[inMonth3])
```

### CRMTransactionFact.month6

```sql
 sum(CRMTransactionFact[inMonth6])
```

### CRMTransactionFact.month12

```sql
 sum(CRMTransactionFact[inMonth12])
```

### CRMTransactionFact.month18

```sql
 sum(CRMTransactionFact[inMonth18])
```

### CRMTransactionFact.month24

```sql
 sum(CRMTransactionFact[inMonth24])
```

### CRMTransactionFact.month36

```sql
 sum(CRMTransactionFact[inMonth36])
```

### CRMTransactionFact.CRMGaapTrans

```sql
DISTINCTCOUNT ( [CRMTransactionID] )
```

### DiscountFact.NetDiscounts

```sql
 sumx('DiscountFact','DiscountFact'[DiscountUnits] * ('DiscountFact'[DiscountUnitGrossAmount]))
```

### DiscountFact.disc

```sql
 sumx('DiscountFact',(ABS('DiscountFact'[DiscountUnitGrossAmount])))
```

### DiscountFact.PercDiscount

```sql
 Divide (-1 * sum(DiscountFact[DiscountUnitGrossAmount]),
		sumx(TransactionFact,'TransactionFact'[GaapSalesAmount] - 'TransactionFact'[TotalDiscountAmount]),
		0)
```

### Azure vwFcastMonths.fcstMonthTotal

```sql
 
IF(
    HASONEFILTER(Stores[StoreNum-Name]),
        ROUND(sum('Azure vwFcastMonths'[fcastMonth]),0)
,
	""
)
```

### Azure vwFcastMonths.fcastStoreDesign

```sql
 IF(
    HASONEFILTER(Stores[StoreNum-Name]),
CALCULATE (
    FIRSTNONBLANK ( 'StoreCompDim'[StoreDesign], 1 ),
    FILTER ( ALL ( NewDateDim ),  max('StoreCompDim'[CalendarDate]) )
)
,
	BLANK()
)
```

### Azure vwFcastMonths.storeDesignForMatrix

```sql
 IF(
    HASONEFILTER(Stores[StoreNum-Name]),
    CALCULATE(
        FIRSTNONBLANK('Stores'[StoreDesign], 1),ALL('Stores'[StoreDesign])
    ),
    BLANK()
)

```

### DailyInventory.yesterdaysSales

```sql
Calculate (sum(WebOrderItems[Qty]),DATEADD(NewDateDim[Date_Key],-1,DAY))
```

### DailyInventory.WTDSales

```sql
var CurrentDate=LASTDATE(NewDateDim[Date_Key])
var DayNumberOfWeek=WEEKDAY(LASTDATE(NewDateDim[Date_Key]),1)
return
CALCULATE(
    SUM(WebOrderItems[Qty]),
DATESBETWEEN(
   NewDateDim[Date_Key],
DATEADD(
    CurrentDate,
    -1*DayNumberOfWeek + 1,
    DAY),
    CurrentDate))
```

### DailyInventory.YesterdayEnterpriseSales

```sql
Calculate (sum(WebOrderItems[Qty]),WebOrders[ESFlag] = 1,DATEADD(NewDateDim[Date_Key],-1,DAY))
```

### DailyInventory.WTDEnterpriseSales

```sql
var CurrentDate=LASTDATE(NewDateDim[Date_Key])
var DayNumberOfWeek=WEEKDAY(LASTDATE(NewDateDim[Date_Key]),1)
return
CALCULATE(
    SUM(WebOrderItems[Qty]),WebOrders[ESFlag] = 1,
DATESBETWEEN(
   NewDateDim[Date_Key],
DATEADD(
    CurrentDate,
    -1*DayNumberOfWeek + 1,
    DAY),
    CurrentDate))
```

### DailyInventory.PWSales

```sql

var DayNumberOfWeek=WEEKDAY(LASTDATE(NewDateDim[Date_Key]),1)
var EndDate=DateAdd(LASTDATE(NewDateDim[Date_Key]),-1*DayNumberOfWeek ,
    DAY)
var BegDate=DateAdd(EndDate, -6,
    DAY)
return
CALCULATE(
    SUM(WebOrderItems[Qty]),
DATESBETWEEN(
   NewDateDim[Date_Key],
    BegDate,
    EndDate))
```

### DailyInventory.MTDSales

```sql

var EndDate=DateAdd(LASTDATE(NewDateDim[Date_Key]),-1 ,   DAY)
var BegDate=LOOKUPVALUE(NewDateDim[Fiscal_Month_Key],NewDateDim[Date_Key],EndDate)
return
CALCULATE(
    SUM(WebOrderItems[Qty]),
DATESBETWEEN(
   NewDateDim[Date_Key],
    BegDate,
    EndDate))
```

### DailyInventory.PWEnterpriseSales

```sql

var DayNumberOfWeek=WEEKDAY(LASTDATE(NewDateDim[Date_Key]),1)
var EndDate=DateAdd(LASTDATE(NewDateDim[Date_Key]),-1*DayNumberOfWeek ,
    DAY)
var BegDate=DateAdd(EndDate, -6,
    DAY)
return
CALCULATE(
    SUM(WebOrderItems[Qty]),WebOrders[ESFlag] = 1,
DATESBETWEEN(
   NewDateDim[Date_Key],
    BegDate,
    EndDate))
```

### DailyInventory.MTDEnterpriseSales

```sql

var EndDate=DateAdd(LASTDATE(NewDateDim[Date_Key]),-1 ,   DAY)
var BegDate=LOOKUPVALUE(NewDateDim[Fiscal_Month_Key],NewDateDim[Date_Key],EndDate)
return
CALCULATE(
    SUM(WebOrderItems[Qty]),WebOrders[ESFlag] = 1,
DATESBETWEEN(
   NewDateDim[Date_Key],
    BegDate,
    EndDate))
```

### DailyInventory.DaysSupply

```sql
DIVIDE (
    SUM ( DailyInventory[EffectiveInv] ),
    DIVIDE (
        ( [PWSales] + [WTDSales] ),
        ( 7 + WEEKDAY ( LASTDATE ( NewDateDim[Date_Key] ), 1 ) )
    ),
    9999
)
```

### CRMcustomerMasterData.totalCustomerCount

```sql
 DISTINCTCOUNT([CustomerNumber])
```

### CRMcustomerMasterData.bonusClubTy

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isBonusClubTY]=1))
```

### CRMcustomerMasterData.bonusClubLy

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isBonusClubLY]=1))
```

### CRMcustomerMasterData.bonusClubYoY

```sql
 DIVIDE([bonusClubTy]-[bonusClubLy],[bonusClubLy], 0)
```

### CRMcustomerMasterData.bonusClubTyPercTtl

```sql
 DIVIDE([bonusClubTy],[bonusClubTy], 0)
```

### CRMcustomerMasterData.bonusClubLyPercTtl

```sql
 DIVIDE([bonusClubLy],[bonusClubLy], 0)
```

### CRMcustomerMasterData.bonusClubActive1YearsTY

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isbonusClubActive1YearsTY]=1))
```

### CRMcustomerMasterData.bonusClubActive1YearsLY

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isbonusClubActive1YearsLY]=1))
```

### CRMcustomerMasterData.bonusClubActive1YearsYoY

```sql
 DIVIDE([bonusClubActive1YearsTY]-[bonusClubActive1YearsLY],[bonusClubActive1YearsLY], 0)
```

### CRMcustomerMasterData.bonusClubActive1YearsTyPerTtl

```sql
 DIVIDE([bonusClubActive1YearsTY],[bonusClubTy], 0)
```

### CRMcustomerMasterData.bonusClubActive1YearsLyPerTtl

```sql
 DIVIDE([bonusClubActive1YearsLY],[bonusClubLy], 0)
```

### CRMcustomerMasterData.bonusClubActive2YearsTY

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isbonusClubActive2YearsTY]=1))
```

### CRMcustomerMasterData.bonusClubActive2YearsLY

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isbonusClubActive2YearsLY]=1))
```

### CRMcustomerMasterData.bonusClubActive2YearsYoY

```sql
 DIVIDE([bonusClubActive2YearsTY]-[bonusClubActive2YearsLY],[bonusClubActive2YearsLY], 0)
```

### CRMcustomerMasterData.bonusClubActive2YearsTyPerTtl

```sql
 DIVIDE([bonusClubActive2YearsTY], [bonusClubTy],0)
```

### CRMcustomerMasterData.bonusClubActive2YearsLyPerTtl

```sql
 DIVIDE([bonusClubActive2YearsLY],[bonusClubLy], 0)
```

### CRMcustomerMasterData.bonusClubActive3YearsTY

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isbonusClubActive3YearsTY]=1))
```

### CRMcustomerMasterData.bonusClubActive3YearsLY

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isbonusClubActive3YearsLY]=1))
```

### CRMcustomerMasterData.bonusClubActive3YearsYoY

```sql
 DIVIDE([bonusClubActive3YearsTY]-[bonusClubActive3YearsLY],[bonusClubActive3YearsLY], 0)
```

### CRMcustomerMasterData.bonusClubActive3YearsTyPerTtl

```sql
 DIVIDE([bonusClubActive3YearsTY], [bonusClubTy],0)
```

### CRMcustomerMasterData.bonusClubActive3YearsLyPerTtl

```sql
 DIVIDE([bonusClubActive3YearsLY],[bonusClubLy], 0)
```

### CRMcustomerMasterData.bonusClubActive5YearsTY

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isbonusClubActive5YearsTY]=1))
```

### CRMcustomerMasterData.bonusClubActive5YearsLY

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isbonusClubActive5YearsLY]=1))
```

### CRMcustomerMasterData.bonusClubActive5YearsYoY

```sql
 DIVIDE([bonusClubActive5YearsTY]-[bonusClubActive5YearsLY],[bonusClubActive5YearsLY], 0)
```

### CRMcustomerMasterData.bonusClubActive5YearsTyPerTtl

```sql
 DIVIDE([bonusClubActive5YearsTY], [bonusClubTy],0)
```

### CRMcustomerMasterData.bonusClubActive5YearsLyPerTtl

```sql
 DIVIDE([bonusClubActive5YearsLY], [bonusClubLy],0)
```

### CRMcustomerMasterData.bonusClubEmailOpted

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isOptInEmail]=1 && 'CRMcustomerMasterData'[isActive]=1))
```

### CRMcustomerMasterData.bonusCLubSmsOpted

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isOptInText]=1 && 'CRMcustomerMasterData'[isActive]=1))
```

### CRMcustomerMasterData.bonusCLubEmailOpenLast24

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isBonusClubEmailorTextOpenLast24Month]=1 && 'CRMcustomerMasterData'[isActive]=1))
```

### CRMcustomerMasterData.bonusCLubEmailOpen

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isBonusClubWEmailOpen]=1 && 'CRMcustomerMasterData'[isActive]=1))
```

### CRMcustomerMasterData.bonusClubEmailOpenRev

```sql
CALCULATE (
    SUM ( CRMcustomerMasterData[MonetarySumTTL] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isBonusClubWEmailOpen] = 1
            && 'CRMcustomerMasterData'[isActive] = 1
    )
)
```

### CRMcustomerMasterData.bonusClubAvgLTV

```sql
 
CALCULATE (
    AVERAGE (CRMcustomerMasterData[MonetarySumTTL] ),
    CALCULATETABLE (
        VALUES ( CRMcustomerMasterData[MonetarySumTTL] ),
        'CRMcustomerMasterData'[isBonusClubEmailorTextOpenLast24Month]=1,
        'CRMcustomerMasterData'[isActive]=1
    )
)
```

### CRMcustomerMasterData.ltvRev12mo

```sql
 SUM('CRMcustomerMasterData'[MonetarySum12m])
```

### CRMcustomerMasterData.ltvRev24mo

```sql
SUM('CRMcustomerMasterData'[MonetarySum24m])
```

### CRMcustomerMasterData.ltvMembers12mo

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[LastTransactionDate] >= TODAY()-365))
```

### CRMcustomerMasterData.ltvMembers24mo

```sql
 countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[LastTransactionDate] >= TODAY()-730))
```

### CRMcustomerMasterData.ltvTransactions12mo

```sql
SUM( 'CRMTransactionFact'[inMonth12])
```

### CRMcustomerMasterData.ltvTransactions24mo

```sql
SUM( 'CRMTransactionFact'[inMonth24])
```

### CRMcustomerMasterData.ltvDPT12mo

```sql
 DIVIDE([ltvRev12mo], [ltvTransactions12mo],  0)
```

### CRMcustomerMasterData.ltvDPT24mo

```sql
 divide([ltvRev24mo], [ltvTransactions24mo], 0)
```

### CRMcustomerMasterData.ltvAvg12mo

```sql
DIVIDE([ltvRev12mo], [ltvMembers12mo], 0)
```

### CRMcustomerMasterData.ltvAvg24mo

```sql
 DIVIDE([ltvRev24mo], [ltvMembers24mo], 0)
```

### CRMcustomerMasterData.ltvRevPrev12mo

```sql
 [ltvRev24mo] - [ltvRev12mo]
```

### CRMcustomerMasterData.ltvRevPrev24mo

```sql
  [ltvRev36mo] -[ltvRev24mo]
```

### CRMcustomerMasterData.ltvRev36mo

```sql
 SUM('CRMcustomerMasterData'[MonetarySum36m])
```

### CRMcustomerMasterData.ltvMembersPrev12mo

```sql
 calculate(countrows('CRMcustomerMasterData'),DATESBETWEEN('CRMcustomerMasterData'[LastTransactionDate],TODAY()-730,TODAY()-365)) 
```

### CRMcustomerMasterData.ltvMembersPrev24mo

```sql
CALCULATE (
    COUNTROWS ( 'CRMcustomerMasterData' ),
    DATESBETWEEN (
        'CRMcustomerMasterData'[LastTransactionDate],
        TODAY () - 1095,
        TODAY () - 365
    )
)
```

### CRMcustomerMasterData.ltvTransactionsPrev12mo

```sql
  CRMTransactionFact[month24] - CRMTransactionFact[month12]
```

### CRMcustomerMasterData.ltvTransactionsPrev24mo

```sql
  CRMTransactionFact[month36] - CRMTransactionFact[month12]
```

### CRMcustomerMasterData.ltvDPTprev12mo

```sql
DIVIDE([ltvRevPrev12mo], [ltvTransactionsPrev12mo], 0)
```

### CRMcustomerMasterData.ltvDPTprev24mo

```sql
DIVIDE([ltvRevPrev24mo], [ltvTransactionsPrev24mo], 0)
```

### CRMcustomerMasterData.ltvAvgPrev12mo

```sql
DIVIDE([ltvRevPrev12mo], [ltvMembersPrev12mo], 0)
```

### CRMcustomerMasterData.ltvAvgPrev24mo

```sql
DIVIDE([ltvRevPrev24mo], [ltvMembersPrev24mo], 0)
```

### CRMcustomerMasterData.ltvRevVar12m0

```sql
	[ltvRev12mo] - [ltvRevPrev12mo]
```

### CRMcustomerMasterData.ltvMemberVar12mo

```sql
 [ltvMembers12mo] - [ltvMembersPrev12mo]
```

### CRMcustomerMasterData.ltvTransVar12mo

```sql
 [ltvTransactions12mo] - [ltvTransactionsPrev12mo]
```

### CRMcustomerMasterData.ltvDPTvar12mo

```sql
 [ltvDPT12mo] - [ltvDPTprev12mo]
```

### CRMcustomerMasterData.ltvAvgVar12mo

```sql
 [ltvAvg12mo] - [ltvAvgPrev12mo]
```

### CRMcustomerMasterData.ltvRevVar24m0

```sql
 [ltvRev24mo] - [ltvRevPrev24mo] 
```

### CRMcustomerMasterData.ltvMemberVar24mo

```sql
 [ltvMembers24mo] - [ltvMembersPrev24mo]
```

### CRMcustomerMasterData.ltvTransVar24mo

```sql
 [ltvTransactions24mo] - [ltvTransactionsPrev24mo]
```

### CRMcustomerMasterData.ltvDPTvar24mo

```sql
 [ltvDPT24mo] - [ltvDPTprev24mo] 
```

### CRMcustomerMasterData.ltvAvgVar24mo

```sql
 [ltvAvg24mo] - [ltvAvgPrev24mo]
```

### CRMcustomerMasterData.ltvRevPerVar12m0

```sql
DIVIDE([ltvRevVar12m0], [ltvRevPrev12mo], 0)
```

### CRMcustomerMasterData.ltvMemberPerVar12mo

```sql
DIVIDE([ltvMemberVar12mo], [ltvMembersPrev12mo],0) 
```

### CRMcustomerMasterData.ltvTransPerVar12mo

```sql
DIVIDE([ltvTransVar12mo], [ltvTransactionsPrev12mo],0)
```

### CRMcustomerMasterData.ltvDPTPervar12mo

```sql
DIVIDE([ltvDPTvar12mo], [ltvDPTprev12mo], 0)	
```

### CRMcustomerMasterData.ltvAvgPerVar12mo

```sql
DIVIDE([ltvAvgVar12mo], [ltvAvgPrev12mo], 0)	
```

### CRMcustomerMasterData.ltvRevPerVar24mo

```sql
DIVIDE([ltvRevVar24m0],[ltvRevPrev24mo], 0)
```

### CRMcustomerMasterData.ltvMemberPerVar24mo

```sql
DIVIDE([ltvMemberVar24mo], [ltvMembersPrev24mo],0)
```

### CRMcustomerMasterData.ltvTransPerVar24mo

```sql
DIVIDE([ltvTransVar24mo], [ltvTransactionsPrev24mo],0)
```

### CRMcustomerMasterData.ltvDPTPervar24mo

```sql
DIVIDE([ltvDPTvar24mo], [ltvDPTprev24mo], 0)
```

### CRMcustomerMasterData.ltvAvgPerVar24mo

```sql
DIVIDE([ltvAvgVar24mo], [ltvAvgPrev24mo], 0)
```

### CRMcustomerMasterData.avgTrans12moLY

```sql
 DIVIDE([ltvTransactionsPrev12mo], [ltvMembersPrev12mo], 0)
```

### CRMcustomerMasterData.avgTrans24moLY

```sql
 DIVIDE([ltvTransactionsPrev24mo], [ltvMembersPrev24mo], 0)
```

### CRMcustomerMasterData.avgTrans12moTY

```sql
 DIVIDE([ltvTransactions12mo], [ltvMembers12mo], 0)
```

### CRMcustomerMasterData.avgTrans24moTY

```sql
 DIVIDE([ltvTransactions24mo], [ltvMembers24mo], 0)
```

### CRMcustomerMasterData.ltvRevTotal

```sql
SUM ( 'CRMcustomerMasterData'[MonetarySumTTL] )
```

### CRMcustomerMasterData.ltvTransactionTotal

```sql
SUM( 'CRMcustomerMasterData'[FrequencyCountTTL])
```

### CRMcustomerMasterData.ltvAverage

```sql
DIVIDE ( [ltvRevTotal], [ltvTransactionTotal], 0 )
```

### CRMcustomerMasterData.bonusClubEmailLast729

```sql
countrows(filter('CRMcustomerMasterData','CRMcustomerMasterData'[isBonusClubEmailorTextOpenLast729Day]=1 && 'CRMcustomerMasterData'[isActive]=1))
```

### CRMcustomerMasterData.bonusClubEmailLast365

```sql
COUNTROWS (
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isBonusClubEmailorTextOpenLast365Day] = 1
            && 'CRMcustomerMasterData'[isActive] = 1
    )
)
```

### WebOrderInboundDemandTrackingFacts.orderCount

```sql
 DISTINCTCOUNT([OrderNumber])
```

### WebOrderInboundDemandTrackingFacts.orderGiftsCount

```sql
 

VAR myTable = 

SUMMARIZE(  'WebOrderInboundDemandTrackingFacts', 'WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[isGiftOrder])

RETURN

SUMX(myTable, [isGiftOrder])
```

### WebOrderInboundDemandTrackingFacts.ordersGrossShipMax

```sql
 

VAR myTable = 

SUMMARIZE(  'WebOrderInboundDemandTrackingFacts', 'WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[GrossSHippingRevenue])

RETURN

SUMX(myTable, [GrossShippingRevenue])
```

### WebOrderInboundDemandTrackingFacts.ordersShipDiscountsMax

```sql
 

VAR myTable = 

SUMMARIZE(  'WebOrderInboundDemandTrackingFacts', 'WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[ShippingDiscounts])

RETURN

SUMX(myTable, [ShippingDiscounts])
```

### WebOrderInboundDemandTrackingFacts.ordersNetShipRevMax

```sql
 

VAR myTable = 

SUMMARIZE(  'WebOrderInboundDemandTrackingFacts', 'WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[NetShippingRevenue])

RETURN

SUMX(myTable, [NetShippingRevenue])
```

### WebOrderInboundDemandTrackingFacts.pendingWavedAverageAgeSincePlacedUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

DIVIDE(SUMX(myTable, [DaysSincePendingStatus]),
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1)

)


)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedMostOccurringSincePlacedUS

```sql
 
VAR myTable = SUMMARIZE('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
"Count",CALCULATE(
    COUNT('WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus]), 
    FILTER(WebOrderInboundDemandTrackingFacts, WebOrderInboundDemandTrackingFacts[isUS] = 1 
    && WebOrderInboundDemandTrackingFacts[CurrentStatus] in {"Pending",BLANK()})
))

VAR myTable2 = FILTER(myTable,[Count]=MAXX(myTable,[Count]))
VAR Mode1 = MAXX(LASTNONBLANK(myTable2,[DaysSincePendingStatus]),[DaysSincePendingStatus])
RETURN Mode1
```

### WebOrderInboundDemandTrackingFacts.youngestPendingWaveSincePlacedUS

```sql
 
VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MINX(myTable, [DaysSincePendingStatus])

```

### WebOrderInboundDemandTrackingFacts.MiddlestPendingWaveSincePlacedUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MEDIANX(myTable, [DaysSincePendingStatus])


```

### WebOrderInboundDemandTrackingFacts.oldestPendingWaveSincePlacedUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MAXX(myTable, [DaysSincePendingStatus])

   
```

### WebOrderInboundDemandTrackingFacts.wavedAverageAgeSincePlacedUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

DIVIDE(SUMX(myTable, [DaysSincePendingStatus]),
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1)

)


)

```

### WebOrderInboundDemandTrackingFacts.wavedMostOccurringSincePlacedUS

```sql
 
VAR myTable = SUMMARIZE('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
"Count",CALCULATE(
    COUNT('WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus]), 
    FILTER(WebOrderInboundDemandTrackingFacts, WebOrderInboundDemandTrackingFacts[isUS] = 1 
    && WebOrderInboundDemandTrackingFacts[CurrentStatus]  IN {"Waved","StoreWaved"})
))

VAR myTable2 = FILTER(myTable,[Count]=MAXX(myTable,[Count]))
VAR Mode1 = MAXX(LASTNONBLANK(myTable2,[DaysSincePendingStatus]),[DaysSincePendingStatus])
RETURN Mode1
```

### WebOrderInboundDemandTrackingFacts.youngestWaveSincePlacedUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MINX(myTable, [DaysSincePendingStatus])


```

### WebOrderInboundDemandTrackingFacts.MiddlestWaveSincePlacedUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MEDIANX(myTable, [DaysSincePendingStatus])

```

### WebOrderInboundDemandTrackingFacts.oldestWaveSincePlacedUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MAXX(myTable, [DaysSincePendingStatus])
```

### WebOrderInboundDemandTrackingFacts.pendingWavedSincePlacedUScount

```sql
 

   CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1)

)
```

### WebOrderInboundDemandTrackingFacts.wavedSincePlacedUScount

```sql
 

CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]),

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}
 && 'WebOrderInboundDemandTrackingFacts'[isUS]=1)

)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount1SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 1)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount2SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 2)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount3SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 3)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount4SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 4)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount5SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 5)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount6SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 6)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount7SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 7)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent1SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount1SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent2SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount2SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent3SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount3SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent4SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount4SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent5SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount5SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent6SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount6SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent7SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount7SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount1SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 1)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount2SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 2)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount3SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 3)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount4SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 4)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount5SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 5)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount6SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 6)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount7SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 7 )

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent1SincePlacedUS

```sql
 DIVIDE([wavedDayCount1SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent2SincePlacedUS

```sql
 DIVIDE([wavedDayCount2SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent3SincePlacedUS

```sql
 DIVIDE([wavedDayCount3SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent4SincePlacedUS

```sql
 DIVIDE([wavedDayCount4SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent5SincePlacedUS

```sql
 DIVIDE([wavedDayCount5SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent6SincePlacedUS

```sql
 DIVIDE([wavedDayCount6SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent7SincePlacedUS

```sql
 DIVIDE([wavedDayCount7SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount1SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 1)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount2SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 2)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount3SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 3)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount4SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 4)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount5SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 5)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount6SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 6)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount7SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 7)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent1SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount1SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedAverageAgeSincePlacedUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

DIVIDE(SUMX(myTable, [DaysSincePendingStatus]),
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1)

)


)

```

### WebOrderInboundDemandTrackingFacts.pendingWavedMostOccurringSincePlacedUK

```sql
 

VAR myTable = SUMMARIZE('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
"Count",CALCULATE(
    COUNT('WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus]), 
    FILTER(WebOrderInboundDemandTrackingFacts, WebOrderInboundDemandTrackingFacts[isUK] = 1 
    && WebOrderInboundDemandTrackingFacts[CurrentStatus] IN {"Pending",BLANK()})
))

VAR myTable2 = FILTER(myTable,[Count]=MAXX(myTable,[Count]))
VAR Mode1 = MAXX(LASTNONBLANK(myTable2,[DaysSincePendingStatus]),[DaysSincePendingStatus])
RETURN Mode1

```

### WebOrderInboundDemandTrackingFacts.youngestPendingWaveSincePlacedUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MINX(myTable, [DaysSincePendingStatus])
```

### WebOrderInboundDemandTrackingFacts.MiddlestPendingWaveSincePlacedUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MEDIANX(myTable, [DaysSincePendingStatus])


```

### WebOrderInboundDemandTrackingFacts.oldestPendingWaveSincePlacedUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MAXX(myTable, [DaysSincePendingStatus])
```

### WebOrderInboundDemandTrackingFacts.wavedAverageAgeSincePlacedUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

DIVIDE(SUMX(myTable, [DaysSincePendingStatus]),
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1)

)


)

```

### WebOrderInboundDemandTrackingFacts.wavedMostOccurringSincePlacedUK

```sql
 
VAR myTable = SUMMARIZE('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
"Count",CALCULATE(
    COUNT('WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus]), 
    FILTER(WebOrderInboundDemandTrackingFacts, WebOrderInboundDemandTrackingFacts[isUK] = 1 
    && WebOrderInboundDemandTrackingFacts[CurrentStatus]  IN {"Waved","StoreWaved"})
))

VAR myTable2 = FILTER(myTable,[Count]=MAXX(myTable,[Count]))
VAR Mode1 = MAXX(LASTNONBLANK(myTable2,[DaysSincePendingStatus]),[DaysSincePendingStatus])
RETURN Mode1
```

### WebOrderInboundDemandTrackingFacts.youngestWaveSincePlacedUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MINX(myTable, [DaysSincePendingStatus])

```

### WebOrderInboundDemandTrackingFacts.MiddlestWaveSincePlacedUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MEDIANX(myTable, [DaysSincePendingStatus])
```

### WebOrderInboundDemandTrackingFacts.oldestWaveSincePlacedUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MAXX(myTable, [DaysSincePendingStatus])
```

### WebOrderInboundDemandTrackingFacts.pendingWavedSincePlacedUKcount

```sql
 

   CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1)

)
```

### WebOrderInboundDemandTrackingFacts.wavedSincePlacedUKcount

```sql
 

CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}
 && 'WebOrderInboundDemandTrackingFacts'[isUK]=1)

)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent2SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount2SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent3SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount3SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent4SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount4SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent5SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount5SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent6SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount6SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent7SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount7SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount1SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 1)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount2SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 2)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount3SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 3)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount4SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 4)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount5SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 5)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount6SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 6)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount7SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 7)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent1SincePlacedUK

```sql
 DIVIDE([wavedDayCount1SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent2SincePlacedUK

```sql
 DIVIDE([wavedDayCount2SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent3SincePlacedUK

```sql
 DIVIDE([wavedDayCount3SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent4SincePlacedUK

```sql
 DIVIDE([wavedDayCount4SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent5SincePlacedUK

```sql
 DIVIDE([wavedDayCount5SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent6SincePlacedUK

```sql
 DIVIDE([wavedDayCount6SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedAverageAgeSinceUpdateUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

DIVIDE(SUMX(myTable, [DaysSinceLastStatus]),
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1)

)


)

```

### WebOrderInboundDemandTrackingFacts.pendingWavedMostOccurringSinceUpdateUS

```sql
 

VAR myTable = SUMMARIZE('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
"Count",CALCULATE(
    COUNT('WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus]), 
    FILTER(WebOrderInboundDemandTrackingFacts, WebOrderInboundDemandTrackingFacts[isUS] = 1 
    && WebOrderInboundDemandTrackingFacts[CurrentStatus] in {"Pending",BLANK()})
))

VAR myTable2 = FILTER(myTable,[Count]=MAXX(myTable,[Count]))
VAR Mode1 = MAXX(LASTNONBLANK(myTable2,[DaysSinceLastStatus]),[DaysSinceLastStatus])
RETURN Mode1
```

### WebOrderInboundDemandTrackingFacts.youngestPendingWaveSinceUpdateUS

```sql
 
VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MINX(myTable, [DaysSinceLastStatus])

```

### WebOrderInboundDemandTrackingFacts.MiddlestPendingWaveSinceUpdateUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MEDIANX(myTable, [DaysSinceLastStatus])


```

### WebOrderInboundDemandTrackingFacts.oldestPendingWaveSinceUpdateUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MAXX(myTable, [DaysSinceLastStatus])

   
```

### WebOrderInboundDemandTrackingFacts.wavedAverageAgeSinceUpdateUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

DIVIDE(SUMX(myTable, [DaysSinceLastStatus]),
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1)

)


)

```

### WebOrderInboundDemandTrackingFacts.wavedMostOccurringSinceUpdateUS

```sql
 
VAR myTable = SUMMARIZE('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
"Count",CALCULATE(
    COUNT('WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus]), 
    FILTER(WebOrderInboundDemandTrackingFacts, WebOrderInboundDemandTrackingFacts[isUS] = 1 
    && WebOrderInboundDemandTrackingFacts[CurrentStatus]  IN {"Waved","StoreWaved"})
))

VAR myTable2 = FILTER(myTable,[Count]=MAXX(myTable,[Count]))
VAR Mode1 = MAXX(LASTNONBLANK(myTable2,[DaysSinceLastStatus]),[DaysSinceLastStatus])
RETURN Mode1
```

### WebOrderInboundDemandTrackingFacts.youngestWaveSinceUpdateUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MINX(myTable, [DaysSinceLastStatus])


```

### WebOrderInboundDemandTrackingFacts.MiddlestWaveSinceUpdateUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MEDIANX(myTable, [DaysSinceLastStatus])

```

### WebOrderInboundDemandTrackingFacts.oldestWaveSinceUpdateUS

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1))

RETURN

MAXX(myTable, [DaysSinceLastStatus])
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount1SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 1)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount2SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] =2)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount3SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 3)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount4SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 4)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount5SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 5)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount6SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 6)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount7SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 7)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent1SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount1SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent2SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount2SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent3SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount3SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent4SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount4SinceUpdateUS],[pendingWavedSincePlacedUScount],0)

```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent5SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount5SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent6SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount6SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent7SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount7SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount1SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 1)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount2SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 2)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount3SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 3)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount4SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 4)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount5SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 5)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount6SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 6)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount7SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 7 )

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent1SinceUpdateUS

```sql
 DIVIDE([wavedDayCount1SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent3SinceUpdateUS

```sql
 DIVIDE([wavedDayCount3SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent4SinceUpdateUS

```sql
 DIVIDE([wavedDayCount4SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent5SinceUpdateUS

```sql
 DIVIDE([wavedDayCount5SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent6SinceUpdateUS

```sql
 DIVIDE([wavedDayCount6SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent2SinceUpdateUS

```sql
 DIVIDE([wavedDayCount2SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent7SinceUpdateUS

```sql
 DIVIDE([wavedDayCount7SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedAverageAgeSinceUpdateUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

DIVIDE(SUMX(myTable, [DaysSinceLastStatus]),
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1)

)


)

```

### WebOrderInboundDemandTrackingFacts.pendingWavedMostOccurringSinceUpdateUK

```sql
 

VAR myTable = SUMMARIZE('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
"Count",CALCULATE(
    COUNT('WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus]), 
    FILTER(WebOrderInboundDemandTrackingFacts, WebOrderInboundDemandTrackingFacts[isUK] = 1 
    && WebOrderInboundDemandTrackingFacts[CurrentStatus] IN {"Pending",BLANK()})
))

VAR myTable2 = FILTER(myTable,[Count]=MAXX(myTable,[Count]))
VAR Mode1 = MAXX(LASTNONBLANK(myTable2,[DaysSinceLastStatus]),[DaysSinceLastStatus])
RETURN Mode1

```

### WebOrderInboundDemandTrackingFacts.youngestPendingWaveSinceUpdateUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MINX(myTable, [DaysSinceLastStatus])
```

### WebOrderInboundDemandTrackingFacts.MiddlestPendingWaveSinceUpdateUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MEDIANX(myTable, [DaysSinceLastStatus])


```

### WebOrderInboundDemandTrackingFacts.oldestPendingWaveSinceUpdateUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Pending",BLANK()} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MAXX(myTable, [DaysSinceLastStatus])
```

### WebOrderInboundDemandTrackingFacts.wavedAverageAgeSinceUpdateUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

DIVIDE(SUMX(myTable, [DaysSinceLastStatus]),
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1)

)


)
```

### WebOrderInboundDemandTrackingFacts.wavedMostOccurringSinceUpdateUK

```sql
 
VAR myTable = SUMMARIZE('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
"Count",CALCULATE(
    COUNT('WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus]), 
    FILTER(WebOrderInboundDemandTrackingFacts, WebOrderInboundDemandTrackingFacts[isUK] = 1 
    && WebOrderInboundDemandTrackingFacts[CurrentStatus]  IN {"Waved","StoreWaved"})
))

VAR myTable2 = FILTER(myTable,[Count]=MAXX(myTable,[Count]))
VAR Mode1 = MAXX(LASTNONBLANK(myTable2,[DaysSinceLastStatus]),[DaysSinceLastStatus])
RETURN Mode1
```

### WebOrderInboundDemandTrackingFacts.youngestWaveSinceUpdateUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MINX(myTable, [DaysSinceLastStatus])

```

### WebOrderInboundDemandTrackingFacts.MiddlestWaveSinceUpdateUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MEDIANX(myTable, [DaysSinceLastStatus])


```

### WebOrderInboundDemandTrackingFacts.oldestWaveSinceUpdateUK

```sql
 

VAR myTable = 

SUMMARIZECOLUMNS('WebOrderInboundDemandTrackingFacts'[OrderNumber], 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus],
FILTER ( 'WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1))

RETURN

MAXX(myTable, [DaysSinceLastStatus])
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount1SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 1)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount2SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 2)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount3SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 3)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount4SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 4)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount5SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 5)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount6SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 6)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount7SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 7)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent1SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount1SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent2SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount2SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent3SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount3SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent4SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount4SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent5SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount5SinceUpdateUK],[pendingWavedSincePlacedUKcount])
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent6SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount6SinceUpdateUK],[pendingWavedSincePlacedUKcount])
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent7SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount7SinceUpdateUK],[pendingWavedSincePlacedUKcount])
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount1SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 1)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount2SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 2)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount3SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 3)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount4SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 4)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount5SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 5)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount6SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 6)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount7SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 7)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent1SinceUpdateUK

```sql
 DIVIDE([wavedDayCount1SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent2SinceUpdateUK

```sql
 DIVIDE([wavedDayCount2SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent3SinceUpdateUK

```sql
 DIVIDE([wavedDayCount3SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent4SinceUpdateUK

```sql
 DIVIDE([wavedDayCount4SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent5SinceUpdateUK

```sql
 DIVIDE([wavedDayCount5SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent6SinceUpdateUK

```sql
 DIVIDE([wavedDayCount6SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent7SinceUpdateUK

```sql
 DIVIDE([wavedDayCount7SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent7SincePlacedUK

```sql
 DIVIDE([wavedDayCount7SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount8SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 8)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount8SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 8)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount8SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 8)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount8SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 8)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount9SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 9)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount9SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 9)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount9SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 9)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount9SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 9)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount10SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 10)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount10SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 10)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount10SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 10)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount10SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 10)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount11SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 11 && 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 15)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount11SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 11 && 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 15)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount11SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 11 && 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 15)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount11SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 11 && 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 15)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount12SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 16 && 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 25)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount12SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 16 && 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 25)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount12SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 16 && 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 25)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount12SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 16 && 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 25)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount13SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 26)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount13SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 26)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount13SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 26)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCount13SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus]="Pending" && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 26)

)+0
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent8SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount8SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent8SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount8SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent8SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount8SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent8SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount8SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent9SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount9SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent9SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount9SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent9SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount9SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent9SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount9SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent10SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount10SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent10SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount10SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent10SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount10SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent10SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount10SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent11SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount11SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent11SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount11SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent11SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount11SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent11SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount11SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent12SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount12SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent12SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount12SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent12SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount12SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent12SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount12SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent13SincePlacedUK

```sql
 DIVIDE([pendingWavedDayCount13SincePlacedUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent13SincePlacedUS

```sql
 DIVIDE([pendingWavedDayCount13SincePlacedUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent13SinceUpdateUK

```sql
 DIVIDE([pendingWavedDayCount13SinceUpdateUK],[pendingWavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.pendingWavedDayCountPercent13SinceUpdateUS

```sql
 DIVIDE([pendingWavedDayCount13SinceUpdateUS],[pendingWavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount8SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 8)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount8SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 8 )

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount8SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 8)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount8SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 8 )

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount9SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 9)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount9SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 9 )

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount9SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"StoreWaved","Waved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 9)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount9SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 9 )

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount10SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 10 )

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount10SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 10)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount10SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] = 10 )

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount11SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 11 && 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 15)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount10SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] = 10)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount11SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 11 && 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 15)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount11SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 11 && 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 15)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount11SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 11 && 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 15)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount12SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 16 && 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 25)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount12SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 16 && 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] <= 25)
)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount12SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 16 && 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 25)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount12SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 16 && 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] <= 25)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount13SincePlacedUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"}  && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 26)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount13SincePlacedUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSincePendingStatus] >= 26)
)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount13SinceUpdateUK

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUK]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 26)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCount13SinceUpdateUS

```sql
 
CALCULATE(

     DISTINCTCOUNT('WebOrderInboundDemandTrackingFacts'[OrderNumber]), 

     FILTER('WebOrderInboundDemandTrackingFacts','WebOrderInboundDemandTrackingFacts'[CurrentStatus] IN {"Waved","StoreWaved"} && 'WebOrderInboundDemandTrackingFacts'[isUS]=1
	&& 'WebOrderInboundDemandTrackingFacts'[DaysSinceLastStatus] >= 26)

)+0
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent8SincePlacedUK

```sql
 DIVIDE([wavedDayCount8SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent8SincePlacedUS

```sql
 DIVIDE([wavedDayCount8SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent8SinceUpdateUK

```sql
 DIVIDE([wavedDayCount8SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent8SinceUpdateUS

```sql
 DIVIDE([wavedDayCount8SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent9SincePlacedUK

```sql
 DIVIDE([wavedDayCount9SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent9SincePlacedUS

```sql
 DIVIDE([wavedDayCount9SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent9SinceUpdateUK

```sql
 DIVIDE([wavedDayCount9SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent9SinceUpdateUS

```sql
 DIVIDE([wavedDayCount9SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent10SincePlacedUK

```sql
 DIVIDE([wavedDayCount10SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent10SincePlacedUS

```sql
 DIVIDE([wavedDayCount10SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent10SinceUpdateUK

```sql
 DIVIDE([wavedDayCount10SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent10SinceUpdateUS

```sql
 DIVIDE([wavedDayCount10SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent11SincePlacedUK

```sql
 DIVIDE([wavedDayCount11SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent11SincePlacedUS

```sql
 DIVIDE([wavedDayCount11SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent11SinceUpdateUK

```sql
 DIVIDE([wavedDayCount11SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent11SinceUpdateUS

```sql
 DIVIDE([wavedDayCount11SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent12SincePlacedUK

```sql
 DIVIDE([wavedDayCount12SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent12SincePlacedUS

```sql
 DIVIDE([wavedDayCount12SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent12SinceUpdateUK

```sql
 DIVIDE([wavedDayCount12SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent12SinceUpdateUS

```sql
 DIVIDE([wavedDayCount12SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent13SincePlacedUK

```sql
 DIVIDE([wavedDayCount13SincePlacedUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent13SincePlacedUS

```sql
 DIVIDE([wavedDayCount13SincePlacedUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent13SinceUpdateUK

```sql
 DIVIDE([wavedDayCount13SinceUpdateUK],[wavedSincePlacedUKcount],0)
```

### WebOrderInboundDemandTrackingFacts.wavedDayCountPercent13SinceUpdateUS

```sql
 DIVIDE([wavedDayCount13SinceUpdateUS],[wavedSincePlacedUScount],0)
```

### WebOrderInboundDemandTrackingFacts.orderInboundTotal

```sql
 WebOrderInboundIntegrationTracking[ordersInD365] + WebOrderInboundIntegrationTracking[ordersBOSFS] + WebOrderInboundIntegrationTracking[ordersUKftp]+ WebOrderInboundIntegrationTracking[ordersBOSFSuk]
```

### WebOrderInboundIntegrationTracking.ordersInD365

```sql
 COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isUSWeb] = 1 && WebOrderInboundIntegrationTracking[isMissingInDynamics]=0))+0
```

### WebOrderInboundIntegrationTracking.ordersNotInD365

```sql
 COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isUSWeb] = 1 && WebOrderInboundIntegrationTracking[isMissingInDynamics]=1))+0
```

### WebOrderInboundIntegrationTracking.ordersUKftp

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isUKWeb] = 1 && WebOrderInboundIntegrationTracking[isMissingInUKFTP]=0))+0
```

### WebOrderInboundIntegrationTracking.ordersNotInUKftp

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isUKWeb] = 1 && WebOrderInboundIntegrationTracking[isMissingInUKFTP]=1))+0
```

### WebOrderInboundIntegrationTracking.ordersUKwms

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isUKWeb] = 1 && WebOrderInboundIntegrationTracking[isMissingInUKwms]=0))+0
```

### WebOrderInboundIntegrationTracking.ordersNotInUKwms

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isUKWeb] = 1 && WebOrderInboundIntegrationTracking[isMissingInUKwms]=1))+0
```

### WebOrderInboundIntegrationTracking.ordersDeck

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isMissingInDeckFile]=0))+0
```

### WebOrderInboundIntegrationTracking.ordersNotInDeck

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isMissingInDeckFile]=1))+0
```

### WebOrderInboundIntegrationTracking.ordersImported

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isMissingInImportLog]=0))+0
```

### WebOrderInboundIntegrationTracking.ordersNotImported

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isMissingInImportLog]=1))+0
```

### WebOrderInboundIntegrationTracking.ordersWOP

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isWebOrderProcessing]=1))+0
```

### WebOrderInboundIntegrationTracking.ordersNotInWOP

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isMissingInWebOrderProcessing]=1))+0
```

### WebOrderInboundIntegrationTracking.ordersBOSFS

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isUSStore] = 1))+0
```

### WebOrderInboundIntegrationTracking.ordersBOSFSuk

```sql
COUNTROWS(FILTER('WebOrderInboundIntegrationTracking',WebOrderInboundIntegrationTracking[isUKStore] = 1))+0
```

### WebOrderInboundIntegrationTracking.orderTotal

```sql
 COUNTROWS('WebOrderInboundIntegrationTracking')+0
```

### WebOrderInboundIntegrationTracking.orderTotalDelta

```sql
 
var deltaAmount = WebOrderInboundIntegrationTracking[orderTotal]
return deltaAmount - WebOrderInboundIntegrationTracking[ordersInD365] - WebOrderInboundIntegrationTracking[ordersBOSFS] - WebOrderInboundIntegrationTracking[ordersUKftp] - WebOrderInboundIntegrationTracking[ordersBOSFSuk]
```

### WebOrderOutboundIntegrationTracking.shippedUSintegration

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isInUSIntegration]=1))+0
```

### WebOrderOutboundIntegrationTracking.shippedNotUSintegration

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isInUSIntegration]=0))+0
```

### WebOrderOutboundIntegrationTracking.shippedUKintegration

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isInUKIntegration]=1))+0
```

### WebOrderOutboundIntegrationTracking.shippedNotUKintegration

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isInUKIntegration]=0))+0
```

### WebOrderOutboundIntegrationTracking.yesterdayCST

```sql
format(now()-29/24,"mm/dd/yy hh:mm AM/PM")
```

### WebOrderOutboundIntegrationTracking.inUSSalesAudit

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isNotInSalesAudit]=0))+0
```

### WebOrderOutboundIntegrationTracking.notInUSSalesAudit

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isNotInSalesAudit]=1))+0
```

### WebOrderOutboundIntegrationTracking.inUKSalesAudit

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isNotInSalesAudit]=0))+0
```

### WebOrderOutboundIntegrationTracking.notInUKSalesAudit

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isNotInSalesAudit]=1))+0
```

### WebOrderOutboundIntegrationTracking.isUSshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isShippedUS]=1))+0
```

### WebOrderOutboundIntegrationTracking.isNotUSshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isShippedUS]=0))+0
```

### WebOrderOutboundIntegrationTracking.isUKshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isShippedUK]=1))+0
```

### WebOrderOutboundIntegrationTracking.isNotUKshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isShippedUK]=0))+0
```

### WebOrderOutboundIntegrationTracking.isWOPUSshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isWOPShipped]=1))+0
```

### WebOrderOutboundIntegrationTracking.isNotWOPUSshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isWOPShipped]=0))+0
```

### WebOrderOutboundIntegrationTracking.isWOPUKshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isWOPShipped]=1))+0
```

### WebOrderOutboundIntegrationTracking.isNotWOPUKshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isWOPShipped]=0))+0
```

### WebOrderOutboundIntegrationTracking.isOMSUSshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isOMSShipped]=1))+0
```

### WebOrderOutboundIntegrationTracking.isNotOMSUSshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUS]=1 && 'WebOrderOutboundIntegrationTracking'[isOMSShipped]=0))+0
```

### WebOrderOutboundIntegrationTracking.isOMSUKshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isOMSShipped]=1))+0
```

### WebOrderOutboundIntegrationTracking.isNotOMSUKshipped

```sql
COUNTROWS(FILTER('WebOrderOutboundIntegrationTracking','WebOrderOutboundIntegrationTracking'[isUK]=1 && 'WebOrderOutboundIntegrationTracking'[isOMSShipped]=0))+0
```

### WebOrderOutboundIntegrationTracking.shippedTotal

```sql
 COUNTROWS('WebOrderOutboundIntegrationTracking')+0
```

### WebOrderOutboundIntegrationTracking.ordersShippedDelta

```sql
 
var deltaAmount = WebOrderOutboundIntegrationTracking[shippedTotal]
return deltaAmount - WebOrderOutboundIntegrationTracking[isUSshipped] - WebOrderOutboundIntegrationTracking[isUKshipped] 
```

### WebOrderOutboundIntegrationTracking.shippedInIntegrationDelta

```sql

var deltaAmount = WebOrderOutboundIntegrationTracking[shippedTotal]

return deltaAmount - WebOrderOutboundIntegrationTracking[shippedUSintegration] - WebOrderOutboundIntegrationTracking[shippedUKintegration] 
```

### WebOrderOutboundIntegrationTracking.shippedInWOPDelta

```sql

var deltaAmount = WebOrderOutboundIntegrationTracking[shippedTotal]
return deltaAmount - WebOrderOutboundIntegrationTracking[isWOPUSshipped] - WebOrderOutboundIntegrationTracking[isWOPUKshipped] 
```

### WebOrderOutboundIntegrationTracking.shippedInOMSDelta

```sql

var deltaAmount = WebOrderOutboundIntegrationTracking[shippedTotal]

return deltaAmount - WebOrderOutboundIntegrationTracking[isOMSUSshipped] - WebOrderOutboundIntegrationTracking[isOMSUKshipped] 
```

### WebOrderOutboundIntegrationTracking.shippedInSalesAuditDelta

```sql

var deltaAmount = WebOrderOutboundIntegrationTracking[shippedTotal]

return deltaAmount - WebOrderOutboundIntegrationTracking[inUSSalesAudit] - WebOrderOutboundIntegrationTracking[inUKSalesAudit] 
```

### WebOrderOutboundIntegrationTracking.ordersShippedTotal

```sql
 WebOrderOutboundIntegrationTracking[isUSshipped] + WebOrderOutboundIntegrationTracking[isUKshipped] 
```

### WebOrderOutboundIntegrationTracking.shippedInIntegrationTotal

```sql
 WebOrderOutboundIntegrationTracking[shippedUSintegration] + WebOrderOutboundIntegrationTracking[shippedUKintegration] 
```

### WebOrderOutboundIntegrationTracking.shippedInWOPTotal

```sql
 WebOrderOutboundIntegrationTracking[isWOPUSshipped] + WebOrderOutboundIntegrationTracking[isWOPUKshipped] 
```

### WebOrderOutboundIntegrationTracking.shippedInOMSTotal

```sql
 WebOrderOutboundIntegrationTracking[isOMSUSshipped] + WebOrderOutboundIntegrationTracking[isOMSUKshipped]
```

### WebOrderOutboundIntegrationTracking.shippedInSalesAuditTotal

```sql
 WebOrderOutboundIntegrationTracking[inUSSalesAudit] + WebOrderOutboundIntegrationTracking[inUKSalesAudit]
```

### CRMTransactionKeyStoryRanking.newCustomer1

```sql
 

CALCULATE(

     DISTINCTCOUNT('CRMTransactionKeyStoryRanking'[CustomerNumber]),

     FILTER('CRMTransactionKeyStoryRanking','CRMTransactionKeyStoryRanking'[isNewCustomer] =1)

)
```

### CRMTransactionKeyStoryRanking.repeatCustomer1

```sql
 

CALCULATE(

     DISTINCTCOUNT('CRMTransactionKeyStoryRanking'[CustomerNumber]),

     FILTER('CRMTransactionKeyStoryRanking','CRMTransactionKeyStoryRanking'[isRepeatCustomer] =1)

)
```

### CRMTransactionKeyStoryRanking.newCustWebRetTrans

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.repeatCustWebRetTrans

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0
    )
) + 0
```

### CRMTransactionKeyStoryRanking.totCustWebRetTrans

```sql
CALCULATE ( DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ) ) + 0
```

### CRMTransactionKeyStoryRanking.newCustWebRetRev

```sql
VAR myTable =
    SUMMARIZECOLUMNS (
        'CRMTransactionKeyStoryRanking'[TransactionID],
        'CRMTransactionKeyStoryRanking'[GaapSalesTranTotal],
        FILTER (
            'CRMTransactionKeyStoryRanking',
            'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 1
        )
    )
RETURN
    SUMX ( myTable, [GaapSalesTranTotal] ) + 0
```

### CRMTransactionKeyStoryRanking.repeatCustWebRetRev

```sql
VAR myTable =
    SUMMARIZECOLUMNS (
        'CRMTransactionKeyStoryRanking'[TransactionID],
        'CRMTransactionKeyStoryRanking'[GaapSalesTranTotal],
        FILTER (
            'CRMTransactionKeyStoryRanking',
            'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0
        )
    )
RETURN
    SUMX ( myTable, [GaapSalesTranTotal] ) + 0
```

### CRMTransactionKeyStoryRanking.totCustWebRetRev

```sql
VAR myTable =
    SUMMARIZECOLUMNS (
        'CRMTransactionKeyStoryRanking'[TransactionID],
        'CRMTransactionKeyStoryRanking'[GaapSalesTranTotal]
    )
RETURN
    SUMX ( myTable, [GaapSalesTranTotal] ) + 0
```

### CRMTransactionKeyStoryRanking.newCustWebTrans

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 1
            && 'CRMTransactionKeyStoryRanking'[isWeb] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.repeatCustWebTrans

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0
            && 'CRMTransactionKeyStoryRanking'[isWeb] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.totCustWebTrans

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isWeb] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.newCustWebRev

```sql
VAR myTable =
    SUMMARIZECOLUMNS (
        'CRMTransactionKeyStoryRanking'[TransactionID],
        'CRMTransactionKeyStoryRanking'[GaapSalesTranTotal],
        FILTER (
            'CRMTransactionKeyStoryRanking',
            'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 1
                && 'CRMTransactionKeyStoryRanking'[isWeb] = 1
        )
    )
RETURN
    SUMX ( myTable, [GaapSalesTranTotal] ) + 0
```

### CRMTransactionKeyStoryRanking.repeatCustWebRev

```sql
VAR myTable =
    SUMMARIZECOLUMNS (
        'CRMTransactionKeyStoryRanking'[TransactionID],
        'CRMTransactionKeyStoryRanking'[GaapSalesTranTotal],
        FILTER (
            'CRMTransactionKeyStoryRanking',
            'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0
                && 'CRMTransactionKeyStoryRanking'[isWeb] = 1
        )
    )
RETURN
    SUMX ( myTable, [GaapSalesTranTotal] ) + 0
```

### CRMTransactionKeyStoryRanking.totCustWebRev

```sql
VAR myTable =
    SUMMARIZECOLUMNS (
        'CRMTransactionKeyStoryRanking'[TransactionID],
        'CRMTransactionKeyStoryRanking'[GaapSalesTranTotal],
        FILTER (
            'CRMTransactionKeyStoryRanking',
            'CRMTransactionKeyStoryRanking'[isWeb] = 1
        )
    )
RETURN
    SUMX ( myTable, [GaapSalesTranTotal] ) + 0
```

### CRMTransactionKeyStoryRanking.newCustRetTrans

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 1
            && 'CRMTransactionKeyStoryRanking'[isRetail] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.repeatCustRetTrans

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0
            && 'CRMTransactionKeyStoryRanking'[isRetail] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.totCustRetTrans

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isRetail] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.newCustRetRev

```sql
VAR myTable =
    SUMMARIZECOLUMNS (
        'CRMTransactionKeyStoryRanking'[TransactionID],
        'CRMTransactionKeyStoryRanking'[GaapSalesTranTotal],
        FILTER (
            'CRMTransactionKeyStoryRanking',
            'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 1
                && 'CRMTransactionKeyStoryRanking'[isRetail] = 1
        )
    )
RETURN
    SUMX ( myTable, [GaapSalesTranTotal] ) + 0
```

### CRMTransactionKeyStoryRanking.repeatCustRetRev

```sql
VAR myTable =
    SUMMARIZECOLUMNS (
        'CRMTransactionKeyStoryRanking'[TransactionID],
        'CRMTransactionKeyStoryRanking'[GaapSalesTranTotal],
        FILTER (
            'CRMTransactionKeyStoryRanking',
            'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0
                && 'CRMTransactionKeyStoryRanking'[isRetail] = 1
        )
    )
RETURN
    SUMX ( myTable, [GaapSalesTranTotal] ) + 0
```

### CRMTransactionKeyStoryRanking.totCustRetRev

```sql
VAR myTable =
    SUMMARIZECOLUMNS (
        'CRMTransactionKeyStoryRanking'[TransactionID],
        'CRMTransactionKeyStoryRanking'[GaapSalesTranTotal],
        FILTER (
            'CRMTransactionKeyStoryRanking',
            'CRMTransactionKeyStoryRanking'[isRetail] = 1
        )
    )
RETURN
    SUMX ( myTable, [GaapSalesTranTotal] ) + 0
```

### CRMTransactionKeyStoryRanking.transTotal

```sql
 DISTINCTCOUNT('CRMTransactionKeyStoryRanking'[TransactionID])
```

### CRMTransactionKeyStoryRanking.transNew

```sql
 CALCULATE(DISTINCTCOUNT('CRMTransactionKeyStoryRanking'[TransactionID]), FILTER('CRMTransactionKeyStoryRanking','CRMTransactionKeyStoryRanking'[isFirstPurchase] =1))+0
```

### CRMTransactionKeyStoryRanking.transPercNew

```sql
 DIVIDE([transNew], [transTotal], 0)
```

### CRMTransactionKeyStoryRanking.transRepeat

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transPercRepeat

```sql
 DIVIDE([transRepeat], [transTotal], 0)
```

### CRMTransactionKeyStoryRanking.revTotal

```sql
 SUM('CRMTransactionKeyStoryRanking'[KeyStorySales])
```

### CRMTransactionKeyStoryRanking.revNew

```sql
 CALCULATE(SUM('CRMTransactionKeyStoryRanking'[KeyStorySales]),'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 1)
```

### CRMTransactionKeyStoryRanking.revNewPerc

```sql
 DIVIDE([revNew], [revTotal], 0)
```

### CRMTransactionKeyStoryRanking.revRepeat

```sql
 CALCULATE(SUM('CRMTransactionKeyStoryRanking'[KeyStorySales]),'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0)
```

### CRMTransactionKeyStoryRanking.revRepeatPerc

```sql
 DIVIDE([revRepeat], [revTotal], 0)
```

### CRMTransactionKeyStoryRanking.trans12mo

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 365
    )
) + 0
```

### CRMTransactionKeyStoryRanking.trans12moPrev

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 729
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 365
    )
) + 0
```

### CRMTransactionKeyStoryRanking.trans12moVar

```sql
 [trans12mo] - [trans12moPrev]
```

### CRMTransactionKeyStoryRanking.trans12moVarPerc

```sql
 DIVIDE([trans12moVar], [trans12moPrev], 0)
```

### CRMTransactionKeyStoryRanking.rev12mo

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 365
    )
) + 0
```

### CRMTransactionKeyStoryRanking.rev12moPrev

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 729
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 365
    )
) + 0
```

### CRMTransactionKeyStoryRanking.rev12moVar

```sql
 [rev12mo] - [rev12moPrev]
```

### CRMTransactionKeyStoryRanking.rev12moVarPerc

```sql
 DIVIDE([rev12moVar],  [rev12moPrev], 0)
```

### CRMTransactionKeyStoryRanking.trans3mo

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 90
    )
) + 0
```

### CRMTransactionKeyStoryRanking.trans3moLy

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 454
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 365
    )
) + 0
```

### CRMTransactionKeyStoryRanking.trans3moLyVar

```sql
[trans3mo] - [trans3moLy]
```

### CRMTransactionKeyStoryRanking.trans3moLyVarPerc

```sql
DIVIDE([trans3moLyVar], [trans3moLy], 0)
```

### CRMTransactionKeyStoryRanking.rev3mo

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 90
    )
)
```

### CRMTransactionKeyStoryRanking.rev3moLy

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 454
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 365
    )
)
```

### CRMTransactionKeyStoryRanking.rev3moLyVar

```sql
[rev3mo] - [rev3moLy]
```

### CRMTransactionKeyStoryRanking.rev3moLyVarPerc

```sql
DIVIDE([rev3moLyVar],  [rev3moLy], 0)
```

### CRMTransactionKeyStoryRanking.trans3moPrev

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 180
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 91
    )
) + 0
```

### CRMTransactionKeyStoryRanking.trans3moPrevVar

```sql
[trans3mo] - [trans3moPrev]
```

### CRMTransactionKeyStoryRanking.rev3moPrev

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 180
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 91
    )
)
```

### CRMTransactionKeyStoryRanking.rev3moPrevVar

```sql
[rev3mo] - [rev3moPrev]
```

### CRMTransactionKeyStoryRanking.rev3moPrevVarPerc

```sql
DIVIDE ( [rev3moPrevVar], [rev3moPrev], 0 )
```

### CRMTransactionKeyStoryRanking.trans3moPrevVarPerc

```sql
DIVIDE([trans3moPrevVar], [trans3moPrev], 0)
```

### CRMTransactionKeyStoryRanking.trans1mo

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 30
    )
)
```

### CRMTransactionKeyStoryRanking.trans1moLy

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 394
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 365
    )
) + 0
```

### CRMTransactionKeyStoryRanking.trans1moLyVar

```sql
[trans1mo] - [trans1moLy]
```

### CRMTransactionKeyStoryRanking.trans1moLyVarPerc

```sql
DIVIDE ( [trans1moLyVar], [trans1moLy], 0 )
```

### CRMTransactionKeyStoryRanking.trans1moPrev

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 60
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 31
    )
) + 0
```

### CRMTransactionKeyStoryRanking.trans1moPrevVar

```sql
[trans1mo] - [trans1moPrev]
```

### CRMTransactionKeyStoryRanking.trans1moPrevVarPerc

```sql
DIVIDE ( [trans1moPrevVar], [trans1moPrev], 0 )
```

### CRMTransactionKeyStoryRanking.trans1wk

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 7
    )
)
```

### CRMTransactionKeyStoryRanking.trans1wkLy

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 371
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 365
    )
) + 0
```

### CRMTransactionKeyStoryRanking.trans1wkLyVar

```sql
[trans1wk] - [trans1wkLy]
```

### CRMTransactionKeyStoryRanking.trans1wkLyVarPerc

```sql
DIVIDE ( [trans1wkLyVar], [trans1wkLy], 0 )
```

### CRMTransactionKeyStoryRanking.trans1wkPrev

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 14
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 8
    )
) + 0
```

### CRMTransactionKeyStoryRanking.trans1wkPrevVar

```sql
[trans1wk] - [trans1wkPrev]
```

### CRMTransactionKeyStoryRanking.trans1wkPrevVarPerc

```sql
DIVIDE ( [trans1wkPrevVar], [trans1wkPrev], 0 )
```

### CRMTransactionKeyStoryRanking.rev1mo

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 30
    )
)
```

### CRMTransactionKeyStoryRanking.rev1moLy

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 394
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 365
    )
)
```

### CRMTransactionKeyStoryRanking.rev1moLyVar

```sql
[rev1mo] - [rev1moLy]
```

### CRMTransactionKeyStoryRanking.rev1moLyVarPerc

```sql
DIVIDE ( [rev1moLyVar], [rev1moLy], 0 )
```

### CRMTransactionKeyStoryRanking.rev1moPrev

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 60
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 31
    )
)
```

### CRMTransactionKeyStoryRanking.rev1moPrevVar

```sql
[rev1mo] - [rev1moPrev]
```

### CRMTransactionKeyStoryRanking.rev1moPrevVarPerc

```sql
DIVIDE ( [rev1moPrevVar], [rev1moPrev], 0 )
```

### CRMTransactionKeyStoryRanking.rev1wk

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 7
    )
)
```

### CRMTransactionKeyStoryRanking.rev1wkLy

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 371
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 365
    )
)
```

### CRMTransactionKeyStoryRanking.rev1wkLyVar

```sql
[rev1wk] - [rev1wkLy]
```

### CRMTransactionKeyStoryRanking.rev1wkLyVarPerc

```sql
DIVIDE ( [rev1wkLyVar], [rev1wkLy], 0 )
```

### CRMTransactionKeyStoryRanking.rev1wkPrev

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
            >= TODAY () - 14
            && 'CRMTransactionKeyStoryRanking'[TransactionDate]
                <= TODAY () - 8
    )
)
```

### CRMTransactionKeyStoryRanking.rev1wkPrevVar

```sql
[rev1wk] - [rev1wkPrev]
```

### CRMTransactionKeyStoryRanking.rev1wkPrevVarPerc

```sql
DIVIDE ( [rev1wkPrevVar], [rev1wkPrev], 0 )
```

### CRMTransactionKeyStoryRanking.dptTotal

```sql
SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] )
    / DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] )
```

### CRMTransactionKeyStoryRanking.revLY

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] )
)
```

### CRMTransactionKeyStoryRanking.revYoy

```sql
DIVIDE ( [revTotal] - [revLY], [revLY], 0 )
```

### CRMTransactionKeyStoryRanking.transLY

```sql
CALCULATE ( [transTotal], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.transYoy

```sql
DIVIDE ( [transTotal] - [transLY], [transLy], 0 )
```

### CRMTransactionKeyStoryRanking.transBC

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 1 )
) + 0
```

### CRMTransactionKeyStoryRanking.transBCperc

```sql
DIVIDE ( [transBC], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transNonBC

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 0 )
) + 0
```

### CRMTransactionKeyStoryRanking.transNonBCperc

```sql
DIVIDE ( [transNonBC], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revBC

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 1 )
) + 0
```

### CRMTransactionKeyStoryRanking.revNonBCperc

```sql
DIVIDE ( [revNonBC], [revTotal], 0 ) + 0
```

### CRMTransactionKeyStoryRanking.transBCnewGuest

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 1 ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 1
    ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFreshCustomer] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transBCnewGuestPerc

```sql
DIVIDE ( [transBCnewGuest], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuest

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 1 ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0
    ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFreshCustomer] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestPerc

```sql
DIVIDE([transBCrepeatGuest], [transTotal],0)
```

### CRMTransactionKeyStoryRanking.transBCGuestTotal

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 1 ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFreshCustomer] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revNonBC

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 0 )
) + 0
```

### CRMTransactionKeyStoryRanking.revBcPerc

```sql
DIVIDE ( [revBC], [revTotal], 0 ) + 0
```

### CRMTransactionKeyStoryRanking.transBCfreq2

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 1
            && 'CRMcustomerMasterData'[FrequencyCount24m] = 2
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transBCfreq2Perc

```sql
DIVIDE ( [transBCfreq2], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 1
            && ( 'CRMcustomerMasterData'[FrequencyCount24m] = 3
            || 'CRMcustomerMasterData'[FrequencyCount24m] = 4 )
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4Perc

```sql
DIVIDE ( [transBCfreq3_4], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 1
            && ( 'CRMcustomerMasterData'[FrequencyCount24m] = 5
            || 'CRMcustomerMasterData'[FrequencyCount24m] = 7 )
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7Perc

```sql
DIVIDE ( [transBCfreq5_7], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transBCfreq8+

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 1
            && 'CRMcustomerMasterData'[FrequencyCount24m] >= 8
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transBCfreq8+Perc

```sql
DIVIDE ( [transBCfreq8+], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transBClapsed

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 0
            && 'CRMcustomerMasterData'[FrequencyCount24m] > 0
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transBClapsedPerc

```sql
DIVIDE ( [transBClapsed], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency1m

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] < 31
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transRecency1mPerc

```sql
DIVIDE ( [transRecency1m], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency1_3m

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 31 
&&  'CRMcustomerMasterData'[RecencyCountTTL] < 90
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transRecency1_3mPerc

```sql
DIVIDE ( [transRecency1_3m], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency12_18m

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 365
&&  'CRMcustomerMasterData'[RecencyCountTTL] < 545
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transRecency12_18mPerc

```sql
DIVIDE ( [transRecency12_18m], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency18_24m

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 545
&&  'CRMcustomerMasterData'[RecencyCountTTL] < 720
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transRecency18_24mPerc

```sql
DIVIDE ( [transRecency18_24m], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency24m+

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 720
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transRecency24m+Perc

```sql
DIVIDE ( [transRecency24m+], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revBCfreq2

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 1
            && 'CRMcustomerMasterData'[FrequencyCount24m] = 2
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revBCfreq2Perc

```sql
DIVIDE ( [revBCfreq2], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 1
            && ( 'CRMcustomerMasterData'[FrequencyCount24m] = 3
            || 'CRMcustomerMasterData'[FrequencyCount24m] = 4 )
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4Perc

```sql
DIVIDE ( [revBCfreq3_4], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 1
            && ( 'CRMcustomerMasterData'[FrequencyCount24m] = 5
            || 'CRMcustomerMasterData'[FrequencyCount24m] = 7 )
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7Perc

```sql
DIVIDE ( [revBCfreq5_7], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revBCfreq8+

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 1
            && 'CRMcustomerMasterData'[FrequencyCount24m] >= 8
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revBCfreq8+Perc

```sql
DIVIDE ( [revBCfreq8+], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revBClapsed

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[isActive] = 0
            && 'CRMcustomerMasterData'[FrequencyCount24m] > 0
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revBClapsedPerc

```sql
DIVIDE ( [revBClapsed], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency1m

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] < 31
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revRecency1mPerc

```sql
DIVIDE ( [revRecency1m], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency1_3m

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 31
            && 'CRMcustomerMasterData'[RecencyCountTTL] < 90
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revRecency1_3mPerc

```sql
DIVIDE ( [revRecency1_3m], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency12_18m

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 365
            && 'CRMcustomerMasterData'[RecencyCountTTL] < 545
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revRecency12_18mPerc

```sql
DIVIDE ( [revRecency12_18m], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency18_24m

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 545
            && 'CRMcustomerMasterData'[RecencyCountTTL] < 720
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revRecency18_24mPerc

```sql
DIVIDE ( [revRecency18_24m], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency24m+

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 720
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revRecency24m+Perc

```sql
DIVIDE ( [revRecency24m+], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.averageSales

```sql
DIVIDE ( [revTotal], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transCountCYC

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasCountYourCandles] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transCountCYCperc

```sql
DIVIDE ( [transCountCYC], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transCountBDgift

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasBirthdayGift] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transCountBDgiftPerc

```sql
DIVIDE ( [transCountBDgift], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transCountHalfBD

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasHalfBirthday] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transCountHalfBDperc

```sql
DIVIDE ( [transCountHalfBD], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transCountWinback

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasWinback] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transCountWinbackPerc

```sql
DIVIDE ( [transCountWinback], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transCountOther

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasOther] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transCountOtherPerc

```sql
DIVIDE ( [transCountOther], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revSumCYC

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasCountYourCandles] = 1
    )
)
```

### CRMTransactionKeyStoryRanking.revSumCYCperc

```sql
DIVIDE ( [revSumCYC], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revSumBDgift

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasBirthdayGift] = 1
    )
)
```

### CRMTransactionKeyStoryRanking.revSumBDgiftPerc

```sql
DIVIDE ( [revSumBDgift], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revSumHalfBD

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasHalfBirthday] = 1
    )
)
```

### CRMTransactionKeyStoryRanking.revSumWinback

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasWinback] = 1
    )
)
```

### CRMTransactionKeyStoryRanking.revSumWinbackPerc

```sql
DIVIDE ( [revSumWinback], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revSumOther

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[hasOther] = 1
    )
)
```

### CRMTransactionKeyStoryRanking.revSumOtherPerc

```sql
DIVIDE ( [revSumOther], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency3_6m

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 90
&&  'CRMcustomerMasterData'[RecencyCountTTL] < 180
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transRecency3_6mPerc

```sql
DIVIDE ( [transRecency3_6m], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency6_12m

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRanking'[TransactionID] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 180
&&  'CRMcustomerMasterData'[RecencyCountTTL] < 365
    )
) + 0
```

### CRMTransactionKeyStoryRanking.transRecency6_12mPerc

```sql
DIVIDE ( [transRecency6_12m], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency3_6m

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 90
            && 'CRMcustomerMasterData'[RecencyCountTTL] < 180
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revRecency3_6mPerc

```sql
DIVIDE ( [revRecency3_6m], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency6_12m

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER (
        'CRMcustomerMasterData',
        'CRMcustomerMasterData'[RecencyCountTTL] > 180
            && 'CRMcustomerMasterData'[RecencyCountTTL] < 365
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revRecency6_12mPerc

```sql
DIVIDE ( [revRecency6_12m], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transBCly

```sql
CALCULATE ( [transBC], DATEADD ( 'NewDateDim'[Date_Key], -364, DAY ) )
```

### CRMTransactionKeyStoryRanking.transBCyoy

```sql
DIVIDE ( [transBC] - [transBCly], [transBCly], 0 )
```

### CRMTransactionKeyStoryRanking.transNonBCly

```sql
CALCULATE ( [transNonBC], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transNonBCyoy

```sql
DIVIDE ( [transNonBC] - [transNonBCly], [transNonBCly], 0 )
```

### CRMTransactionKeyStoryRanking.transBCguestTotalLY

```sql
CALCULATE ( [transBCguestTotal], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCguestTotalYoy

```sql
DIVIDE ( [transBCguestTotal] - [transBCguestTotalLY], [transBCguestTotalLY], 0 )
```

### CRMTransactionKeyStoryRanking.transBCnewGuestLy

```sql
CALCULATE ( [transBCnewGuest], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCnewGuestYoy

```sql
DIVIDE ( [transBCnewGuest] - [transBCnewGuestLy], [transBCnewGuestLy], 0 )
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestLy

```sql
CALCULATE (
    [transBCrepeatGuest],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestYoy

```sql
DIVIDE (
    [transBCrepeatGuest] - [transBCrepeatGuestLy],
    [transBCrepeatGuestLy],
    0
)
```

### CRMTransactionKeyStoryRanking.transBCfreq2ly

```sql
CALCULATE ( [transBCfreq2], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCfreq2yoy

```sql
DIVIDE ( [transBCfreq2] - [transBCfreq2ly], [transBCfreq2ly], 0 )
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4ly

```sql
CALCULATE ( [transBCfreq3_4], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4yoy

```sql
DIVIDE ( [transBCfreq3_4] - [transBCfreq3_4ly], [transBCfreq3_4ly], 0 )
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7ly

```sql
CALCULATE ( [transBCfreq5_7], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7yoy

```sql
DIVIDE ( [transBCfreq5_7] - [transBCfreq5_7ly], [transBCfreq5_7ly], 0 )
```

### CRMTransactionKeyStoryRanking.transBCfreq8+ly

```sql
CALCULATE ( [transBCfreq8+], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCfreq8+yoy

```sql
DIVIDE ( [transBCfreq8+] - [transBCfreq8+ly], [transBCfreq8+ly], 0 )
```

### CRMTransactionKeyStoryRanking.transBClapsedLY

```sql
CALCULATE ( [transBClapsed], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBClapsedYoy

```sql
DIVIDE ( [transBClapsed] - [transBClapsedLY], [transBClapsedLY], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency1mLy

```sql
CALCULATE ( [transRecency1m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency1myoy

```sql
DIVIDE ( [transRecency1m] - [transRecency1mLy], [transRecency1mLy], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency1_3mLY

```sql
CALCULATE ( [transRecency1_3m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency1_3mYoy

```sql
DIVIDE ( [transRecency1_3m] - [transRecency1_3mLY], [transRecency1_3mLY], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency3_6mLY

```sql
CALCULATE ( [transRecency3_6m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency3_6mYoy

```sql
DIVIDE ( [transRecency3_6m] - [transRecency3_6mLY], [transRecency3_6mLY], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency6_12mLY

```sql
CALCULATE ( [transRecency6_12m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency6_12mYoy

```sql
DIVIDE ( [transRecency6_12m] - [transRecency6_12mLY], [transRecency6_12mLY], 0 )
```

### CRMTransactionKeyStoryRanking.transRecency12_18mLY

```sql
CALCULATE (
    [transRecency12_18m],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency12_18mYoy

```sql
DIVIDE (
    [transRecency12_18m] - [transRecency12_18mLY],
    [transRecency12_18mLY],
    0
)
```

### CRMTransactionKeyStoryRanking.transRecency18_24mLY

```sql
CALCULATE (
    [transRecency18_24m],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency18_24mYoy

```sql
DIVIDE (
    [transRecency18_24m] - [transRecency18_24mLY],
    [transRecency18_24mLY],
    0
)
```

### CRMTransactionKeyStoryRanking.transRecency24m+LY

```sql
CALCULATE ( [transRecency24m+], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency24m+Yoy

```sql
DIVIDE ( [transRecency24m+] - [transRecency24m+LY], [transRecency24m+LY], 0 )
```

### CRMTransactionKeyStoryRanking.transCountCYCly

```sql
CALCULATE ( [transCountCYC], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountCYCYoy

```sql
DIVIDE ( [transCountCYC] - [transCountCYCly], [transCountCYCly], 0 )
```

### CRMTransactionKeyStoryRanking.transCountBDgiftLY

```sql
CALCULATE ( [transCountBDgift], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountBDgiftYoy

```sql
DIVIDE ( [transCountBDgift] - [transCountBDgiftLY], [transCountBDgiftLY], 0 )
```

### CRMTransactionKeyStoryRanking.transCountHalfBDly

```sql
CALCULATE ( [transCountHalfBD], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountHalfBDYoy

```sql
DIVIDE([transCountHalfBD]-[transCountHalfBDly],[transCountHalfBDly],0)
```

### CRMTransactionKeyStoryRanking.transCountOtherLY

```sql
CALCULATE ( [transCountOther], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountOtherYoy

```sql
DIVIDE ( [transCountOther] - [transCountOtherLY], [transCountOtherLY], 0 )
```

### CRMTransactionKeyStoryRanking.transCountWinbackLY

```sql
CALCULATE ( [transCountWinback], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountWinbackYoy

```sql
DIVIDE ( [transCountWinback] - [transCountWinbackLY], [transCountWinbackLY], 0 )
```

### CRMTransactionKeyStoryRanking.revSumHalfBDperc

```sql
DIVIDE ( [revSumHalfBD], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transBCGuestTotalPerc

```sql
DIVIDE ( [transBCGuestTotal], [totCustWebRetTrans], 0 )
```

### CRMTransactionKeyStoryRanking.transBClyPerc

```sql
CALCULATE ( [transBCperc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCyoyMix

```sql
( [transBCperc] - [transBClyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transNonBClyPerc

```sql
CALCULATE ( [transNonBCperc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transNonBCyoyMix

```sql
( [transNonBCperc] - [transNonBClyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCGuestTotalLYperc

```sql
CALCULATE (
    [transBCguestTotalPerc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCguestTotalYoyMix

```sql
( [transBCGuestTotalperc] - [transBCGuestTotalLYperc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCnewGuestLYperc

```sql
CALCULATE (
    [transBCnewGuestPerc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCnewGuestYoyMix

```sql
( [transBCnewGuestPerc] - [transBCnewGuestLYperc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestLYperc

```sql
CALCULATE (
    [transBCrepeatGuestPerc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestYoyMix

```sql
( [transBCrepeatGuestPerc] - [transBCrepeatGuestLYperc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCfreq2lyPerc

```sql
CALCULATE ( [transBCfreq2perc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCfreq2yoyMix

```sql
( [transBCfreq2Perc] - [transBCfreq2lyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4lyPerc

```sql
CALCULATE (
    [transBCfreq3_4perc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4yoyMix

```sql
( [transBCfreq3_4Perc] - [transBCfreq3_4lyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7lyPerc

```sql
CALCULATE (
    [transBCfreq5_7Perc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7yoyMix

```sql
( [transBCfreq5_7Perc] - [transBCfreq5_7lyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCfreq8+lyPerc

```sql
CALCULATE ( [transBCfreq8+Perc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBCfreq8+yoyMix

```sql
( [transBCfreq8+Perc] - [transBCfreq8+lyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBClapsedLyPerc

```sql
CALCULATE ( [transBClapsedPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transBClapsedYoyMix

```sql
( [transBClapsedPerc] - [transBClapsedLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency1mLyPerc

```sql
CALCULATE (
    [transRecency1mPerc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency1mYoyMix

```sql
( [transRecency1mPerc] - [transRecency1mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency1_3mLyPerc

```sql
CALCULATE (
    [transRecency1_3mPerc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency1_3mYoyMix

```sql
( [transRecency1_3mPerc] - [transRecency1_3mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency3_6mLyPerc

```sql
CALCULATE (
    [transRecency3_6mPerc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency3_6mYoyMix

```sql
( [transRecency3_6mPerc] - [transRecency3_6mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency6_12mLyPerc

```sql
CALCULATE (
    [transRecency6_12mPerc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency6_12mYoyMix

```sql
( [transRecency6_12mPerc] - [transRecency6_12mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency12_18mLyPerc

```sql
CALCULATE (
    [transRecency12_18mPerc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency12_18mYoyMix

```sql
( [transRecency12_18mPerc] - [transRecency12_18mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency18_24mLyPerc

```sql
CALCULATE (
    [transRecency18_24mPerc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency18_24mYoyMix

```sql
( [transRecency18_24mPerc] - [transRecency18_24mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency24m+LyPerc

```sql
CALCULATE (
    [transRecency24m+Perc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transRecency24m+YoyMix

```sql
( [transRecency24m+Perc] - [transRecency24m+LyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountCYClyPerc

```sql
CALCULATE ( [transCountCYCPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountCYCyoyMix

```sql
( [transCountCYCperc] - [transCountCYClyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountBDgiftLyPerc

```sql
CALCULATE (
    [transCountBDgiftPerc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountBDgiftYoyMix

```sql
( [transCountBDgiftPerc] - [transCountBDgiftLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountHalfBDlyPerc

```sql
CALCULATE (
    [transCountHalfBDperc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountHalfBDyoyMix

```sql
( [transCountHalfBDperc] - [transCountHalfBDlyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountOtherLyPerc

```sql
CALCULATE (
    [transCountOtherPerc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountOtherYoyMix

```sql
( [transCountOtherPerc] - [transCountOtherLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountWinbackLyPerc

```sql
CALCULATE (
    [transCountWinbackPerc],
  DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transCountWinbackYoyMix

```sql
( [transCountWinbackPerc] - [transCountWinbackLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCly

```sql
CALCULATE ( [revBC], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCyoy

```sql
DIVIDE ( [revBC] - [revBCly], [revBCly], 0 )
```

### CRMTransactionKeyStoryRanking.revBClyPerc

```sql
CALCULATE ( [revBCperc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCyoyMix

```sql
( [revBCperc] - [revBClyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revNonBCly

```sql
CALCULATE ( [revNonBC], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revNonBCyoy

```sql
DIVIDE ( [revNonBC] - [revNonBCly], [revNonBCly], 0 )
```

### CRMTransactionKeyStoryRanking.revNonBClyPerc

```sql
CALCULATE ( [revNonBCperc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revNonBCyoyMix

```sql
( [revNonBCperc] - [revNonBClyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCguestTotalLY

```sql
CALCULATE ( [revBC], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCguestTotalYoy

```sql
DIVIDE ( [revBC] - [revBCguestTotalLY], [revBCguestTotalLY], 0)
```

### CRMTransactionKeyStoryRanking.revBCGuestTotalLYperc

```sql
CALCULATE (
    [revBCguestTotalPerc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCguestTotalYoyMix

```sql
( [revBCGuestTotalperc] - [revBCGuestTotalLYperc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCnewGuestLy

```sql
CALCULATE ( [revBCnewGuest], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCnewGuestYoy

```sql
DIVIDE ( [revBCnewGuest] - [revBCnewGuestLy], [revBCnewGuestLy], 0 )
```

### CRMTransactionKeyStoryRanking.revBCnewGuestLYperc

```sql
CALCULATE ( [revBCnewGuestPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCnewGuestYoyMix

```sql
( [revBCnewGuestPerc] - [revBCnewGuestLYperc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestLy

```sql
CALCULATE ( [revBCrepeatGuest], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestYoy

```sql
DIVIDE ( [revBCrepeatGuest] - [revBCrepeatGuestLy], [revBCrepeatGuestLy], 0 )
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestLYperc

```sql
CALCULATE (
    [revBCrepeatGuestPerc],
  DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestYoyMix

```sql
( [revBCrepeatGuestPerc] - [revBCrepeatGuestLYperc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCfreq2ly

```sql
CALCULATE ( [revBCfreq2], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCfreq2yoy

```sql
DIVIDE ( [revBCfreq2] - [revBCfreq2ly], [revBCfreq2ly], 0 )
```

### CRMTransactionKeyStoryRanking.revBCfreq2lyPerc

```sql
CALCULATE ( [revBCfreq2perc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCfreq2yoyMix

```sql
( [revBCfreq2Perc] - [revBCfreq2lyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4ly

```sql
CALCULATE ( [revBCfreq3_4], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4yoy

```sql
DIVIDE ( [revBCfreq3_4] - [revBCfreq3_4ly], [revBCfreq3_4ly], 0 )
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4lyPerc

```sql
CALCULATE ( [revBCfreq3_4perc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4yoyMix

```sql
( [revBCfreq3_4Perc] - [revBCfreq3_4lyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7ly

```sql
CALCULATE ( [revBCfreq5_7], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7yoy

```sql
DIVIDE ( [revBCfreq5_7] - [revBCfreq5_7ly], [revBCfreq5_7ly], 0 )
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7lyPerc

```sql
CALCULATE ( [revBCfreq5_7Perc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7yoyMix

```sql
( [revBCfreq5_7Perc] - [revBCfreq5_7lyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCfreq8+ly

```sql
CALCULATE ( [revBCfreq8+], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCfreq8+yoy

```sql
DIVIDE ( [revBCfreq8+] - [revBCfreq8+ly], [revBCfreq8+ly], 0 )
```

### CRMTransactionKeyStoryRanking.revBCfreq8+lyPerc

```sql
CALCULATE ( [revBCfreq8+Perc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBCfreq8+yoyMix

```sql
( [revBCfreq8+Perc] - [revBCfreq8+lyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBClapsedLY

```sql
CALCULATE ( [revBClapsed], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBClapsedYoy

```sql
DIVIDE ( [revBClapsed] - [revBClapsedLY], [revBClapsedLY], 0 )
```

### CRMTransactionKeyStoryRanking.revBClapsedLyPerc

```sql
CALCULATE ( [revBClapsedPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revBClapsedYoyMix

```sql
( [revBClapsedPerc] - [revBClapsedLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency1mLy

```sql
CALCULATE ( [revRecency1m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency1myoy

```sql
DIVIDE ( [revRecency1m] - [revRecency1mLy], [revRecency1mLy], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency1mLyPerc

```sql
CALCULATE ( [revRecency1mPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency1mYoyMix

```sql
( [revRecency1mPerc] - [revRecency1mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency1_3mLY

```sql
CALCULATE ( [revRecency1_3m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency1_3mYoy

```sql
DIVIDE ( [revRecency1_3m] - [revRecency1_3mLY], [revRecency1_3mLY], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency1_3mLyPerc

```sql
CALCULATE (
    [revRecency1_3mPerc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency1_3mYoyMix

```sql
( [revRecency1_3mPerc] - [revRecency1_3mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency3_6mLY

```sql
CALCULATE ( [revRecency3_6m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency3_6mYoy

```sql
DIVIDE ( [revRecency3_6m] - [revRecency3_6mLY], [revRecency3_6mLY], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency3_6mLyPerc

```sql
CALCULATE (
    [revRecency3_6mPerc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency3_6mYoyMix

```sql
( [revRecency3_6mPerc] - [revRecency3_6mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency6_12mLY

```sql
CALCULATE ( [revRecency6_12m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency6_12mYoy

```sql
DIVIDE ( [revRecency6_12m] - [revRecency6_12mLY], [revRecency6_12mLY], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency6_12mLyPerc

```sql
CALCULATE (
    [revRecency6_12mPerc],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency6_12mYoyMix

```sql
( [revRecency6_12mPerc] - [revRecency6_12mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency12_18mLY

```sql
CALCULATE ( [revRecency12_18m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency12_18mYoy

```sql
DIVIDE ( [revRecency12_18m] - [revRecency12_18mLY], [revRecency12_18mLY], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency12_18mLyPerc

```sql
CALCULATE (
    [revRecency12_18mPerc],
  DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency12_18mYoyMix

```sql
( [revRecency12_18mPerc] - [revRecency12_18mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency18_24mLY

```sql
CALCULATE ( [revRecency18_24m], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency18_24mYoy

```sql
DIVIDE ( [revRecency18_24m] - [revRecency18_24mLY], [revRecency18_24mLY], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency18_24mLyPerc

```sql
CALCULATE (
    [revRecency18_24mPerc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency18_24mYoyMix

```sql
( [revRecency18_24mPerc] - [revRecency18_24mLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency24m+LY

```sql
CALCULATE ( [revRecency24m+], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency24m+Yoy

```sql
DIVIDE ( [revRecency24m+] - [revRecency24m+LY], [revRecency24m+LY], 0 )
```

### CRMTransactionKeyStoryRanking.revRecency24m+LyPerc

```sql
CALCULATE (
    [revRecency24m+Perc],
   DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revRecency24m+YoyMix

```sql
( [revRecency24m+Perc] - [revRecency24m+LyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revSumCYCly

```sql
CALCULATE ( [revSumCYC], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumCYCYoy

```sql
DIVIDE ( [revSumCYC] - [revSumCYCly], [revSumCYCly], 0 )
```

### CRMTransactionKeyStoryRanking.revSumCYClyPerc

```sql
CALCULATE ( [revSumCYCPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumCYCyoyMix

```sql
( [revSumCYCperc] - [revSumCYClyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revSumBDgiftLY

```sql
CALCULATE ( [revSumBDgift], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumBDgiftYoy

```sql
DIVIDE ( [revSumBDgift] - [revSumBDgiftLY], [revSumBDgiftLY], 0 )
```

### CRMTransactionKeyStoryRanking.revSumBDgiftLyPerc

```sql
CALCULATE ( [revSumBDgiftPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumBDgiftYoyMix

```sql
( [revSumBDgiftPerc] - [revSumBDgiftLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revSumHalfBDly

```sql
CALCULATE ( [revSumHalfBD], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumHalfBDYoy

```sql
DIVIDE ( [revSumHalfBD] - [revSumHalfBDly], [revSumHalfBDly], 0 )
```

### CRMTransactionKeyStoryRanking.revSumHalfBDlyPerc

```sql
CALCULATE ( [revSumHalfBDperc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumHalfBDyoyMix

```sql
( [revSumHalfBDperc] - [revSumHalfBDlyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revSumOtherLY

```sql
CALCULATE ( [revSumOther], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumOtherYoy

```sql
DIVIDE ( [revSumOther] - [revSumOtherLY], [revSumOtherLY], 0 )
```

### CRMTransactionKeyStoryRanking.revSumOtherLyPerc

```sql
CALCULATE ( [revSumOtherPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumOtherYoyMix

```sql
( [revSumOtherPerc] - [revSumOtherLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revSumWinbackLY

```sql
CALCULATE ( [revSumWinback], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumWinbackYoy

```sql
DIVIDE ( [revSumWinback] - [revSumWinbackLY], [revSumWinbackLY], 0 )
```

### CRMTransactionKeyStoryRanking.revSumWinbackLyPerc

```sql
CALCULATE ( [revSumWinbackPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revSumWinbackYoyMix

```sql
( [revSumWinbackPerc] - [revSumWinbackLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCguestTotalPerc

```sql
DIVIDE ( [revBC], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revBCnewGuest

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 1 ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 1
    ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFreshCustomer] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revBCnewGuestPerc

```sql
DIVIDE ( [revBCnewGuest], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuest

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 1 ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFirstPurchase] = 0
    ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFreshCustomer] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestPerc

```sql
DIVIDE ( [revBCrepeatGuest], [revBC], 0 )
```

### CRMTransactionKeyStoryRanking.transTotalLy

```sql
CALCULATE (
    [totCustWebRetTrans],
    DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transTotalYoy

```sql
DIVIDE ( [transTotal] - [transTotalLy], [transTotalLy], 0 )
```

### CRMTransactionKeyStoryRanking.revTotalLy

```sql
CALCULATE ( [revTotal], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revTotalYoy

```sql
DIVIDE ( [revTotal] - [revTotalLy], [revTotalLy], 0 )
```

### CRMTransactionKeyStoryRanking.transTotalPerc

```sql
DIVIDE ( [transTotal], [transTotal], 0 )
```

### CRMTransactionKeyStoryRanking.transTotalLyPerc

```sql
CALCULATE ( [transTotalPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.transTotalYoyMix

```sql
( [transTotalPerc] - [transTotalLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revTotalPerc

```sql
DIVIDE ( [revTotal], [revTotal], 0 )
```

### CRMTransactionKeyStoryRanking.revTotalLyPerc

```sql
CALCULATE ( [revTotalPerc], DATEADD('NewDateDim'[Date_Key], -364, DAY)  )
```

### CRMTransactionKeyStoryRanking.revTotalYoyMix

```sql
( [revTotalPerc] - [revTotalLyPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCguestTotal

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 1 ),
    FILTER (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[isFreshCustomer] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRanking.dptBC

```sql
DIVIDE ( [revBC], [transBC], 0 )
```

### CRMTransactionKeyStoryRanking.dptNonBC

```sql
DIVIDE ( [revNonBC], [transNonBC], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCguestTotal

```sql
DIVIDE ( [revBCguestTotal], [transBCGuestTotal], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCnewGuest

```sql
DIVIDE ( [revBCnewGuest], [transBCnewGuest], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCrepeatGuest

```sql
DIVIDE ( [revBCrepeatGuest], [transBCrepeatGuest], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCfreq2

```sql
DIVIDE ( [revBCfreq2], [transBCfreq2], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCfreq3_4

```sql
DIVIDE ( [revBCfreq3_4], [transBCfreq3_4], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCfreq5_7

```sql
DIVIDE ( [revBCfreq5_7], [transBCfreq5_7], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCfreq8+

```sql
DIVIDE ( [revBCfreq8+], [transBCfreq8+], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency1m

```sql
DIVIDE ( [revRecency1m], [transRecency1m], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency1_3m

```sql
DIVIDE ( [revRecency1_3m], [transRecency1_3m], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency3_6m

```sql
DIVIDE ( [revRecency3_6m], [transRecency3_6m], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency6_12m

```sql
DIVIDE ( [revRecency6_12m], [transRecency6_12m], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency12_18m

```sql
DIVIDE ( [revRecency12_18m], [transRecency12_18m], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency18_24m

```sql
DIVIDE ( [revRecency18_24m], [transRecency18_24m], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency24m+

```sql
DIVIDE ( [revRecency24m+], [transRecency24m+], 0 )
```

### CRMTransactionKeyStoryRanking.dptCYC

```sql
DIVIDE ( [revSumCYC], [transCountCYC], 0 )
```

### CRMTransactionKeyStoryRanking.dptBDgift

```sql
DIVIDE ( [revSumBDgift], [transCountBDgift], 0 )
```

### CRMTransactionKeyStoryRanking.dptHalfBD

```sql
DIVIDE ( [revSumHalfBD], [transCountHalfBD], 0 )
```

### CRMTransactionKeyStoryRanking.dptOther

```sql
DIVIDE ( [revSumOther], [transCountOther], 0 )
```

### CRMTransactionKeyStoryRanking.dptWinback

```sql
DIVIDE ( [revSumWinback], [transCountWinback], 0 )
```

### CRMTransactionKeyStoryRanking.dptBClapsed

```sql
DIVIDE ( [revBClapsed], [transBClapsed], 0 )
```

### CRMTransactionKeyStoryRanking.dptTotalLy

```sql
CALCULATE ( [dptTotal], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBCly

```sql
CALCULATE ( [dptBC], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptNonBCly

```sql
CALCULATE ( [dptNonBC], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBCguestTotalLy

```sql
CALCULATE ( [dptBCguestTotal], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBCnewGuestLy

```sql
CALCULATE ( [dptBCnewGuest], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBCrepeatGuestLy

```sql
CALCULATE ( [dptBCrepeatGuest], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBCfreq2Ly

```sql
CALCULATE ( [dptBCfreq2], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBCfreq3_4Ly

```sql
CALCULATE ( [dptBCfreq3_4], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBCfreq5_7Ly

```sql
CALCULATE ( [dptBCfreq5_7], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBCfreq8+Ly

```sql
CALCULATE ( [dptBCfreq8+], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBClapsedLy

```sql
CALCULATE ( [dptBClapsed], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptRecency1mLy

```sql
CALCULATE ( [dptRecency1m], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptRecency1_3mLy

```sql
CALCULATE ( [dptRecency1_3m], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptRecency3_6mLy

```sql
CALCULATE ( [dptRecency3_6m], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptRecency6_12mLy

```sql
CALCULATE ( [dptRecency6_12m], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptRecency12_18mLy

```sql
CALCULATE ( [dptRecency12_18m], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptRecency18_24mLy

```sql
CALCULATE ( [dptRecency18_24m], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptRecency24m+Ly

```sql
CALCULATE ( [dptRecency24m+], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptCYCly

```sql
CALCULATE ( [dptCYC], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptBDgiftLy

```sql
CALCULATE ( [dptBDgift], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptHalfBDly

```sql
CALCULATE ( [dptHalfBD], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptOtherLy

```sql
CALCULATE ( [dptOther], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptWinbackLy

```sql
CALCULATE ( [dptWinback], SAMEPERIODLASTYEAR ( 'NewDateDim'[Date_Key] ) )
```

### CRMTransactionKeyStoryRanking.dptTotalYoy

```sql
DIVIDE ( [dptTotal] - [dptTotalLy], [dptTotalLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCYoy

```sql
DIVIDE ( [dptBC] - [dptBCly], [dptBCly], 0 )
```

### CRMTransactionKeyStoryRanking.dptNonBCYoy

```sql
DIVIDE ( [dptNonBC] - [dptNonBCly], [dptNonBCly], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCguestTotalYoy

```sql
DIVIDE ( [dptBCguestTotal] - [dptBCguestTotalLy], [dptBCguestTotalLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCnewGuestYoy

```sql
DIVIDE ( [dptBCnewGuest] - [dptBCnewGuestLy], [dptBCnewGuestLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCrepeatGuestYoy

```sql
DIVIDE ( [dptBCrepeatGuest] - [dptBCrepeatGuestLy], [dptBCrepeatGuestLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCfreq2Yoy

```sql
DIVIDE ( [dptBCfreq2] - [dptBCfreq2Ly], [dptBCfreq2Ly], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCfreq3_4Yoy

```sql
DIVIDE ( [dptBCfreq3_4] - [dptBCfreq3_4Ly], [dptBCfreq3_4Ly], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCfreq5_7Yoy

```sql
DIVIDE ( [dptBCfreq5_7] - [dptBCfreq5_7Ly], [dptBCfreq5_7Ly], 0 )
```

### CRMTransactionKeyStoryRanking.dptBCfreq8+Yoy

```sql
DIVIDE ( [dptBCfreq8+] - [dptBCfreq8+Ly], [dptBCfreq8+Ly], 0 )
```

### CRMTransactionKeyStoryRanking.dptBClapsedYoy

```sql
DIVIDE ( [dptBClapsed] - [dptBClapsedLy], [dptBClapsedLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency1mYoy

```sql
DIVIDE ( [dptRecency1m] - [dptRecency1mLy], [dptRecency1mLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency1_3mYoy

```sql
DIVIDE ( [dptRecency1_3m] - [dptRecency1_3mLy], [dptRecency1_3mLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency3_6mYoy

```sql
DIVIDE ( [dptRecency3_6m] - [dptRecency3_6mLy], [dptRecency3_6mLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency6_12mYoy

```sql
DIVIDE ( [dptRecency6_12m] - [dptRecency6_12mLy], [dptRecency6_12mLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency12_18mYoy

```sql
DIVIDE ( [dptRecency12_18m] - [dptRecency12_18mLy], [dptRecency12_18mLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency18_24mYoy

```sql
DIVIDE ( [dptRecency18_24m] - [dptRecency18_24mLy], [dptRecency18_24mLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptRecency24m+Yoy

```sql
DIVIDE ( [dptRecency24m+] - [dptRecency24m+Ly], [dptRecency24m+Ly], 0 )
```

### CRMTransactionKeyStoryRanking.dptCYCYoy

```sql
DIVIDE ( [dptCYC] - [dptCYCLy], [dptCYCLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptBDgiftYoy

```sql
DIVIDE ( [dptBDgift] - [dptBDgiftLy], [dptBDgiftLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptHalfBDYoy

```sql
DIVIDE ( [dptHalfBD] - [dptHalfBDLy], [dptHalfBDLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptOtherYoy

```sql
DIVIDE ( [dptOther] - [dptOtherLy], [dptOtherLy], 0 )
```

### CRMTransactionKeyStoryRanking.dptWinbackYoy

```sql
DIVIDE ( [dptWinback] - [dptWinbackLy], [dptWinbackLy], 0 )
```

### CRMTransactionKeyStoryRanking.transTotalLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transTotalPerc],
        ALL ( 'NewDateDim'[Date_Key] ),
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transTotalMoM

```sql
( [transTotalPerc] - [transTotalLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBClmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transBCperc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transBCmoM

```sql
( [transBCperc] - [transBClmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transNonBClmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transNonBCperc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transNonBCmoM

```sql
( [transNonBCperc] - [transNonBClmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revTotalLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revTotalPerc],
        ALL ( 'NewDateDim'[Date_Key] ),
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revTotalMoM

```sql
( [revTotalPerc] - [revTotalLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBClmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revBCPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revBCMoM

```sql
( [revBCperc] - [revBClmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revNonBClmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revNonBCperc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revNonBCmoM

```sql
( [revNonBCPerc] - [revNonBClmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.dptTotalLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptTotal],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBClm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBC],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptTotalMoM

```sql
( [dptTotal] - [dptTotalLm] ) / [dptTotalLm]
```

### CRMTransactionKeyStoryRanking.dptBCMoM

```sql
( [dptBC] - [dptBCLm] ) / [dptBCLm]
```

### CRMTransactionKeyStoryRanking.dptNonBClm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptNonBC],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptNonBCmoM

```sql
( [dptNonBC] - [dptNonBClm] ) / [dptNonBClm]
```

### CRMTransactionKeyStoryRanking.transBCguestTotalLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transBCguestTotalPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transBCguestTotalMoM

```sql
( [transBCguestTotalPerc] - [transBCguestTotalLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCnewGuestLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transBCnewGuestPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transBCnewGuestMoM

```sql
( [transBCnewGuestPerc] - [transBCnewGuestLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transBCrepeatGuestPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestMoM

```sql
( [transBCrepeatGuestPerc] - [transBCrepeatGuestLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCfreq2LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transBCfreq2Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transBCfreq2MoM

```sql
( [transBCfreq2Perc] - [transBCfreq2LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transBCfreq3_4Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4MoM

```sql
( [transBCfreq3_4Perc] - [transBCfreq3_4LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transBCfreq5_7Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7MoM

```sql
( [transBCfreq5_7Perc] - [transBCfreq5_7LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBCfreq8+LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transBCfreq8+Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transBCfreq8+MoM

```sql
( [transBCfreq8+Perc] - [transBCfreq8+LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transBClapsedLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transBClapsedPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transBClapsedMoM

```sql
( [transBClapsedPerc] - [transBClapsedLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency1mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transRecency1mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transRecency1mMoM

```sql
( [transRecency1mPerc] - [transRecency1mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency1_3mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transRecency1_3mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transRecency1_3mMoM

```sql
( [transRecency1_3mPerc] - [transRecency1_3mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency3_6mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transRecency3_6mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transRecency3_6mMoM

```sql
( [transRecency3_6mPerc] - [transRecency3_6mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency6_12mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transRecency6_12mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transRecency6_12mMoM

```sql
( [transRecency6_12mPerc] - [transRecency6_12mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency12_18mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transRecency12_18mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transRecency12_18mMoM

```sql
( [transRecency12_18mPerc] - [transRecency12_18mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency18_24mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transRecency18_24mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transRecency18_24mMoM

```sql
( [transRecency18_24mPerc] - [transRecency18_24mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transRecency24m+LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transRecency24m+Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transRecency24m+MoM

```sql
( [transRecency24m+Perc] - [transRecency24m+LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountCYClmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transCountCYCPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transCountCYCmoM

```sql
( [transCountCYCPerc] - [transCountCYClmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountBDgiftLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transCountBDgiftPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transCountBDgiftMoM

```sql
( [transCountBDgiftPerc] - [transCountBDgiftLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountHalfBDlmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transCountHalfBDPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transCountHalfBDmOM

```sql
( [transCountHalfBDPerc] - [transCountHalfBDlmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountOtherLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transCountOtherPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transCountOtherMoM

```sql
( [transCountOtherPerc] - [transCountOtherLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.transCountWinbackLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [transCountWinbackPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.transCountWinbackMoM

```sql
( [transCountWinbackPerc] - [transCountWinbackLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCguestTotalLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revBCguestTotalPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revBCguestTotalMoM

```sql
( [revBCguestTotalPerc] - [revBCguestTotalLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCnewGuestLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revBCnewGuestPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revBCnewGuestMoM

```sql
( [revBCnewGuestPerc] - [revBCnewGuestLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revBCrepeatGuestPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestMoM

```sql
( [revBCrepeatGuestPerc] - [revBCrepeatGuestLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCfreq2LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revBCfreq2Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revBCfreq2MoM

```sql
( [revBCfreq2Perc] - [revBCfreq2LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revBCfreq3_4Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4MoM

```sql
( [revBCfreq3_4Perc] - [revBCfreq3_4LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revBCfreq5_7Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7MoM

```sql
( [revBCfreq5_7Perc] - [revBCfreq5_7LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBCfreq8+LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revBCfreq8+Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revBCfreq8+MoM

```sql
( [revBCfreq8+Perc] - [revBCfreq8+LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revBClapsedLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revBClapsedPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revBClapsedMoM

```sql
( [revBClapsedPerc] - [revBClapsedLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency1mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revRecency1mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revRecency1mMoM

```sql
( [revRecency1mPerc] - [revRecency1mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency1_3mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revRecency1_3mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revRecency1_3mMoM

```sql
( [revRecency1_3mPerc] - [revRecency1_3mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency3_6mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revRecency3_6mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revRecency3_6mMoM

```sql
( [revRecency3_6mPerc] - [revRecency3_6mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency6_12mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revRecency6_12mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revRecency6_12mMoM

```sql
( [revRecency6_12mPerc] - [revRecency6_12mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency12_18mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revRecency12_18mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revRecency12_18mMoM

```sql
( [revRecency12_18mPerc] - [revRecency12_18mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency18_24mLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revRecency18_24mPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revRecency18_24mMoM

```sql
( [revRecency18_24mPerc] - [revRecency18_24mLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revRecency24m+LmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revRecency24m+Perc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revRecency24m+MoM

```sql
( [revRecency24m+Perc] - [revRecency24m+LmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.dptBCguestTotalLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBCguestTotal],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBCguestTotalMoM

```sql
( [dptBCguestTotal] - [dptBCguestTotalLm] ) / [dptBCguestTotalLm]
```

### CRMTransactionKeyStoryRanking.dptBCnewGuestLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBCnewGuest],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBCnewGuestMoM

```sql
( [dptBCnewGuest] - [dptBCnewGuestLm] ) / [dptBCnewGuestLm]
```

### CRMTransactionKeyStoryRanking.dptBCrepeatGuestLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBCrepeatGuest],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBCrepeatGuestMoM

```sql
( [dptBCrepeatGuest] - [dptBCrepeatGuestLm] ) / [dptBCrepeatGuestLm]
```

### CRMTransactionKeyStoryRanking.dptBCfreq2Lm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBCfreq2],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBCfreq2MoM

```sql
( [dptBCfreq2] - [dptBCfreq2Lm] ) / [dptBCfreq2Lm]
```

### CRMTransactionKeyStoryRanking.dptBCfreq3_4Lm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBCfreq3_4],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBCfreq3_4MoM

```sql
( [dptBCfreq3_4] - [dptBCfreq3_4Lm] ) / [dptBCfreq3_4Lm]
```

### CRMTransactionKeyStoryRanking.dptBCfreq5_7Lm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBCfreq5_7],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBCfreq5_7MoM

```sql
( [dptBCfreq5_7] - [dptBCfreq5_7Lm] ) / [dptBCfreq5_7Lm]
```

### CRMTransactionKeyStoryRanking.dptBCfreq8+Lm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBCfreq8+],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBCfreq8+MoM

```sql
( [dptBCfreq8+] - [dptBCfreq8+Lm] ) / [dptBCfreq8+Lm]
```

### CRMTransactionKeyStoryRanking.dptBClapsedLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBClapsed],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBClapsedMoM

```sql
( [dptBClapsed] - [dptBClapsedLm] ) / [dptBClapsedLm]
```

### CRMTransactionKeyStoryRanking.dptRecency1mLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptRecency1m],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptRecency1mMoM

```sql
( [dptRecency1m] - [dptRecency1mLm] ) / [dptRecency1mLm]
```

### CRMTransactionKeyStoryRanking.dptRecency1_3mLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptRecency1_3m],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptRecency1_3mMoM

```sql
( [dptRecency1_3m] - [dptRecency1_3mLm] ) / [dptRecency1_3mLm]
```

### CRMTransactionKeyStoryRanking.dptRecency3_6mLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptRecency3_6m],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptRecency3_6mMoM

```sql
( [dptRecency3_6m] - [dptRecency3_6mLm] ) / [dptRecency3_6mLm]
```

### CRMTransactionKeyStoryRanking.dptRecency6_12mLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptRecency6_12m],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptRecency6_12mMoM

```sql
( [dptRecency6_12m] - [dptRecency6_12mLm] ) / [dptRecency6_12mLm]
```

### CRMTransactionKeyStoryRanking.dptRecency12_18mLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptRecency12_18m],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptRecency12_18mMoM

```sql
( [dptRecency12_18m] - [dptRecency12_18mLm] ) / [dptRecency12_18mLm]
```

### CRMTransactionKeyStoryRanking.dptRecency18_24mLm 

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptRecency18_24m],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptRecency18_24mMoM

```sql
( [dptRecency18_24m] - [dptRecency18_24mLm ] ) / [dptRecency18_24mLm ]
```

### CRMTransactionKeyStoryRanking.dptRecency24m+Lm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptRecency24m+],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptRecency24m+MoM

```sql
( [dptRecency24m+] - [dptRecency24m+Lm] ) / [dptRecency24m+Lm]
```

### CRMTransactionKeyStoryRanking.revSumCYClmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revSumCYCPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revSumCYCmoM

```sql
( [revSumCYCPerc] - [revSumCYClmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revSumBDgiftLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revSumBDgiftPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revSumBDgiftMoM

```sql
( [revSumBDgiftPerc] - [revSumBDgiftLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revSumHalfBDlmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revSumHalfBDPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revSumHalfBDmOM

```sql
( [revSumHalfBDPerc] - [revSumHalfBDlmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revSumOtherLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revSumOtherPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revSumOtherMoM

```sql
( [revSumOtherPerc] - [revSumOtherLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.revSumWinbackLmPerc

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [revSumWinbackPerc],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.revSumWinbackMoM

```sql
( [revSumWinbackPerc] - [revSumWinbackLmPerc] ) * 100
```

### CRMTransactionKeyStoryRanking.dptCYClm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptCYC],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptCYCmoM

```sql
( [dptCYC] - [dptCYClm] ) / [dptCYClm]
```

### CRMTransactionKeyStoryRanking.dptBDgiftLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptBDgift],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptBDgiftMoM

```sql
( [dptBDgift] - [dptBDgiftLm] ) / [dptBDgiftLm]
```

### CRMTransactionKeyStoryRanking.dptHalfBDlm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptHalfBD],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptHalfBDmOM

```sql
( [dptHalfBD] - [dptHalfBDlm] ) / [dptHalfBDlm]
```

### CRMTransactionKeyStoryRanking.dptOtherLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptOther],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptOtherMoM

```sql
( [dptOther] - [dptOtherLm] ) / [dptOtherLm]
```

### CRMTransactionKeyStoryRanking.dptWinbackLm

```sql
VAR currentMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month_Of_Year_Key] )
VAR lastMonth = currentMonth - 1
VAR currentFiscalYearString =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Year] )
VAR currentYear =
    RIGHT ( currentFiscalYearString, 4 )
VAR lastYear =
    VALUE ( RIGHT ( currentYear, 4 ) - 1 )
VAR lastFiscalYearString =
    "FY " & FORMAT ( lastYear, "General Number" )
VAR currentFiscalMonth =
    SELECTEDVALUE ( 'NewDateDim'[Fiscal_Month] )
VAR lastFiscalMonth =
    "FY "
        & SWITCH (
            currentMonth,
            1, "Jan",
            2, "Feb",
            3, "Mar",
            4, "Apr",
            5, "May",
            6, "Jun",
            7, "Jul",
            8, "Aug",
            9, "Sep",
            10, "Oct",
            11, "Nov",
            12, "Dec"
        ) & ","
        & IF ( currentMonth = 1, lastYear, currentYear )
RETURN
    CALCULATE (
        [dptWinback],
        FILTER ( ALL ( 'NewDateDim' ), 'NewDateDim'[Fiscal_Month] = lastFiscalMonth ),
        ALL ( 'NewDateDim' )
    )
```

### CRMTransactionKeyStoryRanking.dptWinbackMoM

```sql
( [dptWinback] - [dptWinbackLm] ) / [dptWinbackLm]
```

### CRMTransactionKeyStoryRanking.revTotalYTD

```sql
CALCULATE (
    [revTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revNonBCYTD

```sql
CALCULATE (
    [revNonBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCYTD

```sql
CALCULATE (
    [revBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCguestTotalYTD 

```sql
CALCULATE (
    [revBCguestTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCnewGuestYTD

```sql
CALCULATE (
    [revBCnewGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestYTD

```sql
CALCULATE (
    [revBCrepeatGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq2YTD

```sql
CALCULATE (
    [revBCfreq2],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4YTD

```sql
CALCULATE (
    [revBCfreq3_4],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7YTD

```sql
CALCULATE (
    [revBCfreq5_7],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq8+YTD

```sql
CALCULATE (
    [revBCfreq8+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBClapsedYTD

```sql
CALCULATE (
    [revBClapsed],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency1mYTD

```sql
CALCULATE (
    [revRecency1m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency1_3mYTD

```sql
CALCULATE (
    [revRecency1_3m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency3_6mYTD

```sql
CALCULATE (
    [revRecency3_6m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency6_12mYTD

```sql
CALCULATE (
    [revRecency6_12m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency12_18mYTD

```sql
CALCULATE (
    [revRecency12_18m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency18_24mYTD

```sql
CALCULATE (
    [revRecency18_24m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumCYCYTD

```sql
CALCULATE (
    [revSumCYC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumBDgiftYTD

```sql
CALCULATE (
    [revSumBDgift],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumHalfBDYTD

```sql
CALCULATE (
    [revSumHalfBD],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumOtherYTD

```sql
CALCULATE (
    [revSumOther],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumWinbackYTD

```sql
CALCULATE (
    [revSumWinback],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revTotalPercYTD

```sql
CALCULATE (
    [revTotalPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revNonBCpercYTD

```sql
CALCULATE (
    [revNonBCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCpercYTD

```sql
CALCULATE (
    [revBCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCguestTotalPercYTD

```sql
CALCULATE (
    [revBCguestTotalPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCnewGuestPercYTD

```sql
CALCULATE (
    [revBCnewGuestPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestPercYTD

```sql
CALCULATE (
    [revBCrepeatGuestPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq2PercYTD

```sql
CALCULATE (
    [revBCfreq2Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4PercYTD

```sql
CALCULATE (
    [revBCfreq3_4Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7PercYTD

```sql
CALCULATE (
    [revBCfreq5_7Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq8+PercYTD

```sql
CALCULATE (
    [revBCfreq8+Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBClapsedPercYTD

```sql
CALCULATE (
    [revBClapsedPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency1mPercYTD

```sql
CALCULATE (
    [revRecency1mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency1_3mPercYTD

```sql
CALCULATE (
    [revRecency1_3mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency3_6mPercYTD

```sql
CALCULATE (
    [revRecency3_6mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency6_12mPercYTD

```sql
CALCULATE (
    [revRecency6_12mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency12_18mPercYTD

```sql
CALCULATE (
    [revRecency12_18mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency18_24mPercYTD

```sql
CALCULATE (
    [revRecency18_24mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumCYCpercYTD

```sql
CALCULATE (
    [revSumCYCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumBDgiftPercYTD

```sql
CALCULATE (
    [revSumBDgiftPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumHalfBDpercYTD

```sql
CALCULATE (
    [revSumHalfBDperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumOtherPercYTD

```sql
CALCULATE (
    [revSumOtherPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumWinbackPercYTD

```sql
CALCULATE (
    [revSumWinbackPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency24m+PercYTD

```sql
CALCULATE (
    [revRecency24m+Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency24m+YTD

```sql
CALCULATE (
    [revRecency24m+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transTotalYTD

```sql
CALCULATE (
    [transTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transNonBCYTD

```sql
CALCULATE (
    [transNonBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCYTD

```sql
CALCULATE (
    [transBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCguestTotalYTD

```sql
CALCULATE (
    [transBCguestTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCnewGuestYTD

```sql
CALCULATE (
    [transBCnewGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestYTD

```sql
CALCULATE (
    [transBCrepeatGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq2YTD

```sql
CALCULATE (
    [transBCfreq2],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4YTD

```sql
CALCULATE (
    [transBCfreq3_4],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7YTD

```sql
CALCULATE (
    [transBCfreq5_7],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq8+YTD

```sql
CALCULATE (
    [transBCfreq8+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBClapsedYTD

```sql
CALCULATE (
    [transBClapsed],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency1mYTD

```sql
CALCULATE (
    [transRecency1m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency1_3mYTD

```sql
CALCULATE (
    [transRecency1_3m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency3_6mYTD

```sql
CALCULATE (
    [transRecency3_6m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency6_12mYTD

```sql
CALCULATE (
    [transRecency6_12m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency12_18mYTD

```sql
CALCULATE (
    [transRecency12_18m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency18_24mYTD

```sql
CALCULATE (
    [transRecency18_24m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency24m+YTD 

```sql
CALCULATE (
    [transRecency24m+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountCYCYTD

```sql
CALCULATE (
    [transCOuntCYC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountBDgiftYTD

```sql
CALCULATE (
    [transCountBDgift],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountHalfBDYTD

```sql
CALCULATE (
    [transCountHalfBD],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountOtherYTD

```sql
CALCULATE (
    [transCountOther],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountWinbackYTD

```sql
CALCULATE (
    [transCountWinback],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transTotalPercYTD

```sql
CALCULATE (
    [transTotalPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transNonBCpercYTD

```sql
CALCULATE (
    [transNonBCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCpercYTD

```sql
CALCULATE (
    [transBCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCguestTotalPercYTD

```sql
CALCULATE (
    [transBCguestTotalPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCnewGuestPercYTD

```sql
CALCULATE (
    [transBCnewGuestPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestPercYTD

```sql
CALCULATE (
    [transBCrepeatGuestPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq2PercYTD

```sql
CALCULATE (
    [transBCfreq2Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4PercYTD

```sql
CALCULATE (
    [transBCfreq3_4Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7PercYTD

```sql
CALCULATE (
    [transBCfreq5_7Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq8+PercYTD

```sql
CALCULATE (
    [transBCfreq8+Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBClapsedPercYTD

```sql
CALCULATE (
    [transBClapsedPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency1mPercYTD

```sql
CALCULATE (
    [transRecency1mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency1_3mPercYTD

```sql
CALCULATE (
    [transRecency1_3mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency3_6mPercYTD

```sql
CALCULATE (
    [transRecency3_6mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency6_12mPercYTD

```sql
CALCULATE (
    [transRecency6_12mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency12_18mPercYTD

```sql
CALCULATE (
    [transRecency12_18mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency18_24mPercYTD

```sql
CALCULATE (
    [transRecency18_24mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency24m+PercYTD

```sql
CALCULATE (
    [transRecency24m+Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountCYCpercYTD

```sql
CALCULATE (
    [transCountCYCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountBDgiftPercYTD

```sql
CALCULATE (
    [transCountBDgiftPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountHalfBDpercYTD

```sql
CALCULATE (
    [transCountHalfBDperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountOtherPercYTD

```sql
CALCULATE (
    [transCountOtherPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountWinbackPercYTD

```sql
CALCULATE (
    [transCountWinbackPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptTotalYTD

```sql
CALCULATE (
    [dptTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptNonBCYTD

```sql
CALCULATE (
    [dptNonBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCYTD

```sql
CALCULATE (
    [dptBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCguestTotalYTD

```sql
CALCULATE (
    [dptBCguestTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCnewGestYTD

```sql
CALCULATE (
    [dptBCnewGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCrepeatGuestYTD

```sql
CALCULATE (
    [dptBCrepeatGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCfreq2YTD

```sql
CALCULATE (
    [dptBCfreq2],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCfreq3_4YTD

```sql
CALCULATE (
    [dptBCfreq3_4],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCfreq5_7YTD

```sql
CALCULATE (
    [dptBCfreq5_7],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCfreq8+YTD

```sql
CALCULATE (
    [dptBCfreq8+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBClapsedYTD

```sql
CALCULATE (
    [dptBClapsed],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency1mYTD

```sql
CALCULATE (
    [dptRecency1m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency1_3mYTD

```sql
CALCULATE (
    [dptRecency1_3m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency3_6mYTD

```sql
CALCULATE (
    [dptRecency3_6m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency6_12mYTD

```sql
CALCULATE (
    [dptRecency6_12m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency12_18mYTD

```sql
CALCULATE (
    [dptRecency12_18m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency18_24mYTD

```sql
CALCULATE (
    [dptRecency18_24m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency24m+YTD

```sql
CALCULATE (
    [dptRecency24m+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptCYCYTD

```sql
CALCULATE (
    [dptCYC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBDgiftYTD

```sql
CALCULATE (
    [dptBDgift],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptHalfBDYTD

```sql
CALCULATE (
    [dptHalfBD],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptOtherYTD

```sql
CALCULATE (
    [dptOther],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptWinbackYTD

```sql
CALCULATE (
    [dptWinback],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Year] = VALUES ( NewDateDim[Fiscal_Year] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revTotalQTD

```sql
CALCULATE (
    [revTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revNonBCQTD

```sql
CALCULATE (
    [revNonBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCQTD

```sql
CALCULATE (
    [revBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCguestTotalQTD

```sql
CALCULATE (
    [revBCguestTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCnewGuestQTD

```sql
CALCULATE (
    [revBCnewGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestQTD

```sql
CALCULATE (
    [revBCrepeatGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq2QTD

```sql
CALCULATE (
    [revBCfreq2],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4QTD

```sql
CALCULATE (
    [revBCfreq3_4],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7QTD

```sql
CALCULATE (
    [revBCfreq5_7],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq8+QTD

```sql
CALCULATE (
    [revBCfreq8+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBClapsedQTD

```sql
CALCULATE (
    [revBClapsed],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency1mQTD

```sql
CALCULATE (
    [revRecency1m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency1_3mQTD

```sql
CALCULATE (
    [revRecency1_3m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency3_6mQTD

```sql
CALCULATE (
    [revRecency3_6m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency6_12mQTD

```sql
CALCULATE (
    [revRecency6_12m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency12_18mQTD

```sql
CALCULATE (
    [revRecency12_18m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency18_24mQTD

```sql
CALCULATE (
    [revRecency18_24m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency24m+QTD

```sql
CALCULATE (
    [revRecency24m+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumCYCQTD

```sql
CALCULATE (
    [revSumCYC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumBDgiftQTD

```sql
CALCULATE (
    [revSumBDgift],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumHalfBDQTD

```sql
CALCULATE (
    [revSumHalfBD],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumOtherQTD

```sql
CALCULATE (
    [revSumOther],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumWinbackQTD

```sql
CALCULATE (
    [revSumWinback],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revTotalPercQTD

```sql
CALCULATE (
    [revTotalPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revNonBCpercQTD

```sql
CALCULATE (
    [revNonBCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCpercQTD

```sql
CALCULATE (
    [revBCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCguestTotalPercQTD

```sql
CALCULATE (
    [revBCguestTotalPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCnewGuestPercQTD

```sql
CALCULATE (
    [revBCnewGuestPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCrepeatGuestPercQTD

```sql
CALCULATE (
    [revBCrepeatGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq2PercQTD

```sql
CALCULATE (
    [revBCfreq2Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq3_4PercQTD

```sql
CALCULATE (
    [revBCfreq3_4Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq5_7PercQTD

```sql
CALCULATE (
    [revBCfreq5_7Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBCfreq8+PercQTD

```sql
CALCULATE (
    [revBCfreq8+Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revBClapsedPercQTD

```sql
CALCULATE (
    [revBClapsedPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency1mPercQTD

```sql
CALCULATE (
    [revRecency1mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency1_3mPercQTD

```sql
CALCULATE (
    [revRecency1_3mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency3_6mPercQTD

```sql
CALCULATE (
    [revRecency3_6mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency6_12mPercQTD

```sql
CALCULATE (
    [revRecency6_12mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency12_18mPercQTD

```sql
CALCULATE (
    [revRecency12_18mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency18_24mPercQTD

```sql
CALCULATE (
    [revRecency18_24mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revRecency24m+PercQTD

```sql
CALCULATE (
    [revRecency24m+Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumCYCpercQTD

```sql
CALCULATE (
    [revSumCYCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumBDgiftPercQTD

```sql
CALCULATE (
    [revSumBDgiftPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumHalfBDpercQTD

```sql
CALCULATE (
    [revSumHalfBDperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumOtherPercQTD

```sql
CALCULATE (
    [revSumOtherPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.revSumWinbackPercQTD

```sql
CALCULATE (
    [revSumWinbackPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transTotalQTD

```sql
CALCULATE (
    [transTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transNonBCQTD

```sql
CALCULATE (
    [transNonBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCQTD

```sql
CALCULATE (
    [transBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCguestTotalQTD

```sql
CALCULATE (
    [transBCguestTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCnewGuestQTD

```sql
CALCULATE (
    [transBCnewGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestQTD

```sql
CALCULATE (
    [transBCrepeatGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq2QTD

```sql
CALCULATE (
    [transBCfreq2],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4QTD

```sql
CALCULATE (
    [transBCfreq3_4],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7QTD

```sql
CALCULATE (
    [transBCfreq5_7],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq8+QTD

```sql
CALCULATE (
    [transBCfreq8+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBClapsedQTD

```sql
CALCULATE (
    [transBClapsed],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency1mQTD

```sql
CALCULATE (
    [transRecency1m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency1_3mQTD

```sql
CALCULATE (
    [transRecency1_3m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency3_6mQTD

```sql
CALCULATE (
    [transRecency3_6m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency6_12mQTD

```sql
CALCULATE (
    [transRecency6_12m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency12_18mQTD

```sql
CALCULATE (
    [transRecency12_18m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency18_24mQTD

```sql
CALCULATE (
    [transRecency18_24m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency24m+QTD

```sql
CALCULATE (
    [transRecency24m+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountCYCQTD

```sql
CALCULATE (
    [transCOuntCYC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountBDgiftQTD

```sql
CALCULATE (
    [transCountBDgift],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountHalfBDQTD

```sql
CALCULATE (
    [transCountHalfBD],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountOtherQTD

```sql
CALCULATE (
    [transCountOther],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountWinbackQTD

```sql
CALCULATE (
    [transCountWinback],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transTotalPercQTD

```sql
CALCULATE (
    [transTotalPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transNonBCpercQTD

```sql
CALCULATE (
    [transNonBCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCpercQTD

```sql
CALCULATE (
    [transBCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCguestTotalPercQTD

```sql
CALCULATE (
    [transBCguestTotalPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCnewGuestPercQTD

```sql
CALCULATE (
    [transBCnewGuestPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCrepeatGuestPercQTD

```sql
CALCULATE (
    [transBCrepeatGuestPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq2PercQTD

```sql
CALCULATE (
    [transBCfreq2Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq3_4PercQTD

```sql
CALCULATE (
    [transBCfreq3_4Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq5_7PercQTD

```sql
CALCULATE (
    [transBCfreq5_7Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBCfreq8+PercQTD

```sql
CALCULATE (
    [transBCfreq8+Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transBClapsedPercQTD

```sql
CALCULATE (
    [transBClapsedPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency1mPercQTD

```sql
CALCULATE (
    [transRecency1mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency3_6mPercQTD

```sql
CALCULATE (
    [transRecency3_6mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency6_12mPercQTD

```sql
CALCULATE (
    [transRecency6_12mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency12_18mPercQTD

```sql
CALCULATE (
    [transRecency12_18mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency18_24mPercQTD

```sql
CALCULATE (
    [transRecency18_24mPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transRecency24m+PercQTD

```sql
CALCULATE (
    [transRecency24m+Perc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountCYCpercQTD

```sql
CALCULATE (
    [transCountCYCperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountBDgiftPercQTD

```sql
CALCULATE (
    [transCountBDgiftPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountHalfBDpercQTD

```sql
CALCULATE (
    [transCountHalfBDperc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountOtherPercQTD

```sql
CALCULATE (
    [transCountOtherPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.transCountWinbackPercQTD

```sql
CALCULATE (
    [transCountWinbackPerc],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptTotalQTD

```sql
CALCULATE (
    [dptTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptNonBCQTD

```sql
CALCULATE (
    [dptNonBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCQTD

```sql
CALCULATE (
    [dptBC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCguestTotalQTD

```sql
CALCULATE (
    [dptBCguestTotal],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCnewGestQTD

```sql
CALCULATE (
    [dptBCnewGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCrepeatGuestQTD

```sql
CALCULATE (
    [dptBCrepeatGuest],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCfreq2QTD

```sql
CALCULATE (
    [dptBCfreq2],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCfreq3_4QTD

```sql
CALCULATE (
    [dptBCfreq3_4],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCfreq5_7QTD

```sql
CALCULATE (
    [dptBCfreq5_7],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBCfreq8+QTD

```sql
CALCULATE (
    [dptBCfreq8+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBClapsedQTD

```sql
CALCULATE (
    [dptBClapsed],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency1mQTD

```sql
CALCULATE (
    [dptRecency1m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency1_3mQTD

```sql
CALCULATE (
    [dptRecency1_3m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency3_6mQTD

```sql
CALCULATE (
    [dptRecency3_6m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency6_12mQTD

```sql
CALCULATE (
    [dptRecency6_12m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency18_24mQTD

```sql
CALCULATE (
    [dptRecency18_24m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency24m+QTD

```sql
CALCULATE (
    [dptRecency24m+],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptCYCQTD

```sql
CALCULATE (
    [dptCYC],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptBDgiftQTD

```sql
CALCULATE (
    [dptBDgift],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptHalfBDQTD

```sql
CALCULATE (
    [dptHalfBD],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptOtherQTD

```sql
CALCULATE (
    [dptOther],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptWinbackQTD

```sql
CALCULATE (
    [dptWinback],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.dptRecency12_18mQTD

```sql
CALCULATE (
    [dptRecency12_18m],
    FILTER (
        ALL ( NewDateDim ),
        NewDateDim[Fiscal_Quarter] = VALUES ( NewDateDim[Fiscal_Quarter] )
            && NewDateDim[Date_Key] <= MAX ( NewDateDim[Date_Key] )
    )
)
```

### CRMTransactionKeyStoryRanking.bcUnits

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStoryUnits] ),
    FILTER ( 'CRMcustomerMasterData', 'CRMcustomerMasterData'[isActive] = 1 )
) + 0
```

### CRMTransactionKeyStoryRanking.trans12moCurTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 365
)
```

### CRMTransactionKeyStoryRanking.trans12moCurPctTtl

```sql
DIVIDE([trans12mo], [trans12moCurTtl])
```

### CRMTransactionKeyStoryRanking.trans12moPriorTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 729
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365
)
```

### CRMTransactionKeyStoryRanking.trans12moPriorPctTtl

```sql
DIVIDE ( [trans12moPrev], [trans12moPriorTtl] )
```

### CRMTransactionKeyStoryRanking.trans3moLyCurTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 90
)
```

### CRMTransactionKeyStoryRanking.trans3moLyCurPctTtl

```sql
DIVIDE ( [trans3mo], [trans3moLyCurTtl] )
```

### CRMTransactionKeyStoryRanking.trans3moLyPriorTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 454
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365
)
```

### CRMTransactionKeyStoryRanking.trans3moLyPriorPctTtl

```sql
DIVIDE([trans3moLy], [trans3moLyPriorTtl])
```

### CRMTransactionKeyStoryRanking.trans3moPrevPriorTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 180
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 91
)
```

### CRMTransactionKeyStoryRanking.trans3moPrevPriorPctTtl

```sql
DIVIDE ( [trans3moPrev], [trans3moPrevPriorTtl] )
```

### CRMTransactionKeyStoryRanking.trans1moCurTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 30
)
```

### CRMTransactionKeyStoryRanking.trans1moCurPctTtl

```sql
DIVIDE([trans1mo], [trans1moCurTtl])
```

### CRMTransactionKeyStoryRanking.trans1moLyTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 394
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365
)
```

### CRMTransactionKeyStoryRanking.trans1moLyPctTtl

```sql
DIVIDE([trans1moLy], [trans1moLyTtl])
```

### CRMTransactionKeyStoryRanking.trans1moPrevCurTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 60
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 31
)
```

### CRMTransactionKeyStoryRanking.trans1moPrevPctTtl

```sql
DIVIDE ( [trans1moPrev], [trans1moPrevCurTtl] )
```

### CRMTransactionKeyStoryRanking.trans1wkCurTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 7
)
```

### CRMTransactionKeyStoryRanking.trans1wkCurPctTtl 

```sql
DIVIDE([trans1wk], [trans1wkCurTtl])
```

### CRMTransactionKeyStoryRanking.trans1wkLyCurTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 371
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365
)
```

### CRMTransactionKeyStoryRanking.trans1wkLyPctTtl

```sql
DIVIDE ( [trans1wkLy], [trans1wkLyCurTtl] )
```

### CRMTransactionKeyStoryRanking.trans1wkPrevCurTtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 14
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 8
)
```

### CRMTransactionKeyStoryRanking.trans1wkPrevPctTtl

```sql
DIVIDE([trans1wkPrev], [trans1wkPrevCurTtl])
```

### CRMTransactionKeyStoryRanking.trans12moCurTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans12moCurPerTtlRtl 

```sql
DIVIDE ( [trans12mo], [trans12moCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.trans12moPrevTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 729
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans12moPrevPerTtlRtl

```sql
DIVIDE ( [trans12moPrev], [trans12moPrevTtlRtl] )
```

### CRMTransactionKeyStoryRanking.trans3moLyCurTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 90,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans3moLyCurPctTtlRtl

```sql
DIVIDE ( [trans3mo], [trans3moLyCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.trans3moLyPriorTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 454
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans3moLyPriorPctTtlRtl

```sql
DIVIDE([trans3moLy], [trans3moLyPriorTtlRtl])
```

### CRMTransactionKeyStoryRanking.trans3moPrevPriorTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 180
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 91,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans3moPrevPriorPctTtlRtl

```sql
DIVIDE ( [trans3moPrev], [trans3moPrevPriorTtlRtl] )
```

### CRMTransactionKeyStoryRanking.trans1moCurTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 30,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1moCurPctTtlRtl

```sql
DIVIDE([trans1mo], [trans1moCurTtlRtl])
```

### CRMTransactionKeyStoryRanking.trans1moLyTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 394
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1moLyPctTtlRtl

```sql
DIVIDE([trans1moLy], [trans1moLyTtlRtl])
```

### CRMTransactionKeyStoryRanking.trans1moPrevCurTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 60
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 31,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1moPrevPctTtlRtl

```sql
DIVIDE ( [trans1moPrev], [trans1moPrevCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.trans1wkCurTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 7,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1wkCurPctTtlRtl

```sql
DIVIDE([trans1wk], [trans1wkCurTtlRtl])
```

### CRMTransactionKeyStoryRanking.trans1wkLyCurTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 371
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1wkLyPctTtlRtl

```sql
DIVIDE ( [trans1wkLy], [trans1wkLyCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.trans1wkPrevCurTtlRtl

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 14
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 8,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1wkPrevPctTtlRtl

```sql
DIVIDE([trans1wkPrev], [trans1wkPrevCurTtlRtl])
```

### CRMTransactionKeyStoryRanking.trans12moCurTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans12moCurPerTtlWeb

```sql
DIVIDE ( [trans12mo], [trans12moCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.trans12moPrevTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 729
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans12moPrevPerTtlWeb

```sql
DIVIDE ( [trans12moPrev], [trans12moPrevTtlWeb] )
```

### CRMTransactionKeyStoryRanking.trans3moLyCurTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 90,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans3moLyCurPctTtlWeb

```sql
DIVIDE ( [trans3mo], [trans3moLyCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.trans3moLyPriorTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 454
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans3moLyPriorPctTtlWeb

```sql
DIVIDE([trans3moLy], [trans3moLyPriorTtlWeb])
```

### CRMTransactionKeyStoryRanking.trans3moPrevPriorTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 180
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 91,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans3moPrevPriorPctTtlWeb

```sql
DIVIDE ( [trans3moPrev], [trans3moPrevPriorTtlWeb] )
```

### CRMTransactionKeyStoryRanking.trans1moCurTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 30,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1moCurPctTtlWeb

```sql
DIVIDE([trans1mo], [trans1moCurTtlWeb])
```

### CRMTransactionKeyStoryRanking.trans1moLyTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 394
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1moLyPctTtlWeb

```sql
DIVIDE([trans1moLy], [trans1moLyTtlWeb])
```

### CRMTransactionKeyStoryRanking.trans1moPrevCurTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 60
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 31,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1moPrevPctTtlWeb

```sql
DIVIDE ( [trans1moPrev], [trans1moPrevCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.trans1wkCurTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 7,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1wkCurPctTtlWeb

```sql
DIVIDE([trans1wk], [trans1wkCurTtlWeb])
```

### CRMTransactionKeyStoryRanking.trans1wkLyCurTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 371
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1wkLyPctTtlWeb

```sql
DIVIDE ( [trans1wkLy], [trans1wkLyCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.trans1wkPrevCurTtlWeb

```sql
CALCULATE (
    DISTINCTCOUNT ( CRMTransactionKeyStoryRanking[TransactionID] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 14
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 8,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.trans1wkPrevPctTtlWeb

```sql
DIVIDE([trans1wkPrev], [trans1wkPrevCurTtlWeb])
```

### CRMTransactionKeyStoryRanking.rev12moCurTtl

```sql
CALCULATE ( SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ), ALLEXCEPT('CRMTransactionKeyStoryRanking','CRMTransactionKeyStoryRanking'[TransactionDate]), 'CRMTransactionKeyStoryRanking'[TransactionDate] >= TODAY () - 365)

```

### CRMTransactionKeyStoryRanking.rev12moCurPctTtl

```sql
DIVIDE ( [rev12mo], [rev12moCurTtl] )
```

### CRMTransactionKeyStoryRanking.rev12moPriorTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 729
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365
)
```

### CRMTransactionKeyStoryRanking.rev12moPriorPctTtl

```sql
DIVIDE ( [rev12moPrev], [rev12moPriorTtl] )
```

### CRMTransactionKeyStoryRanking.rev3moLyCurTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 90
)
```

### CRMTransactionKeyStoryRanking.rev3moLyCurPctTtl

```sql
DIVIDE ( [rev3mo], [rev3moLyCurTtl] )
```

### CRMTransactionKeyStoryRanking.rev3moLyPriorTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 454
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365
)
```

### CRMTransactionKeyStoryRanking.rev3moLyPriorPctTtl

```sql
DIVIDE([rev3moLy], [rev3moLyPriorTtl])
```

### CRMTransactionKeyStoryRanking.rev3moPrevPriorTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 180
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 91
)
```

### CRMTransactionKeyStoryRanking.rev3moPrevPriorPctTtl

```sql
DIVIDE ( [rev3moPrev], [rev3moPrevPriorTtl] )
```

### CRMTransactionKeyStoryRanking.rev1moCurTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 30
)
```

### CRMTransactionKeyStoryRanking.rev1moCurPctTtl

```sql
DIVIDE([rev1mo], [rev1moCurTtl])
```

### CRMTransactionKeyStoryRanking.rev1moLyTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 394
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365
)
```

### CRMTransactionKeyStoryRanking.rev1moLyPctTtl

```sql
DIVIDE([rev1moLy], [rev1moLyTtl])
```

### CRMTransactionKeyStoryRanking.rev1moPrevCurTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 60
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 31
)
```

### CRMTransactionKeyStoryRanking.rev1moPrevPctTtl 

```sql
DIVIDE ( [rev1moPrev], [rev1moPrevCurTtl] )
```

### CRMTransactionKeyStoryRanking.rev1wkCurTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 7
)
```

### CRMTransactionKeyStoryRanking.rev1wkCurPctTtl

```sql
DIVIDE([rev1wk], [rev1wkCurTtl])
```

### CRMTransactionKeyStoryRanking.rev1wkLyCurTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 371
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365
)
```

### CRMTransactionKeyStoryRanking.rev1wkLyPctTtl

```sql
DIVIDE ( [rev1wkLy], [rev1wkLyCurTtl] )
```

### CRMTransactionKeyStoryRanking.rev1wkPrevCurTtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 14
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 8
)
```

### CRMTransactionKeyStoryRanking.rev1wkPrevPctTtl 

```sql
DIVIDE([rev1wkPrev], [rev1wkPrevCurTtl])
```

### CRMTransactionKeyStoryRanking.rev12moCurTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev12moCurPctTtlRtl

```sql
DIVIDE ( [rev12mo], [rev12moCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.rev12moPriorTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 729
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev12moPriorPctTtlRtl

```sql
DIVIDE ( [rev12moPrev], [rev12moPriorTtlRtl] )
```

### CRMTransactionKeyStoryRanking.rev3moLyCurTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 90,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev3moLyCurPctTtlRtl

```sql
DIVIDE ( [rev3mo], [rev3moLyCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.rev3moLyPriorTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 454
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev3moLyPriorPctTtlRtl

```sql
DIVIDE([rev3moLy], [rev3moLyPriorTtlRtl])
```

### CRMTransactionKeyStoryRanking.rev3moPrevPriorTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 180
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 91,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev3moPrevPriorPctTtlRtl

```sql
DIVIDE ( [rev3moPrev], [rev3moPrevPriorTtlRtl] )
```

### CRMTransactionKeyStoryRanking.rev1moCurTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 30,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1moCurPctTtlRtl

```sql
DIVIDE([rev1mo], [rev1moCurTtlRtl])
```

### CRMTransactionKeyStoryRanking.rev1moLyPctTtlRtl

```sql
DIVIDE([rev1moLy], [rev1moLyTtlRtl])
```

### CRMTransactionKeyStoryRanking.rev1moPrevCurTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 60
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 31,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1moPrevPctTtlRtl 

```sql
DIVIDE ( [rev1moPrev], [rev1moPrevCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.rev1wkCurTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 7,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1wkCurPctTtlRtl

```sql
DIVIDE ( [rev1wk], [rev1wkCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.rev1wkLyCurTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 371
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1wkLyPctTtlRtl

```sql
DIVIDE ( [rev1wkLy], [rev1wkLyCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.rev1wkPrevCurTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 14
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 8,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1wkPrevPctTtlRtl

```sql
DIVIDE ( [rev1wkPrev], [rev1wkPrevCurTtlRtl] )
```

### CRMTransactionKeyStoryRanking.rev12moCurTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1moCurTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 30,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev12moCurPctTtlWeb

```sql
DIVIDE ( [rev12mo], [rev12moCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.rev12moPriorTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 729
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev12moPriorPctTtlWeb

```sql
DIVIDE ( [rev12moPrev], [rev12moPriorTtlWeb] )
```

### CRMTransactionKeyStoryRanking.rev3moLyCurTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 90,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev3moLyCurPctTtlWeb

```sql
DIVIDE ( [rev3mo], [rev3moLyCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.rev3moLyPriorTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 454
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev3moLyPriorPctTtlWeb

```sql
DIVIDE([rev3moLy], [rev3moLyPriorTtlWeb])
```

### CRMTransactionKeyStoryRanking.rev3moPrevPriorTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 180
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 91,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev3moPrevPriorPctTtlWeb

```sql
DIVIDE ( [rev3moPrev], [rev3moPrevPriorTtlWeb] )
```

### CRMTransactionKeyStoryRanking.rev1moCurPctTtlWeb

```sql
DIVIDE([rev1mo], [rev1moCurTtlWeb])
```

### CRMTransactionKeyStoryRanking.rev1moLyTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 394
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1moLyPctTtlWeb

```sql
DIVIDE([rev1moLy], [rev1moLyTtlWeb])
```

### CRMTransactionKeyStoryRanking.rev1moPrevCurTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 60
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 31,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1moPrevPctTtlWeb

```sql
DIVIDE ( [rev1moPrev], [rev1moPrevCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.rev1wkCurTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 7,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1wkCurPctTtlWeb

```sql
DIVIDE ( [rev1wk], [rev1wkCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.rev1wkLyCurTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 371
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1wkLyPctTtlWeb

```sql
DIVIDE ( [rev1wkLy], [rev1wkLyCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.rev1wkPrevCurTtlWeb

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 14
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 8,
    'CRMTransactionKeyStoryRanking'[isWeb] = 1
)
```

### CRMTransactionKeyStoryRanking.rev1wkPrevPctTtlWeb

```sql
DIVIDE ( [rev1wkPrev], [rev1wkPrevCurTtlWeb] )
```

### CRMTransactionKeyStoryRanking.rev1moLyTtlRtl

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRanking'[KeyStorySales] ),
    ALLEXCEPT (
        'CRMTransactionKeyStoryRanking',
        'CRMTransactionKeyStoryRanking'[TransactionDate]
    ),
    'CRMTransactionKeyStoryRanking'[TransactionDate]
        >= TODAY () - 394
        && 'CRMTransactionKeyStoryRanking'[TransactionDate]
            <= TODAY () - 365,
    'CRMTransactionKeyStoryRanking'[isRetail] = 1
)
```

### CRMTransactionKeyStoryRankingPurchases.totalKSunits

```sql
SUM ( 'CRMTransactionKeyStoryRankingPurchases'[GaapUnits] )
```

### CRMTransactionKeyStoryRankingPurchases.NonBCtrans

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRankingPurchases'[GaapUnits] ),
    FILTER (
        'CRMTransactionKeyStoryRankingPurchases',
        'CRMTransactionKeyStoryRankingPurchases'[customerNumber] = BLANK ()
    )
) + 0
```

### CRMTransactionKeyStoryRankingPurchases.percNonBCtrans

```sql
DIVIDE ( [NonBCtrans], [totalKSunits] )
```

### CRMTransactionKeyStoryRankingPurchases.totalBCtrans

```sql
CALCULATE(SUM('CRMTransactionKeyStoryRankingPurchases'[GaapUnits]),FILTER('CRMTransactionKeyStoryRankingPurchases','CRMTransactionKeyStoryRankingPurchases'[customerNumber] <> BLANK()))+0
```

### CRMTransactionKeyStoryRankingPurchases.percBCtrans

```sql
DIVIDE ( [totalBCtrans], [totalKSunits] )
```

### CRMTransactionKeyStoryRankingPurchases.repeatBCtrans

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRankingPurchases'[GaapUnits] ),
    FILTER (
        'CRMTransactionKeyStoryRankingPurchases',
        'CRMTransactionKeyStoryRankingPurchases'[isRepeatCustomer] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRankingPurchases.repeatBCperc

```sql
DIVIDE ( [repeatBCtrans], [totalBCtrans] )
```

### CRMTransactionKeyStoryRankingPurchases.newBCtrans

```sql
CALCULATE (
    SUM ( 'CRMTransactionKeyStoryRankingPurchases'[GaapUnits] ),
    FILTER (
        'CRMTransactionKeyStoryRankingPurchases',
        'CRMTransactionKeyStoryRankingPurchases'[isNewCustomer] = 1
    )
) + 0
```

### CRMTransactionKeyStoryRankingPurchases.newBCperc

```sql
DIVIDE ( [newBCtrans], [totalBCtrans] )
```

### CRMTransactionKeyStoryRankingPurchases.newGuestRepeatCustomers

```sql
CALCULATE (
    DISTINCTCOUNT ( 'CRMTransactionKeyStoryRankingPurchases'[customerNumber] ),
    FILTER (
        'CRMTransactionKeyStoryRankingPurchases',
        'CRMTransactionKeyStoryRankingPurchases'[isRepeatCustomer] = 1
            && 'CRMTransactionKeyStoryRankingPurchases'[customerNumber] <> BLANK ()
    )
)+0
```

### CRMTransactionKeyStoryRankingPurchases.percGuestRepeated

```sql
DIVIDE ( [newGuestRepeatCustomers], [newBCtrans] )
```

### CRMTransactionKeyStoryRankingPurchases.top2ndPurchase

```sql
VAR currStory =
    MIN ( 'CRMTransactionKeyStoryRankingPurchases'[KeyStory] )
VAR topStories =
    SUMMARIZE (
        FILTER (
            'CRMTransactionKeyStoryRankingPurchases',
            'CRMTransactionKeyStoryRankingPurchases'[2ndPurchase] <> BLANK ()
                && 'CRMTransactionKeyStoryRankingPurchases'[keyStory] = currStory
        ),
        'CRMTransactionKeyStoryRankingPurchases'[2ndpurchase],
        "2ndTop", COUNT ( 'CRMTransactionKeyStoryRankingPurchases'[2ndpurchase] )
    )
RETURN
    MAXX (
        TOPN ( 1, topStories, [2ndTop] ),
        'CRMTransactionKeyStoryRankingPurchases'[2ndPurchase]
    )
```

### CRMTransactionKeyStoryRankingPurchases.top3rdPurchase

```sql
VAR currStory =
    MIN ( 'CRMTransactionKeyStoryRankingPurchases'[KeyStory] )
VAR topStories =
    SUMMARIZE (
        FILTER (
            'CRMTransactionKeyStoryRankingPurchases',
            'CRMTransactionKeyStoryRankingPurchases'[3rdPurchase] <> BLANK ()
                && 'CRMTransactionKeyStoryRankingPurchases'[keyStory] = currStory
        ),
        'CRMTransactionKeyStoryRankingPurchases'[3rdpurchase],
        "3rdTop", COUNT ( 'CRMTransactionKeyStoryRankingPurchases'[3rdpurchase] )
    )
RETURN
    MAXX (
        TOPN ( 1, topStories, [3rdTop] ),
        'CRMTransactionKeyStoryRankingPurchases'[3rdPurchase]
    )
```

### CRMTransactionKeyStoryRankingPurchases.top4thPurchase

```sql
VAR currStory =
    MIN ( 'CRMTransactionKeyStoryRankingPurchases'[KeyStory] )
VAR topStories =
    SUMMARIZE (
        FILTER (
            'CRMTransactionKeyStoryRankingPurchases',
            'CRMTransactionKeyStoryRankingPurchases'[4thPurchase] <> BLANK ()
                && 'CRMTransactionKeyStoryRankingPurchases'[keyStory] = currStory
        ),
        'CRMTransactionKeyStoryRankingPurchases'[4thpurchase],
        "4thTop", COUNT ( 'CRMTransactionKeyStoryRankingPurchases'[4thpurchase] )
    )
RETURN
    MAXX (
        TOPN ( 1, topStories, [4thTop] ),
        'CRMTransactionKeyStoryRankingPurchases'[4thPurchase]
    )
```

### PCHealthChecks.TotalHostsImpacted

```sql
DISTINCTCOUNT([Hostname])
```

### PCHealthChecks.TotalStoresImpacted

```sql
DISTINCTCOUNT([Store])
```

### WMS_cycleCount_accuracy2.unitAccuracy2

```sql
1-ABS(
    DIVIDE(
        SUM('WMS_cycleCount_accuracy'[UnitDifference]),
        SUM('WMS_cycleCount_accuracy'[AmtBeforeCount])
))
```

### WMS_cycleCount_accuracy2.dollarAccuracy2

```sql
1-ABS(
    DIVIDE(
        SUM('WMS_cycleCount_accuracy'[dollarDifference]),
        SUM('WMS_cycleCount_accuracy'[perpetualDollarAmt])
))

```

### WMS_cycleCount_accuracy.unitAccuracy

```sql
1-ABS(
    DIVIDE(
        SUM('WMS_cycleCount_accuracy'[UnitDifference]),
        SUM('WMS_cycleCount_accuracy'[AmtBeforeCount])
))
```

### WMS_cycleCount_accuracy.dollarAccuracy

```sql
1-ABS(
    DIVIDE(
        SUM('WMS_cycleCount_accuracy'[dollarDifference]),
        SUM('WMS_cycleCount_accuracy'[perpetualDollarAmt])
))

```

### IT_CommWorks.TotalClosedIncidents

```sql
calculate(distinctcount('IT_CommWorks'[id]), FILTER('IT_CommWorks', 'IT_CommWorks'[closedFlag] = TRUE)) + 0
```

### IT_CommWorks.TotalOpenIncidents

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_CommWorks'[ID] ),
    FILTER ( 'IT_CommWorks', 'IT_CommWorks'[closedFlag] = FALSE )
) + 0
```

### IT_CommWorks.avgResolveMinutes

```sql
average([resolveMinutes])
```

### IT_Heat.HeatTotalClosedIncidents

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER ( 'IT_Heat', 'IT_Heat'[Status] = "Closed" )
) + 0
```

### IT_Heat.HeatTotalWaiting3pIncidents

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER ( 'IT_Heat', 'IT_Heat'[Status] = "Waiting for 3rd Party" )
) + 0
```

### IT_Heat.HeatTotalLoggedIncidents

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER ( 'IT_Heat', 'IT_Heat'[Status] = "Logged" )
) + 0
```

### IT_Heat.HeatTotalResolvedIncidents

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER ( 'IT_Heat', 'IT_Heat'[Status] = "Resolved" )
) + 0
```

### IT_Heat.HeatTotalWaitingForResIncidents

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER ( 'IT_Heat', 'IT_Heat'[Status] = "Waiting for Resolution" )
) + 0
```

### IT_Heat.HeatTotalWaitingForCustIncidents

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER ( 'IT_Heat', 'IT_Heat'[Status] = "Waiting for Customer" )
) + 0
```

### IT_Heat.HeatTotalActiveIncidents

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER ( 'IT_Heat', 'IT_Heat'[Status] = "Active" )
) + 0
```

### IT_Heat.Heat_killRate

```sql
DIVIDE (
    CALCULATE (
        DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
        FILTER (
            'IT_Heat',
            'IT_Heat'[Status] = "Closed"
                || 'IT_Heat'[Status] = "Resolved"
        )
    ),
    CALCULATE ( DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ) )
)
```

### IT_Heat.Heat_MTTR

```sql

    var oDays = SUMX('IT_Heat', DATEDIFF('IT_Heat'[CreatedDateTime], if('IT_Heat'[CreatedDateTime] > 'IT_Heat'[ClosedDateTime],  'IT_Heat'[CreatedDateTime] ,   'IT_Heat'[ClosedDateTime] ) , DAY))
    
VAR tCount =
    CALCULATE (
        DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
        FILTER (
            'IT_Heat',
            'IT_Heat'[Status] = "Closed"
                || 'IT_Heat'[Status] = "Resolved"
        ),
        FILTER ( 'IT_Heat', 'IT_Heat'[ClosedDateTime] <> BLANK () )
    )
RETURN
    DIVIDE ( oDays, tCount )
```

### IT_Heat.Heat_totalClosures

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER (
        'IT_Heat',
        'IT_Heat'[Status] = "Closed"
            || 'IT_Heat'[Status] = "Resolved"
    )
)
```

### IT_Heat.Heat_ticketsNotUpdated7days

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER ( 'IT_Heat', 'IT_Heat'[Status] = "Active" || 'IT_Heat'[Status] = "Logged" || 'IT_Heat'[Status] = "Waiting for 3rd Party" 
    || 'IT_Heat'[Status] = "Waiting for Customer" || 'IT_Heat'[Status] = "Waiting for Resolution"),
    FILTER ( 'IT_Heat', 'IT_Heat'[updateDate] < TODAY()-7 || 'IT_Heat'[UpdateDate] = BLANK()))+0
```

### IT_Heat.Heat_ticketsOpenedMoreThan14days

```sql
CALCULATE (
    DISTINCTCOUNT ( 'IT_Heat'[IncidentNumber] ),
    FILTER ( 'IT_Heat', 'IT_Heat'[Status] = "Active" || 'IT_Heat'[Status] = "Logged" || 'IT_Heat'[Status] = "Waiting for 3rd Party" 
    || 'IT_Heat'[Status] = "Waiting for Customer" || 'IT_Heat'[Status] = "Waiting for Resolution"),
    FILTER ( 'IT_Heat', 'IT_Heat'[CreatedDateTime] <= TODAY()-14 ))+0
```

### IT_Heat.Heat_incidentLink

```sql
"https://babwservicedesk.saasit.com//Default.aspx?Scope=ObjectWorkspace&CommandId=Search&ObjectType=Incident%23&CommandData=IncidentNumber,%3D,0,"
    & SELECTEDVALUE ( 'IT_Heat'[IncidentNumber] )
```

### UKLoyatly.Total New Accounts Created

```sql
 sum('UKLoyatly'[Tablet New Accounts Created]) + sum ('UKLoyatly'[POS New Accounts Created])
```

### UKLoyatly.UK Tablet Capture Rate

```sql
 divide(sum(UKLoyatly[Tablet New Accounts Created]),sum(TransactionFact[GAAPTransaction]),0)
```

### UKLoyatly.Tablet%

```sql
 divide(sum(UKLoyatly[Tablet New Accounts Created]),UKLoyatly[Total New Accounts Created],0)
```

### UKLoyatly.OptIn%

```sql
 divide(sum(UKLoyatly[Tablet New Account Email Opt Ins]),sum(UKLoyatly[Tablet New Accounts Created]),0)
```

### CRMCustomerLeadGeneration.leads

```sql
CALCULATE (
    COUNTA ( 'CRMCustomerLeadGeneration'[EntryDate] ),
    ALLEXCEPT ( 'CRMCustomerLeadGeneration', 'CRMCustomerLeadGeneration'[Campaign],'CRMCustomerLeadGeneration'[EntryDate] )
)
```

### CRMCustomerLeadGeneration.leads_campaign_days

```sql
DATEDIFF ( MIN ( [EntryDate] ), MAX ( [EntryDate] ), DAY )
```

### CRMCustomerLeadGeneration.leads_per_day

```sql
DIVIDE ( [leads], [leads_Campaign_Days], 0 )
```

### CRMCustomerLeadGeneration.leads_distinct_guests

```sql
VAR insertDate =
    SELECTEDVALUE ( CRMCustomerLeadGeneration[EntryDate] )
RETURN
    CALCULATE (
        DISTINCTCOUNT ( 'CRMTransactionFact'[CustomerNumber] ),
        FILTER (
            'CRMTransactionFact',
            'CRMTransactionFact'[TransactionDate] > insertDate
        )
    )
```

### CRMCustomerLeadGeneration.leads_conversion_guests

```sql
DIVIDE (
    CRMCustomerLeadGeneration[leads_distinct_guests],
    CRMCustomerLeadGeneration[leads],
    0
)
```

### CRMCustomerLeadGeneration.leads_total_trans

```sql
VAR insertDate =
    MIN ( CRMCustomerLeadGeneration[EntryDate] )
RETURN
    CALCULATE (
        DISTINCTCOUNT ( 'CRMTransactionFact'[CRMTransactionID] ),
        FILTER (
            'CRMTransactionFact',
            'CRMTransactionFact'[TransactionDate] > insertDate
        )
    )
```

### CRMCustomerLeadGeneration.leads_total_gaap_sales

```sql
VAR insertDate =
    MIN ( CRMCustomerLeadGeneration[EntryDate] )
RETURN
    CALCULATE (
        SUM ( 'CRMTransactionFact'[GaapSales] ),
        FILTER (
            'CRMTransactionFact',
            'CRMTransactionFact'[TransactionDate] > insertDate
        )
    )
```

### CRMCustomerLeadGeneration.leads_DPT

```sql
DIVIDE ( [leads_Total_GAAP_Sales], [leads_Total_Trans], 0 )
```

### CRMCustomerLeadGeneration.leads_retail_trans

```sql
VAR insertDate =
    MIN ( CRMCustomerLeadGeneration[EntryDate] )
RETURN
    CALCULATE (
        DISTINCTCOUNT ( 'CRMTransactionFact'[CRMTransactionID] ),
        FILTER (
            'CRMTransactionFact',
            'CRMTransactionFact'[TransactionDate] > insertDate
                && NOT 'CRMTransactionFact'[StoreID] IN { "13", "2013", "0", "470", "990", "991" }
        )
    ) + 0
```

### CRMCustomerLeadGeneration.leads_perc_retail_trans

```sql
DIVIDE ( [leads_retail_trans], CRMCustomerLeadGeneration[leads_Total_Trans], 0 )
```

### CRMCustomerLeadGeneration.leads_retail_gaap_sales

```sql
VAR insertDate =
    MIN( CRMCustomerLeadGeneration[EntryDate] )
RETURN
    CALCULATE (
        SUM ( 'CRMTransactionFact'[GaapSales] ),
        FILTER (
            'CRMTransactionFact',
            'CRMTransactionFact'[TransactionDate] > insertDate
                && NOT 'CRMTransactionFact'[StoreID] IN { "13", "2013", "0", "470", "990", "991" }
        )
    ) + 0
```

### CRMCustomerLeadGeneration.leads_retail_dpt

```sql
DIVIDE ( [leads_retail_gaap_sales], [leads_Retail_Trans], 0 )
```

### CRMCustomerLeadGeneration.leads_web_trans

```sql
VAR insertDate =
    MIN( CRMCustomerLeadGeneration[EntryDate] )
RETURN
    CALCULATE (
        DISTINCTCOUNT ( 'CRMTransactionFact'[CRMTransactionID] ),
        FILTER (
            'CRMTransactionFact',
            'CRMTransactionFact'[TransactionDate] > insertDate
                && 'CRMTransactionFact'[StoreID] IN { "13", "2013" }
        )
    ) + 0
```

### CRMCustomerLeadGeneration.leads_perc_web_trans

```sql
DIVIDE ( [leads_web_trans], CRMCustomerLeadGeneration[leads_total_trans], 0 )
```

### CRMCustomerLeadGeneration.leads_web_gaap_sales

```sql
VAR insertDate =
    MIN ( CRMCustomerLeadGeneration[EntryDate] )
RETURN
    CALCULATE (
        SUM ( 'CRMTransactionFact'[GaapSales] ),
        FILTER (
            'CRMTransactionFact',
            'CRMTransactionFact'[TransactionDate] > insertDate
                && 'CRMTransactionFact'[StoreID] IN { "13", "2013" }
        )
    ) + 0
```

### CRMCustomerLeadGeneration.leads_web_dpt

```sql
DIVIDE ( [leads_web_gaap_sales], [leads_web_trans], 0 )
```

### WebOrderTrueAttachmentConcatenatedSkus.WebOrderTrueAttachmentOrderCount

```sql
DISTINCTCOUNT ( 'WebOrderTrueAttachmentConcatenatedSkus'[OrderNum] )
```

### WebOrderTrueAttachmentConcatenatedSkus.WebOrderTrueAttachmentSumQty

```sql
SUM ( 'WebOrderTrueAttachmentConcatenatedSkus'[Quantity] )
```

### WebOrderTrueAttachmentConcatenatedSkus.WebOrderTrueAttachmentDistinctSKUstring

```sql
DISTINCTCOUNT ( 'WebOrderTrueAttachmentConcatenatedSkus'[SkuString] )
```

### WebOrderTrueAttachmentConcatenatedSkus.WebOrderTrueAttachmentDistinctKeyStoryCount

```sql
DISTINCTCOUNT('WebOrderTrueAttachmentConcatenatedSkus'[KeyStoryString])

```

### WebOrderTrueAttachmentConcatenatedSkus.WebOrderTrueAttachmentMSTATcount

```sql
DISTINCTCOUNT ( 'WebOrderTrueAttachmentConcatenatedSkus'[MstatString] )
```

### WebOrderTrueAttachmentConcatenatedSkus.WebOrderTrueAttachmentSumRetail

```sql
SUM ( 'WebOrderTrueAttachmentConcatenatedSkus'[Retail] )
```

### ShipFromStoresUnshipped.DCsourceInventory

```sql
 
VAR thisYear = 
CALCULATE(MAX (WHInventory[workYear]), WHInventory[WorkYear]<>2089)

VAR thisWeek = 
CALCULATE(MAX (WHInventory[workWeek]), WHInventory[WorkYear]<>2089)

VAR inv980 = 
lookupvalue(WHInventory[Ohio980 Available],WHInventory[ProductKey],SELECTEDVALUE(ShipFromStoresUnshipped[ProductKey]),WHInventory[workYear],thisYear,WHInventory[workweek],thisWeek)

VAR inv960 = 
lookupvalue(WHInventory[WC960 Available],WHInventory[ProductKey],SELECTEDVALUE(ShipFromStoresUnshipped[ProductKey]),WHInventory[workYear],thisYear,WHInventory[workweek],thisWeek)

RETURN 
IF (SELECTEDVALUE(ShipFromStoresUnshipped[DCsource]) = "960",inv960, inv980) 
```

### ServiceDeskClosed.TotalServiceDeskClosedIncidents

```sql
DISTINCTCOUNT([Incident])
```

### ServiceDeskOpen.TotalServiceDeskOpenIncidents

```sql
DISTINCTCOUNT([Incident])
```

### Filter Products.UnitsSoldInSameOrder

```sql
 
Calculate (
	sum(TransactionDetailFact[Units]),
	CALCULATETABLE( 
		Summarize(
		'TransactionDetailFact',TransactionDetailFact[TransactionKey]),
		ALL('Products'),
		USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey])
)
)
```

### Filter Products.OrdersWithBothProducts

```sql

Calculate (COUNT(TransactionFact[TransactionKey]) , 
  	CalculateTable (
		Summarize (TransactionDetailFact,TransactionDetailFact[TransactionKey]),
		ALL (Products),
		USERELATIONSHIP(TransactionDetailFact[ProductKey],'Filter Products'[ProductKey])
	)
)
```

### Filter Products.SalesValue

```sql
 
Calculate (
	sum(TransactionDetailFact[UnitGrossAmount])-sum(TransactionDetailFact[UnitDiscAmount]),
	CALCULATETABLE( 
		Summarize(
		'TransactionDetailFact',TransactionDetailFact[TransactionKey]),
		ALL('Products'),
		USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey])
)
)
```

### Filter Products.Orders

```sql
 Calculate([OrdersWithBothProducts],all(Products))
```

### Filter Products.SameProductSelection

```sql
 
IF (
	hasonevalue(Products[ProductKey]) && HASONEVALUE('Filter Products'[ProductKey]),
	if (
		VALUES (Products[ProductKey]) = vALUES ('Filter Products'[ProductKey]),
		true
	)
)
```

### Filter Products.OrdersPerc

```sql
 
	Divide ([OrdersWithBothProducts],[Orders],0)
```

### Filter Products.TotalSalesValue

```sql
Calculate([SalesValue],all(Products))
```

### Filter Products.ProductAUR

```sql
 divide([NetSalesValue],[ProductUnitsSold],0)
```

### Filter Products.SalesPerc

```sql
 

	
	Divide ([SalesValue],[TotalSalesValue],0)

```

### Filter Products.ProductUPT

```sql
 divide('Filter Products'[ProductUnitsSold],[OrdersWithBothProducts],0)
```

### Filter Products.GrossAmount

```sql
 Calculate (
	sum(TransactionDetailFact[UnitGrossAmount]),
	CALCULATETABLE( 
		Summarize(
		'TransactionDetailFact',TransactionDetailFact[ProductKey]),
		ALL('Products'),
		USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey])
)
)
```

### Filter Products.DiscAmount

```sql
 Calculate (
	sum(TransactionDetailFact[UnitDiscAmount]),
	CALCULATETABLE( 
		Summarize(
		'TransactionDetailFact',TransactionDetailFact[ProductKey]),
		ALL('Products'),
		USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey])
)
)
```

### Filter Products.NetSalesValue

```sql
 [GrossAmount] - [DiscAmount]
```

### Filter Products.ProductUnitsSold

```sql
  Calculate (
	sum(TransactionDetailFact[Units]),
	CALCULATETABLE( 
		Summarize(
		'TransactionDetailFact',TransactionDetailFact[ProductKey]),
		ALL('Products'),
		USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey])
)
)
```

### Filter Products.TotalDPT

```sql
 calculate ([DPT],USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey]))
```

### Filter Products.FilterWHInventory

```sql
 Calculate([LatestWHInventory],USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey]))
```

### Filter Products.FilterStoreInventory

```sql
 Calculate([LatestStoreInventory],USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey]))
```

### Filter Products.TotalUPT

```sql
 calculate ([UPT],USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey]))
```

### Filter Products.FilterNameMeCount

```sql
 calculate([NameMeTransactions],USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey]))
```

### Filter Products.DiscPerc

```sql
 divide([DiscAmount],[GrossAmount],0)
```

### Filter Products.TotalGrossAmount

```sql
  Calculate (
	sum(TransactionDetailFact[UnitGrossAmount]),
	CALCULATETABLE( 
		Summarize(
		'TransactionDetailFact',TransactionDetailFact[TransactionKey]),
		ALL('Products'),
		USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey])
)
)
```

### Filter Products.TotalDiscAmount

```sql
    Calculate (
	sum(TransactionDetailFact[UnitDiscAmount]),
	CALCULATETABLE( 
		Summarize(
		'TransactionDetailFact',TransactionDetailFact[TransactionKey]),
		ALL('Products'),
		USERELATIONSHIP('TransactionDetailFact'[ProductKey],'Filter Products'[ProductKey])
)
)
```

### Filter Products.UnitsPerc

```sql
 divide([UnitsSoldInSameOrder],calculate([UnitsSoldInSameOrder],all(Products)),0)
```

### merchonOrder.OnOrderM1

```sql
 
VAR NextP = Values(NewDateDim[FiscalPeriodSequenceKey]) + 1
Return
 Var LastW =  switch(Values(NewDateDim[Fiscal_Week_Of_Year_Key]),4,5,9,4,13,4,17,5,22,4,26,4,30,5,35,4,39,4,43,5,48,4,52,4,1)
Return
IF (  hasonevalue(NewDateDim[FiscalPeriodSequenceKey]),  calculate(
	sum(merchonOrder[OnOrderQTY]),
                       filter (
	           all (NewDateDim),
		( NewDateDim[FiscalPeriodSequenceKey] = NextP
                                  && NewDateDim[Fiscal_Week_Of_Month_Key] = LastW)
	)	
                              )
	     ,

Blank())
```

### merchonOrder.OnOrderM2

```sql
 
VAR NextP = Values(NewDateDim[FiscalPeriodSequenceKey]) + 2
Return
Var LastW =  switch(Values(NewDateDim[Fiscal_Week_Of_Year_Key]),4,4,9,4,13,5,17,4,22,4,26,5,30,4,35,4,39,5,43,4,48,4,52,5,1)
Return
IF (  hasonevalue(NewDateDim[FiscalPeriodSequenceKey]),
  calculate(
	sum(merchonOrder[OnOrderQTY]),
                       filter (
	           all (NewDateDim),
		( NewDateDim[FiscalPeriodSequenceKey] = NextP
                                  && NewDateDim[Fiscal_Week_Of_Month_Key] = LastW)
	)	
                              )
	     ,

Blank())
```

### merchonOrder.OnOrderM3

```sql
 
VAR NextP = Values(NewDateDim[FiscalPeriodSequenceKey]) + 3
Return
Var LastW =  switch(Values(NewDateDim[Fiscal_Week_Of_Year_Key]),4,4,9,5,13,4,17,4,22,5,26,4,30,4,35,5,39,4,43,4,48,5,52,4,1)
Return
IF (  hasonevalue(NewDateDim[FiscalPeriodSequenceKey]),
  calculate(
	sum(merchonOrder[OnOrderQTY]),
                       filter (
	           all (NewDateDim),
		( NewDateDim[FiscalPeriodSequenceKey] = NextP
                                  && NewDateDim[Fiscal_Week_Of_Month_Key] = LastW)
	)	
                              )
	     ,

Blank())
```

### merchonOrder.OnOrderM4

```sql
 
VAR NextP = Values(NewDateDim[FiscalPeriodSequenceKey]) + 4
Return
Var LastW =  switch(Values(NewDateDim[Fiscal_Week_Of_Year_Key]),4,5,9,4,13,4,17,5,22,4,26,4,30,5,35,4,39,4,43,5,48,4,52,4,1)
Return
IF (  hasonevalue(NewDateDim[FiscalPeriodSequenceKey]),
  calculate(
	sum(merchonOrder[OnOrderQTY]),
                       filter (
	           all (NewDateDim),
		( NewDateDim[FiscalPeriodSequenceKey] = NextP
                                  && NewDateDim[Fiscal_Week_Of_Month_Key] = LastW)
	)	
                              )
	     ,

Blank())
```

### merchonOrder.OnOrderM5

```sql
 VAR NextP = Values(NewDateDim[FiscalPeriodSequenceKey]) + 5
Return
Var LastW =  switch(Values(NewDateDim[Fiscal_Week_Of_Year_Key]),4,4,9,4,13,5,17,4,22,4,26,5,30,4,35,4,39,5,43,4,48,4,52,5,1)
Return
IF (  hasonevalue(NewDateDim[FiscalPeriodSequenceKey]),
  calculate(
	sum(merchonOrder[OnOrderQTY]),
                       filter (
	           all (NewDateDim),
		( NewDateDim[FiscalPeriodSequenceKey] = NextP
                                  && NewDateDim[Fiscal_Week_Of_Month_Key] = LastW)
	)	
                              )
	     ,

Blank())
```

### merchonOrder.OnOrderPastDue

```sql
 
Var EndDate = max(NewDateDim[Fiscal_Week_Key])
Return
Var  TotalFlag = Switch(VALUES(NewDateDim[Fiscal_week_Of_Year_Key]),	1,	21,2,	14,3,	7,4,	0,5,	21,6,	21,7,	14,8,	7,9,	0,
								10,	21,11,	14,12,	7,13,	0,14,	21,15,	14,16,	7,17,	0,18,	21,
								19,	21,20,	14,21,	7,22,	0,23,	21,24,	14,25,	7,26,	0,27,	21,
								28,	14,29,	7,30,	0,31,	21,32,	21,33,	14,34,	7,35,	0,36,	21,
								37,	14,38,	7,39,	0,40,	21,41,	14,42,	7,43,	0,44,	21,45,	21,
								46,	14,47,	7,48,	0,49,	21,50,	14,51,	7,52,	0)
Return
Calculate (
	sum(merchonOrder[OnOrderQTY]),
                       filter (
	           all (NewDateDim),NewDateDim[Date_Key] < EndDate),merchonOrder[TotalFlag] =TotalFlag)
```

### merchonOrder.ChinaOnOrder

```sql
 Calculate(sum(merchonOrder[On_Order]),Products[StyleCode] = "8",Stores[StoreNumber] = "3970")
```

### FlashGaapSales.SalesvsLY

```sql
 divide(
                    sumx('FlashGaapSales','FlashGaapSales'[FlashGaapSalesUSD])-sumx('FlashGaapSales','FlashGaapSales'[LYSalesThisHourUSD]),
                    sumx('FlashGaapSales','FlashGaapSales'[LYSalesThisHourUSD]),
                    0)
```

### FlashGaapSales.CompSalesvsLY

```sql
 divide(
                    sumx('FlashGaapSales','FlashGaapSales'[CompFlashGaapSalesUSD])-sumx('FlashGaapSales','FlashGaapSales'[CompLYSalesThisHourUSD]),
                    sumx('FlashGaapSales','FlashGaapSales'[CompLYSalesThisHourUSD]),
                    0)
```

### FlashGaapSales.CompSalesvsLYTotal

```sql
 divide(
                    sumx('FlashGaapSales','FlashGaapSales'[CompFlashGaapSalesUSD]),
                    sumx('FlashGaapSales','FlashGaapSales'[CompLYGaapSalesDayTotalUSD]),
                    0)
```

### FlashGaapSales.SalestoPlan

```sql
 divide(sumx('FlashGaapSales','FlashGaapSales'[CompFlashGaapSalesLocal]),sumx('FlashGaapSales','FlashGaapSales'[DaySalesPlan]),0)
```

### FlashGaapSales.SalesvsLYTotal

```sql
 divide(
                    sumx('FlashGaapSales','FlashGaapSales'[FlashGaapSalesUSD]),
                    sumx('FlashGaapSales','FlashGaapSales'[LYGaapSalesDayTotalUSD]),
                    0)
```

### MerchSales.UnitsLW

```sql
 CALCULATE(
			sum(MerchSales[NetSalesUnits]),
		DATEADD('NewDateDim'[Date_Key], -7, DAY)
	) 
```

### MerchSales.UnitsLW2

```sql
  CALCULATE(
			sum(MerchSales[NetSalesUnits]),
		DATEADD('NewDateDim'[Date_Key], -14, DAY)
	) 
```

### MerchSales.UnitsLW3

```sql
 CALCULATE(
			sum(MerchSales[NetSalesUnits]),
		DATEADD('NewDateDim'[Date_Key], -21, DAY)
	) 
```

### MerchSales.UnitsLY

```sql
 CALCULATE(
			sum(MerchSales[NetSalesUnits]),
		DATEADD('NewDateDim'[Date_Key], -264, DAY)
	) 
```

### MerchSales.UnitsLYLW

```sql
 CALCULATE(
			sum(MerchSales[NetSalesUnits]),
		DATEADD('NewDateDim'[Date_Key], -371, DAY)
	) 
```

### MerchSales.UnitsLYLW2

```sql
 CALCULATE(
			sum(MerchSales[NetSalesUnits]),
		DATEADD('NewDateDim'[Date_Key], -378, DAY)
	) 
```

### MerchSales.UnitsLWLY3

```sql
 CALCULATE(
			sum(MerchSales[NetSalesUnits]),
		DATEADD('NewDateDim'[Date_Key], -385, DAY)
	) 
```

### MerchSales.UnitsYTD

```sql
  IF (HasOneValue( NewDateDim[Fiscal_Year]),
	Calculate (
		Sum(MerchSales[NetSalesUnits]),
    		Filter (
  		      all(NewDateDim),
		      NewDateDim[Fiscal_Year] = Values (NewDateDim[Fiscal_Year])
			&& NewDateDim[Date_Key] <= Max(  NewDateDim[Date_Key])
		         )
                               ),
                    Blank()
) 
```

### MerchSales.SalesYTD

```sql
  IF (HasOneValue( NewDateDim[Fiscal_Year]),
	Calculate (
		Sum(MerchSales[NetSalesRetail]),
    		Filter (
  		      all(NewDateDim),
		      NewDateDim[Fiscal_Year] = Values (NewDateDim[Fiscal_Year])
			&& NewDateDim[Date_Key] <= Max(  NewDateDim[Date_Key])
		         )
                               ),
                    Blank()
) 
```

### MerchSales.UnitsPYTD

```sql
 

Var CurentDayOfYear =   MAX(NewDateDim[Fiscal_Day_of_year_Key])
Return 
  IF (
	hasonevalue (NewDateDim[Fiscal_Year]),
	CALCULATE (
		SUM( MerchSales[NetSalesUnits]),
		filter (
		  ALL (NewDateDim),
		  NewDateDim[FiscalYearNumber] = VALUES (NewDateDim[FiscalYearNumber]) -1 
			&& NewDateDim[Fiscal_Day_of_year_Key] <= CurentDayOfYear

		      )
		),
		BLANK()
)
```

### MerchSales.SalesPYTD

```sql
 
Var CurentDayOfYear =   MAX(NewDateDim[Fiscal_Day_of_year_Key])
Return 
  IF (
	hasonevalue (NewDateDim[Fiscal_Year]),
	CALCULATE (
		SUM( MerchSales[NetSalesRetail]),
		filter (
		  ALL (NewDateDim),
		  NewDateDim[FiscalYearNumber] = VALUES (NewDateDim[FiscalYearNumber]) -1 
			&& NewDateDim[Fiscal_Day_of_year_Key] <= CurentDayOfYear

		      )
		),
		BLANK()
)
```

### MerchSales.SalesLW

```sql
 CALCULATE(
			sum(MerchSales[NetSalesRetail]),
		DATEADD('NewDateDim'[Date_Key], -7, DAY)
	) 
```

### MerchSales.SalesLW2

```sql
  CALCULATE(
			sum(MerchSales[NetSalesRetail]),
		DATEADD('NewDateDim'[Date_Key], -14, DAY)
	) 
```

### MerchSales.SalesLW3

```sql
  CALCULATE(
			sum(MerchSales[NetSalesRetail]),
		DATEADD('NewDateDim'[Date_Key], -21, DAY)
	) 
```

### MerchSales.SalesLY

```sql
  CALCULATE(
			sum(MerchSales[NetSalesRetail]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### MerchSales.SalesLYLW

```sql
  CALCULATE(
			sum(MerchSales[NetSalesRetail]),
		DATEADD('NewDateDim'[Date_Key], -371, DAY)
	) 
```

### MerchSales.SalesLYLW2

```sql
 CALCULATE(
			sum(MerchSales[NetSalesRetail]),
		DATEADD('NewDateDim'[Date_Key], -378, DAY)
	) 
```

### MerchSales.SalesLYLW3

```sql
 CALCULATE(
			sum(MerchSales[NetSalesRetail]),
		DATEADD('NewDateDim'[Date_Key], -385, DAY)
	) 
```

### MerchSales.TopStylel

```sql
 RankX(allselected('Products'), Calculate(sum([NetSalesRetail]),AllExcept(Stores,Stores[StoreKey]),NewDateDim,NewDateDim[Date_Key]),,DESC,Dense)
```

### MerchSales.AurLW

```sql
 Divide([SalesLW],[UnitsLW],0)
```

### MerchSales.ukAurLW

```sql
 Divide(CALCULATE(
			sum(MerchSales[PoundConversion]),
		DATEADD('NewDateDim'[Date_Key], -7, DAY)
	) 
,[UnitsLW],0)
```

### MerchSales.CurrentDayOfYear

```sql
 Max(NewDateDim[Fiscal_Day_of_year_Key])
```

### MerchSales.8wF

```sql
 LOOKUPVALUE(FWOSFactors[8weekFactor],FWOSFactors[FWOSKey],
CONCATENATE
(
"NA",
if(lastdate(NewDateDim[Date_Key]) >= TODAY(),
SWITCH(FORMAT(max(NewDateDim[Fiscal_Week_Of_Year_key]), "General Number"), "1", "52", "2", "01", "3", "02", "4", "03", "5", "04", "6", "05", "7", "06", "8", "07"  
               			, "9", "08", "10", "09", "11", "10", "12", "11", "13", "12", "14", "13", "15", "14", "16", "15"  
				, "17", "16", "18", "17", "19", "18", "20", "19", "21", "20", "22", "21", "23", "22", "24", "23"  
				, "25", "24", "26", "25", "27", "26", "28", "27", "29", "28", "30", "29", "31", "30", "32", "31"  
				, "33", "32", "34", "33", "35", "34", "36", "35", "37", "36", "38", "37", "39", "38", "40", "39"  
				, "41", "40", "42", "41", "43", "42", "44", "43", "45", "44", "46", "45", "47", "46", "48", "47"  
				, "49", "48", "50", "49", "51", "50", "52", "51", "53", "52", max(NewDateDim[Fiscal_Week_Of_Year_key])-1) 

,if(max(NewDateDim[Fiscal_Week_Of_Year_key]) < 10, CONCATENATE("0",max(NewDateDim[Fiscal_Week_Of_Year_key])), max(NewDateDim[Fiscal_Week_Of_Year_key]))
)))
```

### MerchSales.26wF

```sql
 LOOKUPVALUE(FWOSFactors[26weekFactor],FWOSFactors[FWOSKey],
CONCATENATE
(
"NA",
if(lastdate(NewDateDim[Date_Key]) >= TODAY(),
SWITCH(FORMAT(max(NewDateDim[Fiscal_Week_Of_Year_key]), "General Number"), "1", "52", "2", "01", "3", "02", "4", "03", "5", "04", "6", "05", "7", "06", "8", "07"  
               			, "9", "08", "10", "09", "11", "10", "12", "11", "13", "12", "14", "13", "15", "14", "16", "15"  
				, "17", "16", "18", "17", "19", "18", "20", "19", "21", "20", "22", "21", "23", "22", "24", "23"  
				, "25", "24", "26", "25", "27", "26", "28", "27", "29", "28", "30", "29", "31", "30", "32", "31"  
				, "33", "32", "34", "33", "35", "34", "36", "35", "37", "36", "38", "37", "39", "38", "40", "39"  
				, "41", "40", "42", "41", "43", "42", "44", "43", "45", "44", "46", "45", "47", "46", "48", "47"  
				, "49", "48", "50", "49", "51", "50", "52", "51", "53", "52", max(NewDateDim[Fiscal_Week_Of_Year_key])-1) 

,if(max(NewDateDim[Fiscal_Week_Of_Year_key]) < 10, CONCATENATE("0",max(NewDateDim[Fiscal_Week_Of_Year_key])), max(NewDateDim[Fiscal_Week_Of_Year_key]))
)))
```

### MerchSales.52wF

```sql
 LOOKUPVALUE(FWOSFactors[52weekFactor],FWOSFactors[FWOSKey],
CONCATENATE
(
"NA",
if(lastdate(NewDateDim[Date_Key]) >= TODAY(),
SWITCH(FORMAT(max(NewDateDim[Fiscal_Week_Of_Year_key]), "General Number"), "1", "52", "2", "01", "3", "02", "4", "03", "5", "04", "6", "05", "7", "06", "8", "07"  
               			, "9", "08", "10", "09", "11", "10", "12", "11", "13", "12", "14", "13", "15", "14", "16", "15"  
				, "17", "16", "18", "17", "19", "18", "20", "19", "21", "20", "22", "21", "23", "22", "24", "23"  
				, "25", "24", "26", "25", "27", "26", "28", "27", "29", "28", "30", "29", "31", "30", "32", "31"  
				, "33", "32", "34", "33", "35", "34", "36", "35", "37", "36", "38", "37", "39", "38", "40", "39"  
				, "41", "40", "42", "41", "43", "42", "44", "43", "45", "44", "46", "45", "47", "46", "48", "47"  
				, "49", "48", "50", "49", "51", "50", "52", "51", "53", "52", max(NewDateDim[Fiscal_Week_Of_Year_key])-1) 

,if(max(NewDateDim[Fiscal_Week_Of_Year_key]) < 10, CONCATENATE("0",max(NewDateDim[Fiscal_Week_Of_Year_key])), max(NewDateDim[Fiscal_Week_Of_Year_key]))
)))
```

### MerchSales.aU1

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInv2]) || MerchSales[TotalInv2] = 0,0,MerchSales[TotalInv2]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[8wF],
			0),
	0),0)
```

### MerchSales.aU2

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInv2]) || MerchSales[TotalInv2] = 0,0,MerchSales[TotalInv2]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[26wF],
			0),
	0),0)
```

### MerchSales.aU3

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInv2]) || MerchSales[TotalInv2] = 0,0,MerchSales[TotalInv2]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[52wF],
			0),
	0),0)
```

### MerchSales.FWOSf2

```sql
 if(MerchSales[aU1] > 8, if(MerchSales[aU2] > 26, MerchSales[aU3],MerchSales[aU2]),MerchSales[aU1])
```

### MerchSales.aU1a

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInvB2]) || MerchSales[TotalInvB2] = 0,0,MerchSales[TotalInvB2]),		
  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[8wF],
			0),
	0),0)
```

### MerchSales.aU2a

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInvB2]) || MerchSales[TotalInvB2] = 0,0,MerchSales[TotalInvB2]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[26wF],
			0),
	0),0)
```

### MerchSales.aU3a

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInvB2]) || MerchSales[TotalInvB2] = 0,0,MerchSales[TotalInvB2]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[52wF],
			0),
	0),0)
```

### MerchSales.FWOSiOo2

```sql
 if(MerchSales[aU1a] > 8,if(MerchSales[aU2a] > 26, MerchSales[aU3a],MerchSales[aU2a]), MerchSales[aU1a])
```

### MerchSales.TotalInv2

```sql
 WHInventory[Ohio980available2] + WHInventory[WC960available2]+sum(StoreInventory[CHAIN Available]) 
		+ sum(StoreInventory[OUTLET Available]) + sum(StoreInventory[WEB Available]) + sum(StoreInventory[Store In Transit]) + WHInventory[OhioLockedAvailable2]
```

### MerchSales.TotalInvB2

```sql
 WHInventory[Ohio980available2] + WHInventory[WC960available2]+sum(StoreInventory[CHAIN Available]) 
		+ sum(StoreInventory[OUTLET Available]) + sum(StoreInventory[WEB Available]) + sum(StoreInventory[Store In Transit]) + WHInventory[OhioLockedAvailable2] +
		merchonOrder[OnOrderPastDue] + merchonOrder[OnOrderM1]+merchonOrder[OnOrderM2]+merchonOrder[OnOrderM3]+merchonOrder[OnOrderM4]+merchonOrder[OnOrderM5] +sum(merchonOrder[On_Order])
```

### MerchSales.8wFe

```sql
 LOOKUPVALUE(FWOSFactors[8weekFactor],FWOSFactors[FWOSKey],
CONCATENATE
(
"EU",
if(lastdate(NewDateDim[Date_Key]) >= TODAY(),
SWITCH(FORMAT(max(NewDateDim[Fiscal_Week_Of_Year_key]), "General Number"), "1", "52", "2", "01", "3", "02", "4", "03", "5", "04", "6", "05", "7", "06", "8", "07"  
               			, "9", "08", "10", "09", "11", "10", "12", "11", "13", "12", "14", "13", "15", "14", "16", "15"  
				, "17", "16", "18", "17", "19", "18", "20", "19", "21", "20", "22", "21", "23", "22", "24", "23"  
				, "25", "24", "26", "25", "27", "26", "28", "27", "29", "28", "30", "29", "31", "30", "32", "31"  
				, "33", "32", "34", "33", "35", "34", "36", "35", "37", "36", "38", "37", "39", "38", "40", "39"  
				, "41", "40", "42", "41", "43", "42", "44", "43", "45", "44", "46", "45", "47", "46", "48", "47"  
				, "49", "48", "50", "49", "51", "50", "52", "51", "53", "52", max(NewDateDim[Fiscal_Week_Of_Year_key])-1) 

,if(max(NewDateDim[Fiscal_Week_Of_Year_key]) < 10, CONCATENATE("0",max(NewDateDim[Fiscal_Week_Of_Year_key])), max(NewDateDim[Fiscal_Week_Of_Year_key]))
)))
```

### MerchSales.26wFe

```sql
 LOOKUPVALUE(FWOSFactors[26weekFactor],FWOSFactors[FWOSKey],
CONCATENATE
(
"EU",
if(lastdate(NewDateDim[Date_Key]) >= TODAY(),
SWITCH(FORMAT(max(NewDateDim[Fiscal_Week_Of_Year_key]), "General Number"), "1", "52", "2", "01", "3", "02", "4", "03", "5", "04", "6", "05", "7", "06", "8", "07"  
               			, "9", "08", "10", "09", "11", "10", "12", "11", "13", "12", "14", "13", "15", "14", "16", "15"  
				, "17", "16", "18", "17", "19", "18", "20", "19", "21", "20", "22", "21", "23", "22", "24", "23"  
				, "25", "24", "26", "25", "27", "26", "28", "27", "29", "28", "30", "29", "31", "30", "32", "31"  
				, "33", "32", "34", "33", "35", "34", "36", "35", "37", "36", "38", "37", "39", "38", "40", "39"  
				, "41", "40", "42", "41", "43", "42", "44", "43", "45", "44", "46", "45", "47", "46", "48", "47"  
				, "49", "48", "50", "49", "51", "50", "52", "51", "53", "52", max(NewDateDim[Fiscal_Week_Of_Year_key])-1) 

,if(max(NewDateDim[Fiscal_Week_Of_Year_key]) < 10, CONCATENATE("0",max(NewDateDim[Fiscal_Week_Of_Year_key])), max(NewDateDim[Fiscal_Week_Of_Year_key]))
)))
```

### MerchSales.52wFe

```sql
 LOOKUPVALUE(FWOSFactors[52weekFactor],FWOSFactors[FWOSKey],
CONCATENATE
(
"EU",
if(lastdate(NewDateDim[Date_Key]) >= TODAY(),
SWITCH(FORMAT(max(NewDateDim[Fiscal_Week_Of_Year_key]), "General Number"), "1", "52", "2", "01", "3", "02", "4", "03", "5", "04", "6", "05", "7", "06", "8", "07"  
               			, "9", "08", "10", "09", "11", "10", "12", "11", "13", "12", "14", "13", "15", "14", "16", "15"  
				, "17", "16", "18", "17", "19", "18", "20", "19", "21", "20", "22", "21", "23", "22", "24", "23"  
				, "25", "24", "26", "25", "27", "26", "28", "27", "29", "28", "30", "29", "31", "30", "32", "31"  
				, "33", "32", "34", "33", "35", "34", "36", "35", "37", "36", "38", "37", "39", "38", "40", "39"  
				, "41", "40", "42", "41", "43", "42", "44", "43", "45", "44", "46", "45", "47", "46", "48", "47"  
				, "49", "48", "50", "49", "51", "50", "52", "51", "53", "52", max(NewDateDim[Fiscal_Week_Of_Year_key])-1) 

,if(max(NewDateDim[Fiscal_Week_Of_Year_key]) < 10, CONCATENATE("0",max(NewDateDim[Fiscal_Week_Of_Year_key])), max(NewDateDim[Fiscal_Week_Of_Year_key]))
)))
```

### MerchSales.aU1e

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInv2e]) || MerchSales[TotalInv2e] = 0,0,MerchSales[TotalInv2e]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[8wFe],
			0),
	0),0)
```

### MerchSales.aU2e

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInv2e]) || MerchSales[TotalInv2e] = 0,0,MerchSales[TotalInv2e]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[26wFe],
			0),
	0),0)
```

### MerchSales.aU3e

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInv2e]) || MerchSales[TotalInv2e] = 0,0,MerchSales[TotalInv2e]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[52wFe],
			0),
	0),0)
```

### MerchSales.aU1ae

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInvB2e]) || MerchSales[TotalInvB2e] = 0,0,MerchSales[TotalInvB2e]),		
  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[8wFe],
			0),
	0),0)
```

### MerchSales.aU2ae

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInvB2e]) || MerchSales[TotalInvB2e] = 0,0,MerchSales[TotalInvB2e]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[26wFe],
			0),
	0),0)
```

### MerchSales.aU3ae

```sql
 ROUND(Divide(IF(ISBLANK(MerchSales[TotalInvB2e]) || MerchSales[TotalInvB2e] = 0,0,MerchSales[TotalInvB2e]),
		  Divide( if(max(NewDateDim[Date_Key]) >= TODAY(),IF(ISBLANK(MerchSales[UnitsLW]) || MerchSales[UnitsLW] = 0,1,MerchSales[UnitsLW]),
			IF(ISBLANK(sum(MerchSales[NetSalesUnits])) || sum(MerchSales[NetSalesUnits]) = 0,1,sum(MerchSales[NetSalesUnits]))),MerchSales[52wFe],
			0),
	0),0)
```

### MerchSales.FWOSf2e

```sql
 if(MerchSales[aU1e] > 8, if(MerchSales[aU2e] > 26, MerchSales[aU3e],MerchSales[aU2e]),MerchSales[aU1e])
```

### MerchSales.FWOSiOo2e

```sql
 if(MerchSales[aU1ae] > 8,if(MerchSales[aU2ae] > 26, MerchSales[aU3ae],MerchSales[aU2ae]), MerchSales[aU1ae])
```

### MerchSales.TotalInv2e

```sql
 WHInventory[UK2970available2] + sum(StoreInventory[CHAIN Available]) + sum(StoreInventory[OUTLET Available]) + sum(StoreInventory[WEB Available]) + sum(StoreInventory[Store In Transit])
```

### MerchSales.TotalInvB2e

```sql
 WHInventory[UK2970available2] + sum(StoreInventory[CHAIN Available]) + sum(StoreInventory[OUTLET Available]) + sum(StoreInventory[WEB Available]) + sum(StoreInventory[Store In Transit]) + merchonOrder[OnOrderPastDue] + merchonOrder[OnOrderM1] + merchonOrder[OnOrderM2] + merchonOrder[OnOrderM3] + merchonOrder[OnOrderM4] + merchonOrder[OnOrderM5] + sum(merchonOrder[On_Order])
```

### MerchSales.sumNetSalesRetail

```sql
SUM(MerchSales[NetSalesRetail])
```

### MerchSales.percTotalSales

```sql
DIVIDE(
    [sumNetSalesRetail],
CALCULATE([sumNetSalesRetail], ALL('Products'[Style]))
,0)


```

### MerchSales.percSellThrough

```sql
DIVIDE (
    'TransactionFact'[totalStoreUnitsBRF],
    'TransactionFact'[totalStoreUnitsBRF] + 'WHInventory'[LatestStoreInventory],
    0
)
```

### MerchSales.percSellThroughWeb

```sql
DIVIDE (
    'TransactionFact'[totalTransWeb],
    SUM ( 'Products'[WebInventory] ) + 'TransactionFact'[totalTransWeb]
)
```

### MerchSales.percSellThroughWebChain

```sql
DIVIDE (
    'TransactionFact'[totalStoreAndWebUnitsBRF],
    'TransactionFact'[totalStoreAndWebUnitsBRF] + 'WHInventory'[LatestStoreAndWebInventory],
    0
)
```

### NameMeTransactionFact.UnitsSold

```sql
 COUNT([ProductKey])
```

### NameMeTransactionFact.UnitsSoldBoys

```sql
 (CALCULATE([UnitsSold],or('NameMeTransactionFact'[RecipientAgeGroup] = "Older Boys",'NameMeTransactionFact'[RecipientAgeGroup] = "Young Boys" )))
```

### NameMeTransactionFact.PercentSoldToBoys

```sql
 if([UnitsSoldToAllGroups] > 10,divide([UnitsSoldBoys],(Calculate([UnitsSold],All('NameMeTransactionFact'[RecipientAgeGroup]))),0),0)
```

### NameMeTransactionFact.UnitsSoldToAllGroups

```sql
 (Calculate([UnitsSold],All('NameMeTransactionFact'[RecipientAgeGroup])))
```

### NameMeTransactionFact.UnitsSoldOlderGirls

```sql
 (CALCULATE([UnitsSold],'NameMeTransactionFact'[RecipientAgeGroup] = "Older Girls"))
```

### NameMeTransactionFact.UnitsSoldYoungGirls

```sql
  (CALCULATE([UnitsSold],'NameMeTransactionFact'[RecipientAgeGroup] = "Young Girls"))
```

### NameMeTransactionFact.UnitsSoldUniversal

```sql
  (CALCULATE([UnitsSold],'NameMeTransactionFact'[RecipientAgeGroup] = "Universal"))
```

### NameMeTransactionFact.PercentSoldToOlderGirls

```sql
 if([UnitsSoldToAllGroups] > 10,divide([UnitsSoldOlderGirls],(Calculate([UnitsSold],All('NameMeTransactionFact'[RecipientAgeGroup]))),0),0)
```

### NameMeTransactionFact.PercentSoldToYougGirls

```sql
 if([UnitsSoldToAllGroups] > 10,divide([UnitsSoldYoungGirls],(Calculate([UnitsSold],All('NameMeTransactionFact'[RecipientAgeGroup]))),0),0)
```

### NameMeTransactionFact.PercentSoldUniversal

```sql
 if([UnitsSoldToAllGroups] > 10,divide([UnitsSoldUniversal],(Calculate([UnitsSold],All('NameMeTransactionFact'[RecipientAgeGroup]))),0),0)
```

### NameMeTransactionFact.NameMeTransactions

```sql
 COUNT(NameMeTransactionFact[NameMeTransactionKey])
```

### SalesPlanFact.Native_Sales_Plan_LY

```sql
 CALCULATE(
		SUM(SalesPlanFact[NativeSalesPlan]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### SalesPlanFact.Sales_Plan_LY

```sql
 CALCULATE(
		SUM(SalesPlanFact[SalesPlan]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### WHInventory.LastFiscalWeek

```sql
 Calculate(Max(NewDateDim[Fiscal_Week_Key]),ALLSELECTED(NewDateDim))
```

### WHInventory.Lastest980

```sql
CALCULATE (
    SUM ( WHInventory[Ohio980 Available] ),
    FILTER ( NewDateDim, NewDateDim[Fiscal_Week_Key] = [LastFiscalWeek] )
)
```

### WHInventory.LatestWHInventory

```sql
CALCULATE (
    SUM ( WHInventory[Ohio980 Available] ) + SUM ( WHInventory[UK2970 Available] ),
    FILTER ( NewDateDim, NewDateDim[Fiscal_Week_Key] = [LastFiscalWeek] )
)
```

### WHInventory.LatestStoreInventory

```sql
CALCULATE (
    SUM ( StoreInventory[CHAIN Available] )
        + SUM ( StoreInventory[OUTLET Available] ),
    FILTER ( NewDateDim, NewDateDim[Fiscal_Week_Key] = [LastFiscalWeek] )
)
```

### WHInventory.Ohio980available2

```sql
CALCULATE(SUM(WHInventory[Ohio980 Available]),ALL(Stores))
```

### WHInventory.WC960available2

```sql
 CALCULATE(SUM(WHInventory[WC960 Available]),ALL(Stores))
```

### WHInventory.OhioLockedAvailable2

```sql
 CALCULATE(sum(WHInventory[OhioLocked Available]),All(Stores))
```

### WHInventory.UK2970available2

```sql
  CALCULATE(SUM(WHInventory[UK2970 Available]),ALL(Stores))
```

### WHInventory.LatestStoreAndWebInventory

```sql
CALCULATE (
    'WHInventory'[LatestStoreInventory] + SUM ( 'Products'[WebInventory] )
)
```

### TrafficFact.Traffic_LY

```sql

	CALCULATE(
		SUM('TrafficFact'[Traffic]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### TrafficFact.Traffic_Growth

```sql

Divide(sum(TrafficFact[Traffic])-'TrafficFact'[Traffic_LY],'TrafficFact'[Traffic_LY],0)
```

### TrafficFact.Traffic_Current

```sql

	CALCULATE(
		SUM('TrafficFact'[Traffic]))
```

### WebOrderShippingFacts.OrdersShipped

```sql
 counta(WebOrderShippingFacts[OrderNumber])
```

### TransactionFact.TotalTransactions

```sql
COUNT(TransactionFact[TransactionID])
```

### TransactionFact.Sales_LY

```sql
 
	CALCULATE(
		SUM('TransactionFact'[GAAPSalesAmount]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### TransactionFact.Units_LY

```sql
 
	CALCULATE(
		SUM('TransactionFact'[GAAPUnits]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### TransactionFact.DPT

```sql
 
SUM('TransactionFact'[GAAPSalesAmount])/Sum(TransactionFact[GAAPTransaction])

```

### TransactionFact.UPT

```sql
 
sum(TransactionFact[GAAPUnits])/Sum(TransactionFact[GAAPTransaction])

```

### TransactionFact.Transactions_LY

```sql
 
	CALCULATE(
		SUM('TransactionFact'[GAAPTransaction]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### TransactionFact.UPT_LY

```sql
 divide(
         CALCULATE(
		SUM('TransactionFact'[GAAPUnits]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY))
	 ,

        CALCULATE(
		SUM('TransactionFact'[GAAPTransaction]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY))
	 ,0)
```

### TransactionFact.Dpt_LY

```sql
 divide([Sales_LY],[Transactions_LY])

```

### TransactionFact.Sales_Local_LY

```sql
 
	CALCULATE(
		SUM('TransactionFact'[NativeGAAPSalesAmount]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### TransactionFact.DPT_Local_LY

```sql
 divide([Sales_Local_LY],[Transactions_LY],0)

```

### TransactionFact.DPT_Local

```sql
 
divide(SUM('TransactionFact'[NativeGAAPSalesAmount]),sum(TransactionFact[GAAPTransaction]),0)

```

### TransactionFact.SalesGrowth

```sql
 divide(sum(TransactionFact[GaapSalesAmount]) -'TransactionFact'[Sales_LY],'TransactionFact'[Sales_LY],0)
```

### TransactionFact.SalesGrowth_Local

```sql
 divide(sum(TransactionFact[NativeGaapSalesAmount]) -'TransactionFact'[Sales_Local_LY],'TransactionFact'[Sales_Local_LY],0)
```

### TransactionFact.DPTChange

```sql
 'TransactionFact'[DPT] - 'TransactionFact'[Dpt_LY]
```

### TransactionFact.DPTChange_Local

```sql
 'TransactionFact'[DPT_Local] - 'TransactionFact'[DPT_Local_LY]
```

### TransactionFact.UPTChange

```sql
 'TransactionFact'[UPT] - 'TransactionFact'[UPT_LY]
```

### TransactionFact.Conversion_LY

```sql

Divide ('TransactionFact'[Transactions_LY],'TrafficFact'[Traffic_LY],0)
```

### TransactionFact.Conversion

```sql

Divide (sum(TransactionFact[GAAPTransaction]),sum(TrafficFact[Traffic]),0)
```

### TransactionFact.ConversionChange

```sql

'TransactionFact'[Conversion] - 'TransactionFact'[Conversion_LY]
```

### TransactionFact.SalesVsPlan_LY

```sql

divide('TransactionFact'[Sales_LY]-'SalesPlanFact'[Sales_Plan_LY],'SalesPlanFact'[Sales_Plan_LY],0)
```

### TransactionFact.SalesVsPlan

```sql

divide(sum(TransactionFact[GaapSalesAmount])-sum(SalesPlanFact[SalesPlan]),sum(SalesPlanFact[SalesPlan]),0)
```

### TransactionFact.SalesVsPlan_Local

```sql

divide(sum(TransactionFact[NativeGAAPSalesAmount])-sum(SalesPlanFact[NativeSalesPlan]),sum(SalesPlanFact[NativeSalesPlan]),0)
```

### TransactionFact.SalesVsPlan_Local_LY

```sql

divide('TransactionFact'[Sales_Local_LY]-'SalesPlanFact'[Native_Sales_Plan_LY],'SalesPlanFact'[Native_Sales_Plan_LY],0)
```

### TransactionFact.DPTGrowth_Local

```sql
 divide([DPTChange_Local],[DPT_Local_LY],0)

```

### TransactionFact.AUR_LY

```sql
 Divide(	CALCULATE(
		SUM('TransactionFact'[GAAPSalesAmount]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)),
          CALCULATE(
		SUM('TransactionFact'[GAAPUnits]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)),
        0
	) 

```

### TransactionFact.AUR_Local_LY

```sql
  Divide(	CALCULATE(
		SUM('TransactionFact'[NativeGAAPSalesAmount]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)),
          CALCULATE(
		SUM('TransactionFact'[GAAPUnits]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)),
        0
	) 
```

### TransactionFact.AURChange

```sql
 'TransactionFact'[AUR_]-'TransactionFact'[AUR_LY]
```

### TransactionFact.AURGrowth

```sql
 Divide(
'TransactionFact'[AURChange],'TransactionFact'[AUR_Local_LY],0)
```

### TransactionFact.AUR_Local

```sql
 divide (sum('TransactionFact'[NativeGAAPSalesAmount]),sum(TransactionFact[GAAPUnits]),0)
```

### TransactionFact.AURChange_Local

```sql
 'TransactionFact'[AUR_Local]-'TransactionFact'[AUR_Local_LY]
```

### TransactionFact.AURGrowth_Local

```sql
 Divide('TransactionFact'[AURChange_Local],'TransactionFact'[AUR_Local_LY],0)

```

### TransactionFact.UPTGrowth

```sql
 divide('TransactionFact'[UPTChange],'TransactionFact'[UPT_LY],0)
```

### TransactionFact.CompSales

```sql
 sumx('TransactionFact',TransactionFact[GaapSalesAmount] * 'TransactionFact'[CompStatus])

```

### TransactionFact.CompSales_LY

```sql


	CALCULATE(
		SUMx('TransactionFact','TransactionFact'[GAAPSalesAmount] * 'TransactionFact'[NYCompStatus]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### TransactionFact.CompSalesGrowth

```sql
 divide([CompSales] - [CompSales_LY],[CompSales_LY],0)
```

### TransactionFact.CompSales_Local

```sql
  sumx('TransactionFact',TransactionFact[NativeGAAPSalesAmount] * 'TransactionFact'[CompStatus])
```

### TransactionFact.CompSales_Local_LY

```sql
  CALCULATE(
		SUMx('TransactionFact','TransactionFact'[NativeGAAPSalesAmount] * 'TransactionFact'[NYCompStatus]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### TransactionFact.CompSalesGrowth_Local

```sql
 Divide([CompSales_Local] - [CompSales_Local_LY],[CompSales_Local_LY],0)

```

### TransactionFact.CompUnits

```sql
  sumx('TransactionFact',TransactionFact[GAAPUnits] * 'TransactionFact'[CompStatus])
```

### TransactionFact.CompUnits_LY

```sql
 
	CALCULATE(
		SUMx('TransactionFact','TransactionFact'[GAAPUnits] * 'TransactionFact'[NYCompStatus]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	)
```

### TransactionFact.CompUnitsGrowth

```sql
 divide([CompUnits]-[CompUnits_LY],[CompUnits_LY],0)

```

### TransactionFact.CompTransactions

```sql
 sumx('TransactionFact',TransactionFact[GAAPTransaction] * 'TransactionFact'[CompStatus])
```

### TransactionFact.CompTransactions_LY

```sql
 CALCULATE(
		SUMx('TransactionFact','TransactionFact'[GAAPTransaction] * 'TransactionFact'[NYCompStatus]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)
	) 
```

### TransactionFact.CompTransactionsGrowth

```sql
 divide([CompTransactions]-[CompTransactions_LY],[CompTransactions_LY],0)

```

### TransactionFact.CompUPT

```sql
 divide([CompUnits],[CompTransactions],0)

```

### TransactionFact.CompUPT_LY

```sql
 divide([CompUnits_LY],[CompTransactions_LY],0)

```

### TransactionFact.CompUPTChange

```sql
 [CompUPT] - [CompUPT_LY]
```

### TransactionFact.CompUPTGrowth

```sql
 divide([CompUPTChange],[CompUPT_LY],0)

```

### TransactionFact.CompDPT

```sql
 divide([CompSales],[CompTransactions],0)

```

### TransactionFact.DPTGrowth

```sql
 divide([DPTChange],[Dpt_LY],0)

```

### TransactionFact.CompAUR

```sql
 divide([CompSales],[CompUnits],0)

```

### TransactionFact.CompAUR_Local

```sql
 Divide([CompSales_Local],[CompUnits],0)

```

### TransactionFact.CompAUR_LY

```sql
 divide([CompSales_LY],[CompUnits_LY],0)

```

### TransactionFact.CompAUR_Local_LY

```sql
 divide( [CompSales_Local_LY],[CompUnits_LY],0)

```

### TransactionFact.CompAURChange

```sql
 [CompAUR] - [CompAUR_LY]
```

### TransactionFact.CompAURChange_Local

```sql
 [CompAUR_Local] - [CompAUR_Local_LY]
```

### TransactionFact.CompAURGrowth

```sql
 Divide([CompAURChange],[CompAUR_LY],0)

```

### TransactionFact.CompAURGrowth_Local

```sql
 divide([CompAURChange_Local],[CompAUR_Local_LY],0)

```

### TransactionFact.ES_DPT

```sql
 divide(
                 sumx('TransactionFact','TransactionFact'[EnterpriseSellingStoreSalesAmount]),
                 sumx('TransactionFact','TransactionFact'[EnterpriseSellingTransaction]),
                  0)
```

### TransactionFact.ESOnly_DPT

```sql
 divide(sumx('TransactionFact','TransactionFact'[EnterpriseSellingAmount]),sumx('TransactionFact','TransactionFact'[EnterpriseSellingTransaction]),0)
```

### TransactionFact.Store_DPT

```sql
  divide(
                 sumx('TransactionFact','TransactionFact'[EnterpriseSellingStoreSalesAmount]),
                 sumx('TransactionFact','TransactionFact'[StoreTransaction]),
                  0)
```

### TransactionFact.TransactionsGrowth

```sql
 Divide(Sumx('TransactionFact','TransactionFact'[GAAPTransaction])-'TransactionFact'[Transactions_LY],
			'TransactionFact'[Transactions_LY],
			0)
```

### TransactionFact.SoundsToSkins

```sql

Divide(sum(TransactionFact[SoundUnits]),sum(TransactionFact[AnimalUnits]),0)
```

### TransactionFact.SoundsToSkins_LY

```sql
 Divide(
Calculate(sum(TransactionFact[SoundUnits]),DateAdd('NewDateDim'[Date_Key], - 364,Day)),
Calculate(sum(TransactionFact[AnimalUnits]),DateAdd('NewDateDim'[Date_Key], - 364,Day)),0)
```

### TransactionFact.ShoesToSkins

```sql
 Divide(sum(TransactionFact[FootwearUnits]),sum(TransactionFact[AnimalUnits]),0)
```

### TransactionFact.ShoesToSkins_LY

```sql
 Divide(
Calculate(sum(TransactionFact[FootwearUnits]),DateAdd('NewDateDim'[Date_Key], - 364 ,Day)),
Calculate(sum(TransactionFact[AnimalUnits]),DateAdd('NewDateDim'[Date_Key], - 364,Day)),0)
```

### TransactionFact.GC_Sales_LY

```sql

(CALCULATE(
		SUM('TransactionFact'[GiftCardUnitGrossAmount]),
		DATEADD('NewDateDim'[Date_Key], -364, DAY)))
```

### TransactionFact.GC_Sales_vs_LY

```sql
 SUM('TransactionFact'[GiftCardUnitGrossAmount]) -[GC_Sales_LY] 
```

### TransactionFact.GC_Perc_Sales

```sql
 
Calculate (Divide(sum('TransactionFact'[GiftCardUnitGrossAmount]),(sum([NativeGAAPSalesAmount]))))
```

### TransactionFact.CompDPT_LY

```sql
 divide([CompSales_LY],[CompTransactions_LY],0)
```

### TransactionFact.CompDPTChange

```sql
 [CompDPT]-[CompDPT_LY]
```

### TransactionFact.CompDPT_Local

```sql
 divide([CompSales_Local],[CompTransactions],0)
```

### TransactionFact.CompDPT_Local_LY

```sql
 divide([CompSales_Local_LY],[CompTransactions_LY],0)
```

### TransactionFact.CompDPTChange_Local

```sql
 [CompDPT_Local]-[CompDPT_Local_LY]
```

### TransactionFact.CompDPTGrowth_Local

```sql
 divide([CompDPTChange_Local],[CompDPT_Local_LY],0)
```

### TransactionFact.CompDPTGrowth

```sql
 divide([CompDPTChange],[CompDPT_LY],0)
```

### TransactionFact.DiscountPerc

```sql
 1 - ([AUR_]/max(Products[HomeCurrentRetail]))
```

### TransactionFact.CompSales_L2Y

```sql


	CALCULATE(
		SUMx('TransactionFact','TransactionFact'[GAAPSalesAmount] * 'TransactionFact'[NYCompStatus]),
		DATEADD('NewDateDim'[Date_Key], -728, DAY)
	) 
```

### TransactionFact.CompSalesGrowth2

```sql
 divide([CompSales_LY] - [CompSales_L2Y],[CompSales_L2Y],0)
```

### TransactionFact.AvgCompGrowth6mos

```sql

VAR busPeriod = LOOKUPVALUE('Azure vwFcastMonths'[Fiscal_Month],'Azure vwFcastMonths'[fcastMonth], 12)
VAR busPeriod2 = LOOKUPVALUE('Azure vwFcastMonths'[Fiscal_Month],'Azure vwFcastMonths'[fcastMonth], 11)
VAR busPeriod3 = LOOKUPVALUE('Azure vwFcastMonths'[Fiscal_Month],'Azure vwFcastMonths'[fcastMonth], 10)
VAR busPeriod4 = LOOKUPVALUE('Azure vwFcastMonths'[Fiscal_Month],'Azure vwFcastMonths'[fcastMonth], 9)
VAR busPeriod5 = LOOKUPVALUE('Azure vwFcastMonths'[Fiscal_Month],'Azure vwFcastMonths'[fcastMonth], 8)
VAR busPeriod6 = LOOKUPVALUE('Azure vwFcastMonths'[Fiscal_Month],'Azure vwFcastMonths'[fcastMonth], 7)
RETURN
IF(
    HASONEFILTER(Stores[StoreNum-Name]),
DIVIDE(
CALCULATE(
		Divide([CompSales_Local] - [CompSales_Local_LY],[CompSales_Local_LY],0),
		FILTER(ALL('NewDateDim'),NewDateDim[Fiscal_Month] = busPeriod))
+
CALCULATE(
		Divide([CompSales_Local] - [CompSales_Local_LY],[CompSales_Local_LY],0),
		FILTER(ALL('NewDateDim'),NewDateDim[Fiscal_Month] = busPeriod2))
+
CALCULATE(
		Divide([CompSales_Local] - [CompSales_Local_LY],[CompSales_Local_LY],0),
		FILTER(ALL('NewDateDim'),NewDateDim[Fiscal_Month] = busPeriod3))
+
CALCULATE(
		Divide([CompSales_Local] - [CompSales_Local_LY],[CompSales_Local_LY],0),
		FILTER(ALL('NewDateDim'),NewDateDim[Fiscal_Month] = busPeriod4))
+
CALCULATE(
		Divide([CompSales_Local] - [CompSales_Local_LY],[CompSales_Local_LY],0),
		FILTER(ALL('NewDateDim'),NewDateDim[Fiscal_Month] = busPeriod5))
+
CALCULATE(
		Divide([CompSales_Local] - [CompSales_Local_LY],[CompSales_Local_LY],0),
		FILTER(ALL('NewDateDim'),NewDateDim[Fiscal_Month] = busPeriod6)),6,0),0)
```

### TransactionFact.fcstSalesAvg

```sql

SUM('TransactionFact'[NativeGAAPSalesAmount])+([AvgCompGrowth6mos]*SUM('TransactionFact'[NativeGAAPSalesAmount]))
```

### TransactionFact.fcstSalesLwrBnd

```sql
 
IF(
    HASONEFILTER(Stores[StoreNum-Name]),
 	[fcstSalesAvg] + ( [fcstSalesAvg] * -0.05)
,
CALCULATE(
    SUMX(VALUES(Stores[StoreNum-Name]),
[fcstSalesAvg] + ( [fcstSalesAvg] * -0.05))))
```

### TransactionFact.fcstSalesUprBnd

```sql
 
IF(
    HASONEFILTER(Stores[StoreNum-Name]),
 	[fcstSalesAvg] + ( [fcstSalesAvg] * 0.05)
,
CALCULATE(
    SUMX(VALUES(Stores[StoreNum-Name]),
[fcstSalesAvg] + ( [fcstSalesAvg] * 0.05))))
```

### TransactionFact.AUR_

```sql
 divide (sum('TransactionFact'[GAAPSalesAmount]),sum(TransactionFact[GAAPUnits]),0)
```

### TransactionFact.fcstSalesAvgTotal

```sql
 
IF(
    HASONEFILTER(Stores[StoreNum-Name]),
        SUM('TransactionFact'[NativeGAAPSalesAmount])+([AvgCompGrowth6mos]*SUM('TransactionFact'[NativeGAAPSalesAmount]))
,
CALCULATE(
    SUMX(VALUES(Stores[StoreNum-Name]),
        'TransactionFact'[fcstSalesAvg])
       
)
)
```

### TransactionFact.AvgCompGrowth6mosTotal

```sql

IF(
    HASONEFILTER(Stores[StoreNum-Name]),
        'TransactionFact'[AvgCompGrowth6mos]
,
    ""
)
```

### TransactionFact.fcstSalesAvgUSD

```sql

SUM('TransactionFact'[GAAPSalesAmount])+([AvgCompGrowth6mos]*SUM('TransactionFact'[GAAPSalesAmount]))
```

### TransactionFact.fcstSalesAvgTotalUSD

```sql
 
IF(
    HASONEFILTER(Stores[StoreNum-Name]),
        SUM('TransactionFact'[GAAPSalesAmount])+([AvgCompGrowth6mos]*SUM('TransactionFact'[GAAPSalesAmount]))
,
CALCULATE(
    SUMX(VALUES(Stores[StoreNum-Name]),
        'TransactionFact'[fcstSalesAvgUSD])
       
)
)
```

### TransactionFact.fcstSalesLwrBndUSD

```sql
 
IF(
    HASONEFILTER(Stores[StoreNum-Name]),
	[fcstSalesAvgUSD] + ( [fcstSalesAvgUSD] * -0.05)
,
CALCULATE(
    SUMX(VALUES(Stores[StoreNum-Name]),
        [fcstSalesAvgUSD] + ( [fcstSalesAvgUSD] * -0.05)
       
)
)
)
```

### TransactionFact.fcstSalesUprBndUSD

```sql
 
IF(
    HASONEFILTER(Stores[StoreNum-Name]),
	[fcstSalesAvgUSD] + ( [fcstSalesAvgUSD] * 0.05)
,
CALCULATE(
    SUMX(VALUES(Stores[StoreNum-Name]),
        [fcstSalesAvgUSD] + ( [fcstSalesAvgUSD] * 0.05)
       
)
)

)
```

### TransactionFact.DPT_ShipFromStore

```sql
divide(                  sumx('TransactionFact','TransactionFact'[ShipFromStoreAmount]),                  sumx('TransactionFact','TransactionFact'[isShipFromStore]),                   0)
```

### TransactionFact.DPT_PickUpFromStore

```sql
divide(                  sumx('TransactionFact','TransactionFact'[PickUpFromStoreAmount]),                  sumx('TransactionFact','TransactionFact'[isPickUpFromStore]),                   0)
```

### TransactionFact.UPT_ShipFromStore

```sql
divide(                  sumx('TransactionFact','TransactionFact'[ShipFromStoreUnits]),                  sumx('TransactionFact','TransactionFact'[isShipFromStore]),                   0)
```

### TransactionFact.UPT_PickUpFromStore

```sql
divide(                  sumx('TransactionFact','TransactionFact'[PickUpFromStoreUnits]),                  sumx('TransactionFact','TransactionFact'[isPickUpFromStore]),                   0)
```

### TransactionFact.GaapSales

```sql
SUM('TransactionFact'[GaapSalesAmount])
```

### TransactionFact.GaapSalesUnits

```sql
SUM ( 'TransactionFact'[GAAPUnits] )
```

### TransactionFact.percStoreVsWebFulfill

```sql
DIVIDE (
    'TransactionFact'[TotalTransactions],
    CALCULATE (
        COUNT ( 'TransactionFact'[TransactionID] ),
        FILTER (
            ALL ( 'Stores' ),
            'Stores'[StoreID] = "13"
                || 'Stores'[StoreID] = "2013"
        ),
        FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE )
    ),
    0
)
```

### TransactionFact.percWebFulfilled

```sql
DIVIDE (
    CALCULATE (
        COUNT ( 'TransactionFact'[TransactionID] ),
        FILTER (
            ALL ( 'Stores' ),
            'Stores'[StoreID] = "13"
                || 'Stores'[StoreID] = "2013"
        ),
        FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE )
    ),
    'TransactionFact'[TotalTransactions],
    0
)
```

### TransactionFact.totalTransWeb

```sql
CALCULATE (
    COUNT ( 'TransactionFact'[TransactionID] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] = "13"
            || 'Stores'[StoreID] = "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE )
)
```

### TransactionFact.totalTransWebPerc

```sql

DIVIDE (
    CALCULATE (
        COUNT ( 'TransactionFact'[TransactionID] ),
        FILTER (
            ALL ( 'Stores' ),
            'Stores'[StoreID] = "13"
                || 'Stores'[StoreID] = "2013"
        ),
        FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE )
    ),
    CALCULATE (
        'TransactionFact'[TotalTransactions]
            + CALCULATE (
                COUNT ( 'TransactionFact'[TransactionID] ),
                FILTER (
                    ALL ( 'Stores' ),
                    'Stores'[StoreID] = "13"
                        || 'Stores'[StoreID] = "2013"
                ),
                FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE )
            )
    )
)
```

### TransactionFact.totalStoreTransBRF

```sql
CALCULATE (
    COUNT ( 'TransactionFact'[TransactionID] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] <> "13"
            && 'Stores'[StoreID] <> "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 ),
    FILTER ( 'Stores', 'Stores'[WebOrStore] = "Store" )
)
```

### TransactionFact.totalStoreUnitsBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[Units] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] <> "13"
            && 'Stores'[StoreID] <> "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 ),
    FILTER ( 'Stores', 'Stores'[WebOrStore] = "Store" )
)
```

### TransactionFact.totalStoreAmountBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[UnitGrossAmount] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] <> "13"
            && 'Stores'[StoreID] <> "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 ),
    FILTER ( 'Stores', 'Stores'[WebOrStore] = "Store" )
)
```

### TransactionFact.totalWebTransBRF

```sql
CALCULATE (
    COUNT ( 'TransactionFact'[TransactionID] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] = "13"
            || 'Stores'[StoreID] = "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[WebOrStore] = "Web" )
)
```

### TransactionFact.totalWebUnitsBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[Units] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] = "13"
            || 'Stores'[StoreID] = "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[WebOrStore] = "Web" )
)
```

### TransactionFact.totalWebAmountBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[UnitGrossAmount] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] = "13"
            || 'Stores'[StoreID] = "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[WebOrStore] = "Web" )
)
```

### TransactionFact.totalStoreAndWebTransBRF

```sql
CALCULATE (
    COUNT ( 'TransactionFact'[TransactionID] ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 )
)
```

### TransactionFact.totalStoreAndWebUnitsBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[Units] ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 )
)
```

### TransactionFact.totalStoreAndWebAmountBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[UnitGrossAmount] ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 )
)
```

### TransactionFact.totalPercStoreTransBRF

```sql
DIVIDE ( [totalStoreTransBRF], [totalStoreAndWebTransBRF], 0 )
```

### TransactionFact.totalPercStoreUnitsBRF

```sql
DIVIDE ( [totalStoreUnitsBRF], [totalStoreAndWebUnitsBRF], 0 )
```

### TransactionFact.totalPercStoreAmountBRF

```sql
DIVIDE ( [totalStoreAmountBRF], [totalStoreAndWebAmountBRF], 0 )
```

### TransactionFact.totalPercStoreOhBRF

```sql
DIVIDE ( [LatestStoreInventory], [LatestStoreAndWebInventory], 0 )
```

### TransactionFact.totalStoreUnitsBopisBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[Units] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] <> "13"
            && 'Stores'[StoreID] <> "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 ),
    FILTER ( 'TransactionFact', 'TransactionFact'[isPickUpFromStore] = 1 )
)
```

### TransactionFact.totalStoreTransBopisBRF

```sql
CALCULATE (
    COUNT ( 'TransactionFact'[TransactionID] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] <> "13"
            && 'Stores'[StoreID] <> "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 ),
    FILTER ( 'TransactionFact', 'TransactionFact'[isPickUpFromStore] = 1 )
)
```

### TransactionFact.totalStoreAmountBopisBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[UnitGrossAmount] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] <> "13"
            && 'Stores'[StoreID] <> "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 ),
    FILTER ( 'TransactionFact', 'TransactionFact'[isPickUpFromStore] = 1 )
)
```

### TransactionFact.totalStoreBopisStBRF

```sql
DIVIDE (
    [totalStoreUnitsBopisBRF],
    'WHInventory'[LatestStoreInventory] + [totalStoreUnitsBopisBRF],
    0
)
```

### TransactionFact.totalStoreTransBosfsBRF

```sql
CALCULATE (
    COUNT ( 'TransactionFact'[TransactionID] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] <> "13"
            && 'Stores'[StoreID] <> "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 ),
    FILTER ( 'TransactionFact', 'TransactionFact'[isShipFromStore] = 1 )
)
```

### TransactionFact.totalStoreUnitsBosfsBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[Units] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] <> "13"
            && 'Stores'[StoreID] <> "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 ),
    FILTER ( 'TransactionFact', 'TransactionFact'[isShipFromStore] = 1 )
)
```

### TransactionFact.totalStoreAmountBosfsBRF

```sql
CALCULATE (
    SUM ( 'TransactionDetailFact'[UnitGrossAmount] ),
    FILTER (
        ALL ( 'Stores' ),
        'Stores'[StoreID] <> "13"
            && 'Stores'[StoreID] <> "2013"
    ),
    FILTER ( 'Products', 'Products'[isBRFstyle] = TRUE ),
    FILTER ( 'Stores', 'Stores'[isBRFstore] = 1 ),
    FILTER ( 'TransactionFact', 'TransactionFact'[isShipFromStore] = 1 )
)
```

### TransactionFact.totalStoreBosfsStBRF

```sql
DIVIDE (
    [totalStoreUnitsBosfsBRF],
    'WHInventory'[LatestStoreInventory] + [totalStoreUnitsBosfsBRF],
    0
)
```

### TransactionFact.totalTransByStoreBRF

```sql
CALCULATE ( [totalStoreTransBRF], ALLSELECTED (), VALUES ( 'Products'[Style] ) )
```

### TransactionFact.totalPercTransBRF

```sql
DIVIDE([totalStoreTransBRF],[totalTransByStoreBRF], 0)
```

### TransactionFact.totalUnitsByStoreBRF

```sql
CALCULATE (
    [totalStoreUnitsBRF],
    ALLSELECTED (),
    VALUES ( 'Products'[Style] )
)
```

### TransactionFact.totalPercUnitsBRF

```sql
DIVIDE([totalStoreUnitsBRF],[totalUnitsByStoreBRF], 0)
```

### TransactionFact.totalAmountByStoreBRF

```sql
CALCULATE (
    [totalStoreAmountBRF],
    ALLSELECTED (),
    VALUES ( 'Products'[Style] )
)
```

### TransactionFact.totalPercAmountBRF

```sql
DIVIDE([totalStoreAmountBRF],[totalAmountByStoreBRF], 0)
```

### TransactionFact.totalPercOhBRF

```sql
DIVIDE ( [LatestStoreInventory], [LatestStoreAndWebInventory], 0 )
```

### TransactionFact.border1

```sql
""
```

### TransactionFact.border2

```sql
""
```

### TransactionFact.border3

```sql
""
```

### TransactionFact.border4

```sql
""
```

### TransactionFact.border5

```sql
""
```

### TransactionFact.totalInvByStore

```sql
CALCULATE (
    'WHInventory'[LatestStoreInventory],
    ALLSELECTED (),
    VALUES ( 'Products'[Style] )
)
```

### TransactionFact.totalPercOHbyStoreBRF

```sql
DIVIDE ( [LatestStoreInventory], [totalInvByStore], 0 )
```

### FranchiseeMonthlyRoyalty.mTotalSales

```sql
SUM([TotalSales])
```

### FranchiseeMonthlyRoyalty.mFootwareSales

```sql
SUM([FootwareSales])
```

### FranchiseeMonthlyRoyalty.mSoundSales

```sql
SUM([SoundSales])
```

### FranchiseeMonthlyRoyalty.mUnstuffedSales

```sql
SUM([UnstuffedSales])
```

### FranchiseeMonthlyRoyalty.mPartySales

```sql
SUM([PartySales])
```

### FranchiseeMonthlyRoyalty.mGiftCardSales

```sql
SUM([GiftCardSales])
```

### FranchiseeMonthlyRoyalty.mAccessoriesSales

```sql
SUM([AccessoriesSales])
```

### FranchiseeMonthlyRoyalty.mClothesSales

```sql
SUM([ClothesSales])
```

### FranchiseeMonthlyRoyalty.mSportsSales

```sql
SUM([SportsSales])
```

### FranchiseeMonthlyRoyalty.mPrestuffedSales

```sql
SUM([PrestuffedSales])
```

### FranchiseeMonthlyRoyalty.mGiftCardsRedeemed

```sql
SUM([GiftCardsRedeemed])
```

### FranchiseeMonthlyRoyalty.mFriendSales

```sql
SUM([FriendSales])
```

### FranchiseeMonthlyRoyalty.mHumanSales

```sql
SUM([HumanSales])
```

### FranchiseeMonthlyRoyalty.mPetSales

```sql
SUM([PetSales])
```

### FranchiseeMonthlyRoyalty.mStuffersSales

```sql
SUM([StuffersSales])
```

### FranchiseeMonthlyRoyalty.mGaapSales

```sql
SUM([GaapSales])
```

### FranchiseeMonthlyRoyalty.mGaapSalesUSD

```sql
SUM([GaapSalesUSD])
```

### FranchiseeMonthlyRoyalty.mTotalRoyalty

```sql
SUM([TotalRoyalty])
```

### FranchiseeMonthlyRoyalty.mTaxWitholding

```sql
SUM([TaxWitholding])
```

### FranchiseeMonthlyRoyalty.mTotalRoyaltyDue

```sql
SUM([TotalRoyaltyDue])
```

### Products.TopStoriesCorp

```sql
Rankx(ALLSelected('Products'[KeyStory]), sumx(RELATEDTABLE('TransactionDetailFact'),[Units]),,DESC,Dense)
```

### Products.BottomStoriesCorp

```sql
Rankx(ALLSelected('Products'[KeyStory]), sumx(RELATEDTABLE('TransactionDetailFact'),[Units]),,ASC,Dense)
```

### Products.TopStyleBoys

```sql
RankX(all('Products'[Style]),[PercentSoldToBoys],,DESC,Dense)
```

### Products.TopStyleYoungGirls

```sql
 RankX(all('Products'[Style]),[PercentSoldToYougGirls],,DESC,Dense)
```

### Products.TopStyleOlderGirls

```sql
 RankX(all('Products'[Style]),[PercentSoldToOlderGirls],,DESC,Dense)
```

### Products.TopStyleUniveral

```sql
 RankX(all('Products'[Style]),[PercentSoldUniversal],,DESC,Dense)
```

### Products.Int_TopStylesUnits

```sql
 Rankx(allSelected(Products[Style]),sumx(RELATEDTABLE('TransactionDetailFact'),[Units]),,desc,Dense)
```

### Products.Int_TopStylesSales

```sql
  Rankx(all(Products[Style]),'TransactionDetailFact'[NetSales],,desc,Dense)
```

### Products.TotalAllSylesUnits

```sql
 calculate(sumx('TransactionDetailFact','TransactionDetailFact'[Units]),all('Products'[Style]))
```

### Products.TotalAllStylesNet

```sql
 	
		calculate(sumX(TransactionDetailFact,'TransactionDetailFact'[UnitGrossAmount]+
			'TransactionDetailFact'[unitdiscamount]),
	all('Products'[Style]))
```

### Products.TopStyleTotal

```sql
  RankX(allExcept(Products,Products[Department]), sumx(RELATEDTABLE(MerchSales),[NetSalesUnits]),,DESC,Dense)
```

### Products.TopStyleDept

```sql
RankX(allExcept(Products,Products[Department]), sumx(RELATEDTABLE(MerchSales),[NetSalesUnits]),,DESC,Dense)
```

### Products.TopStyleConsGroup

```sql
 
RankX(allExcept(Products,Products[Department],Products[Chain]), sumx(RELATEDTABLE(MerchSales),[NetSalesUnits]),,DESC,Dense)
```

### Products.TopStyleTotalLY

```sql
 RankX(allselected('Products'), [UnitsLY],,DESC,Dense)
```

### Products.TopStyleTotalPW

```sql
 RankX(allselected('Products'), [UnitsLW],,DESC,Dense)
```

### Products.TopStyleTotalPWLY

```sql
 RankX(allselected('Products'),[UnitsLYLW],,DESC,Dense)
```

### Products.TopStyleDeptLY

```sql
 RankX(allExcept(Products,Products[Department]),[UnitsLY],,DESC,Dense)
```

### Products.TopStyleDeptPW

```sql
RankX(allExcept(Products,Products[Department]), [UnitsLW],,DESC,Dense)
```

### Products.TopStyleDeptPWLY

```sql
RankX(allExcept(Products,Products[Department]),[UnitsLYLW],,DESC,Dense)
```

### Products.TopStyleConsGroupLY

```sql
 
RankX(allExcept(Products,Products[Chain],Products[Department]),[UnitsLY],,DESC,Dense)
```

### Products.TopStyleConsGroupPW

```sql
 RankX(allExcept(Products,Products[Chain],Products[Department]),[UnitsLW],,DESC,Dense)
```

### Products.TopStyleConsGroupPWLY

```sql
 RankX(allExcept(Products,Products[Chain],Products[Department]), [UnitsLYLW],,DESC,Dense)
```

### Products.OHAvailable

```sql
 CALCULATE(sum(WHInventory[Ohio980 Available]),All(Stores))
```

### Products.WCAvailable

```sql
  CALCULATE(sum(WHInventory[WC960 Available]),All(Stores))
```

### Products.UKAvailable

```sql
  CALCULATE(sum(WHInventory[UK2970 Available]),All(Stores))
```

### Products.OHLockedAvailable

```sql
  CALCULATE(sum(WHInventory[OhioLocked Available]),All(Stores))
```

### Products.PendingShrink

```sql
  CALCULATE(sum(WHInventory[WH Pending Shrink]),All(Stores))
```

### Products.InTransit

```sql
  CALCULATE(sum(WHInventory[WH In Transit]),All(Stores))
```

### Products.Discrepancy

```sql
  CALCULATE(sum(WHInventory[WH Discrepancy]),All(Stores))
```

### Products.Allocated

```sql
  CALCULATE(sum(WHInventory[WH Allocated]),All(Stores))
```

### Products.Damaged

```sql
  CALCULATE(sum(WHInventory[WH Damaged]),All(Stores))
```

### Products.ReservedCustomerOrder

```sql
  CALCULATE(sum(WHInventory[WH Reserved Cust Order]),All(Stores))
```

### Products.FilteredStoreCount

```sql
 Calculate(count(StoreList[StoreKey]),crossfilter(ProductsStyleGroup[StyleCode],Products[StyleCode],Both))
```

### Products.OtherAvailable

```sql
 calculate (sum(WHInventory[Other Available]),all(Stores))
```

### Products.EOP_OH_Avalable

```sql
 Products[OHAvailable] + Products[OHLockedAvailable] + Products[OtherAvailable] + Products[UKAvailable] + Products[WCAvailable]
```

### Products.EOP_OH_Discrepancy2

```sql
Calculate(sum(WHInventory[WH Discrepancy]),all(Stores)) +
			 sum(StoreInventory[Store Discrepancy])
```

### Products.eop_OH_Available

```sql
  Calculate( sum(WHInventory[Ohio980 Available]) ,All(stores)) + Calculate( sum(WHInventory[OhioLocked Available]) ,All(stores)) +
		 Calculate( sum(WHInventory[Other Available]) ,All(stores))+ Calculate( sum(WHInventory[UK2970 Available]),All(stores)) + 
		 Calculate( sum(WHInventory[WC960 Available]),All(stores))
```

### Products.EOP_OH_PendingShrink2

```sql
Calculate(sum(WHInventory[WH Pending Shrink]),all(Stores)) +
			( sum(StoreInventory[Store Pending Shrink]))
```

### Products.EOP_OH_ReservedCustOrde2r

```sql
 Calculate( sum(WHInventory[WH Reserved Cust Order]),all(Stores))  +
			  sum(StoreInventory[Store Reserved Cust Order])

```

### Products.EOP_OH_Damaged2

```sql
 Calculate( sum(WHInventory[WH Damaged]),all(Stores) ) +
		  sum(StoreInventory[Store Damaged])
```

### Products.OthersByUnits

```sql
if('Products'[Int_TopStylesUnits]<11,"Top","Others")
```

### Products.TopStyleTotalYTD

```sql

 RankX(allExcept(Products,Products[Department]),
 IF (HasOneValue( NewDateDim[Fiscal_Year]),
	Calculate (
		Sum(MerchSales[NetSalesUnits]),
    		Filter (
  		      all(NewDateDim),
		      NewDateDim[Fiscal_Year] = Values (NewDateDim[Fiscal_Year])
			&& NewDateDim[Date_Key] <= Max(  NewDateDim[Date_Key])
		         )
                               ),
                    Blank()
) 
,,DESC,Dense)
```

### Products.TopStyleDeptYTD

```sql
RankX(allExcept(Products,Products[Department]),
 IF (HasOneValue( NewDateDim[Fiscal_Year]),
	Calculate (
		Sum(MerchSales[NetSalesUnits]),
    		Filter (
  		      all(NewDateDim),
		      NewDateDim[Fiscal_Year] = Values (NewDateDim[Fiscal_Year])
			&& NewDateDim[Date_Key] <= Max(  NewDateDim[Date_Key])
		         )
                               ),
                    Blank()
) ,,DESC,Dense)
```

### Products.TopStyleConsGroupYTD

```sql
RankX(allExcept(Products,Products[Chain],Products[Department]), 
 IF (HasOneValue( NewDateDim[Fiscal_Year]),
	Calculate (
		Sum(MerchSales[NetSalesUnits]),
    		Filter (
  		      all(NewDateDim),
		      NewDateDim[Fiscal_Year] = Values (NewDateDim[Fiscal_Year])
			&& NewDateDim[Date_Key] <= Max(  NewDateDim[Date_Key])
		         )
                               ),
                    Blank()
) ,,DESC,Dense)
```

## Power Query Source (per table)

### CRMCustomerDim

```sql
azure_crm_customer_dim
```

### WebOrderItems

```sql
azure_web_oder_items
```

### TransactionDetailFact

```sql
azure_transaction_detail_fact
```

### CRMTransactionFact

```sql
azure_crm_transaction_fact
```

### DiscountFact

```sql
azure_discount_fact
```

### Azure vwFcastMonths

```sql
azure_f_cast_months
```

### AWTransactionPostVoids

```sql
azure_a_w_transaction_post_voids
```

### PartyFact

```sql
azure_party_facts
```

### WebTransactions

```sql
azure_webtransactions
```

### DailyInventory

```sql
azure_daily_inventory
```

### GiftCardFact

```sql
azure_gift_card_manager_gift_card_fact
```

### InventoryRollups

```sql
azure_web_inventory_rollups
```

### CRMcustomerMasterData

```sql
azure_customer_master_data
```

### WebOrderInboundDemandTrackingFacts

```sql
azure_web_order_inbound_demand_tracking_facts
```

### WebOrderInboundIntegrationTracking

```sql
azure_web_order_inbound_integration_tracking
```

### WebOrderOutboundIntegrationTracking

```sql
azure_web_order_outbound_integration_tracking
```

### Pricebooks

```sql
azure_webpricebooks
```

### DynamicsTransactionExceptions

```sql
azure_dynamics_transaction_exceptions
```

### CRMemailFactRollupSummary

```sql
azure_crm_email_fact_rollup_summary
```

### CRMTransactionKeyStoryRanking

```sql
azure_crm_transaction_key_story_ranking
```

### CRMTransactionKeyStoryRankingPurchases

```sql
azure_crm_transaction_key_story_ranking_purchases
```

### DynamicsPOReceiptVarianceVsAptos

```sql
azure_dynamicsporeceiptvariances
```

### PCHealthChecks

```sql
azure_pchealthchecks
```

### DynamicsTransactionsStuckInStaging

```sql
azure_dynamics_transactions_stuck_in_staging
```

### CRMtrendMonths

```sql
azure_crm_trend_months
```

### CRMtrendQuarters

```sql
azure_crm_trend_quarters
```

### StoreCount

```sql
azure_store_count
```

### CategoryMap

```sql
azure_webproductstorefrontcategorymap
```

### WMS_cycleCount_accuracy2

```sql
azure_wms_cyclecount_accuracy2
```

### WMS_cycleCount_accuracy

```sql
azure_wms_cyclecount_accuracy
```

### CatalogAttributes

```sql
azure_webproductcatalogmasterattributes
```

### IT_CommWorks

```sql
azure_it_comm_works
```

### IT_Heat

```sql
azure_it_heat
```

### POSCompareJumpMindStageUnpublishedMessages

```sql
azure_pos_compare_jump_mind_stage_unpublished_messages
```

### FranchiseeTSPA

```sql
azure_franchiseetspa
```

### CRM_Data_Dictionary

```sql
azure_crmdatadictionary
```

### WebOrders

```sql
azure_web_orders
```

### WebShippingDiscounts

```sql
azure_webshippingdiscounts
```

### UKLoyatly

```sql
azure_ukloyatly
```

### CRMCustomerLeadGeneration

```sql
azure_customer_lead_generation
```

### WebOrderTrueAttachmentConcatenatedSkus

```sql
webordertrueattachmentconcatenatedskus
```

### ShipFromStoresUnshipped

```sql
azure_unshipped_skus
```

### ServiceDeskClosed

```sql
azure_service_desk_closed
```

### ServiceDeskOpen

```sql
azure_service_desk_open
```

### CRMsurveyResults

```sql
crm_surveyresults
```

### CRMsurveyQuestions

```sql
crm_surveyquestions
```

### ProductsStyleGroup

```sql
azure_products_style_group
```

### StoreOperationalHours

```sql
azure_store_operational_hours
```

### GiftCardLocations

```sql
azure_gift_card_locations
```

### Filter Products

```sql
azure_filter_products
```

### POSCompareJumpMindStageToSalesAudit

```sql
azure_pos_compare_jump_mind_stage_to_sales_audit
```

### Azure vwFcastDays

```sql
azure_f_cast_days
```

### CurrencyExchangeFact

```sql
azure_currency_exchange_fact
```

### EntepriseSellingFact

```sql
azure_enteprise_selling_fact
```

### EnterpriseSellingLifecycleFacts

```sql
azure_enterprise_selling_lifecycle_facts
```

### FWOSFactors

```sql
azure_fwosfactors
```

### merchonOrder

```sql
azure_merchonorder
```

### FlashGaapSales

```sql
azure_flash_gaap_sales
```

### MerchSales

```sql
azure_merch_sales
```

### PoOnOrder

```sql
azure_po_on_order
```

### NameMeTransactionFact

```sql
azure_name_me_transaction_fact
```

### SalesPlanFact

```sql
azure_sales_plan_fact
```

### StoreInventory

```sql
azure_store_inventory
```

### StoreCompDim

```sql
azure_store_comp_dim
```

### WHInventory

```sql
azure_wh_inventory
```

### TrafficFact

```sql
azure_traffic_fact
```

### Stores

```sql
azure_stores
```

### WMS_cycleCount_occurrence

```sql
azure_wms_cyclecount_occurrence
```

### WMS_cycleCount_adjustments

```sql
azure_wms_cyclecount_adjustments
```

### WebOrderShippingFacts

```sql
azure_webordershippingfacts
```

### TransactionFact

```sql
azure_transaction_fact
```

### FranchiseeMonthlyRoyalty

```sql
azure_franchisee_monthly_royalty
```

### NewDateDim

```sql
azure_newdatedim
```

### StoreList

```sql
azure_store_listby_week
```

### Products

```sql
azure_products
```

## Shared Expressions

### DatabaseQuery (0)

```sql
let
    database = Sql.Database("4DB76RLXAXCUVMUH5KW37WBNQQ-OXJJWECEL5TEHM2DTNA3LT5QIA.datawarehouse.fabric.microsoft.com", "e284da85-ec61-4c68-bf14-be9566f211b4")
in
    database
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4DB76RLXAXCUVMUH5KW37WBNQQ-OXJJWECEL5TEHM2DTNA3LT5QIA.datawarehouse.fabric.microsoft.com | e284da85-ec61-4c68-bf14-be9566f211b4 | _(not found in SQL documentation)_ |
