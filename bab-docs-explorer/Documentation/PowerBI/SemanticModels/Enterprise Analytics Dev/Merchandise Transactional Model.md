# Merchandise Transactional Model

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| DateTableTemplate_bd621608-5813-48a2-9dfc-9f7f8eb0b93c | 8 | 0 | Yes |
| PurchasingTransView | 75 | 23 |  |
| LocalDateTable_573bd59f-30e3-4724-a9dc-d049d5bd88ff | 8 | 0 | Yes |
| d365LocationMapping_View | 15 | 0 |  |
| InventJourTransView | 27 | 0 |  |
| PurchChargesView | 30 | 0 |  |
| LocalDateTable_aacd14c4-d89f-4cb0-85ad-9f533fe79b60 | 8 | 0 | Yes |
| product_dim_le | 83 | 1 |  |
| LocalDateTable_cf03c37c-1de9-4a30-acc0-a765861f7251 | 8 | 0 | Yes |
| ProductDim_attribute | 7 | 0 |  |
| date_dim | 37 | 0 |  |
| LocalDateTable_5fcd5113-f6c2-46a0-843e-b67db11e6e91 | 8 | 0 | Yes |
| RetailSalesTransactionView | 43 | 3 |  |
| weeklyOnHandView | 18 | 0 |  |
| InventtranferView | 8 | 0 |  |
| productattributesummaryview | 24 | 0 |  |
| LocalDateTable_78797bf2-1159-4b72-9fbf-a2062fd2bb4d | 8 | 0 | Yes |
| LocalDateTable_62b65351-8b3a-49b2-a51a-53216f1831ad | 8 | 0 | Yes |
| suntafretailreplenactivesettingsview | 8 | 0 |  |
| InventSettlementView | 10 | 0 |  |
| VendorNameView | 9 | 0 |  |
| PurchChargeViewPivotTable | 19 | 18 |  |
| suntafretailreplenproductcopyfromview | 11 | 0 |  |
| ProductCategoryHierarchyPivotView | 21 | 0 |  |
| InventSumCurrentView | 26 | 0 |  |
| LocalDateTable_07b72677-2169-4197-b55d-fd526d2cb314 | 8 | 0 | Yes |
| VendorXFDepartmentView | 25 | 10 |  |
| VendorXFFactoryDepartmentView | 27 | 24 |  |
| VendorXFVendorDepartmentView | 28 | 50 |  |
| VendorXFVendorFactoryView | 27 | 24 |  |
| VendorXFItemDetailView | 12 | 0 |  |
| VendorXFDepartmentVendorView | 28 | 24 |  |
| ReceiptCostFreightFactorView | 23 | 26 |  |
| ReportingPeriod | 4 | 0 |  |
| CurrentVendorPurchasePriceView | 11 | 0 |  |
| LocalDateTable_186ce2e6-b4c7-4c7a-ab05-99aa0e062b6c | 8 | 0 | Yes |
| LocalDateTable_de9a3999-eb4d-41c9-9d48-eece6916f9f0 | 8 | 0 | Yes |
| ReceiptYear | 2 | 0 |  |
| InventTransView | 20 | 0 |  |
| PurchLineAggView | 7 | 0 |  |
| InventSumCurrentViewForWHSEnabledItems | 42 | 1 |  |
| LocalDateTable_a6461a22-e031-4fd1-906a-50d7244f8985 | 8 | 0 | Yes |
| LocalDateTable_a562226d-3841-4d5e-92eb-65a8d2c9e2b2 | 8 | 0 | Yes |
| LocalDateTable_3265e62e-c157-4707-ad34-7638663aa1c1 | 8 | 0 | Yes |
| DJR_Receipt_InventoryTransCost | 12 | 0 |  |
| LocalDateTable_487903f4-72ba-41a3-a15c-bcf6acebc9a0 | 8 | 0 | Yes |
| VendInvoiceView | 16 | 0 |  |
| LocalDateTable_415d9453-0230-4171-a34d-89c3f50676b5 | 8 | 0 | Yes |
| LocalDateTable_9d70e007-67fe-4f8a-bfb4-61b9eb24e0d5 | 8 | 0 | Yes |
| LocalDateTable_0b4d1899-0a08-4e2d-ab9d-f0dbaec0bd37 | 8 | 0 | Yes |
| InventJourTransView Missing Keys | 27 | 0 |  |
| DJRInventJournalReportView | 10 | 0 |  |
| RetailSalesTransactionLicensedView | 41 | 0 |  |
| LocalDateTable_1bae8e7a-3d5e-4c3f-819e-2f8ad5c3e95a | 8 | 0 | Yes |
| CycleCountView | 38 | 18 |  |
| LocalDateTable_4464229a-5c0f-4de1-a17e-947afe2fee87 | 8 | 0 | Yes |
| LocalDateTable_6299d0a0-f27c-4e81-868b-e0fabb84918e | 8 | 0 | Yes |
| LocalDateTable_9eb68c62-a1e7-4a42-bdfa-b1edac34f926 | 8 | 0 | Yes |
| LocalDateTable_c01dc564-bdcb-4f2b-8e59-6e5e0ac8d6b2 | 8 | 0 | Yes |

## Measures

### PurchasingTransView.BALANCE ON ORDER RETAIL $

```sql

    COALESCE(SUM('PurchasingTransView'[on order retail]), 0) - 
    COALESCE(SUM('PurchasingTransView'[retail received]), 0)
```

### PurchasingTransView.BALANCE ON ORDER UNITS

```sql

    COALESCE(SUM('PurchasingTransView'[on order units]), 0) - 
    COALESCE(SUM('PurchasingTransView'[units received]), 0)
```

### PurchasingTransView.FOB Royalty Amount

```sql

VAR ChargeAmount = 
    CALCULATE(
        SUM(PurchChargesView[ChargeAmount]),
        KEEPFILTERS(PurchChargesView[MarkupCode] = "FOBROY")
    )
RETURN ChargeAmount
```

### PurchasingTransView.FOB Royalty %

```sql

VAR FOBBOYChargeVaule =
CALCULATE(
    SUM(PurchChargesView[ChargeAmount]),
    KEEPFILTERS(PurchChargesView[MarkupCode] = "FOBROY")
)
VAR SumCost =  SUM(PurchasingTransView[units received]) * SUM(PurchasingTransView[first cost])
RETURN DIVIDE(FOBBOYChargeVaule,SumCost)
```

### PurchasingTransView.On Order Units (Max value)

```sql

IF (
    ISINSCOPE('PurchasingTransView'[Expected Receipt Date]), 
    MAX ( 'PurchasingTransView'[on order units]),
    SUM ( 'PurchasingTransView'[on order units] )
)
```

### PurchasingTransView.(Max Value) On Order Units

```sql

VAR _LineIDs = VALUES ( 'PurchasingTransView'[PurchLine RecID] )
RETURN
CALCULATE (
    SUM ( PurchLineAggView[UnitsPerLine] ),
    KEEPFILTERS ( TREATAS ( _LineIDs, PurchLineAggView[PurchLineRecID] ) )
)

/*
VAR LeafRow =
    ISINSCOPE ( 'PurchasingTransView'[PurchLine RecID] ) &&
    HASONEVALUE ( 'PurchasingTransView'[PurchLine RecID] )
RETURN
IF (
    LeafRow,
    [On Order Units (Per Line)],
    CALCULATE (
        SUM ( PurchLineAggView[UnitsPerLine] ),
        TREATAS (
            VALUES ( 'PurchasingTransView'[PurchLine RecID] ),
            PurchLineAggView[PurchLineRecID]
        )
    )
)
*/
```

### PurchasingTransView.(Max Value) On Order Total Cost

```sql

VAR _LineIDs =
    VALUES ( 'PurchasingTransView'[PurchLine RecID] )
RETURN
CALCULATE (
    SUM ( PurchLineAggView[TotalCostPerLine] ),
    KEEPFILTERS ( TREATAS ( _LineIDs, PurchLineAggView[PurchLineRecID] ) )
)
/*
VAR LeafRow =
    ISINSCOPE ( 'PurchasingTransView'[PurchLine RecID] ) &&
    HASONEVALUE ( 'PurchasingTransView'[PurchLine RecID] )
RETURN
IF (
    LeafRow,
    [On Order Total Cost (Per Line)],
    CALCULATE (
        SUM ( PurchLineAggView[TotalCostPerLine] ),
        TREATAS (
            VALUES ( 'PurchasingTransView'[PurchLine RecID] ),
            PurchLineAggView[PurchLineRecID]
        )
    )
)
IF(
    ISINSCOPE('PurchasingTransView'[PurchLine RecID]),
    MAX('PurchasingTransView'[on order total cost]),
    SUM('PurchasingTransView'[on order total cost])
)
*/
```

### PurchasingTransView.(Max Value) On Order Total Cost w/o Charge

```sql

VAR LeafRow =
    ISINSCOPE ( 'PurchasingTransView'[PurchLine RecID] ) &&
    HASONEVALUE ( 'PurchasingTransView'[PurchLine RecID] )
RETURN
IF (
    LeafRow,
    [On Order Total Cost w/o Charge (Per Line)],
    CALCULATE (
        SUM ( PurchLineAggView[TotalCostNoChargePerLine] ),
        TREATAS (
            VALUES ( 'PurchasingTransView'[PurchLine RecID] ),
            PurchLineAggView[PurchLineRecID]
        )
    )
)
/*
IF(
    ISINSCOPE('PurchasingTransView'[PurchLine RecID]),
    MAX('PurchasingTransView'[on order total cost without chargeAmout]),
    SUM('PurchasingTransView'[on order total cost without chargeAmout])
)
*/
```

### PurchasingTransView.(Max Value) On Order Retail $

```sql

VAR _LineIDs = VALUES ( 'PurchasingTransView'[PurchLine RecID] )
RETURN
CALCULATE (
    SUM ( PurchLineAggView[RetailPerLine] ),
    KEEPFILTERS ( TREATAS ( _LineIDs, PurchLineAggView[PurchLineRecID] ) )
)

/*
VAR LeafRow =
    ISINSCOPE ( 'PurchasingTransView'[PurchLine RecID] ) &&
    HASONEVALUE ( 'PurchasingTransView'[PurchLine RecID] )
RETURN
IF (
    LeafRow,
    [On Order Retail $ (Per Line)],
    CALCULATE (
        SUM ( PurchLineAggView[RetailPerLine] ),
        TREATAS (
            VALUES ( 'PurchasingTransView'[PurchLine RecID] ),
            PurchLineAggView[PurchLineRecID]
        )
    )
)
*/
```

### PurchasingTransView.(Max Value) Balance On Order Units

```sql

VAR Grain =
    SUMMARIZE (
        'PurchasingTransView',
        'PurchasingTransView'[PurchLine RecID]
    )
VAR Result =
    SUMX (
        Grain,
        [(Max Value) On Order Units]
            - CALCULATE ( SUM ( 'PurchasingTransView'[units received] ) )
    )
RETURN
    IF ( Result < 0, 0, Result )

```

### PurchasingTransView.(Max Value) Balance On Order Retail $

```sql

VAR Grain =
    SUMMARIZE(
        'PurchasingTransView',
        'PurchasingTransView'[PurchLine RecID]
    )
RETURN
SUMX(
    Grain,
    [(Max Value) On Order Retail $]
        - CALCULATE( SUM('PurchasingTransView'[retail received]) )
)

```

### PurchasingTransView.Cancel Fiscal Month Year

```sql

VAR FYP = [Cancel FY Period (TREATAS)]
VAR T   = IF( ISBLANK(FYP), BLANK(), FORMAT(FYP, "000000") )
VAR FY  = VALUE( LEFT(T,4) )
VAR FM  = VALUE( RIGHT(T,2) )
VAR CalMonth = IF( FM = 12, 1, FM + 1 )
VAR CalYear  = IF( FM = 12, FY, FY )
RETURN IF( ISBLANK(FYP), BLANK(), FORMAT( DATE(CalYear, CalMonth, 1), "MMM yyyy" ) )
```

### PurchasingTransView.ERD Fiscal Month Year

```sql

VAR FYP = [ERD FY Period (TREATAS)]
VAR T   = IF( ISBLANK(FYP), BLANK(), FORMAT(FYP, "000000") )
VAR FY  = VALUE( LEFT(T,4) )
VAR FM  = VALUE( RIGHT(T,2) )
VAR CalMonth = IF( FM = 12, 1, FM + 1 )
VAR CalYear  = IF( FM = 12, FY, FY )
RETURN IF( ISBLANK(FYP), BLANK(), FORMAT( DATE(CalYear, CalMonth, 1), "MMM yyyy" ) )

```

### PurchasingTransView.Cancel FY Period (TREATAS)

```sql

VAR dTruncTable =
    SELECTCOLUMNS(
        VALUES( PurchasingTransView[Cancel date] ),
        "Actual Date", TRUNC( PurchasingTransView[Cancel date] )
    )
RETURN
CALCULATE(
    SELECTEDVALUE( Date_Dim[FiscalYearPeriod] ),
    TREATAS( dTruncTable, date_dim[actual_date] )
)
```

### PurchasingTransView.ERD FY Period (TREATAS)

```sql

VAR dTruncTable =
    SELECTCOLUMNS(
        VALUES( PurchasingTransView[Expected Receipt date] ),
        "Actual Date", TRUNC( PurchasingTransView[Expected Receipt date] )
    )
RETURN
CALCULATE(
    SELECTEDVALUE( Date_Dim[FiscalYearPeriod] ),
    TREATAS( dTruncTable, date_dim[actual_date] )
)

```

### PurchasingTransView.On Order Units (Per Line)

```sql

MAX ( PurchLineAggView[PurchLineRecID] )
```

### PurchasingTransView.On Order Retail $ (Per Line)

```sql

MAX ( PurchLineAggView[RetailPerLine] )
```

### PurchasingTransView.On Order Total Cost (Per Line)

```sql

MAX ( PurchLineAggView[TotalCostPerLine] )
```

### PurchasingTransView.On Order Total Cost w/o Charge (Per Line)

```sql

MAX ( PurchLineAggView[TotalCostNoChargePerLine] )
```

### PurchasingTransView.VAR _LineIDs

```sql

    VALUES ( 'PurchasingTransView'[PurchLine RecID] )
```

### PurchasingTransView.(Max Value) LineChargeAmount

```sql

VAR _LineIDs = VALUES ( 'PurchasingTransView'[PurchLine RecID] )
RETURN
CALCULATE (
    SUM ( PurchLineAggView[TotalLineChargeAmount] ),
    KEEPFILTERS ( TREATAS ( _LineIDs, PurchLineAggView[PurchLineRecID] ) )
)
```

### PurchasingTransView.Received Cost W/o Charge by Receipt Date

```sql

    CALCULATE(
        SUM ( 'PurchasingTransView'[Receipt cost w/o charges] ),
        USERELATIONSHIP( 'date_dim'[actual_date], 'PurchasingTransView'[Receipt Date] )
    )
```

### PurchasingTransView.Received Cost With adjustment by Receipt Date

```sql

CALCULATE(
    SUM('PurchasingTransView'[Receipt_cost_w_adjustment]), -- <--- Your expression (e.g., SUM, COUNTROWS, etc.)
    USERELATIONSHIP(
        'date_dim'[actual_date],                            -- <--- Column from your Date Table
        'purchasingTransView'[Receipt Date]           -- <--- Column from your Fact Table (the inactive one)
    )
)
```

### product_dim_le.Style Inner Case Pack Qty (Sum, 0)

```sql

COALESCE( SUM(product_dim_le[innerpack]), 0 )
```

### RetailSalesTransactionView.qty sum

```sql

VAR Result = SUM(RetailSalesTransactionView[qty])
RETURN (Result)
```

### RetailSalesTransactionView.PurchasePrice_CurrentVendor

```sql

VAR SelectedItemId =
    SELECTEDVALUE ( RetailSalesTransactionView[product_key])

VAR SelectedFiscalYearPeriod =
    SELECTEDVALUE ( date_dim[FiscalYearPeriod] )

VAR PeriodMinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER (   date_dim , date_dim[FiscalYearPeriod] = SelectedFiscalYearPeriod )
    )
VAR PeriodMaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER (  date_dim , date_dim[FiscalYearPeriod] = SelectedFiscalYearPeriod )
    )

VAR Result =
    CALCULATE (
        SUM ( CurrentVendorPurchasePriceView[PurchasePrice] ),
        FILTER (
            ALL ( CurrentVendorPurchasePriceView ),
            CurrentVendorPurchasePriceView[product_key] = SelectedItemId
            &&  CurrentVendorPurchasePriceView[FromDate] <= PeriodMaxDate
                && CurrentVendorPurchasePriceView[ToDate] >= PeriodMinDate
        )
    )
RETURN
Result
```

### RetailSalesTransactionView.NetSalesUnitsDay

```sql
[qty sum] * -1
```

### PurchChargeViewPivotTable.Chg – Ocean Freight

```sql

SUM ( PurchChargeViewPivotTable[OCEANFRT] )
```

### PurchChargeViewPivotTable.Chg – Duty

```sql

 SUM ( PurchChargeViewPivotTable[DUTY] )
```

### PurchChargeViewPivotTable.Chg – Tariffs

```sql

SUM ( PurchChargeViewPivotTable[TARIFFS] )
```

### PurchChargeViewPivotTable.Chg – Inspection

```sql

SUM ( PurchChargeViewPivotTable[INSPEES] )
```

### PurchChargeViewPivotTable.Chg – FOB Royalty

```sql

SUM ( PurchChargeViewPivotTable[FOBROY] )
```

### PurchChargeViewPivotTable.Chg – Total

```sql

[Chg – Ocean Freight] + [Chg – Duty] + [Chg – Tariffs] + [Chg – Inspection] + [Chg – FOB Royalty]
```

### PurchChargeViewPivotTable.Chg – Ocean Freight (Period)

```sql

VAR TargetYr = [__CurrentYear] + SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
RETURN
CALCULATE (
    [Chg – Ocean Freight],
    REMOVEFILTERS ( PurchChargeViewPivotTable[Receipt Year] ),
    TREATAS ( { TargetYr }, PurchChargeViewPivotTable[Receipt Year] )
)
```

### PurchChargeViewPivotTable.Chg – Duty (Period)

```sql

VAR TargetYr = [__CurrentYear] + SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
RETURN
CALCULATE (
    [Chg – Duty],
    REMOVEFILTERS ( PurchChargeViewPivotTable[Receipt Year] ),
    TREATAS ( { TargetYr }, PurchChargeViewPivotTable[Receipt Year] )
)
```

### PurchChargeViewPivotTable.Chg – Tariffs (Period)

```sql

VAR TargetYr = [__CurrentYear] + SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
RETURN
CALCULATE (
    [Chg – Tariffs],
    REMOVEFILTERS ( PurchChargeViewPivotTable[Receipt Year] ),
    TREATAS ( { TargetYr }, PurchChargeViewPivotTable[Receipt Year] )
)
```

### PurchChargeViewPivotTable.Chg – Inspection (Period)

```sql

VAR TargetYr = [__CurrentYear] + SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
RETURN
CALCULATE (
    [Chg – Inspection],
    REMOVEFILTERS ( PurchChargeViewPivotTable[Receipt Year] ),
    TREATAS ( { TargetYr }, PurchChargeViewPivotTable[Receipt Year] )
)
```

### PurchChargeViewPivotTable.Chg – FOB Royalty (Period)

```sql

VAR TargetYr = [__CurrentYear] + SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
RETURN
CALCULATE (
    [Chg – FOB Royalty],
    REMOVEFILTERS ( PurchChargeViewPivotTable[Receipt Year] ),
    TREATAS ( { TargetYr }, PurchChargeViewPivotTable[Receipt Year] )
)
```

### PurchChargeViewPivotTable.Chg – Total (Period)

```sql

[Chg – Ocean Freight (Period)] +
[Chg – Duty (Period)] +
[Chg – Tariffs (Period)] +
[Chg – Inspection (Period)] +
[Chg – FOB Royalty (Period)]
```

### PurchChargeViewPivotTable.Chg – Total per Unit (Period)

```sql

DIVIDE ( [Chg – Total (Period)], [Total Receipts Units (Period)] )
```

### PurchChargeViewPivotTable.Debug – Offset

```sql

SELECTEDVALUE ( ReportingPeriod[Year Offset] )
```

### PurchChargeViewPivotTable.Debug – Target Year

```sql

[__CurrentYear] + [Debug – Offset]
```

### PurchChargeViewPivotTable.Debug – Distinct Years Seen in Charges

```sql

CALCULATE ( DISTINCTCOUNT ( PurchChargeViewPivotTable[Receipt Year] ) )
```

### PurchChargeViewPivotTable.Chg – All excluding tariffs

```sql

[Chg – Ocean Freight] + [Chg – Duty] + [Chg – Inspection] + [Chg – FOB Royalty]
```

### PurchChargeViewPivotTable.Chg – All excluding tariffs (Period)

```sql

[Chg – Ocean Freight (Period)] +
[Chg – Duty (Period)] +
[Chg – Inspection (Period)] +
[Chg – FOB Royalty (Period)]
```

### VendorXFDepartmentView.QTR1 Units (Dept)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentView[QTR1] ),
    VendorXFDepartmentView[DeptSortKey] <> 0
)
```

### VendorXFDepartmentView.QTR2 Units (Dept)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentView[QTR2] ),
    VendorXFDepartmentView[DeptSortKey] <> 0
)
```

### VendorXFDepartmentView.QTR3 Units (Dept)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentView[QTR3] ),
    VendorXFDepartmentView[DeptSortKey] <> 0
)
```

### VendorXFDepartmentView.QTR4 Units (Dept)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentView[QTR4] ),
    VendorXFDepartmentView[DeptSortKey] <> 0
)
```

### VendorXFDepartmentView.QTR1 % Units (Dept)

```sql

VAR Denominator =
    SWITCH(
        TRUE(),

        /* Leaf level: DepartmentName share of that Year’s Department (Label) total */
        ISINSCOPE( VendorXFDepartmentView[DepartmentName] ),
            CALCULATE(
                [QTR1 Units (Dept)],
                ALLSELECTED( VendorXFDepartmentView[DepartmentName] )
            ),

        /* Year level: each Year share of total across selected Years (within current Department selection) */
        ISINSCOPE( VendorXFDepartmentView[Year] ),
            CALCULATE(
                [QTR1 Units (Dept)],
                ALLSELECTED( VendorXFDepartmentView[Year] )
            ),

        BLANK()
    )
RETURN
DIVIDE( [QTR1 Units (Dept)], Denominator )
```

### VendorXFDepartmentView.QTR2 % Units (Dept)

```sql

VAR Num = [QTR2 Units (Dept)]
VAR Den =
    CALCULATE(
        [QTR2 Units (Dept)],
        ALLSELECTED( VendorXFDepartmentView[DepartmentName] )
    )
RETURN
IF(
    ISINSCOPE( VendorXFDepartmentView[DepartmentName] ),
    DIVIDE( Num, Den ),
    BLANK()
)
```

### VendorXFDepartmentView.QTR3 % Units (Dept)

```sql

VAR Num = [QTR3 Units (Dept)]
VAR Den =
    CALCULATE(
        [QTR3 Units (Dept)],
        ALLSELECTED( VendorXFDepartmentView[DepartmentName] )
    )
RETURN
IF(
    ISINSCOPE( VendorXFDepartmentView[DepartmentName] ),
    DIVIDE( Num, Den ),
    BLANK()
)
```

### VendorXFDepartmentView.QTR4 % Units (Dept)

```sql

VAR Num = [QTR4 Units (Dept)]
VAR Den =
    CALCULATE(
        [QTR4 Units (Dept)],
        ALLSELECTED( VendorXFDepartmentView[DepartmentName] )
    )
RETURN
IF(
    ISINSCOPE( VendorXFDepartmentView[DepartmentName] ),
    DIVIDE( Num, Den ),
    BLANK()
)
```

### VendorXFDepartmentView.QTR1 Units (Dept) - Year Total (Selected)

```sql

CALCULATE(
    [QTR1 Units (Dept)],
    ALLSELECTED( VendorXFDepartmentView[DepartmentLabel] ),
    ALLSELECTED( VendorXFDepartmentView[DepartmentName] )
)
```

### VendorXFDepartmentView.QTR1 Denom (Dept - Selected)

```sql

VAR Base = [QTR1 Units (Dept)]
RETURN
SWITCH(
    TRUE(),

    /* Leaf level: DepartmentName (or Department) % of the Year total */
    ISINSCOPE( VendorXFDepartmentView[DepartmentName] ),
        CALCULATE(
            Base,
            ALLSELECTED(
                VendorXFDepartmentView[DepartmentLabel],
                VendorXFDepartmentView[DepartmentName]
            )
        ),

    /* Year level: each Year % of total across selected Years (within current Dept selection) */
    ISINSCOPE( VendorXFDepartmentView[Year] ),
        CALCULATE(
            Base,
            ALLSELECTED( VendorXFDepartmentView[Year] )
        ),

    BLANK()
)
```

### VendorXFFactoryDepartmentView.FD QTR1 Units (Factory-Dept)

```sql

CALCULATE(
    SUM ( VendorXFFactoryDepartmentView[QTR1] ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFFactoryDepartmentView.FD QTR1 Units (All Factories, Same Year)

```sql

VAR SelectedFactories =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFFactoryDepartmentView[FactoryLabel] ),
        REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] )
    )
RETURN
CALCULATE(
    [FD QTR1 Units (Factory-Dept)],
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedFactories )
)
```

### VendorXFFactoryDepartmentView.FD QTR1 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] ),
    [FD QTR1 Units (All Factories, Same Year)]
)
```

### VendorXFFactoryDepartmentView.FD QTR1 % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFFactoryDepartmentView[DepartmentName] ),
    DIVIDE(
        [FD QTR1 Units (Factory-Dept)],
        [FD QTR1 Units (All Factories, Same Year)]
    )
)
```

### VendorXFFactoryDepartmentView.FD QTR2 Units (Factory-Dept)

```sql

CALCULATE(
    SUM ( VendorXFFactoryDepartmentView[QTR2] ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFFactoryDepartmentView.FD QTR2 Units (All Factories, Same Year)

```sql

VAR SelectedFactories =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFFactoryDepartmentView[FactoryLabel] ),
        REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] )
    )
RETURN
CALCULATE(
    [FD QTR2 Units (Factory-Dept)],
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedFactories )
)
```

### VendorXFFactoryDepartmentView.FD QTR2 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] ),
    [FD QTR2 Units (All Factories, Same Year)]
)
```

### VendorXFFactoryDepartmentView.FD QTR2 % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFFactoryDepartmentView[DepartmentName] ),
    DIVIDE(
        [FD QTR2 Units (Factory-Dept)],
        [FD QTR2 Units (All Factories, Same Year)]
    )
)
```

### VendorXFFactoryDepartmentView.FD QTR3 Units (Factory-Dept)

```sql

CALCULATE(
    SUM ( VendorXFFactoryDepartmentView[QTR3] ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFFactoryDepartmentView.FD QTR3 Units (All Factories, Same Year)

```sql

VAR SelectedFactories =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFFactoryDepartmentView[FactoryLabel] ),
        REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] )
    )
RETURN
CALCULATE(
    [FD QTR3 Units (Factory-Dept)],
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedFactories )
)
```

### VendorXFFactoryDepartmentView.FD QTR3 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] ),
    [FD QTR3 Units (All Factories, Same Year)]
)
```

### VendorXFFactoryDepartmentView.FD QTR3 % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFFactoryDepartmentView[DepartmentName] ),
    DIVIDE(
        [FD QTR3 Units (Factory-Dept)],
        [FD QTR3 Units (All Factories, Same Year)]
    )
)
```

### VendorXFFactoryDepartmentView.FD QTR4 Units (Factory-Dept)

```sql

CALCULATE(
    SUM ( VendorXFFactoryDepartmentView[QTR4] ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFFactoryDepartmentView.FD QTR4 Units (All Factories, Same Year)

```sql

VAR SelectedFactories =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFFactoryDepartmentView[FactoryLabel] ),
        REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] )
    )
RETURN
CALCULATE(
    [FD QTR4 Units (Factory-Dept)],
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedFactories )
)
```

### VendorXFFactoryDepartmentView.FD QTR4 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] ),
    [FD QTR4 Units (All Factories, Same Year)]
)
```

### VendorXFFactoryDepartmentView.FD QTR4 % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFFactoryDepartmentView[DepartmentName] ),
    DIVIDE(
        [FD QTR4 Units (Factory-Dept)],
        [FD QTR4 Units (All Factories, Same Year)]
    )
)
```

### VendorXFFactoryDepartmentView.FD Total Year Units (Factory-Dept)

```sql

CALCULATE(
    SUM ( VendorXFFactoryDepartmentView[Total Year] ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFFactoryDepartmentView.FD Total Year Units (All Factories, Same Year)

```sql

VAR SelectedFactories =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFFactoryDepartmentView[FactoryLabel] ),
        REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] )
    )
RETURN
CALCULATE(
    [FD Total Year Units (Factory-Dept)],
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedFactories )
)
```

### VendorXFFactoryDepartmentView.FD Total Year Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] ),
    [FD Total Year Units (All Factories, Same Year)]
)
```

### VendorXFFactoryDepartmentView.FD Total Year % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFFactoryDepartmentView[DepartmentName] ),
    DIVIDE(
        [FD Total Year Units (Factory-Dept)],
        [FD Total Year Units (All Factories, Same Year)]
    )
)
```

### VendorXFFactoryDepartmentView.FD Total Cost (Factory-Dept)

```sql

CALCULATE(
    SUM ( VendorXFFactoryDepartmentView[Total Cost] ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFFactoryDepartmentView.FD Total Cost (All Factories, Same Year)

```sql

VAR SelectedFactories =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFFactoryDepartmentView[FactoryLabel] ),
        REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] )
    )
RETURN
CALCULATE(
    [FD Total Cost (Factory-Dept)],
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[FactoryLabel] ),
    REMOVEFILTERS ( VendorXFFactoryDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedFactories )
)
```

### VendorXFFactoryDepartmentView.FD Total Cost Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] ),
    [FD Total Cost (All Factories, Same Year)]
)
```

### VendorXFFactoryDepartmentView.FD Total Cost % (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFFactoryDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFFactoryDepartmentView[DepartmentName] ),
    DIVIDE(
        [FD Total Cost (Factory-Dept)],
        [FD Total Cost (All Factories, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.QTR1 Units (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[QTR1] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.QTR1 Units (Vendor-Dept) - Total Vendors (Selected)

```sql

CALCULATE(
    [QTR1 Units (Vendor-Dept)],

    /* Remove the current row vendor */
    REMOVEFILTERS( VendorXFVendorDepartmentView[VendorLabel] ),

    /* Re-apply ONLY what’s selected (Vendor slicer / cross-filters) */
    KEEPFILTERS( ALLSELECTED( VendorXFVendorDepartmentView[VendorLabel] ) )
)
```

### VendorXFVendorDepartmentView.QTR1 % Units

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [QTR1 Units (Vendor-Dept)],
        [QTR1 Units (All Vendors, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.QTR1 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [QTR1 Units (All Vendors, Same Year)]
)
```

### VendorXFVendorDepartmentView.QTR1 Units (All Vendors, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorDepartmentView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] )
    )
RETURN
CALCULATE(
    [QTR1 Units (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] ),
    /* Optional: ensures DeptName doesn’t change the denom if you expand it later */
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorDepartmentView.QTR2 Units (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[QTR2] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.QTR2 Units (Vendor-Dept) - Total Vendors (Selected)

```sql

CALCULATE(
    [QTR2 Units (Vendor-Dept)],

    /* Remove the current row vendor */
    REMOVEFILTERS( VendorXFVendorDepartmentView[VendorLabel] ),

    /* Re-apply ONLY what’s selected (Vendor slicer / cross-filters) */
    KEEPFILTERS( ALLSELECTED( VendorXFVendorDepartmentView[VendorLabel] ) )
)
```

### VendorXFVendorDepartmentView.QTR2 Units (All Vendors, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorDepartmentView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] )
    )
RETURN
CALCULATE(
    [QTR2 Units (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] ),
    /* Optional: ensures DeptName doesn’t change the denom if you expand it later */
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorDepartmentView.QTR2 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [QTR2 Units (All Vendors, Same Year)]
)
```

### VendorXFVendorDepartmentView.QTR2 % Units

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [QTR2 Units (Vendor-Dept)],
        [QTR2 Units (All Vendors, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.QTR3 Units (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[QTR3] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.QTR3 Units (Vendor-Dept) - Total Vendors (Selected)

```sql

CALCULATE(
    [QTR3 Units (Vendor-Dept)],

    /* Remove the current row vendor */
    REMOVEFILTERS( VendorXFVendorDepartmentView[VendorLabel] ),

    /* Re-apply ONLY what’s selected (Vendor slicer / cross-filters) */
    KEEPFILTERS( ALLSELECTED( VendorXFVendorDepartmentView[VendorLabel] ) )
)
```

### VendorXFVendorDepartmentView.QTR3 Units (All Vendors, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorDepartmentView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] )
    )
RETURN
CALCULATE(
    [QTR3 Units (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] ),
    /* Optional: ensures DeptName doesn’t change the denom if you expand it later */
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorDepartmentView.QTR3 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [QTR3 Units (All Vendors, Same Year)]
)
```

### VendorXFVendorDepartmentView.QTR3 % Units

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [QTR3 Units (Vendor-Dept)],
        [QTR3 Units (All Vendors, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.QTR4 Units (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[QTR4] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.QTR4 Units (Vendor-Dept) - Total Vendors (Selected)

```sql

CALCULATE(
    [QTR4 Units (Vendor-Dept)],

    /* Remove the current row vendor */
    REMOVEFILTERS( VendorXFVendorDepartmentView[VendorLabel] ),

    /* Re-apply ONLY what’s selected (Vendor slicer / cross-filters) */
    KEEPFILTERS( ALLSELECTED( VendorXFVendorDepartmentView[VendorLabel] ) )
)
```

### VendorXFVendorDepartmentView.QTR4 Units (All Vendors, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorDepartmentView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] )
    )
RETURN
CALCULATE(
    [QTR4 Units (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] ),
    /* Optional: ensures DeptName doesn’t change the denom if you expand it later */
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorDepartmentView.QTR4 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [QTR4 Units (All Vendors, Same Year)]
)
```

### VendorXFVendorDepartmentView.QTR4 % Units

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [QTR4 Units (Vendor-Dept)],
        [QTR4 Units (All Vendors, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.VD Total Year Units (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[Total Year] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.VD Total Year Units (All Vendors, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorDepartmentView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] )
    )
RETURN
CALCULATE(
    [VD Total Year Units (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorDepartmentView.VD Total Year Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [VD Total Year Units (All Vendors, Same Year)]
)
```

### VendorXFVendorDepartmentView.VD Total Year % Units (Vendor Share)

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [VD Total Year Units (Vendor-Dept)],
        [VD Total Year Units (All Vendors, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.VD Total Cost (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[Total Cost] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.VD Total Cost (All Vendors, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorDepartmentView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] )
    )
RETURN
CALCULATE(
    [VD Total Cost (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[VendorLabel] ),
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorDepartmentView.VD Total Cost Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [VD Total Cost (All Vendors, Same Year)]
)
```

### VendorXFVendorDepartmentView.VD Total Cost % (Vendor Share)

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [VD Total Cost (Vendor-Dept)],
        [VD Total Cost (All Vendors, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.VD QTR1 Units (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[QTR1] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.VD QTR1 Units (Vendor Total, Same Year)

```sql

CALCULATE(
    [VD QTR1 Units (Vendor-Dept)],
    /* remove dept context so denom = vendor total across all depts */
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentLabel] ),
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] )
)
```

### VendorXFVendorDepartmentView.VD QTR1 Vendor Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [VD QTR1 Units (Vendor Total, Same Year)]
)
```

### VendorXFVendorDepartmentView.VD QTR1 % Units (Dept Share of Vendor)

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [VD QTR1 Units (Vendor-Dept)],
        [VD QTR1 Units (Vendor Total, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.VD QTR2 Units (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[QTR2] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.VD QTR2 Units (Vendor Total, Same Year)

```sql

CALCULATE(
    [VD QTR2 Units (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentLabel] ),
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] )
)
```

### VendorXFVendorDepartmentView.VD QTR2 Vendor Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [VD QTR2 Units (Vendor Total, Same Year)]
)
```

### VendorXFVendorDepartmentView.VD QTR2 % Units (Dept Share of Vendor)

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [VD QTR2 Units (Vendor-Dept)],
        [VD QTR2 Units (Vendor Total, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.VD QTR3 Units (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[QTR3] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.VD QTR3 Units (Vendor Total, Same Year)

```sql

CALCULATE(
    [VD QTR3 Units (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentLabel] ),
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] )
)
```

### VendorXFVendorDepartmentView.VD QTR3 Vendor Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [VD QTR3 Units (Vendor Total, Same Year)]
)
```

### VendorXFVendorDepartmentView.VD QTR3 % Units (Dept Share of Vendor)

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [VD QTR3 Units (Vendor-Dept)],
        [VD QTR3 Units (Vendor Total, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.VD QTR4 Units (Vendor-Dept)

```sql

CALCULATE(
    SUM ( VendorXFVendorDepartmentView[QTR4] ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorDepartmentView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFVendorDepartmentView.VD QTR4 Units (Vendor Total, Same Year)

```sql

CALCULATE(
    [VD QTR4 Units (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentLabel] ),
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] )
)
```

### VendorXFVendorDepartmentView.VD QTR4 Vendor Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [VD QTR4 Units (Vendor Total, Same Year)]
)
```

### VendorXFVendorDepartmentView.VD QTR4 % Units (Dept Share of Vendor)

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [VD QTR4 Units (Vendor-Dept)],
        [VD QTR4 Units (Vendor Total, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.VD Total Year Units (Vendor Total, Same Year)

```sql

CALCULATE(
    [VD Total Year Units (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentLabel] ),
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] )
)
```

### VendorXFVendorDepartmentView.VD Total Year Vendor Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [VD Total Year Units (Vendor Total, Same Year)]
)
```

### VendorXFVendorDepartmentView.VD Total Year % Units (Dept Share of Vendor)

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [VD Total Year Units (Vendor-Dept)],
        [VD Total Year Units (Vendor Total, Same Year)]
    )
)
```

### VendorXFVendorDepartmentView.VD Total Cost (Vendor Total, Same Year)

```sql

CALCULATE(
    [VD Total Cost (Vendor-Dept)],
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentLabel] ),
    REMOVEFILTERS ( VendorXFVendorDepartmentView[DepartmentName] )
)
```

### VendorXFVendorDepartmentView.VD Total Cost Vendor Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] ),
    [VD Total Cost (Vendor Total, Same Year)]
)
```

### VendorXFVendorDepartmentView.VD Total Cost % (Dept Share of Vendor)

```sql

IF(
    ISINSCOPE ( VendorXFVendorDepartmentView[Year] )
        && NOT ISINSCOPE ( VendorXFVendorDepartmentView[DepartmentName] ),
    DIVIDE(
        [VD Total Cost (Vendor-Dept)],
        [VD Total Cost (Vendor Total, Same Year)]
    )
)
```

### VendorXFVendorFactoryView.VF QTR1 Units (Vendor-Factory)

```sql

CALCULATE(
    SUM ( VendorXFVendorFactoryView[QTR1] ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "All Vendors" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFVendorFactoryView.VF QTR1 Units (All Factories, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorFactoryView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorFactoryView[VendorLabel] )
    )
RETURN
CALCULATE(
    [VF QTR1 Units (Vendor-Factory)],
    /* remove factory row context so denom is Vendor+Year total */
    REMOVEFILTERS ( VendorXFVendorFactoryView[FactoryLabel] ),
    /* keep denom stable at Year level */
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorFactoryView.VF QTR1 Factory Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    [VF QTR1 Units (All Factories, Same Year)]
)
```

### VendorXFVendorFactoryView.VF QTR1 % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    DIVIDE(
        [VF QTR1 Units (Vendor-Factory)],
        [VF QTR1 Units (All Factories, Same Year)]
    )
)
```

### VendorXFVendorFactoryView.VF QTR2 Units (Vendor-Factory)

```sql

CALCULATE(
    SUM ( VendorXFVendorFactoryView[QTR2] ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "All Vendors" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFVendorFactoryView.VF QTR2 Units (All Factories, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorFactoryView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorFactoryView[VendorLabel] )
    )
RETURN
CALCULATE(
    [VF QTR2 Units (Vendor-Factory)],
    /* remove factory row context so denom is Vendor+Year total */
    REMOVEFILTERS ( VendorXFVendorFactoryView[FactoryLabel] ),
    /* keep denom stable at Year level */
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorFactoryView.VF QTR2 Factory Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    [VF QTR2 Units (All Factories, Same Year)]
)
```

### VendorXFVendorFactoryView.VF QTR2 % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    DIVIDE(
        [VF QTR2 Units (Vendor-Factory)],
        [VF QTR2 Units (All Factories, Same Year)]
    )
)
```

### VendorXFVendorFactoryView.VF QTR3 Units (Vendor-Factory)

```sql

CALCULATE(
    SUM ( VendorXFVendorFactoryView[QTR3] ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "All Vendors" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFVendorFactoryView.VF QTR3 Units (All Factories, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorFactoryView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorFactoryView[VendorLabel] )
    )
RETURN
CALCULATE(
    [VF QTR3 Units (Vendor-Factory)],
    /* remove factory row context so denom is Vendor+Year total */
    REMOVEFILTERS ( VendorXFVendorFactoryView[FactoryLabel] ),
    /* keep denom stable at Year level */
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorFactoryView.VF QTR3 Factory Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    [VF QTR3 Units (All Factories, Same Year)]
)
```

### VendorXFVendorFactoryView.VF QTR3 % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    DIVIDE(
        [VF QTR3 Units (Vendor-Factory)],
        [VF QTR3 Units (All Factories, Same Year)]
    )
)
```

### VendorXFVendorFactoryView.VF QTR4 Units (Vendor-Factory)

```sql

CALCULATE(
    SUM ( VendorXFVendorFactoryView[QTR4] ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "All Vendors" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFVendorFactoryView.VF QTR4 Units (All Factories, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorFactoryView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorFactoryView[VendorLabel] )
    )
RETURN
CALCULATE(
    [VF QTR4 Units (Vendor-Factory)],
    /* remove factory row context so denom is Vendor+Year total */
    REMOVEFILTERS ( VendorXFVendorFactoryView[FactoryLabel] ),
    /* keep denom stable at Year level */
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorFactoryView.VF QTR4 Factory Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    [VF QTR4 Units (All Factories, Same Year)]
)
```

### VendorXFVendorFactoryView.VF QTR4 % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    DIVIDE(
        [VF QTR4 Units (Vendor-Factory)],
        [VF QTR4 Units (All Factories, Same Year)]
    )
)
```

### VendorXFVendorFactoryView.VF Total Year Units (Vendor-Factory)

```sql

CALCULATE(
    SUM ( VendorXFVendorFactoryView[Total Year] ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "All Vendors" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFVendorFactoryView.VF Total Year Units (All Factories, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorFactoryView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorFactoryView[VendorLabel] )
    )
RETURN
CALCULATE(
    [VF Total Year Units (Vendor-Factory)],
    /* Remove the current row factory so denom becomes Vendor+Year total */
    REMOVEFILTERS ( VendorXFVendorFactoryView[FactoryLabel] ),
    /* Respect vendor slicer / selections */
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorFactoryView.VF Total Year Factory Total

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    [VF Total Year Units (All Factories, Same Year)]
)
```

### VendorXFVendorFactoryView.VF Total Year % Units (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    DIVIDE(
        [VF Total Year Units (Vendor-Factory)],
        [VF Total Year Units (All Factories, Same Year)]
    )
)
```

### VendorXFVendorFactoryView.VF Total Cost (Vendor-Factory)

```sql

CALCULATE(
    SUM ( VendorXFVendorFactoryView[Total Cost] ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[VendorLabel] <> "All Vendors" ),
    KEEPFILTERS ( VendorXFVendorFactoryView[FactoryLabel] <> "All Factories" )
)
```

### VendorXFVendorFactoryView.VF Total Cost (All Factories, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFVendorFactoryView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFVendorFactoryView[VendorLabel] )
    )
RETURN
CALCULATE(
    [VF Total Cost (Vendor-Factory)],
    /* Remove current row factory => Vendor+Year total cost */
    REMOVEFILTERS ( VendorXFVendorFactoryView[FactoryLabel] ),
    /* Respect vendor slicer / cross-filters */
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFVendorFactoryView.VF Total Cost (Vendor-Year Total)

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    [VF Total Cost (All Factories, Same Year)]
)
```

### VendorXFVendorFactoryView.VF Total Cost % (Factory Share)

```sql

IF(
    ISINSCOPE ( VendorXFVendorFactoryView[Year] ),
    DIVIDE(
        [VF Total Cost (Vendor-Factory)],
        [VF Total Cost (All Factories, Same Year)]
    )
)
```

### VendorXFDepartmentVendorView.DV QTR1 Units (Vendor)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentVendorView[QTR1] ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFDepartmentVendorView.DV QTR1 Units (Dept Total, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFDepartmentVendorView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] )
    )
RETURN
CALCULATE(
    [DV QTR1 Units (Vendor)],
    REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFDepartmentVendorView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFDepartmentVendorView.DV QTR1 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] ),
    [DV QTR1 Units (Dept Total, Same Year)]
)
```

### VendorXFDepartmentVendorView.DV QTR1 % Units (Vendor Share)

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] )
        && NOT ISINSCOPE ( VendorXFDepartmentVendorView[DepartmentName] ),
    DIVIDE(
        [DV QTR1 Units (Vendor)],
        [DV QTR1 Units (Dept Total, Same Year)]
    )
)
```

### VendorXFDepartmentVendorView.DV QTR2 Units (Vendor)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentVendorView[QTR2] ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFDepartmentVendorView.DV QTR2 Units (Dept Total, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFDepartmentVendorView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] )
    )
RETURN
CALCULATE(
    [DV QTR2 Units (Vendor)],
    REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFDepartmentVendorView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFDepartmentVendorView.DV QTR2 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] ),
    [DV QTR2 Units (Dept Total, Same Year)]
)
```

### VendorXFDepartmentVendorView.DV QTR2 % Units (Vendor Share)

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] )
        && NOT ISINSCOPE ( VendorXFDepartmentVendorView[DepartmentName] ),
    DIVIDE(
        [DV QTR2 Units (Vendor)],
        [DV QTR2 Units (Dept Total, Same Year)]
    )
)
```

### VendorXFDepartmentVendorView.DV QTR3 Units (Vendor)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentVendorView[QTR3] ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFDepartmentVendorView.DV QTR3 Units (Dept Total, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFDepartmentVendorView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] )
    )
RETURN
CALCULATE(
    [DV QTR3 Units (Vendor)],
    REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFDepartmentVendorView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFDepartmentVendorView.DV QTR3 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] ),
    [DV QTR3 Units (Dept Total, Same Year)]
)
```

### VendorXFDepartmentVendorView.DV QTR3 % Units (Vendor Share)

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] )
        && NOT ISINSCOPE ( VendorXFDepartmentVendorView[DepartmentName] ),
    DIVIDE(
        [DV QTR3 Units (Vendor)],
        [DV QTR3 Units (Dept Total, Same Year)]
    )
)
```

### VendorXFDepartmentVendorView.DV QTR4 Units (Vendor)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentVendorView[QTR4] ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFDepartmentVendorView.DV QTR4 Units (Dept Total, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFDepartmentVendorView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] )
    )
RETURN
CALCULATE(
    [DV QTR4 Units (Vendor)],
    REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFDepartmentVendorView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFDepartmentVendorView.DV QTR4 Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] ),
    [DV QTR4 Units (Dept Total, Same Year)]
)
```

### VendorXFDepartmentVendorView.DV QTR4 % Units (Vendor Share)

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] )
        && NOT ISINSCOPE ( VendorXFDepartmentVendorView[DepartmentName] ),
    DIVIDE(
        [DV QTR4 Units (Vendor)],
        [DV QTR4 Units (Dept Total, Same Year)]
    )
)
```

### VendorXFDepartmentVendorView.DV Total Year Units (Vendor)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentVendorView[Total Year] ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFDepartmentVendorView.DV Total Year Units (Dept Total, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFDepartmentVendorView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] )
    )
RETURN
CALCULATE(
    [DV Total Year Units (Vendor)],
    REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] ),
    /* keep denom stable if DepartmentName is expanded */
    REMOVEFILTERS ( VendorXFDepartmentVendorView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFDepartmentVendorView.DV Total Year Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] ),
    [DV Total Year Units (Dept Total, Same Year)]
)
```

### VendorXFDepartmentVendorView.DV Total Year % Units (Vendor Share)

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] )
        && NOT ISINSCOPE ( VendorXFDepartmentVendorView[DepartmentName] ),
    DIVIDE(
        [DV Total Year Units (Vendor)],
        [DV Total Year Units (Dept Total, Same Year)]
    )
)
```

### VendorXFDepartmentVendorView.DV Total Cost (Vendor)

```sql

CALCULATE(
    SUM ( VendorXFDepartmentVendorView[Total Cost] ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "Total" ),
    KEEPFILTERS ( VendorXFDepartmentVendorView[VendorLabel] <> "All Vendors" )
)
```

### VendorXFDepartmentVendorView.DV Total Cost (Dept Total, Same Year)

```sql

VAR SelectedVendors =
    CALCULATETABLE(
        ALLSELECTED ( VendorXFDepartmentVendorView[VendorLabel] ),
        REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] )
    )
RETURN
CALCULATE(
    [DV Total Cost (Vendor)],
    REMOVEFILTERS ( VendorXFDepartmentVendorView[VendorLabel] ),
    REMOVEFILTERS ( VendorXFDepartmentVendorView[DepartmentName] ),
    KEEPFILTERS ( SelectedVendors )
)
```

### VendorXFDepartmentVendorView.DV Total Cost Dept Total

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] ),
    [DV Total Cost (Dept Total, Same Year)]
)
```

### VendorXFDepartmentVendorView.DV Total Cost % (Vendor Share)

```sql

IF(
    ISINSCOPE ( VendorXFDepartmentVendorView[Year] )
        && NOT ISINSCOPE ( VendorXFDepartmentVendorView[DepartmentName] ),
    DIVIDE(
        [DV Total Cost (Vendor)],
        [DV Total Cost (Dept Total, Same Year)]
    )
)
```

### ReceiptCostFreightFactorView.Receipts Units

```sql

SUM ( ReceiptCostFreightFactorView[Net Receipts Units] )
```

### ReceiptCostFreightFactorView.Receipts Retail TE $

```sql

SUM ( ReceiptCostFreightFactorView[Net Receipts Retail TE] )
```

### ReceiptCostFreightFactorView.Net Receipt Cost (Measure)

```sql

SUM ( ReceiptCostFreightFactorView[Net Receipt Cost] )
```

### ReceiptCostFreightFactorView.Cost Factors Total Cost (Measure)

```sql

SUM ( ReceiptCostFreightFactorView[Cost Factors Total Cost] )
```

### ReceiptCostFreightFactorView.Cost (Incl Factors)

```sql

[Net Receipt Cost (Measure)] + [Cost Factors Total Cost (Measure)]
```

### ReceiptCostFreightFactorView.Cost (Excl Factors)

```sql

[Net Receipt Cost (Measure)]
```

### ReceiptCostFreightFactorView.__CurrentYear

```sql

var CurrYear = LOOKUPVALUE(
    'Date_dim'[fiscal_year],        -- Column to return
    'Date_dim'[actual_date],        -- Search column
    TODAY()        -- Match value
)
RETURN
CurrYear

/*
YEAR ( TODAY() )
*/

```

### ReceiptCostFreightFactorView.__YTD End (Latest Loaded Date in Current Year)

```sql

VAR CurrYr = [__CurrentYear]
-- Prefer to derive from the FACT date if you have it:
VAR EndFromFact =
    CALCULATE (
        MAX ( ReceiptCostFreightFactorView[Receipt Fiscal Year] ),
        FILTER (
            ALL ( ReceiptCostFreightFactorView[Receipt Fiscal Year] ),
            YEAR ( ReceiptCostFreightFactorView[Receipt Fiscal Year] ) = CurrYr
        )
    )
-- Fallback: if you don't have a fact date, use calendar max within current year:
--VAR EndFromCalendar =
--    CALCULATE (
--        MAX ( 'Calendar'[Date] ),
--        FILTER ( ALL ( 'Calendar' ), 'Calendar'[Year] = CurrYr )
--    )
RETURN
--COALESCE ( EndFromFact, EndFromCalendar )
EndFromFact
```

### ReceiptCostFreightFactorView.__Period Start

```sql

VAR CurrYr   = [__CurrentYear]
VAR Offset   = SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
VAR TargetYr = CurrYr + Offset
RETURN
DATE ( TargetYr, 1, 1 )
```

### ReceiptCostFreightFactorView.__Period End

```sql

VAR CurrYr   = [__CurrentYear]
VAR Offset   = SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
VAR TargetYr = CurrYr + Offset
RETURN
IF ( Offset = 0, [__YTD End (Latest Loaded Date in Current Year)], DATE ( TargetYr, 12, 31 ) )
```

### ReceiptCostFreightFactorView.Receipts Units (Period)

```sql

VAR CurrYr   = [__CurrentYear]      -- or [__AnchorYear (Prefer Current, else Latest in Data)]
VAR Offset   = SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
VAR TargetYr = CurrYr + Offset
RETURN
CALCULATE (
    [Receipts Units],
    REMOVEFILTERS ( ReceiptCostFreightFactorView[Receipt Fiscal Year] ),
    KEEPFILTERS ( ReceiptCostFreightFactorView[Receipt Fiscal Year] = TargetYr )
)
```

### ReceiptCostFreightFactorView.Receipts Retail TE $ (Period)

```sql

VAR CurrYr   = [__CurrentYear]
VAR Offset   = SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
VAR TargetYr = CurrYr + Offset
RETURN
CALCULATE (
    [Receipts Retail TE $],
    REMOVEFILTERS ( ReceiptCostFreightFactorView[Receipt Fiscal Year] ),
    KEEPFILTERS ( ReceiptCostFreightFactorView[Receipt Fiscal Year] = TargetYr )
)
```

### ReceiptCostFreightFactorView.Net Receipt Cost (Period)

```sql

VAR CurrYr   = [__CurrentYear]
VAR Offset   = SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
VAR TargetYr = CurrYr + Offset
RETURN
CALCULATE (
    [Net Receipt Cost (Measure)],
    REMOVEFILTERS ( ReceiptCostFreightFactorView[Receipt Fiscal Year] ),
    KEEPFILTERS ( ReceiptCostFreightFactorView[Receipt Fiscal Year] = TargetYr )
)
```

### ReceiptCostFreightFactorView.Cost Factors Total Cost (Period)

```sql

VAR CurrYr   = [__CurrentYear]
VAR Offset   = SELECTEDVALUE ( ReportingPeriod[Year Offset], 0 )
VAR TargetYr = CurrYr + Offset
RETURN
CALCULATE (
    [Cost Factors Total Cost (Measure)],
    REMOVEFILTERS ( ReceiptCostFreightFactorView[Receipt Fiscal Year] ),
    KEEPFILTERS ( ReceiptCostFreightFactorView[Receipt Fiscal Year] = TargetYr )
)
```

### ReceiptCostFreightFactorView.Total Receipts Units (Period)

```sql

[Receipts Units (Period)]
```

### ReceiptCostFreightFactorView.Total Receipts Retail TE $ (Period)

```sql
[Receipts Retail TE $ (Period)] 
```

### ReceiptCostFreightFactorView.Total Cost Factors (Period)

```sql
[Cost Factors Total Cost (Period)]
```

### ReceiptCostFreightFactorView.Total Receipts Cost Incl Factors (Period)

```sql

[Net Receipt Cost (Period)]
/*
[Net Receipt Cost (Period)] + [Cost Factors Total Cost (Period)]
*/
```

### ReceiptCostFreightFactorView.Receipts Cost Excl Factors (Period)

```sql

[Net Receipt Cost (Period)] - [Cost Factors Total Cost (Period)]

/*
[Net Receipt Cost (Period)]
*/
```

### ReceiptCostFreightFactorView.Avg Unit Receipt Cost (Incl Factors) (Period)

```sql

DIVIDE ( [Total Receipts Cost Incl Factors (Period)], [Total Receipts Units (Period)], 0 )
```

### ReceiptCostFreightFactorView.Avg Unit Receipt Cost (Excl Factors) (Period)

```sql

DIVIDE ( [Receipts Cost Excl Factors (Period)], [Total Receipts Units (Period)], 0 )
```

### ReceiptCostFreightFactorView.Margin $ (Incl Factors) (Period)

```sql

[Total Receipts Retail TE $ (Period)] - [Total Receipts Cost Incl Factors (Period)]
```

### ReceiptCostFreightFactorView.Margin % (Incl Factors) (Period)

```sql

DIVIDE ( [Margin $ (Incl Factors) (Period)], [Total Receipts Retail TE $ (Period)], 0 )
```

### ReceiptCostFreightFactorView.Margin $ (Excl Factors) (Period)

```sql

[Total Receipts Retail TE $ (Period)] - [Receipts Cost Excl Factors (Period)]
```

### ReceiptCostFreightFactorView.Margin % (Excl Factors) (Period)

```sql

DIVIDE ( [Margin $ (Excl Factors) (Period)], [Total Receipts Retail TE $ (Period)], 0 )
```

### ReceiptCostFreightFactorView.Cost Factors % (Period)

```sql
DIVIDE([Total Cost Factors (Period)] , [Receipts Cost Excl Factors (Period)], 0)
```

### InventSumCurrentViewForWHSEnabledItems.in-transit_units_AVAIL

```sql

CALCULATE(
	SUM('InventSumCurrentViewForWHSEnabledItems'[intransit_units]),
	'InventSumCurrentViewForWHSEnabledItems'[inventstatusid]
		IN { "AVAIL" }
)
```

### CycleCountView.Units Adjusted (Detail)

```sql

IF(
    SELECTEDVALUE(CycleCountView[AcceptReject]) = "Reject",
    BLANK(),
    CALCULATE(
        SUM(CycleCountView[AdjustmentQty]),
        CycleCountView[AcceptReject] = "Accept"
    )
)
```

### CycleCountView.Units Adjusted (Total)

```sql

IF(
    SELECTEDVALUE(CycleCountView[AcceptReject]) = "Reject",
    BLANK(),
    CALCULATE(
        SUMX(CycleCountView, ABS(CycleCountView[AdjustmentQty])),
        CycleCountView[AcceptReject] = "Accept"
    )
)
```

### CycleCountView.Cost Adjusted (Detail)

```sql

IF(
    SELECTEDVALUE(CycleCountView[AcceptReject]) = "Reject",
    BLANK(),
    CALCULATE(
        SUM(CycleCountView[CostAdjusted]),
        CycleCountView[AcceptReject] = "Accept"
    )
)
```

### CycleCountView.Cost Adjusted (Total)

```sql

IF(
    SELECTEDVALUE(CycleCountView[AcceptReject]) = "Reject",
    BLANK(),
    CALCULATE(
        SUMX(CycleCountView, ABS(CycleCountView[CostAdjusted])),
        CycleCountView[AcceptReject] = "Accept"
    )
)
```

### CycleCountView.Count of Adjustments

```sql

COUNTROWS(CycleCountView)
```

### CycleCountView.Unique Stores

```sql

DISTINCTCOUNT(CycleCountView[InventLocationId])
```

### CycleCountView.Unique Items

```sql

DISTINCTCOUNT(CycleCountView[ItemId])
```

### CycleCountView.Acceptance Rate

```sql

DIVIDE(
    CALCULATE(
        COUNTROWS(CycleCountView),
        CycleCountView[AcceptReject] = "Accept",
        ALL(CycleCountView[AcceptReject])
    ),
    CALCULATE(
        COUNTROWS(CycleCountView),
        ALL(CycleCountView[AcceptReject])
    )
)
```

### CycleCountView.Auto Approval Rate

```sql

DIVIDE(
    CALCULATE(
        COUNTROWS(CycleCountView),
        CycleCountView[ApprovalType] = "Auto Approved",
        ALL(CycleCountView[ApprovalType])
    ),
    CALCULATE(
        COUNTROWS(CycleCountView),
        ALL(CycleCountView[ApprovalType])
    )
)
```

### CycleCountView.Units Variance Identified (Detail)

```sql

SUM(CycleCountView[AdjustmentQty])
```

### CycleCountView.Units Variance Identified (Total)

```sql

SUMX(CycleCountView, ABS(CycleCountView[AdjustmentQty]))
```

### CycleCountView.Cost Variance Identified (Detail)

```sql

SUM(CycleCountView[CostAdjusted])
```

### CycleCountView.Cost Variance Identified (Total)

```sql

SUMX(CycleCountView, ABS(CycleCountView[CostAdjusted]))
```

### CycleCountView.Rejection Rate

```sql

DIVIDE(
    CALCULATE(
        COUNTROWS(CycleCountView),
        CycleCountView[AcceptReject] = "Reject",
        ALL(CycleCountView[AcceptReject])
    ),
    CALCULATE(
        COUNTROWS(CycleCountView),
        ALL(CycleCountView[AcceptReject])
    )
)
```

### CycleCountView.Avg Days to Approval

```sql

AVERAGEX(
    CycleCountView,
    DATEDIFF(CycleCountView[DateOfCount], CycleCountView[ApprovalDate], DAY)
)
```

### CycleCountView.Cost per Unit Adjusted

```sql

DIVIDE([Cost Adjusted (Detail)], [Units Adjusted (Detail)])
```

### CycleCountView.% of Adjustments > $100

```sql

DIVIDE(
    CALCULATE(
        COUNTROWS(CycleCountView),
        ABS(CycleCountView[CostAdjusted]) > 100
    ),
    COUNTROWS(CycleCountView)
)
```

### CycleCountView.Approval Rate

```sql

VAR CurrentRows = COUNTROWS(CycleCountView)
VAR TotalRows = 
    CALCULATE(
        COUNTROWS(CycleCountView),
        ALL(CycleCountView[AcceptReject])
    )
VAR AcceptanceRate = 
    DIVIDE(
        CALCULATE(
            COUNTROWS(CycleCountView),
            CycleCountView[AcceptReject] = "Accept"
        ),
        TotalRows
    )
VAR RejectionRate = 
    DIVIDE(
        CALCULATE(
            COUNTROWS(CycleCountView),
            CycleCountView[AcceptReject] = "Reject"
        ),
        TotalRows
    )
VAR SelectedStatus = SELECTEDVALUE(CycleCountView[AcceptReject])
RETURN
    IF(
        CurrentRows = 0,
        BLANK(),
        SWITCH(
            TRUE(),
            SelectedStatus = "Reject", RejectionRate,
            SelectedStatus = "Accept", AcceptanceRate,
            1
        )
    )
/*
VAR AcceptanceRate = 
    DIVIDE(
        CALCULATE(
            COUNTROWS(CycleCountView),
            CycleCountView[AcceptReject] = "Accept",
            ALL(CycleCountView[AcceptReject])
        ),
        CALCULATE(
            COUNTROWS(CycleCountView),
            ALL(CycleCountView[AcceptReject])
        )
    )
VAR RejectionRate = 1 - AcceptanceRate
VAR SelectedStatus = SELECTEDVALUE(CycleCountView[AcceptReject])
RETURN
    IF(
        SelectedStatus = "Reject",
        RejectionRate,
        AcceptanceRate
    )
*/
```

## Power Query Source (per table)

### DateTableTemplate_bd621608-5813-48a2-9dfc-9f7f8eb0b93c

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### PurchasingTransView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_PurchasingTransView = Source{[Schema="dbo",Item="PurchasingTransView"]}[Data]
in
    dbo_PurchasingTransView
```

### LocalDateTable_573bd59f-30e3-4724-a9dc-d049d5bd88ff

```sql
Calendar(Date(Year(MIN('PurchasingTransView'[Ship date])), 1, 1), Date(Year(MAX('PurchasingTransView'[Ship date])), 12, 31))
```

### d365LocationMapping_View

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_d365LocationMapping_View = Source{[Schema="dbo",Item="d365LocationMapping_View"]}[Data]
in
    dbo_d365LocationMapping_View
```

### InventJourTransView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_InventJourTransView = Source{[Schema="dbo",Item="InventJourTransView"]}[Data]
in
    dbo_InventJourTransView
```

### PurchChargesView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_PurchChargesView = Source{[Schema="dbo",Item="PurchChargesView"]}[Data]
in
    dbo_PurchChargesView
```

### LocalDateTable_aacd14c4-d89f-4cb0-85ad-9f533fe79b60

```sql
Calendar(Date(Year(MIN('PurchasingTransView'[createddatetime])), 1, 1), Date(Year(MAX('PurchasingTransView'[createddatetime])), 12, 31))
```

### product_dim_le

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_product_dim_le = Source{[Schema="dbo",Item="product_dim_le"]}[Data],
    #"Added Custom Column" = Table.AddColumn(dbo_product_dim_le, "department-level", each let splitdepartment = Splitter.SplitTextByDelimiter("-", QuoteStyle.None)([department]), splitsplitdepartment0 = Splitter.SplitTextByDelimiter(" (", QuoteStyle.None)(splitdepartment{0}?) in Text.Combine(splitsplitdepartment0, " - "), type text)
in
    #"Added Custom Column"
```

### LocalDateTable_cf03c37c-1de9-4a30-acc0-a765861f7251

```sql
Calendar(Date(Year(MIN('product_dim_le'[activation_date])), 1, 1), Date(Year(MAX('product_dim_le'[activation_date])), 12, 31))
```

### ProductDim_attribute

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_ProductDim_attribute = Source{[Schema="dbo",Item="ProductDim_attribute"]}[Data]
in
    dbo_ProductDim_attribute
```

### date_dim

```sql
let
    Source = Sql.Database(ServerName, "LH_Mart"),
    dbo_date_dim = Source{[Schema="dbo",Item="date_dim"]}[Data],
    #"Removed Blank Rows" = Table.SelectRows(dbo_date_dim, each [actual_date] <> null),
    Today = Date.From(DateTime.LocalNow()),
    NextYear = Date.Year(Today) + 1,
    CurrentDate = Date.EndOfMonth(#date(NextYear, 12, 31)),
    #"48MonthsAgo" = Date.AddMonths(Today, -48),
    #"Filtered Last 48 Months" = Table.SelectRows(#"Removed Blank Rows", each Date.From([actual_date]) >= #"48MonthsAgo" and Date.From([actual_date]) <= CurrentDate)
in
    #"Filtered Last 48 Months"
```

### LocalDateTable_5fcd5113-f6c2-46a0-843e-b67db11e6e91

```sql
Calendar(Date(Year(MIN('date_dim'[actual_date])), 1, 1), Date(Year(MAX('date_dim'[actual_date])), 12, 31))
```

### RetailSalesTransactionView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),    
    dbo_RetailSalesTransactionView = Source{[Schema="dbo",Item="RetailSalesTransactionView"]}[Data],
    #"Removed Rows" = Table.SelectRows(dbo_RetailSalesTransactionView, each [businessdate] >= Date.AddMonths(DateTime.LocalNow(), -12))
in
    #"Removed Rows"
```

### weeklyOnHandView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_weeklyOnHandView = Source{[Schema="dbo",Item="weeklyOnHandView"]}[Data],
    #"Removed Rows" = Table.SelectRows(dbo_weeklyOnHandView, each [actual_date] >= Date.AddMonths(DateTime.LocalNow(), -12))
in
    #"Removed Rows"
```

### InventtranferView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_InventtranferView = Source{[Schema="dbo",Item="InventtranferView"]}[Data]
in
    dbo_InventtranferView
```

### productattributesummaryview

```sql

ADDCOLUMNS (
    DISTINCT ( SELECTCOLUMNS ( product_dim_le, "product_key", product_dim_le[product_key] ) ),
    "LICNSR", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "LICNSR" 
    ),
    "MSTAT", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "MSTAT"
    ),
    "CCC", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "CCC" 
    ),
    "LICEN", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "LICEN" 
    ),
    "KEYSTY", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "KEYSTY" 
    ),
    "FACTRY", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "FACTRY" 
    ),
    "IDATE", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "IDATE" 
    ),
    "ODATE", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "ODATE" 
    ),
    "OMSTAT", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "OMSTAT" 
    ),
    "OUTLET", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "OUTLET" 
    ),
    "WEB", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "WEB" 
    ),
    "UKTRF", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "UKTRF"
    ),
    "USTRF", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "USTRF"
    ),
    "CATRF", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "CATRF"
    ),
    "CNTRF", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "CNTRF"
    ),
    "RZTRF", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "RZTRF"
    ),
    "COO", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "COO"
    ),
    "UKTRF_Label", CALCULATE (
        MAX ( ProductDim_attribute[AttributeLabel] ),
        ProductDim_attribute[AttributeName] = "UKTRF"
    ),
    "USTRF_Label", CALCULATE (
        MAX ( ProductDim_attribute[AttributeLabel] ),
        ProductDim_attribute[AttributeName] = "USTRF"
    ),
    "CATRF_Label", CALCULATE (
        MAX ( ProductDim_attribute[AttributeLabel] ),
        ProductDim_attribute[AttributeName] = "CATRF"
    ),
    "COO_Label", CALCULATE (
        MAX ( ProductDim_attribute[AttributeLabel] ),
        ProductDim_attribute[AttributeName] = "COO"
    ),
    "Factory_Label", CALCULATE (
        MAX ( ProductDim_attribute[AttributeLabel] ),
        ProductDim_attribute[AttributeName] = "FACTRY"
    )               
)
```

### LocalDateTable_78797bf2-1159-4b72-9fbf-a2062fd2bb4d

```sql
Calendar(Date(Year(MIN('product_dim_le'[InDate])), 1, 1), Date(Year(MAX('product_dim_le'[InDate])), 12, 31))
```

### LocalDateTable_62b65351-8b3a-49b2-a51a-53216f1831ad

```sql
Calendar(Date(Year(MIN('product_dim_le'[OutDate])), 1, 1), Date(Year(MAX('product_dim_le'[OutDate])), 12, 31))
```

### suntafretailreplenactivesettingsview

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_suntafretailreplenactivesettingsview = Source{[Schema="dbo",Item="suntafretailreplenactivesettingsview"]}[Data],
    #"Changed Type" = Table.TransformColumnTypes(dbo_suntafretailreplenactivesettingsview,{{"product_key", type text}})
in
    #"Changed Type"
```

### InventSettlementView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_InventSettlementView = Source{[Schema="dbo",Item="InventSettlementView"]}[Data]
in
    dbo_InventSettlementView
```

### VendorNameView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 0, 30, 0)]),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_VendorNameView = Source{[Schema="dbo",Item="VendorNameView"]}[Data]
in
    dbo_VendorNameView
```

### PurchChargeViewPivotTable

```sql

VAR Base =
    FILTER (
        DISTINCT (
            SELECTCOLUMNS (
                PurchChargesView,
                "receipt year",         PurchChargesView[Receipt Year],
                "purchlinerecid",       PurchChargesView[PurchLineRecId],
                "PurchChargeview_Key",  PurchChargesView[PurchChargeview_Key],
                "style",                PurchChargesView[itemid],
                "product_key",          PurchChargesView[product_key],
                "po_number",            PurchChargesView[purchid],
                "purchstatus",          PurchChargesView[purchstatus],
                "lineamount",           PurchChargesView[lineamount],
                "receipt_amount",       PurchChargesView[Receipt_cost_w/o_charges],
                "received_date",        PurchChargesView[received_date]
            )
        ),
        NOT ISBLANK ( [PurchChargeview_Key] )
            && NOT ISBLANK ( [received_date] )
    )
RETURN
    ADDCOLUMNS (
        Base,

        /* Charge buckets (scoped to key + received_date) */
        "FOBROY",
            VAR _key  = [PurchChargeview_Key]
            VAR _dt   = [received_date]
            RETURN
                CALCULATE (
                    SUM ( PurchChargesView[ChargeAmount] ),
                    PurchChargesView[markupcode] = "FOBROY",
                    TREATAS ( { _key }, PurchChargesView[PurchChargeview_Key] ),
                    TREATAS ( { _dt  }, PurchChargesView[received_date] )
                ),

        "OCEANFRT",
            VAR _key  = [PurchChargeview_Key]
            VAR _dt   = [received_date]
            RETURN
                CALCULATE (
                    SUM ( PurchChargesView[ChargeAmount] ),
                    PurchChargesView[markupcode] = "OCEANFRT",
                    TREATAS ( { _key }, PurchChargesView[PurchChargeview_Key] ),
                    TREATAS ( { _dt  }, PurchChargesView[received_date] )
                ),

        "DUTY",
            VAR _key  = [PurchChargeview_Key]
            VAR _dt   = [received_date]
            RETURN
                CALCULATE (
                    SUM ( PurchChargesView[ChargeAmount] ),
                    PurchChargesView[markupcode] = "DUTY",
                    TREATAS ( { _key }, PurchChargesView[PurchChargeview_Key] ),
                    TREATAS ( { _dt  }, PurchChargesView[received_date] )
                ),

        "TARIFFS",
            VAR _key  = [PurchChargeview_Key]
            VAR _dt   = [received_date]
            RETURN
                CALCULATE (
                    SUM ( PurchChargesView[ChargeAmount] ),
                    PurchChargesView[markupcode] = "TARIFFS",
                    TREATAS ( { _key }, PurchChargesView[PurchChargeview_Key] ),
                    TREATAS ( { _dt  }, PurchChargesView[received_date] )
                ),

        "INSPEES",
            VAR _key  = [PurchChargeview_Key]
            VAR _dt   = [received_date]
            RETURN
                CALCULATE (
                    SUM ( PurchChargesView[ChargeAmount] ),
                    PurchChargesView[markupcode] = "INSPEES",
                    TREATAS ( { _key }, PurchChargesView[PurchChargeview_Key] ),
                    TREATAS ( { _dt  }, PurchChargesView[received_date] )
                ),

        /* Totals */
        "TotalCharge",
            VAR _key  = [PurchChargeview_Key]
            VAR _dt   = [received_date]
            RETURN
                CALCULATE (
                    SUM ( PurchChargesView[ChargeAmount] ),
                    TREATAS ( { _key }, PurchChargesView[PurchChargeview_Key] ),
                    TREATAS ( { _dt  }, PurchChargesView[received_date] )
                ),

        "TotalLineAmount",
            VAR _key  = [PurchChargeview_Key]
            VAR _dt   = [received_date]
            VAR _charges =
                CALCULATE (
                    SUM ( PurchChargesView[ChargeAmount] ),
                    TREATAS ( { _key }, PurchChargesView[PurchChargeview_Key] ),
                    TREATAS ( { _dt  }, PurchChargesView[received_date] )
                )
            RETURN
                [lineamount] + _charges,

        "FOB Royalty %",
            VAR _key  = [PurchChargeview_Key]
            VAR _dt   = [received_date]
            VAR _num =
                CALCULATE (
                    SUM ( PurchChargesView[ChargeAmount] ),
                    PurchChargesView[MarkupCode] = "FOBROY",
                    TREATAS ( { _key }, PurchChargesView[PurchChargeview_Key] ),
                    TREATAS ( { _dt  }, PurchChargesView[received_date] )
                )
            VAR _den = [receipt_amount]
            RETURN
                ROUND ( DIVIDE ( _num, _den, 0 ) * 100, 2 )
    )

```

### suntafretailreplenproductcopyfromview

```sql
let
    Source = Sql.Database(ServerName, "LH_D365"),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_suntafretailreplenproductcopyfromview = Source{[Schema="dbo",Item="suntafretailreplenproductcopyfromview"]}[Data]
in
    dbo_suntafretailreplenproductcopyfromview
```

### ProductCategoryHierarchyPivotView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 0, 30, 0)]),
    dbo_ProductCategoryHierarchyPivotView = Source{[Schema="dbo",Item="ProductCategoryHierarchyPivotView"]}[Data]
in
    dbo_ProductCategoryHierarchyPivotView
```

### InventSumCurrentView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_InventSumCurrentView = Source{[Schema="dbo",Item="InventSumCurrentView"]}[Data]
in
    dbo_InventSumCurrentView
```

### LocalDateTable_07b72677-2169-4197-b55d-fd526d2cb314

```sql
Calendar(Date(Year(MIN('RetailSalesTransactionView'[transdate])), 1, 1), Date(Year(MAX('RetailSalesTransactionView'[transdate])), 12, 31))
```

### VendorXFDepartmentView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_VendorXFDepartmentView = Source{[Schema="dbo",Item="VendorXFDepartmentView"]}[Data]
in
    dbo_VendorXFDepartmentView
```

### VendorXFFactoryDepartmentView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_VendorXFFactoryDepartmentView = Source{[Schema="dbo",Item="VendorXFFactoryDepartmentView"]}[Data]
in
    dbo_VendorXFFactoryDepartmentView
```

### VendorXFVendorDepartmentView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_VendorXFVendorDepartmentView = Source{[Schema="dbo",Item="VendorXFVendorDepartmentView"]}[Data]
in
    dbo_VendorXFVendorDepartmentView
```

### VendorXFVendorFactoryView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_VendorXFVendorFactoryView = Source{[Schema="dbo",Item="VendorXFVendorFactoryView"]}[Data]
in
    dbo_VendorXFVendorFactoryView
```

### VendorXFItemDetailView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_VendorXFItemDetailView = Source{[Schema="dbo",Item="VendorXFItemDetailView"]}[Data]
in
    dbo_VendorXFItemDetailView
```

### VendorXFDepartmentVendorView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_VendorXFDepartmentVendorView = Source{[Schema="dbo",Item="VendorXFDepartmentVendorView"]}[Data]
in
    dbo_VendorXFDepartmentVendorView
```

### ReceiptCostFreightFactorView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_ReceiptCostFreightFactorView = Source{[Schema="dbo",Item="ReceiptCostFreightFactorView"]}[Data]
in
    dbo_ReceiptCostFreightFactorView
```

### ReportingPeriod

```sql

--This will be used for the Freight Cost/Freight Factor report
DATATABLE (
    "Period Order", INTEGER,
    "Period Label", STRING,
    "Year Offset",  INTEGER,
    {
        { 1, "Actual (Y-2)", -2 },
        { 2, "Actual (Y-1)", -1 },
        { 3, "YTD (Y)",       0 }
    }
    /*
    {
        { 1, "Actual (Y-3)", -3 },
        { 2, "Actual (Y-2)", -2 },
        { 3, "Actual (Y-1)", -1 },
        { 4, "YTD (Y)",       0 }
    }
    */
)
```

### CurrentVendorPurchasePriceView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_CurrentVendorPurchasePriceView = Source{[Schema="dbo",Item="CurrentVendorPurchasePriceView"]}[Data]
in
    dbo_CurrentVendorPurchasePriceView
```

### LocalDateTable_186ce2e6-b4c7-4c7a-ab05-99aa0e062b6c

```sql
Calendar(Date(Year(MIN('CurrentVendorPurchasePriceView'[fromdate])), 1, 1), Date(Year(MAX('CurrentVendorPurchasePriceView'[fromdate])), 12, 31))
```

### LocalDateTable_de9a3999-eb4d-41c9-9d48-eece6916f9f0

```sql
Calendar(Date(Year(MIN('CurrentVendorPurchasePriceView'[todate])), 1, 1), Date(Year(MAX('CurrentVendorPurchasePriceView'[todate])), 12, 31))
```

### ReceiptYear

```sql

FILTER (
    DISTINCT (
        UNION (
            SELECTCOLUMNS ( ReceiptCostFreightFactorView, "Year", INT ( ReceiptCostFreightFactorView[Receipt Year] ) ),
            SELECTCOLUMNS ( PurchChargeViewPivotTable,    "Year", INT ( PurchChargeViewPivotTable[receipt year] ) )
        )
    ),
    NOT ISBLANK ( [Year] )
)
```

### InventTransView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_InventTransView = Source{[Schema="dbo",Item="InventTransView"]}[Data]
in
    dbo_InventTransView
```

### PurchLineAggView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_PurchLineAggView = Source{[Schema="dbo",Item="PurchLineAggView"]}[Data]
in
    dbo_PurchLineAggView
```

### InventSumCurrentViewForWHSEnabledItems

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 2, 0, 0)]),
    dbo_InventSumCurrentView = Source{[Schema="dbo",Item="InventSumCurrentViewForWHSEnabledItems"]}[Data]
in
    dbo_InventSumCurrentView
```

### LocalDateTable_a6461a22-e031-4fd1-906a-50d7244f8985

```sql
Calendar(Date(Year(MIN('PurchasingTransView'[Cancel date])), 1, 1), Date(Year(MAX('PurchasingTransView'[Cancel date])), 12, 31))
```

### LocalDateTable_a562226d-3841-4d5e-92eb-65a8d2c9e2b2

```sql
Calendar(Date(Year(MIN('PurchChargesView'[received_date])), 1, 1), Date(Year(MAX('PurchChargesView'[received_date])), 12, 31))
```

### LocalDateTable_3265e62e-c157-4707-ad34-7638663aa1c1

```sql
Calendar(Date(Year(MIN('date_dim'[Day])), 1, 1), Date(Year(MAX('date_dim'[Day])), 12, 31))
```

### DJR_Receipt_InventoryTransCost

```sql
let
    Source = Sql.Database(#"ServerName", "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    DJR_Receipt_InventoryTransCosts = Source{[Schema="dbo",Item="DJR_Receipt_InventoryTransCost"]}[Data]
in
    DJR_Receipt_InventoryTransCosts
```

### LocalDateTable_487903f4-72ba-41a3-a15c-bcf6acebc9a0

```sql
Calendar(Date(Year(MIN('DJR_Receipt_InventoryTransCost'[Accounting Date])), 1, 1), Date(Year(MAX('DJR_Receipt_InventoryTransCost'[Accounting Date])), 12, 31))
```

### VendInvoiceView

```sql
let
    Source = Sql.Database(#"ServerName", "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    VendInvoiceView = Source{[Schema="dbo",Item="VendInvoiceView"]}[Data]
in
    VendInvoiceView
```

### LocalDateTable_415d9453-0230-4171-a34d-89c3f50676b5

```sql
Calendar(Date(Year(MIN('InventSumCurrentViewForWHSEnabledItems'[Next Ordered Date])), 1, 1), Date(Year(MAX('InventSumCurrentViewForWHSEnabledItems'[Next Ordered Date])), 12, 31))
```

### LocalDateTable_9d70e007-67fe-4f8a-bfb4-61b9eb24e0d5

```sql
Calendar(Date(Year(MIN('ReceiptCostFreightFactorView'[PO_CreateDate])), 1, 1), Date(Year(MAX('ReceiptCostFreightFactorView'[PO_CreateDate])), 12, 31))
```

### LocalDateTable_0b4d1899-0a08-4e2d-ab9d-f0dbaec0bd37

```sql
Calendar(Date(Year(MIN('PurchasingTransView'[PO_CreateDate])), 1, 1), Date(Year(MAX('PurchasingTransView'[PO_CreateDate])), 12, 31))
```

### InventJourTransView Missing Keys

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_InventJourTransView = Source{[Schema="dbo",Item="InventJourTransView_missingKeys"]}[Data]
in
    dbo_InventJourTransView
```

### DJRInventJournalReportView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_InventJourTransView = Source{[Schema="dbo",Item="DJRInventJournalReportView"]}[Data]
in
    dbo_InventJourTransView
```

### RetailSalesTransactionLicensedView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),    
    dbo_RetailSalesTransactionLicensedView = Source{[Schema="dbo",Item="RetailSalesTransactionLicensedView"]}[Data]
in
    dbo_RetailSalesTransactionLicensedView
```

### LocalDateTable_1bae8e7a-3d5e-4c3f-819e-2f8ad5c3e95a

```sql
Calendar(Date(Year(MIN('RetailSalesTransactionLicensedView'[businessdate])), 1, 1), Date(Year(MAX('RetailSalesTransactionLicensedView'[businessdate])), 12, 31))
```

### CycleCountView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    #"Filtered Rows" = Table.SelectRows(Source, each true),
    dbo_InventJourTransView = #"Filtered Rows"{[Schema="dbo",Item="CycleCountView"]}[Data]
in
    dbo_InventJourTransView
```

### LocalDateTable_4464229a-5c0f-4de1-a17e-947afe2fee87

```sql
Calendar(Date(Year(MIN('CycleCountView'[CountCompletedDate])), 1, 1), Date(Year(MAX('CycleCountView'[CountCompletedDate])), 12, 31))
```

### LocalDateTable_6299d0a0-f27c-4e81-868b-e0fabb84918e

```sql
Calendar(Date(Year(MIN('CycleCountView'[JournalPostedDate])), 1, 1), Date(Year(MAX('CycleCountView'[JournalPostedDate])), 12, 31))
```

### LocalDateTable_9eb68c62-a1e7-4a42-bdfa-b1edac34f926

```sql
Calendar(Date(Year(MIN('CycleCountView'[ModifiedDate])), 1, 1), Date(Year(MAX('CycleCountView'[ModifiedDate])), 12, 31))
```

### LocalDateTable_c01dc564-bdcb-4f2b-8e59-6e5e0ac8d6b2

```sql
Calendar(Date(Year(MIN('CycleCountView'[ApprovalDate])), 1, 1), Date(Year(MAX('CycleCountView'[ApprovalDate])), 12, 31))
```

## Shared Expressions

### ServerName (0)

```sql
"4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]
```

## Data Source Cross-References

_No recognized SQL data source references detected._
