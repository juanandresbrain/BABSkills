# SM_Papamart_Partial

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** 8cc39cf7-018f-45f7-9b2c-bf96fe6beabe  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Retention | 8 | 0 |  |
| Region Scorecard Goals Facts | 13 | 0 |  |
| SFS Reward Points Category | 4 | 0 |  |
| Employee Type | 5 | 0 |  |
| Transaction Type | 3 | 0 |  |
| Currency | 8 | 0 |  |
| Communication Channel | 4 | 0 |  |
| OSAT Facts | 10 | 6 |  |
| Is Comp LY | 3 | 0 |  |
| Is Comp TY | 3 | 0 |  |
| Is Shopper Trak Comp LY | 3 | 0 |  |
| Is SOTF | 3 | 0 |  |
| Is Shopper Trak Comp TY | 3 | 0 |  |
| Is On ShopperTrak | 3 | 0 |  |
| Time Calcs | 3 | 0 |  |
| Is Sound Transaction | 3 | 0 |  |
| Internal Time Calcs | 3 | 0 |  |
| Franchise Store - Comp Date | 46 | 0 |  |
| Loyalty Signup Date | 46 | 0 |  |
| Date Issued | 46 | 1 |  |
| Name Data Status | 3 | 0 |  |
| Postal Address Status | 3 | 0 |  |
| Birthday Data Status | 3 | 20 |  |
| Email Address Status | 3 | 0 |  |
| Exchange Rates | 13 | 1 |  |
| Destination Currency | 8 | 0 |  |
| Partial Transaction Fact | 4 | 0 |  |
| Giftcard Activated Fact | 10 | 7 |  |
| Gender | 4 | 0 |  |
| Giftcard Type | 2 | 0 |  |
| Is Gift | 4 | 0 |  |
| Reward Certificate | 5 | 0 |  |
| Sales Plan | 6 | 3 |  |
| Snapshot Date | 46 | 0 |  |
| Trn Dt | 30 | 0 |  |
| Labor Job | 9 | 0 |  |
| Labor Time Code | 5 | 0 |  |
| Near Birthday | 4 | 0 |  |
| Party | 3 | 0 |  |
| Tourism Band | 3 | 0 |  |
| Turnover Type | 4 | 0 |  |
| SFS Transaction Type | 5 | 0 |  |
| Tourism 5to25 Band | 3 | 0 |  |
| Week Ending Date | 30 | 0 |  |
| Hour Type | 4 | 0 |  |
| Labor Cube | 16 | 1 |  |
| Time | 15 | 0 |  |
| Transactions Cube Fanchisees Additional | 14 | 0 |  |
| SFS Guest Facts | 18 | 4 |  |
| Shopper Trak | 14 | 8 |  |
| Registrations | 32 | 0 |  |
| Transactions | 124 | 197 |  |
| Has Traffic | 2 | 0 |  |
| Date | 46 | 5 |  |
| Product | 61 | 0 |  |
| Store | 77 | 0 |  |

## Measures

### OSAT Facts.Rolling Responses

```sql
SUM('OSAT Facts'[roll_responses])
```

### OSAT Facts.Rolling Scores

```sql
SUM('OSAT Facts'[roll_score])
```

### OSAT Facts.YTD Scores

```sql
SUM('OSAT Facts'[ytd_score])
```

### OSAT Facts.YTD Responses

```sql
SUM('OSAT Facts'[ytd_responses])
```

### OSAT Facts.Month Responses

```sql
SUM('OSAT Facts'[mo_responses])
```

### OSAT Facts.OSAT Rolling

```sql
DIVIDE([Rolling Scores], [Rolling Responses])
```

### Date Issued.Org_Month

```sql

VAR MonthText = SELECTEDVALUE('Date Issued'[FiscalMonthName])
RETURN RIGHT(MonthText, 3)

```

### Birthday Data Status.Fiscal Month Ave Rate

```sql
SUM('Exchange Rates'[fiscal_month_ave_rate])
```

### Birthday Data Status.Fiscal Month End Rate

```sql
SUM('Exchange Rates'[fiscal_month_end_rate])
```

### Birthday Data Status.Actual Rate

```sql
SUM('Exchange Rates'[actual_rate])
```

### Birthday Data Status.Bbw Rate

```sql

	var SrcCURR = if(ISFILTERED('Currency'),MAX('Currency'[Currency Code]),"USD")
	var DstCURR = if(ISFILTERED('Destination Currency'),MAX('Destination Currency'[Currency Code]),"USD")
	 
    RETURN 
	CALCULATE(SUM('Exchange Rates'[bbw_rate]), 'Currency'[Currency Code]=SrcCURR,'Destination Currency'[Currency Code]=DstCURR)
```

### Birthday Data Status.Calendar Month Ave Rate

```sql
SUM('Exchange Rates'[calendar_month_ave_rate])
```

### Birthday Data Status.Calendar Month End Rate

```sql
SUM('Exchange Rates'[calendar_month_end_rate])
```

### Birthday Data Status.Partial Transaction Count

```sql
SUM('Partial Transaction Fact'[partial_transaction_count])
```

### Birthday Data Status.Mins Recorded

```sql
SUM('Labor Cube'[minsWorked])
```

### Birthday Data Status.Native GC Activated Amount

```sql
SUM('Giftcard Activated Fact'[activated_amount])
```

### Birthday Data Status.Native GC Discount Amount

```sql
SUM('Giftcard Activated Fact'[discount_amount])
```

### Birthday Data Status.# GC Activated

```sql
COUNTROWS('Giftcard Activated Fact')
```

### Birthday Data Status.GC Activated Amount

```sql
SUM('Giftcard Activated Fact'[activated_amount])
```

### Birthday Data Status.GC Discount Amount

```sql
SUM('Giftcard Activated Fact'[discount_amount])
```

### Birthday Data Status.Enters

```sql
SUM('Shopper Trak'[Enters])
```

### Birthday Data Status.EXITS

```sql
SUM('Shopper Trak'[Exits])
```

### Birthday Data Status.Franch party Count

```sql
SUM('Transactions Cube Fanchisees Additional'[Party_Count])
```

### Birthday Data Status.Franch party Sales

```sql
SUM('Transactions Cube Fanchisees Additional'[Party_Sales])/[Bbw Rate]
```

### Birthday Data Status.Franch GAAP Transactions

```sql
SUM('Transactions Cube Fanchisees Additional'[Transaction_Count])
```

### Birthday Data Status.Coupons And Discounts

```sql
SUM('Transactions Cube Fanchisees Additional'[Coupons_And_Discounts])/[Bbw Rate]
```

### Birthday Data Status.Returns

```sql
SUM('Transactions Cube Fanchisees Additional'[Returns])/[Bbw Rate]
```

### Exchange Rates.Bbw Rate2

```sql

    VAR IsCurrencyFiltered = ISFILTERED('Currency')
    //VARIsDestCurrencyFiltered = ISFILTERED('Destination Currency')
    RETURN IF(IsCurrencyFiltered, 
                //IF(IsDestCurrencyFiltered, SUM('Exchange Rates'[bbw_rate]),
                CALCULATE(SUM('Exchange Rates'[bbw_rate]), 'Destination Currency'[Currency Code]="USD"),SUM('Exchange Rates'[bbw_rate]))
                //),
                //IF(IsDestCurrencyFiltered, CALCULATE(SUM('Exchange Rates'[bbw_rate]), 'Currency'[Currency Code]="USD"), CALCULATE(SUM('Exchange //Rates'[bbw_rate]), 'Currency'[Currency Code]="USD", 'Destination Currency'[Currency Code]="USD")))
```

### Giftcard Activated Fact.Comp GC Activated

```sql
CALCULATE([GC Activated Amount], 'Is Comp TY'[isComp] = 1)

```

### Giftcard Activated Fact.GC Activated LY For Comp

```sql
CALCULATE([GC Activated Amount], DATEADD('Date'[Actual Date], -52*7, DAY), 'Is Comp LY'[isComp] = 1)
```

### Giftcard Activated Fact.NumRegGCActivated

```sql
CALCULATE([# GC Activated], 'Giftcard Type'[GiftcardType] = "Regular")
```

### Giftcard Activated Fact.amtRegGCActivated

```sql
CALCULATE([GC Activated Amount], 'Giftcard Type'[GiftcardType] = "Regular")
```

### Giftcard Activated Fact.compRegGC

```sql
CALCULATE([Comp GC Activated], 'Giftcard Type'[GiftcardType] = "Regular")
```

### Giftcard Activated Fact.compRegGCLY

```sql
CALCULATE([GC Activated LY For Comp], 'Giftcard Type'[GiftcardType] = "Regular")
```

### Giftcard Activated Fact.Reg GC B/W v LY

```sql
[compRegGC] - [compRegGCLY]
```

### Sales Plan.GAAP Sales Plan

```sql
SUM('Sales Plan'[amount]) / [Bbw Rate]
```

### Sales Plan.Native Sales Plan

```sql
SUM('Sales Plan'[amount])
```

### Sales Plan.Store Sales Plan

```sql
[Native Sales Plan]/[Bbw Rate]
```

### Labor Cube.Hours Worked

```sql

CALCULATE(
    [Mins Recorded]/60 , 'Labor Time Code'[iswork] = "Work", 'Hour Type'[ispaid] = "Paid"
)
```

### SFS Guest Facts.New SFS Guests w Email

```sql
DISTINCTCOUNT('SFS Guest Facts'[newsfsvalidemail_gstid])
```

### SFS Guest Facts.New SFS Guests Actual

```sql
DISTINCTCOUNT('SFS Guest Facts'[new_sfsgstid])
```

### SFS Guest Facts.New SFS Guests

```sql
IF(ISBLANK([New SFS Guests Actual]) || [New SFS Guests Actual] = 0, BLANK(), [New SFS Guests Actual] - 1)
```

### SFS Guest Facts.New SFS Email Capture Rate

```sql
DIVIDE([New SFS Guests w Email], [New SFS Guests], BLANK())
```

### Shopper Trak.Traffic

```sql
SUM('Shopper Trak'[Exits])
```

### Shopper Trak.Comp Traffic

```sql
CALCULATE([Traffic], 'Is Shopper Trak Comp TY'[isComp]=1)
```

### Shopper Trak.Comp Traffic LY

```sql
CALCULATE([Comp Traffic],DATEADD('Date'[Actual Date], -52*7, DAY))
```

### Shopper Trak.Traffic LY

```sql
CALCULATE([Traffic], DATEADD('Date'[Actual Date], -52*7, DAY))
```

### Shopper Trak.Traffic B/W LY

```sql
IF(ISBLANK([Traffic]) || [Traffic] = 0 || ISBLANK([Traffic LY]) || [Traffic LY] = 0, BLANK(), [Traffic] - [Traffic LY])
```

### Shopper Trak.Store Conversion TY

```sql

    VAR hasTraffic = CALCULATE([Traffic], 'Has Traffic'[hastraffic] = 1)
    RETURN DIVIDE(CALCULATE([Store Transactions], 'Has Traffic'[hastraffic] = 1), hasTraffic)
```

### Shopper Trak.Store Conversion LY

```sql

    VAR hasTraffic = CALCULATE([Traffic LY], 'Has Traffic'[hastraffic] = 1)
    RETURN DIVIDE(CALCULATE([Store Transactions], 'Has Traffic'[hastraffic] = 1), hasTraffic)
```

### Shopper Trak.STAR

```sql

    VAR hoursWorked = CALCULATE([Hours Worked], 'Is On ShopperTrak'[isShopperTrak] = 1)
    VAR hasTraffic = CALCULATE([Traffic], 'Is On ShopperTrak'[isShopperTrak] = 1)
    RETURN DIVIDE(hasTraffic, hoursWorked, BLANK())
```

### Transactions.Accessory UGA

```sql
SUM(Transactions[accessories_UGA]) / [Bbw Rate]
```

### Transactions.Accessory Units

```sql
SUM(Transactions[accessories_units])
```

### Transactions.All Transactions Count

```sql
Count(Transactions[SFS_TRN_TYP_CD])
```

### Transactions.Animal UGA

```sql
SUM(Transactions[animal_UGA]) / [Bbw Rate]
```

### Transactions.Animal Units

```sql
SUM(Transactions[animal_units])
```

### Transactions.Buy Stuff

```sql
SUM(Transactions[buy_stuff_amount]) / [Bbw Rate]
```

### Transactions.Clothes Units

```sql
SUM(Transactions[clothing_units])
```

### Transactions.ClothingUGA

```sql
SUM(Transactions[clothing_UGA])
```

### Transactions.Company GAAP Transactions

```sql
SUM(Transactions[GAAP_transaction_flag])
```

### Transactions.Company Party Count

```sql
SUM(Transactions[party_flag])
```

### Transactions.Company Store Transactions

```sql
SUM(Transactions[Store_transaction_flag])
```

### Transactions.Coupon Discount

```sql
SUM(Transactions[coupon_discount_amount]) / [Bbw Rate]
```

### Transactions.Cub Cash UGA

```sql
SUM(Transactions[cub_cash_UGA]) / [Bbw Rate]
```

### Transactions.Curbside Sales

```sql
SUM(Transactions[CurbsideAmount])
```

### Transactions.Curbside Transaction Count

```sql
SUM(Transactions[isCurbside])
```

### Transactions.Curbside Transactions With Discount

```sql
SUM(Transactions[numCurbsideTransWithDiscount])
```

### Transactions.Curbside Units

```sql
SUM(Transactions[CurbsideUnits])
```

### Transactions.Direct Mailable

```sql
SUM(Transactions[DM_Transactions])
```

### Transactions.Donations UGA

```sql
SUM(Transactions[donations_UGA]) / [Bbw Rate]
```

### Transactions.Donations Units

```sql
SUM(Transactions[donations_units])
```

### Transactions.Enterprise Selling Amount

```sql
SUM(Transactions[Enterprise_Selling_Amount])
```

### Transactions.Enterprise Selling Only Amount

```sql
SUM(Transactions[Enterprise_Selling_Only_Amount])
```

### Transactions.Enterprise Selling Only Transaction Count

```sql
SUM(Transactions[Enterprise_Selling_Only_Transaction_Count])
```

### Transactions.Enterprise Selling Only Units

```sql
SUM(Transactions[Enterprise_Selling_Only_Units])
```

### Transactions.Enterprise Selling Transaction Count

```sql
SUM(Transactions[Enterprise_Selling_Transaction_Count])
```

### Transactions.Enterprise Selling Units

```sql
SUM(Transactions[Enterprise_Selling_Units])
```

### Transactions.Financial Curbside Sales

```sql
SUM(Transactions[FinancialCurbsideAmount])
```

### Transactions.Financial GAAP Sales

```sql
SUM(Transactions[Financial_GAAP_Sales_Amount]) / [Bbw Rate]
```

### Transactions.Financial Pickup From Store Sales

```sql
SUM(Transactions[FinancialPickupFromStoreAmount]) / [Bbw Rate]
```

### Transactions.Financial SameDayShipt Sales

```sql
SUM(Transactions[FinancialSameDayShiptAmount])
```

### Transactions.Financial Ship From Store Sales

```sql
SUM(Transactions[FinancialShipFromStoreAmount]) / [Bbw Rate]
```

### Transactions.Financial Store Sales

```sql
SUM(Transactions[Financial_Store_Sales_Amount]) / [Bbw Rate]
```

### Transactions.Franchisee Royalty Exchange Rate Applied

```sql
SUM(Transactions[franchisee_exchange_rate])
```

### Transactions.Franchisee Royalty Withholding Tax Rate

```sql
SUM(Transactions[franchisee_withholding_tax_rate])
```

### Transactions.GAAP Sales

```sql
SUM(Transactions[GAAP_sales_amount]) / [Bbw Rate]
```

### Transactions.GAAP Trans With Discount

```sql
SUM(Transactions[numGAAPTransWithDiscount])
```

### Transactions.Gaap Units

```sql
SUM(Transactions[Gaap_Units])
```

### Transactions.Gift Card Discount

```sql
SUM(Transactions[giftcard_discount_amount]) / [Bbw Rate]
```

### Transactions.Gift Card Units

```sql
SUM(Transactions[giftcard_units])
```

### Transactions.Gift Cards Redeemed UGA

```sql
SUM(Transactions[giftcards_redeemed]) / [Bbw Rate]
```

### Transactions.Gift Cards Sold UGA

```sql
SUM(Transactions[giftcard_UGA]) / [Bbw Rate]
```

### Transactions.GiftCard Only Transaction Count

```sql
SUM(Transactions[GiftCard_Only_Flag])
```

### Transactions.Has Phone Number

```sql
SUM(Transactions[HasPhoneNumber])
```

### Transactions.Line Count

```sql
SUM(Transactions[line_count])
```

### Transactions.Merchandise UGA

```sql
SUM(Transactions[merchandise_UGA]) / [Bbw Rate]
```

### Transactions.Merchandise Units

```sql
SUM(Transactions[merchandise_units])
```

### Transactions.Native Accessory UGA

```sql
SUM(Transactions[accessories_UGA])
```

### Transactions.Native Animal UGA

```sql
SUM(Transactions[animal_UGA])
```

### Transactions.Native Buy Stuff

```sql
SUM(Transactions[buy_stuff_amount])
```

### Transactions.Native Clothing UGA

```sql
SUM(Transactions[clothing_UGA])
```

### Transactions.Native Coupon Discount

```sql
SUM(Transactions[coupon_discount_amount])
```

### Transactions.Native Cub Cash UGA

```sql
SUM(Transactions[cub_cash_UGA])
```

### Transactions.Native Curbside Sales

```sql
SUM(Transactions[CurbsideAmount])
```

### Transactions.Native Donations UGA

```sql
SUM(Transactions[donations_UGA])
```

### Transactions.Native Financial GAAP Sales

```sql
SUM(Transactions[Financial_GAAP_Sales_Amount])
```

### Transactions.Native Financial Store Sales

```sql
SUM(Transactions[Financial_Store_Sales_Amount])
```

### Transactions.Native GAAP Sales

```sql
SUM(Transactions[GAAP_sales_amount])
```

### Transactions.Native Gift Card Discount

```sql
SUM(Transactions[giftcard_discount_amount])
```

### Transactions.Native Gift Cards Redeemed UGA

```sql
SUM(Transactions[giftcards_redeemed])
```

### Transactions.Native Gift Cards Sold UGA

```sql
SUM(Transactions[giftcard_UGA])
```

### Transactions.Native Merchandise UGA

```sql
SUM(Transactions[merchandise_UGA])
```

### Transactions.Native Net Sales

```sql
SUM(Transactions[net_sales_amount])
```

### Transactions.Native Non-Animal UGA

```sql
SUM(Transactions[non_animal_UGA])
```

### Transactions.Native Other Fees UGA

```sql
SUM(Transactions[other_fees_UGA])
```

### Transactions.Native Other UGA

```sql
SUM(Transactions[other_UGA])
```

### Transactions.Native Party Deposit UGA

```sql
SUM(Transactions[party_deposit_UGA])
```

### Transactions.Native Pickup From Store Sales

```sql
SUM(Transactions[PickupFromStoreAmount])
```

### Transactions.Native Prestuffed UGA

```sql
SUM(Transactions[prestuffed_UGA])
```

### Transactions.Native Redemptions

```sql
SUM(Transactions[redemption_amount])
```

### Transactions.Native Returns UGA

```sql
SUM(Transactions[returns_UGA])
```

### Transactions.Native Reward Certificate

```sql
SUM(Transactions[reward_certificate_amount])
```

### Transactions.Native SameDayShipt Sales

```sql
SUM(Transactions[SameDayShiptAmount])
```

### Transactions.Native Scent UGA

```sql
SUM(Transactions[Scents_UGA])
```

### Transactions.Native Ship From Store Sales

```sql
SUM(Transactions[ShipFromStoreAmount])
```

### Transactions.Native Shipping UGA

```sql
SUM(Transactions[shipping_UGA])
```

### Transactions.Native Shoe UGA

```sql
SUM(Transactions[footwear_UGA])
```

### Transactions.Native Sound UGA

```sql
SUM(Transactions[sounds_UGA])
```

### Transactions.Native Sports UGA

```sql
SUM(Transactions[sports_UGA])
```

### Transactions.Native Store Sales

```sql
SUM(Transactions[Store_Sales_Amount])
```

### Transactions.Native Stuffing and Supplies UGA

```sql
SUM(Transactions[stuffing_supplies_UGA])
```

### Transactions.Native Tax

```sql
SUM(Transactions[tax_amount])
```

### Transactions.Native Total Discount

```sql
SUM(Transactions[total_discount_amount])
```

### Transactions.Native Unit Disc Amount

```sql
SUM(Transactions[unit_discount_amount])
```

### Transactions.Native Unit Gross Amount

```sql
SUM(Transactions[unit_gross_amount])
```

### Transactions.Native Unit Net Amount

```sql
SUM(Transactions[unit_net_amount])
```

### Transactions.Native Upsell Discount Amount

```sql
SUM(Transactions[Upsell_Discount_Amount])
```

### Transactions.Net Sales

```sql
SUM(Transactions[net_sales_amount]) / [Bbw Rate]
```

### Transactions.Non-Animal UGA

```sql
SUM(Transactions[non_animal_UGA]) / [Bbw Rate]
```

### Transactions.Non-Animal Units

```sql
SUM(Transactions[non_animal_units])
```

### Transactions.Other Fees UGA

```sql
SUM(Transactions[other_fees_UGA]) / [Bbw Rate]
```

### Transactions.Other Fees Units

```sql
SUM(Transactions[other_fees_units])
```

### Transactions.Other UGA

```sql
SUM(Transactions[other_UGA]) / [Bbw Rate]
```

### Transactions.Other Units

```sql
SUM(Transactions[other_units])
```

### Transactions.Party Deposit UGA

```sql
SUM(Transactions[party_deposit_UGA]) / [Bbw Rate]
```

### Transactions.Party Deposit Units

```sql
SUM(Transactions[party_deposit_units])
```

### Transactions.Party Master

```sql
SUM(Transactions[party_master])
```

### Transactions.Pickup From Store Sales

```sql
SUM(Transactions[PickupFromStoreAmount]) / [Bbw Rate]
```

### Transactions.Pickup From Store Transaction Count

```sql
SUM(Transactions[isPickUpFromStore])
```

### Transactions.Pickup From Store Transactions With Discount

```sql
SUM(Transactions[numPickupFromStoreTransWithDiscount])
```

### Transactions.Pickup From Store Units

```sql
SUM(Transactions[PickupFromStoreUnits])
```

### Transactions.Prestuffed UGA

```sql
SUM(Transactions[prestuffed_UGA]) / [Bbw Rate]
```

### Transactions.Prestuffed Units

```sql
SUM(Transactions[prestuffed_units])
```

### Transactions.Redemptions

```sql
SUM(Transactions[redemption_amount]) / [Bbw Rate]
```

### Transactions.Returns UGA

```sql
SUM(Transactions[returns_UGA]) / [Bbw Rate]
```

### Transactions.Reward Certificate

```sql
SUM(Transactions[reward_certificate_amount]) / [Bbw Rate]
```

### Transactions.SameDayShipt Sales

```sql
SUM(Transactions[SameDayShiptAmount])
```

### Transactions.SameDayShipt Transaction Count

```sql
SUM(Transactions[isSameDayShipt])
```

### Transactions.SameDayShipt Transactions With Discount

```sql
SUM(Transactions[numSameDayShiptTransWithDiscount])
```

### Transactions.SameDayShipt Units

```sql
SUM(Transactions[SameDayShiptUnits])
```

### Transactions.Scent UGA

```sql
SUM(Transactions[Scents_UGA]) / [Bbw Rate]
```

### Transactions.Scent Units

```sql
SUM(Transactions[Scents_units])
```

### Transactions.Ship From Store Sales

```sql
SUM(Transactions[ShipFromStoreAmount]) / [Bbw Rate]
```

### Transactions.Ship From Store Transaction Count

```sql
SUM(Transactions[isShipFromStore])
```

### Transactions.Ship From Store Transactions With Discount

```sql
SUM(Transactions[numShipFromStoreTransWithDiscount])
```

### Transactions.Ship From Store Units

```sql
SUM(Transactions[ShipFromStoreUnits])
```

### Transactions.Shipping UGA

```sql
SUM(Transactions[shipping_UGA]) / [Bbw Rate]
```

### Transactions.Shipping Units

```sql
SUM(Transactions[shipping_units])
```

### Transactions.Shoe UGA

```sql
SUM(Transactions[footwear_UGA]) / [Bbw Rate]
```

### Transactions.Shoe Units

```sql
SUM(Transactions[footwear_units])
```

### Transactions.Sound UGA

```sql
SUM(Transactions[sounds_UGA]) / [Bbw Rate]
```

### Transactions.Sound Units

```sql
SUM(Transactions[sounds_units])
```

### Transactions.Sports UGA

```sql
SUM(Transactions[sports_UGA]) / [Bbw Rate]
```

### Transactions.Sports Units

```sql
SUM(Transactions[sports_units])
```

### Transactions.Store Sales

```sql
SUM(Transactions[Store_Sales_Amount]) / [Bbw Rate]
```

### Transactions.Store Trans With Discount

```sql
SUM(Transactions[numStoreTransWithDiscount])
```

### Transactions.Store Units

```sql
SUM(Transactions[Store_units])
```

### Transactions.Stuffing and Supplies UGA

```sql
SUM(Transactions[stuffing_supplies_UGA]) / [Bbw Rate]
```

### Transactions.Tax

```sql
SUM(Transactions[tax_amount]) / [Bbw Rate]
```

### Transactions.Total Discount

```sql
SUM(Transactions[total_discount_amount]) / [Bbw Rate]
```

### Transactions.Transactions Eligible for Capture

```sql
SUM(Transactions[TransactionEligibleForLoyaltyCapture])
```

### Transactions.Unit Disc Amount

```sql
SUM(Transactions[unit_discount_amount]) / [Bbw Rate]
```

### Transactions.Unit Gross Amount

```sql
SUM(Transactions[unit_gross_amount]) / [Bbw Rate]
```

### Transactions.Unit Net Amount

```sql
SUM(Transactions[unit_net_amount]) / [Bbw Rate]
```

### Transactions.Upsell Discount Amount

```sql
SUM(Transactions[Upsell_Discount_Amount]) / [Bbw Rate]
```

### Transactions.GAAP Sales Amount Next

```sql
SUM(Transactions[GAAP_sales_amount])
```

### Transactions.Animal Units LY For Comp

```sql
CALCULATE([Animal Units], 'Is Comp LY'[isComp]=1, SAMEPERIODLASTYEAR('Date'[Actual Date]))
```

### Transactions.Comp Animal Units

```sql
CALCULATE([Animal Units], 'Is Comp TY'[isComp] = 1)
```

### Transactions.Store Transactions

```sql
[Company Store Transactions] + [Franch GAAP Transactions]
```

### Transactions.Comp Store Transactions

```sql
CALCULATE([Store Transactions], 'Is Comp TY'[isComp] = 1)
```

### Transactions.Comp Store Units

```sql
CALCULATE([Store Units], 'Is Comp TY'[isComp]=1)
```

### Transactions.GAAP Transactions

```sql
[Company GAAP Transactions] + [Franch GAAP Transactions]
```

### Transactions.Native Comp GAAP Sales

```sql
CALCULATE([Native GAAP Sales], 'Is Comp TY'[isComp] = 1)
```

### Transactions.Native Comp Store Sales

```sql
CALCULATE([Native Store Sales], 'Is Comp TY'[isComp] = 1)
```

### Transactions.Native GAAP Sales LY

```sql
CALCULATE([Native GAAP Sales], SAMEPERIODLASTYEAR('Date'[Actual Date]))
```

### Transactions.Native GAAP Sales LY For Comp

```sql
CALCULATE([Native GAAP Sales LY], 'Is Comp LY'[isComp] = 1)
```

### Transactions.Native Store Sales LY

```sql
CALCULATE([Native Store Sales],  SAMEPERIODLASTYEAR('Date'[Actual Date])
)
```

### Transactions.Native Store Sales LY For Comp

```sql
CALCULATE([Native Store Sales LY], 'Is Comp LY'[isComp] = 1)
```

### Transactions.Store Transactions LY

```sql
CALCULATE([Store Transactions], SAMEPERIODLASTYEAR('Date'[Actual Date]))
```

### Transactions.Store Transactions LY For Comp

```sql
CALCULATE([Store Transactions LY], 'Is Comp LY'[isComp] = 1)
```

### Transactions.Store Units LY For Comp

```sql
CALCULATE([Store Units], 'Is Comp LY'[isComp] = 1, DATEADD('Date'[Actual Date], -52*7, DAY))
```

### Transactions.Traffic Comp Store Transactions LY

```sql
CALCULATE([Store Transactions LY For Comp], 'Is Shopper Trak Comp LY'[isComp] =1, SAMEPERIODLASTYEAR('Date'[Actual Date])) 
```

### Transactions.Traffic Comp Store Transactions TY

```sql
CALCULATE([Comp Store Transactions], 'Is Shopper Trak Comp TY'[isComp] = 1)
```

### Transactions.Clothing UGA

```sql
SUMX(VALUES('Date'[Actual Date]), [ClothingUGA] /[Bbw Rate])
```

### Transactions.Plus Only Transactions

```sql

CALCULATE(
    [GAAP Transactions],'Transaction Type'[transaction_key] = 3)
```

### Transactions.Bare Bear Transactions

```sql

CALCULATE(
    [GAAP Transactions],'Transaction Type'[transaction_key] = 1)
```

### Transactions.Bear Plus Transactions

```sql

CALCULATE(
    [GAAP Transactions],'Transaction Type'[transaction_key] = 2)
```

### Transactions.Party Count

```sql
[Company Party Count] + [Franch party Count]
```

### Transactions.Native GAAP Party Sales

```sql

CALCULATE(
    [Native GAAP Sales],'Party'[party_key] = 1)
```

### Transactions.SFS GAAP Transactions

```sql

CALCULATE(
    [GAAP Transactions],'SFS Transaction Type'[sfs_transaction_y_n] = "Y")
```

### Transactions.New SFS GAAP Transactions

```sql

CALCULATE(
    [SFS GAAP Transactions],'SFS Transaction Type'[sfs_transaction_new] = "Y")
```

### Transactions.SFS Store Transactions

```sql

CALCULATE(
    [Store Transactions],'SFS Transaction Type'[sfs_transaction_y_n] = "Y")
```

### Transactions.Store Sales LY

```sql
CALCULATE([Store Sales], DATEADD('Date'[Actual Date], -52*7, DAY))
```

### Transactions.Comp Store Sales

```sql
CALCULATE([Store Sales], 'Is Comp TY'[isComp] = 1)
```

### Transactions.Comp Party Count

```sql
CALCULATE([Party Count], 'Is Comp TY'[isComp] = 1)
```

### Transactions.Comp Merchandise Units

```sql
CALCULATE([Merchandise Units], 'Is Comp TY'[isComp] = 1)
```

### Transactions.GAAP Transactions LY For Comp

```sql
CALCULATE([GAAP Transactions], 'Is Comp LY'[isComp] = 1, SAMEPERIODLASTYEAR('Date'[Actual Date]))
```

### Transactions.Transaction Count LY for Comp

```sql
[GAAP Transactions LY For Comp]
```

### Transactions.Party Count LY For Comp

```sql
CALCULATE([Party Count], 'Is Comp LY'[isComp] = 1, DATEADD('Date'[Actual Date], -52*7, DAY))
```

### Transactions.New Loyalty Transactions Count

```sql
CALCULATE([All Transactions Count], 'SFS Transaction Type'[sfs_transaction_type_key] = 1)
```

### Transactions.Repeat Loyalty Transactions Count

```sql
CALCULATE([All Transactions Count], 'SFS Transaction Type'[sfs_transaction_type_key] = 2)
```

### Transactions.Captured Loyalty Transactions

```sql
[New Loyalty Transactions Count] + [Repeat Loyalty Transactions Count]
```

### Transactions.Loyalty Capture Rate %

```sql
DIVIDE([Captured Loyalty Transactions], [Transactions Eligible for Capture])
```

### Transactions.Party Master LY

```sql
CALCULATE([Party Master], DATEADD('Date'[Actual Date], -52*7, DAY))
```

### Transactions.Last 6 Weeks

```sql

VAR SelectedDate = MAX('Date Issued'[week_ending_date])
VAR Last6WeekendsTable = 
    FILTER (
        'Date',
        'Date'[week_ending_date] <= SelectedDate && 'Date'[Day of Week] = 7 && DATEADD('Date'[week_ending_date], 42, DAY) > SelectedDate
    )
RETURN
CALCULATE (
    COUNTROWS (Last6WeekendsTable),
    TOPN (6, Last6WeekendsTable, 'Date'[week_ending_date], DESC))









```

### Transactions.Selected Date

```sql
SELECTEDVALUE('Date Issued'[week_ending_date])
```

### Transactions.Sales v LY

```sql

IF(
    ISBLANK([Store Sales LY]) || [Store Sales LY] = 0, 
    "N/A", 
    DIVIDE([Comp Store Sales] - [Store Sales LY], [Store Sales LY])
)

```

### Transactions.Trans v LY

```sql

IF(
    ISBLANK([Store Transactions LY For Comp]) || [Store Transactions LY For Comp] = 0, 
    "N/A", 
    DIVIDE([Comp Store Transactions] - [Store Transactions LY For Comp], [Store Transactions LY For Comp])
)
```

### Transactions.DPT

```sql
IF(
    ISBLANK([Store Transactions]) || [Store Transactions] = 0, 
    "N/A", 
    DIVIDE([Store Sales], 
           IF([Store Transactions]= 0, 1, [Store Transactions])
    )
)
```

### Transactions.UPT v LY

```sql
if(ISBLANK([Store Transactions LY For Comp]) || [Store Transactions LY For Comp] =0,"N/A",
DIVIDE([Comp Store Sales],if ([Comp Store Transactions] =0,1,[Comp Store Transactions]))-
Divide([Store Sales LY For Comp], [Store Transactions LY For Comp], 0))
```

### Transactions.Store Sales LY For Comp

```sql
CALCULATE([Store Sales LY], 'Is Comp LY'[isComp] = 1)
```

### Transactions.Parties B/W v LY

```sql
IF (ISBLANK([Store Transactions]) || [Store Transactions] = 0,"N/A",
Divide([Merchandise Units],if([Store Transactions] =0,1,[Store Transactions])))
```

### Transactions.% Party Sales

```sql
if(ISBLANK([Store Transactions LY For Comp]) || [Store Transactions LY For Comp] =0,"N/A",
(Divide([Merchandise Units],IF([Comp Store Transactions] =0,1, [Comp Store Transactions])
)
-DIVIDE([Merchandise Units LY For Comp], IF([Store Transactions LY For Comp]=0, 1, [Store Transactions LY For Comp]))))
```

### Transactions.Merchandise Units LY For Comp

```sql
CALCULATE([Merchandise Units], 'Is Comp LY'[isComp] = 1, DATEADD('Date'[Actual Date], -52*7, DAY))
```

### Transactions.Conv TY

```sql
IF ([Traffic] =0,"N/A",
Divide([Store Transactions],[Traffic]))
```

### Transactions.Conv LY

```sql
If([Traffic LY] =0,"L/A",
Divide([Store Transactions LY For Comp],[Traffic LY]))
```

### Transactions.Conv B/W LY

```sql

IF(
    ISBLANK([Store Conversion LY]) || [Store Conversion LY] = 0, 
    "N/A", 
    DIVIDE([Store Transactions], [Traffic]) 
    - 
    DIVIDE([Store Transactions LY For Comp], [Traffic LY])
)

```

### Transactions.Cp

```sql

// IF(SELECTEDVALUE(Transactions[isComp]) = "Y", 1, 0)
IF(SELECTEDVALUE(Transactions[IsComp]) IN {0, 1}, "Y", "N")


```

### Transactions.Last3Months

```sql
VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
VAR StartDate = EOMONTH(SelectedDate, -3) +1  -- Get the first day of the month, two months before the selected date
VAR EndDate = EOMONTH(SelectedDate, 0) -- End at the last day of the selected week-ending date's month

RETURN
CALCULATE(
    CONCATENATEX(
        VALUES('Date'[Org_Month_Name]),
        'Date'[Org_Month_Name],
        ", ",
        'Date'[Org_Month_Name],
        ASC
    ),
    FILTER(
        'Date',
        'Date'[week_ending_date] >= StartDate && 'Date'[week_ending_date] <= EndDate
    )
)
// VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
// VAR StartDate = EOMONTH(SelectedDate, -3) +1  -- Get the first day of the month, two months before the selected date
// VAR EndDate = EOMONTH(SelectedDate, 0) -- End at the last day of the selected week-ending date's month

// RETURN
// CALCULATE(
//     CONCATENATEX(
//         VALUES('Date'[Fiscal Period]),
//         'Date'[Fiscal Period],
//         ", ",
//         'Date'[Fiscal Period],
//         ASC
//     ),
//     FILTER(
//         'Date',
//         'Date'[week_ending_date] >= StartDate && 'Date'[week_ending_date] <= EndDate
//     )
// )


// VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
// VAR StartDate = EOMONTH(SelectedDate, -2) +3  -- Get the first day of the month, two months before the selected date
// VAR EndDate = EOMONTH(SelectedDate, 1) -- End at the last day of the selected week-ending date's month

// RETURN
// CALCULATE(
//     CONCATENATEX(
//         VALUES('Date'[Fiscal Period Of Year]),
//         'Date'[Fiscal period of year],
//         ", ",
//         'Date'[Fiscal period of year],
//         ASC
//     ),
//     FILTER(
//         'Date',
//         'Date'[week_ending_date] >= StartDate && 'Date'[week_ending_date] <= EndDate
//     )
// )







```

### Transactions.Last Year 3 Months

```sql


VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
VAR SelectedDateLastYear = DATE(YEAR(SelectedDate)-1, MONTH(SelectedDate)+1, DAY(SelectedDate)) -- Get the same date last year
VAR StartDateLastYear = EOMONTH(SelectedDateLastYear, -2) + 2 -- Get the first day of the month, two months before the selected date last year
VAR EndDateLastYear = EOMONTH(SelectedDateLastYear, 1) -- End at the last day of the selected week-ending date's month last year

RETURN
CALCULATE(
    CONCATENATEX(
        VALUES('Date'[Org_Month_Name]),
        'Date'[Org_Month_Name],
        ", ",
        'Date'[Org_Month_Name],
        ASC
    ),
    FILTER(
        'Date',
        'Date'[week_ending_date] >= StartDateLastYear && 'Date'[week_ending_date] <= EndDateLastYear
    )
)


```

### Transactions.Last 5 Quarters

```sql
VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
VAR StartDate = EOMONTH(SelectedDate, -12) +2  -- Get the first day of the month, two months before the selected date
VAR EndDate = EOMONTH(SelectedDate, 1) -- End at the last day of the selected week-ending date's month

RETURN
CALCULATE(
    CONCATENATEX(
        VALUES('Date'[Org_Fiscal_Quarter]),
        'Date'[Org_Fiscal_Quarter],
        ", ",
        'Date'[Org_Fiscal_Quarter],
        ASC
    ),
    FILTER(
        'Date',
        'Date'[week_ending_date] >= StartDate && 'Date'[week_ending_date] <= EndDate
    )
)
//  VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
// VAR StartDate = EOMONTH(SelectedDate, -12) +2  -- Get the first day of the month, two months before the selected date
// VAR EndDate = EOMONTH(SelectedDate, 1) -- End at the last day of the selected week-ending date's month

// RETURN
// CALCULATE(
//     CONCATENATEX(
//         VALUES('Date'[Fiscal Quarter]),
//         'Date'[Fiscal Quarter],
//         ", ",
//         'Date'[Fiscal Quarter],
//         ASC
//     ),
//     FILTER(
//         'Date',
//         'Date'[week_ending_date] >= StartDate && 'Date'[week_ending_date] <= EndDate
//     )
// )

```

### Transactions.Last 2 Years

```sql

VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
VAR StartDate = DATE(YEAR(SelectedDate) - 1, 1, 1) -- Get the first day of the year one year before the selected date
VAR EndDate = DATE(YEAR(SelectedDate), 12, 31) -- End at the last day of the selected date's year

RETURN
CALCULATE(
    CONCATENATEX(
        VALUES('Date'[Fiscal Year]),
        'Date'[Fiscal Year],
        ", ",
        'Date'[Fiscal Year],
        ASC
    ),
    FILTER(
        'Date',
        'Date'[week_ending_date] >= StartDate && 'Date'[week_ending_date] <= EndDate &&
        'Date'[Fiscal Year] IN {YEAR(SelectedDate)-1, YEAR(SelectedDate)}
    )
)

// VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
// VAR StartDate = DATE(YEAR(SelectedDate) - 2, MONTH(SelectedDate), DAY(SelectedDate)) -- Get the same date 2 years before the selected date
// VAR EndDate = SelectedDate -- End at the selected date

// RETURN
// CALCULATE(
//     CONCATENATEX(
//         TOPN(
//             2,
//             VALUES('Date'[Fiscal Year]),
//             'Date'[Fiscal Year],
//             ASC
//         ),
//         'Date'[Fiscal Year],
//         ", ",
//         'Date'[Fiscal Year],
//         ASC
//     ),
//     FILTER(
//         'Date',
//         'Date'[week_ending_date] >= StartDate && 'Date'[week_ending_date] <= EndDate
//     )
// )


//  VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
// VAR StartDate = EOMONTH(SelectedDate, -24) +1  -- Get the first day of the month, two months before the selected date
// VAR EndDate = EOMONTH(SelectedDate, 1) -- End at the last day of the selected week-ending date's month

// RETURN
// CALCULATE(
//     CONCATENATEX(
//         VALUES('Date'[Fiscal Year]),
//         'Date'[Fiscal Year],
//         ", ",
//         'Date'[Fiscal Year],
//         ASC
//     ),
//     FILTER(
//         'Date',
//         'Date'[week_ending_date] >= StartDate && 'Date'[week_ending_date] <= EndDate
//     )
// )

```

### Transactions.DPT vs LY

```sql
if(ISBLANK([Store Transactions LY For Comp])|| [Store Transactions LY For Comp] =0,"N/A", Divide([Comp Store Transactions]- [Store Transactions LY For Comp],[Store Transactions LY For Comp]))
```

### Transactions.UPT

```sql
DIVIDE([Merchandise Units], [Store Transactions])
```

### Transactions.Sales vs Plan

```sql
DIVIDE([Store Sales] - [Store Sales Plan], [Store Sales Plan])
```

### Transactions.CompFlag

```sql
IF(SELECTEDVALUE(Transactions[isComp], "") = "Y", 1, 0)

```

### Transactions.CP2

```sql
IF(MINX(Transactions, [CompFlag]) = 1, "Y", "N")


```

### Transactions.Last 6 Weeks2

```sql

VAR SelectedDate = MAX('Date Issued'[week_ending_date])
VAR Last6WeekendsTable =
    CALCULATETABLE (
        VALUES('Date'[week_ending_date]),
        'Date'[week_ending_date] <= SelectedDate,
        'Date'[Day of Week] = 7,
        'Date'[week_ending_date] > SelectedDate - 42
    )
VAR Last6Weekends =
    TOPN (
        6,
        Last6WeekendsTable,
        'Date'[week_ending_date],
        DESC
    )
RETURN
    CONCATENATEX(Last6Weekends, 'Date'[week_ending_date], UNICHAR(10))

```

### Date.In Last Six Weeks

```sql

VAR SelectedDate = MAX('Date'[Actual Date])
VAR Last6WeekendsTable = 
    FILTER (
        'Date',
        'Date'[Actual Date] <= SelectedDate &&
        'Date'[Day of Week] = 7
    )
RETURN
CALCULATE (
    COUNTROWS (Last6WeekendsTable),
    TOPN (6, Last6WeekendsTable, 'Date'[Actual Date], DESC)
)
```

### Date.FW

```sql

VAR ColumnValue = SELECTEDVALUE('Date'[Fiscal Week])
RETURN RIGHT(ColumnValue, 2)

```

### Date.FP

```sql


VAR ColumnValue = SELECTEDVALUE('Date'[month_name])
RETURN LEFT(ColumnValue, 3)

```

### Date.Fiscal_Year1

```sql

VAR SelectedDate = MAX('Date Issued'[week_ending_date]) -- Get the selected date from the slicer
VAR StartDate = EOMONTH(SelectedDate, -2) + 3 -- First day of the month, two months before the selected date
VAR EndDate = EOMONTH(SelectedDate, 1) -- End at the last day of the selected week-ending date's month
VAR SelectedMonth = MONTH(SelectedDate) -- Get the month from the selected date
VAR FiscalYear = MAX('Date'[Fiscal Year]) -- Get the fiscal year from the related table
RETURN
IF(
    SelectedMonth >= 2, -- If the selected month is February or later
    FiscalYear, -- Use the current fiscal year
    FiscalYear - 1 -- Use the previous fiscal year
)

```

### Date.Fiscal_Month_Name

```sql

SWITCH(
    TRUE(),
    MONTH(MAX('Date Issued'[week_ending_date])) = 2, "Feb",
    MONTH(MAX('Date Issued'[week_ending_date])) = 3, "Mar",
    MONTH(MAX('Date Issued'[week_ending_date])) = 4, "Apr",
    MONTH(MAX('Date Issued'[week_ending_date])) = 5, "May",
    MONTH(MAX('Date Issued'[week_ending_date])) = 6, "Jun",
    MONTH(MAX('Date Issued'[week_ending_date])) = 7, "Jul",
    MONTH(MAX('Date Issued'[week_ending_date])) = 8, "Aug",
    MONTH(MAX('Date Issued'[week_ending_date])) = 9, "Sep",
    MONTH(MAX('Date Issued'[week_ending_date])) = 10, "Oct",
    MONTH(MAX('Date Issued'[week_ending_date])) = 11, "Nov",
    MONTH(MAX('Date Issued'[week_ending_date])) = 12, "Dec",
    MONTH(MAX('Date Issued'[week_ending_date])) = 1, "Jan"
)

```

## Power Query Source (per table)

### Retention

```sql
retention_mo_facts
```

### Region Scorecard Goals Facts

```sql
region_scorecard_goals_facts
```

### SFS Reward Points Category

```sql
sfs_reward_points_category_dim
```

### Employee Type

```sql
employee_type_dim
```

### Transaction Type

```sql
transaction_type_dim
```

### Currency

```sql
currency
```

### Communication Channel

```sql
communication_channel_dim
```

### OSAT Facts

```sql
osat_mo_facts
```

### Is Comp LY

```sql
is_comp_ly
```

### Is Comp TY

```sql
is_comp_ty
```

### Is Shopper Trak Comp LY

```sql
is_shopper_trak_comp_ly
```

### Is SOTF

```sql
is_sotf
```

### Is Shopper Trak Comp TY

```sql
is_shopper_trak_comp_ty
```

### Is On ShopperTrak

```sql
is_on_shoppertrak
```

### Time Calcs

```sql
time_calcs
```

### Is Sound Transaction

```sql
is_soundtransaction
```

### Internal Time Calcs

```sql
internal_time_calcs
```

### Franchise Store - Comp Date

```sql
franchise_store_comp_date
```

### Loyalty Signup Date

```sql
loyalty_signup_date
```

### Date Issued

```sql
date_issued
```

### Name Data Status

```sql
name_data_status
```

### Postal Address Status

```sql
postal_address_status
```

### Birthday Data Status

```sql
birthday_data_status
```

### Email Address Status

```sql
email_address_status
```

### Exchange Rates

```sql
exchangerates
```

### Destination Currency

```sql
destination_currency
```

### Partial Transaction Fact

```sql
partial_transaction_count_facts
```

### Giftcard Activated Fact

```sql
giftcard_activated_fact
```

### Gender

```sql
gender
```

### Giftcard Type

```sql
giftcard_type_dim
```

### Is Gift

```sql
registrations_isgift_dim
```

### Reward Certificate

```sql
reward_certificate_dim
```

### Sales Plan

```sql
salesplan
```

### Snapshot Date

```sql
snapshot_date
```

### Trn Dt

```sql
trn_dt
```

### Labor Job

```sql
labor_job_dim
```

### Labor Time Code

```sql
labor_timecode_dim
```

### Near Birthday

```sql
registrations_nearbirthday_dim
```

### Party

```sql
party_dim
```

### Tourism Band

```sql
registrations_tourismband_dim
```

### Turnover Type

```sql
turnover_type_dim
```

### SFS Transaction Type

```sql
sfs_transaction_type_dim
```

### Tourism 5to25 Band

```sql
registrations_tourism_5to25_mileband_dim
```

### Week Ending Date

```sql
week_ending_date
```

### Hour Type

```sql
labor_hourtype_dim
```

### Labor Cube

```sql
labour_cube_v3
```

### Time

```sql
time_dim
```

### Transactions Cube Fanchisees Additional

```sql
transactions_cube_franchisees_additional
```

### SFS Guest Facts

```sql
sfsgsts
```

### Shopper Trak

```sql
shopper_trak
```

### Registrations

```sql
registrations_cube_v3
```

### Transactions

```sql
transactions_cube_v3
```

### Has Traffic

```sql
has_traffic
```

### Date

```sql
dim_date
```

### Product

```sql
product_dim
```

### Store

```sql
dim_store
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
| 4DB76RLXAXCUVMUH5KW37WBNQQ-OXJJWECEL5TEHM2DTNA3LT5QIA.datawarehouse.fabric.microsoft.com | e284da85-ec61-4c68-bf14-be9566f211b4 → LH_Reporting | [4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com/LH_Reporting](../../../4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Reporting/) |
