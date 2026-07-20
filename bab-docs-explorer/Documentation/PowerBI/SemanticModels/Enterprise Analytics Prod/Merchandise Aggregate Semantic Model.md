# Merchandise Aggregate Semantic Model

**Workspace:** Enterprise Analytics Prod  
**Dataset ID:** 5a976e29-39d5-4409-83da-0761fa2ce528  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| DateTableTemplate_4b10c522-c7e4-4ea9-8621-9face0c0a790 | 8 | 0 | Yes |
| date_dim | 39 | 2 |  |
| LocalDateTable_e58886bb-220f-4db7-be70-9d550ece5351 | 8 | 0 | Yes |
| weeklyOnHandView | 21 | 141 |  |
| LocalDateTable_f2167fd2-cd0f-4922-bc96-72d212cdcc06 | 8 | 0 | Yes |
| d365LocationMapping_View | 13 | 0 |  |
| product_dim_le | 87 | 0 |  |
| LocalDateTable_aaf54f7c-6bd0-4f26-9a8a-c399ae83e6db | 8 | 0 | Yes |
| ProductDim_attribute | 7 | 0 |  |
| WeeklyAllocationView | 10 | 3 |  |
| WeeklyOnOrderView | 16 | 150 |  |
| WeeklySalesView | 42 | 499 |  |
| LocalDateTable_10c9249e-d232-4e18-a167-2c5932f223de | 8 | 0 | Yes |
| LocalDateTable_ee41d51f-9d46-4ac9-8200-f64175ecdeb0 | 8 | 0 | Yes |
| productattributesummaryview | 27 | 0 |  |
| suntafretailreplenactivesettingsview | 8 | 0 |  |
| VendorNameView | 9 | 0 |  |
| PurchasingTransView | 72 | 13 |  |
| LocalDateTable_2ee2b10b-8404-4b6e-913e-457483769a50 | 8 | 0 | Yes |
| LocalDateTable_b08b6a9c-a796-4fc9-9e6d-b88d2eeb184d | 8 | 0 | Yes |
| LocalDateTable_1452680a-222b-41d5-a1bd-2e0460c19769 | 8 | 0 | Yes |
| LocalDateTable_b73eddbc-f285-4393-81ba-7d345736794d | 8 | 0 | Yes |
| LocalDateTable_3d585c6d-15f6-4f36-926d-49d256ea70af | 8 | 0 | Yes |
| LocalDateTable_f9e1d974-6a04-42a8-a0d8-335b83dbe336 | 8 | 0 | Yes |
| InventtranferView | 8 | 0 |  |
| InventSumCurrentView | 26 | 6 |  |
| ProductCategoryHierarchyPivotView | 21 | 0 |  |
| ReceiptCostFreightFactorView | 22 | 0 |  |
| LocalDateTable_9858066a-f978-47c4-a6ef-952b87e8544d | 8 | 0 | Yes |
| InventSumCurrentViewForWHSEnabledItems | 42 | 22 |  |
| LocalDateTable_0fd1c2bb-f5c0-4b9d-9df9-41872db3be5c | 8 | 0 | Yes |
| LocalDateTable_fd47cfa2-cd82-49fb-a8e9-f9a69d2ff6bf | 8 | 0 | Yes |
| LocalDateTable_0d5a504d-e3b0-4405-b642-1036c75db61e | 8 | 0 | Yes |
| LocalDateTable_a23d376d-5f88-47e1-94f9-8fb237009275 | 8 | 0 | Yes |
| RetailSalesTransactionMerchWeekSummary | 16 | 0 |  |

## Measures

### date_dim.Seleced Date

```sql

VAR d = TODAY()
VAR wd = WEEKDAY(d, 1) 
VAR thisweek = d - (IF(wd = 7, 0, wd)) +7

VAR _SelectedMin =
    MINX ( VALUES(  ( date_dim[actual_date] )), date_dim[actual_date]  )
VAR _SelectedMax =
    MAXX ( VALUES(  ( date_dim[actual_date]  )), date_dim[actual_date]  )
VAR _AllMin =
    CALCULATE ( MIN ( date_dim[actual_date]  ), ALL ( date_dim ) )
VAR _AllMax =
    CALCULATE ( MAX ( date_dim[actual_date]  ), ALL ( date_dim ) )
VAR _FinalDate =
    IF (_SelectedMin = _AllMin && _SelectedMax = _AllMax,
        thisweek,
        IF (_SelectedMin <> _AllMin && _SelectedMax <> _AllMax, _SelectedMax,
        IF (_SelectedMin = _AllMin && _SelectedMax <> _AllMax, _SelectedMax, _SelectedMin)
        )
    )
RETURN
_FinalDate
```

### date_dim.PriorWeekEndDate

```sql

VAR d = TODAY()
VAR wd = WEEKDAY(d, 1) 
RETURN d - (IF(wd = 7, 0, wd)) +7
```

### weeklyOnHandView.EOP OH Units:Total (1 Period(s) Ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR TargetYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[fiscal_year] = TargetYear,
        'date_dim'[fiscal_period] = TargetPeriod
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[fiscal_year] = TargetYear,
        'date_dim'[fiscal_period] = TargetPeriod
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

/*
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR TargetYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = TargetYear, 'date_dim'[fiscal_period] = TargetPeriod )
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = TargetYear, 'date_dim'[fiscal_period] = TargetPeriod )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
*/
```

### weeklyOnHandView.EOP OH Cost:Total (1 Period(s) Ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR TargetYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_unit_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### weeklyOnHandView.EOP OH Units:Inv Status (1 Week(s) ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear  =
    CALCULATE( MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate )
VAR CurrentFiscalWeek  =
    CALCULATE( MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate )

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### weeklyOnHandView.EOP OH Cost:Inv StatusAvailable ( 1 Week(s) Ago )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1 

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_unit_cost]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Inv StatusAvailable (Last 1 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1  

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear - 1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        FILTER ( weeklyOnHandView, weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Str Units:InvStatusAvailable ( 1 Week(s) Ago )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1 


VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)


VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(d365LocationMapping_View[IsDC] = 0),
        FILTER ( weeklyOnHandView, weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH WH Units:InvStatusAvailable ( 1 Week(s) Ago )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1 


VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(d365LocationMapping_View[IsDC] = 1),
        FILTER ( weeklyOnHandView, weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Str Units:InvStatusAvailable (Current week Ly )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0 


VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)
VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(d365LocationMapping_View[IsDC] = 0),
        KEEPFILTERS ( weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH WH Units:InvStatusAvailable ( Last 1 Weeks Ly )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1 

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(d365LocationMapping_View[IsDC] = 1),
        FILTER ( weeklyOnHandView, weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Cost:Inv StatusAvailable ( Last 1 Weeks Ly )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1 

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear - 1
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_unit_cost]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH WH Units:InvStatusUnavail: damaged ( 1 Week(s) Ago )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1 

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "Damaged")
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Inv StatusUnavail: damaged ( Last 1 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )



VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[transfer_in_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "8" || UPPER(weeklyOnHandView[inventory_status_id]) = "DAMAGES")
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:InvStatusUnavail: damaged ( 1 Week(s) Ago )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1 

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "8" || UPPER(weeklyOnHandView[inventory_status_id]) = "DAMAGES")
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Total (1 Week(s) ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR N =1
VAR CurrentFiscalYear  =
    CALCULATE( MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate )
VAR CurrentFiscalWeek  =
    CALCULATE( MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate )

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### weeklyOnHandView.EOP OH Units:Total (Last 1 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1  

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)
VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Total ( Current )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear))
VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### weeklyOnHandView.EOP OH Units:Inv StatusAvailable ( Current )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        FILTER (
            weeklyOnHandView,
            weeklyOnHandView[inventory_status_id] = "1"
                || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL"
        )
    )
RETURN Result
```

### weeklyOnHandView.EOP OH Cost:Inv StatusAvailable ( Current )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_unit_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        FILTER ( weeklyOnHandView, weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )
RETURN Result
```

### weeklyOnHandView.EOP OH Units:Inv StatusUnavail: in transit ( Current )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(            
            weeklyOnHandView[inventory_status_id] = "2"
                || UPPER ( weeklyOnHandView[inventory_status_id] ) = "IN-TRANSIT"
        )
    )
RETURN Result
```

### weeklyOnHandView.BOP OH Units:Total ( Week )

```sql

VAR SelectedDate =  [Seleced Date] 
VAR SeletedYear =  
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate ) 
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SeletedYear && 'date_dim'[fiscal_week] = SelectedPeriod)) 
VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  SeletedYear && 'date_dim'[fiscal_week] = SelectedPeriod))  

VAR Result =  CALCULATE ( SUM ( weeklyOnHandView[on_hand_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result
```

### weeklyOnHandView.BOP OH Cost:Total ( Week )

```sql

VAR SelectedDate =  [Seleced Date] 
VAR SeletedYear =  
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate ) 
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SeletedYear && 'date_dim'[fiscal_week] = SelectedPeriod)) 
VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  SeletedYear && 'date_dim'[fiscal_week] = SelectedPeriod))  

VAR Result =  CALCULATE ( SUM ( weeklyOnHandView[on_hand_unit_cost] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result
```

### weeklyOnHandView.BOP OH Retail:Total te ( Week )

```sql

VAR SelectedDate =  [Seleced Date] 
VAR SeletedYear =  
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate ) 
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SeletedYear && 'date_dim'[fiscal_week] = SelectedPeriod)) 
VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  SeletedYear && 'date_dim'[fiscal_week] = SelectedPeriod))  

VAR Result =  CALCULATE ( SUM ( weeklyOnHandView[on_hand_retail] ),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) 
RETURN Result
```

### weeklyOnHandView.BOP OH Cost:Total ( Quarter 01 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q1StartDate =
    CALCULATE ( MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = SelectedYear
                && date_dim[fiscal_quarter] = 1
        )
    )
VAR TargetDate = Q1StartDate - 1
RETURN 
CALCULATE (
    SUM ( weeklyOnHandView[on_hand_unit_cost] ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Cost:Total ( Quarter 02 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q2StartDate =
    CALCULATE ( MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = SelectedYear
                && date_dim[fiscal_quarter] = 2
        )
    )
VAR TargetDate = Q2StartDate - 1
RETURN
CALCULATE (
    SUM ( weeklyOnHandView[on_hand_unit_cost] ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Cost:Total ( Quarter 03 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q2StartDate =
    CALCULATE ( MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = SelectedYear
                && date_dim[fiscal_quarter] = 3
        )
    )
VAR TargetDate = Q2StartDate - 1
RETURN
CALCULATE (
    SUM ( weeklyOnHandView[on_hand_unit_cost] ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Cost:Total ( Quarter 04 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q4StartDate =
    CALCULATE ( MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = SelectedYear
                && date_dim[fiscal_quarter] = 4
        )
    )
VAR TargetDate = Q4StartDate - 1
RETURN
CALCULATE (
    SUM ( weeklyOnHandView[on_hand_unit_cost] ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Retail:Total ( Quarter 01 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q1StartDate =
    CALCULATE ( MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = SelectedYear
                && date_dim[fiscal_quarter] = 1
        )
    )
VAR TargetDate = Q1StartDate - 1
RETURN
CALCULATE (
    SUMX ( weeklyOnHandView,
        weeklyOnHandView[on_hand_units] * weeklyOnHandView[current_retail]
    ),
   'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Retail:Total ( Quarter 02 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q2StartDate =
    CALCULATE ( MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = SelectedYear
                && date_dim[fiscal_quarter] = 2
        )
    )
VAR TargetDate = Q2StartDate - 1
RETURN
CALCULATE (
    SUMX ( weeklyOnHandView,
        weeklyOnHandView[on_hand_units] * weeklyOnHandView[current_retail]
    ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Units:Total ( Quarter 03 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q3StartDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = SelectedYear && date_dim[fiscal_quarter] = 3 )
    )
VAR TargetDate = Q3StartDate - 1
RETURN
CALCULATE (
    SUM ( weeklyOnHandView[on_hand_units] ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Units:Total ( Quarter 04 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q3StartDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = SelectedYear && date_dim[fiscal_quarter] = 4 )
    )
VAR TargetDate = Q3StartDate - 4
RETURN
CALCULATE (
    SUM ( weeklyOnHandView[on_hand_units] ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP ON Units:Total ( Week 01)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 1)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 1))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 02)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 2)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 2))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 03)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 3)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 3))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 04)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 4)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 4))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 05)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 5)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 5))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 06)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 6)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 6))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 07)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 7)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 7))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 08)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 8)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 8))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 09)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 9)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 9))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 10)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 10)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 10))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 11)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 11)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 11))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 12)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 12)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 12))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 13)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 13)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 13))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 14)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 14)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 14))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 15)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 15)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 15))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 16)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 16)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 16))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 17)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 17)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 17))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 18)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 18)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 18))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 19)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 19)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 19))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 20)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 20)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 20))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 21)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 21)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 21))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 22)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 22)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 22))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 23)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 23)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 23))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 24)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 24)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 24))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 25)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 25)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 25))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 26)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 26)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 26))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 27)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 27)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 27))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 28)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 28)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 28))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 29)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 29)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 29))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 30)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 30)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 30))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 31)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 31)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 31))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 32)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 32)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 32))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 33)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 33)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 33))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 34)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 34)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 34))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 35)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 35)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 35))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 36)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 36)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 36))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 37)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 37)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 37))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 38)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 38)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 38))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 39)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 39)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 39))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 40)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 40)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 40))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 41)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 41)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 41))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 42)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 42)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 42))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 43)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 43)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 43))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 44)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 44)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 44))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 45)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 45)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 45))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 46)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 46)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 46))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 47)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 47)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 47))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 48)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 48)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 48))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 49)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 49)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 49))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 50)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 50)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 50))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 51)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 51)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 51))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )  ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 52)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 52)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 52))  VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### weeklyOnHandView.BOP ON Units:Total ( Week 53)

```sql
VAR CurrentDate =  [Seleced Date]  
VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 53)) 
RETURN IF(MinDate = BLANK(), BLANK() , (
VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 53))  
VAR Result =  CALCULATE ( SUM (  weeklyOnHandView[on_hand_units]  ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result))
```

### weeklyOnHandView.BOP ON Units:Total Week (1-53)

```sql
[BOP ON Units:Total ( Week 01)] + [BOP ON Units:Total ( Week 02)] + [BOP ON Units:Total ( Week 03)] + [BOP ON Units:Total ( Week 04)] + [BOP ON Units:Total ( Week 05)] + [BOP ON Units:Total ( Week 06)] + [BOP ON Units:Total ( Week 07)] + [BOP ON Units:Total ( Week 08)] + [BOP ON Units:Total ( Week 09)] + [BOP ON Units:Total ( Week 10)] + [BOP ON Units:Total ( Week 11)] + [BOP ON Units:Total ( Week 12)] + [BOP ON Units:Total ( Week 13)] + [BOP ON Units:Total ( Week 14)] + [BOP ON Units:Total ( Week 15)] + [BOP ON Units:Total ( Week 16)] + [BOP ON Units:Total ( Week 17)] + [BOP ON Units:Total ( Week 18)] + [BOP ON Units:Total ( Week 19)] + [BOP ON Units:Total ( Week 20)] + [BOP ON Units:Total ( Week 21)] + [BOP ON Units:Total ( Week 22)] + [BOP ON Units:Total ( Week 23)] + [BOP ON Units:Total ( Week 24)] + [BOP ON Units:Total ( Week 25)] + [BOP ON Units:Total ( Week 26)] + [BOP ON Units:Total ( Week 27)] + [BOP ON Units:Total ( Week 28)] + [BOP ON Units:Total ( Week 29)] + [BOP ON Units:Total ( Week 30)] + [BOP ON Units:Total ( Week 31)] + [BOP ON Units:Total ( Week 32)] + [BOP ON Units:Total ( Week 33)] + [BOP ON Units:Total ( Week 34)] + [BOP ON Units:Total ( Week 35)] + [BOP ON Units:Total ( Week 36)] + [BOP ON Units:Total ( Week 37)] + [BOP ON Units:Total ( Week 38)] + [BOP ON Units:Total ( Week 39)] + [BOP ON Units:Total ( Week 40)] + [BOP ON Units:Total ( Week 41)] + [BOP ON Units:Total ( Week 42)] + [BOP ON Units:Total ( Week 43)] + [BOP ON Units:Total ( Week 44)] + [BOP ON Units:Total ( Week 45)] + [BOP ON Units:Total ( Week 46)] + [BOP ON Units:Total ( Week 47)] + [BOP ON Units:Total ( Week 48)] + [BOP ON Units:Total ( Week 49)] + [BOP ON Units:Total ( Week 50)] + [BOP ON Units:Total ( Week 51)] + [BOP ON Units:Total ( Week 52)] + [BOP ON Units:Total ( Week 53)]
```

### weeklyOnHandView.BOP OH Retail:Total ( Quarter 03 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q2StartDate =
    CALCULATE ( MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = SelectedYear
                && date_dim[fiscal_quarter] = 3
        )
    )
VAR TargetDate = Q2StartDate - 1
RETURN
CALCULATE (
    SUMX ( weeklyOnHandView,
        weeklyOnHandView[on_hand_units] * weeklyOnHandView[current_retail]
    ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Retail:Total ( Quarter 04 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q2StartDate =
    CALCULATE ( MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = SelectedYear
                && date_dim[fiscal_quarter] = 4
        )
    )
VAR TargetDate = Q2StartDate - 1
RETURN
CALCULATE (
    SUMX ( weeklyOnHandView,
        weeklyOnHandView[on_hand_units] * weeklyOnHandView[current_retail]
    ),
   'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Units:Total ( Quarter 01 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q3StartDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = SelectedYear && date_dim[fiscal_quarter] = 1 )
    )
VAR TargetDate = Q3StartDate - 4
RETURN
CALCULATE (
    SUM ( weeklyOnHandView[on_hand_units] ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.BOP OH Units:Total ( Quarter 02 )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR Q3StartDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = SelectedYear && date_dim[fiscal_quarter] = 2 )
    )
VAR TargetDate = Q3StartDate - 1
RETURN
CALCULATE (
    SUM ( weeklyOnHandView[on_hand_units] ),
    'date_dim'[actual_date]=TargetDate
)
```

### weeklyOnHandView.EOP OH Retail:Total TE ( Period 09 )

```sql

VAR SelectedDate = [Seleced Date]

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)

VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = CurrentFiscalYear - 1 
            && date_dim[fiscal_week] = 9
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = CurrentFiscalYear - 1
            && date_dim[fiscal_week] = 9
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_retail]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Total ( Period 09 )

```sql

VAR SelectedDate = [Seleced Date]

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)

VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = CurrentFiscalYear - 1 
            && date_dim[fiscal_week] = 9
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = CurrentFiscalYear - 1
            && date_dim[fiscal_week] = 9
        )
    )

VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### weeklyOnHandView.US Web LW Ttl EOP OH U

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR LastWeek = 
    CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = SelectedPeriod ))

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_week] = LastWeek ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_week] = LastWeek ))
VAR Result =
    CALCULATE (
         SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) 
    )
RETURN Result
```

### weeklyOnHandView.UK Web LW Ttl EOP OH U

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR LastWeek = 
    CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = SelectedPeriod ))

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_week] = LastWeek ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_week] = LastWeek ))
VAR Result =
    CALCULATE (
         SUM(weeklyOnHandView[on_hand_units]),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ,
         TREATAS ( VALUES ( product_dim_le[UK ProductKey] ), weeklyOnHandView[product_key] ),
         TREATAS ( VALUES ( d365LocationMapping_View[LocationKey] ), weeklyOnHandView[LocationKey] )
    )
RETURN Result
```

### weeklyOnHandView.DC OH US

```sql

VAR LocationKeys =
    CALCULATETABLE (
        VALUES ( d365LocationMapping_View[LocationKey] ),
        d365LocationMapping_View[LocationCode] = "0980",
        d365LocationMapping_View[JurisidictionCode] = "US"
    )
RETURN
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        TREATAS (
            VALUES ( product_dim_le[product_key] ),
            weeklyOnHandView[product_key]
        ),
        TREATAS (
            LocationKeys,
            weeklyOnHandView[LocationKey]
        )
    )
```

### weeklyOnHandView.DC OH UK

```sql

VAR LocationKeys =
    CALCULATETABLE (
        VALUES ( d365LocationMapping_View[LocationKey] ),
        d365LocationMapping_View[LocationCode] = "2970",
        d365LocationMapping_View[JurisidictionCode] = "UK"
    )
RETURN
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        TREATAS (
            VALUES ( product_dim_le[product_key] ),
            weeklyOnHandView[product_key]
        ),
        TREATAS (
            LocationKeys,
            weeklyOnHandView[LocationKey]
        )
    )
```

### weeklyOnHandView.Store OH US

```sql

VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        TREATAS (
            SELECTCOLUMNS (
                FILTER (
                    d365LocationMapping_View,
                    d365LocationMapping_View[IsDC] = 0
                        && d365LocationMapping_View[JurisidictionCode] = "US"
                ),
                "LocKey", d365LocationMapping_View[LocationKey]
            ),
            weeklyOnHandView[LocationKey]
        )
    )
RETURN
    Result
```

### weeklyOnHandView.Store OH UK

```sql

VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        TREATAS (
            SELECTCOLUMNS (
                FILTER (
                    d365LocationMapping_View,
                    d365LocationMapping_View[IsDC] = 0
                        && d365LocationMapping_View[JurisidictionCode] = "UK"
                ),
                "LocKey", d365LocationMapping_View[LocationKey]
            ),
            weeklyOnHandView[LocationKey]
        ),
        TREATAS ( VALUES ( product_dim_le[UK ProductKey] ), weeklyOnHandView[product_key] )
    )
RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Inv StatusAvailable (Current Week Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear-1
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear - 1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Str Units:InvStatusAvailable ( Current week)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0 


VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)


VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(d365LocationMapping_View[IsDC] = 0),
        FILTER ( weeklyOnHandView, weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH WH Units:InvStatusAvailable (Current Week)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0 


VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(d365LocationMapping_View[IsDC] = 1),
        FILTER ( weeklyOnHandView, weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH WH Units:InvStatusAvailable (Current week Ly )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0 

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear-1
//    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(d365LocationMapping_View[IsDC] = 1),
        KEEPFILTERS ( weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Cost:Inv StatusAvailable ( Current Week Ly )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0 

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear-1
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_unit_cost]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "1" || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL" )
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Inv StatusUnavail: damaged ( Current Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )



VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[transfer_in_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "8" || UPPER(weeklyOnHandView[inventory_status_id]) = "DAMAGES")
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:InvStatusUnavail: damaged (Current Week)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "8" || UPPER(weeklyOnHandView[inventory_status_id]) = "DAMAGED")
    )

RETURN
    Result
```

### weeklyOnHandView.980 - Curr Inv Unit - Available

```sql

VAR CurrentDate = TODAY()
RETURN
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        'date_dim'[actual_date] = CurrentDate
    )
```

### weeklyOnHandView.DBG - EOP OH units:Inv Status Current Week LY Vars

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE ( MAX ( date_dim[fiscal_year] ), date_dim[actual_date] = SelectedDate )
VAR CurrentFiscalWeek =
    CALCULATE ( MAX ( date_dim[fiscal_week] ), date_dim[actual_date] = SelectedDate )
VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear - 1, CurrentFiscalYear - 2 )
VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )
VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )
VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
                && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
                && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR DateSet =
    DATESBETWEEN(date_dim[actual_date], MinDate, MaxDate)    
VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units])
      ,DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
      ,TREATAS(DateSet, weeklyOnHandView[actual_date])
    )
RETURN
    // "SelDate=" & FORMAT ( SelectedDate, "yyyy-mm-dd" )
    // & " | CurFY=" & CurrentFiscalYear
    // & " | CurFW=" & CurrentFiscalWeek
    // & 
    " | TgtFY=" & TargetFiscalYear
    & 
    //" | LastWPrevFY=" & LastWeekPrevYear
    //& 
    " | TgtFW=" & TargetFiscalWeek
    & 
    " | Min=" & FORMAT ( MinDate, "yyyy-mm-dd" )
    & " | Max=" & FORMAT ( MaxDate, "yyyy-mm-dd" )
    & " | Result=" & Result
```

### weeklyOnHandView.DBG EOP OH Units:Inv StatusAvailable (Current Week Ly)

```sql

VAR SelectedDate =
    COALESCE ( [Seleced Date], MAX ( date_dim[actual_date] ) )
VAR N = 0

VAR CurrentFiscalYear =
    MAXX ( FILTER ( ALL ( date_dim ), date_dim[actual_date] = SelectedDate ), date_dim[fiscal_year] )
VAR CurrentFiscalWeek =
    MAXX ( FILTER ( ALL ( date_dim ), date_dim[actual_date] = SelectedDate ), date_dim[fiscal_week] )

VAR WeekOffset = CurrentFiscalWeek - N
VAR TargetFiscalYear_Base = CurrentFiscalYear - 1

VAR LastWeekPrevYear =
    CALCULATE (
        MAX ( date_dim[fiscal_week] ),
        REMOVEFILTERS ( date_dim ),
        date_dim[fiscal_year] = TargetFiscalYear_Base
    )

VAR TargetFiscalYear =
    IF ( WeekOffset > 0, TargetFiscalYear_Base, TargetFiscalYear_Base - 1 )

VAR TargetFiscalWeek =
    IF ( WeekOffset > 0, WeekOffset, LastWeekPrevYear + WeekOffset )

VAR TargetWeekEndDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        REMOVEFILTERS ( date_dim ),
        date_dim[fiscal_year] = TargetFiscalYear,
        date_dim[fiscal_week] = TargetFiscalWeek
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        //REMOVEFILTERS ( weeklyOnHandView[actual_date] ),
        //TREATAS ( {TargetWeekEndDate}, weeklyOnHandView[actual_date] )
         -- Apply LY week-ending date (keeps style_code filter intact)
        KEEPFILTERS ( weeklyOnHandView[actual_date] = TargetWeekEndDate )
    )
```

### weeklyOnHandView.EOP OH Units:Inv Status Available (1 Week(s) ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear  =
    CALCULATE( MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate )
VAR CurrentFiscalWeek  =
    CALCULATE( MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate )

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
        ,KEEPFILTERS(            
            weeklyOnHandView[inventory_status_id] = "1"
                || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL"
        )
        
    )
RETURN Result
```

### weeklyOnHandView.DBG EOP OH Units:Inv Status Available (2 Week(s) ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear  =
    CALCULATE( MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate )
VAR CurrentFiscalWeek  =
    CALCULATE( MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate )

VAR TargetFiscalYear = CurrentFiscalYear - 1 
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(            
            weeklyOnHandView[inventory_status_id] = "1"
                || UPPER ( weeklyOnHandView[inventory_status_id] ) = "AVAIL"
        )
        
    )
RETURN Result
```

### weeklyOnHandView.BOP OH retail (month)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR Result =
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

RETURN
    Result
```

### weeklyOnHandView.BOP OH retail (month 1)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 2)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 3)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 4)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 5)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 6)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 7)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 8)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 9)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 10)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 11)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail (month 12)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.EOP OH Units:Inv Status Unavail: reserved cust order ( Current Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear-1
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =    
        CALCULATE( SUM(weeklyOnHandView[on_hand_units]), 
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ), 
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "9") )       
    
RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Inv Status Unavail: reserved cust order ( Current Weeks)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =    
        CALCULATE( SUM(weeklyOnHandView[on_hand_units]), 
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ), 
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "9") )       
    
RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Inv Status Unavail: pending shrink ( Current Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear -1 
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "7")
    )

RETURN
    Result
```

### weeklyOnHandView.EOP OH Units:Inv Status Unavail: pending shrink ( Current Weeks)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "7")
    )

RETURN
    Result
```

### weeklyOnHandView.BOP OH retail ( month 1 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 2 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 3 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 4 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 5 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 6 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 7 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 8 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 9 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 10 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 11 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.BOP OH retail ( month 12 )

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnHandView,
            weeklyOnHandView[on_hand_units]
                * weeklyOnHandView[current_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

```

### weeklyOnHandView.Short Term alloc

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[allocation_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### weeklyOnHandView.EOP OH Units:Inv StatusPendPut ( Current )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = SelectedYear, 'date_dim'[fiscal_period] = SelectedPeriod )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        FILTER (
            weeklyOnHandView,
            UPPER ( weeklyOnHandView[inventory_status_id] ) = "PENDPUT"
        )
    )
RETURN Result
```

### weeklyOnHandView.EOP OH Units:Total (1 Period(s) Ago) v2

```sql

VAR SelectedDate = [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedPeriod =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR TargetYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )

VAR TargetPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )

VAR EOPSnapshotDate =
    CALCULATE (
        MAXX (
            FILTER (
                VALUES ( 'date_dim'[actual_date] ),
                CALCULATE ( COUNTROWS ( weeklyOnHandView ) ) > 0
            ),
            'date_dim'[actual_date]
        ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[fiscal_year] = TargetYear,
        'date_dim'[fiscal_period] = TargetPeriod
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_units] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = EOPSnapshotDate
    )
```

### weeklyOnHandView.EOP OH Cost:Total (1 Period(s) Ago) v2

```sql

VAR SelectedDate = [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedPeriod =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR TargetYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )

VAR TargetPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )

VAR EOPSnapshotDate =
    CALCULATE (
        MAXX (
            FILTER (
                VALUES ( 'date_dim'[actual_date] ),
                CALCULATE ( COUNTROWS ( weeklyOnHandView ) ) > 0
            ),
            'date_dim'[actual_date]
        ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[fiscal_year] = TargetYear,
        'date_dim'[fiscal_period] = TargetPeriod
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnHandView[on_hand_unit_cost] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = EOPSnapshotDate
    )
```

### WeeklyAllocationView.Short Term Alloc'd

```sql

VAR CurrentDate = TODAY()
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX('date_dim'[fiscal_week]), 'date_dim'[actual_date] = CurrentDate)
VAR SelectedLocation = SELECTEDVALUE('d365LocationMapping_View'[LocationCode])
VAR Currentdatekey = CALCULATE(MAX('date_dim'[date_key]), FILTER( ALL(date_dim), 'date_dim'[fiscal_week] = CurrentFiscalWeek
    && 'date_dim'[fiscal_year] = CurrentFiscalYear))
VAR Result =
CALCULATE(
    SUM(WeeklyAllocationView[allocation_units]),
    FILTER(
        WeeklyAllocationView,
        WeeklyAllocationView[date_key] = Currentdatekey
    )
)
RETURN Result
```

### WeeklyAllocationView.In-Transit units Total (Current Week)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear - 1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(WeeklyAllocationView[allocation_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklyAllocationView.In-Transit units Total (Current Week LY)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear -1 
    

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek = 
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(WeeklyAllocationView[allocation_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklyOnOrderView.On Order Units (This Period)

```sql

VAR SelectedDate = [Seleced Date]

VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )

VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = SelectedPeriod))

VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = SelectedPeriod))

VAR Result =
    CALCULATE (
         SUM ( WeeklyOnOrderView[on_order_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN Result
```

### WeeklyOnOrderView.On Order Units (Total)

```sql
VAR SelectedDate = [Seleced Date]

VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear ))

VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear ))

VAR Result =
    CALCULATE (
         SUM ( WeeklyOnOrderView[on_order_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 1 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 1 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 2 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 2 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 3 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 3 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 4 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 4 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 5 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 5 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 6 Periods)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 6 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 7 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 7 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 8 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 8 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 9 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 9 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 10 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 10 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 11 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 11 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 12 Periods)

```sql
VAR 
SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffset = 12 
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffset - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffset - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 01)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 1)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 1))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 02)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 2)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 2))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 03)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 3)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 3))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 04)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 4)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 4))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 05)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 5)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 5))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 06)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 6)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 6))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 07)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 7)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 7))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 08)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 8)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 8))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 09)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 9)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 9))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 10)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 10)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 10))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 11)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 11)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 11))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 12)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 12)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 12))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 13)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 13)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 13))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 14)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 14)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 14))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 15)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 15)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 15))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 16)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 16)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 16))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 17)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 17)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 17))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 18)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 18)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 18))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 19)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 19)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 19))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 20)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 20)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 20))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 21)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 21)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 21))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 22)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 22)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 22))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 23)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 23)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 23))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 24)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 24)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 24))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 25)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 25)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 25))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 26)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 26)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 26))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 27)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 27)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 27))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 28)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 28)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 28))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 29)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 29)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 29))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 30)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 30)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 30))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 31)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 31)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 31))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 32)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 32)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 32))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 33)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 33)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 33))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 34)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 34)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 34))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 35)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 35)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 35))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 36)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 36)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 36))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 37)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 37)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 37))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 38)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 38)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 38))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 39)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 39)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 39))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 40)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 40)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 40))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 41)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 41)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 41))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 42)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 42)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 42))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 43)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 43)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 43))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 44)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 44)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 44))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 45)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 45)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 45))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 46)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 46)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 46))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 47)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 47)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 47))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 48)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 48)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 48))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 49)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 49)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 49))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 50)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 50)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 50))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 51)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 51)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 51))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 52)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 52)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 52))  VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklyOnOrderView.On Order Units ( Week 53)

```sql
VAR CurrentDate =  [Seleced Date]  
VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 53)) 
RETURN IF(MinDate = BLANK(), BLANK() , (
VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 53))  
VAR Result =  CALCULATE ( SUM (  WeeklyOnOrderView[on_order_units]   ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result))
```

### WeeklyOnOrderView.On Order Units Week (1-53)

```sql
[On Order Units ( Week 01)] + [On Order Units ( Week 02)] + [On Order Units ( Week 03)] + [On Order Units ( Week 04)] + [On Order Units ( Week 05)] + [On Order Units ( Week 06)] + [On Order Units ( Week 07)] + [On Order Units ( Week 08)] + [On Order Units ( Week 09)] + [On Order Units ( Week 10)] + [On Order Units ( Week 11)] + [On Order Units ( Week 12)] + [On Order Units ( Week 13)] + [On Order Units ( Week 14)] + [On Order Units ( Week 15)] + [On Order Units ( Week 16)] + [On Order Units ( Week 17)] + [On Order Units ( Week 18)] + [On Order Units ( Week 19)] + [On Order Units ( Week 20)] + [On Order Units ( Week 21)] + [On Order Units ( Week 22)] + [On Order Units ( Week 23)] + [On Order Units ( Week 24)] + [On Order Units ( Week 25)] + [On Order Units ( Week 26)] + [On Order Units ( Week 27)] + [On Order Units ( Week 28)] + [On Order Units ( Week 29)] + [On Order Units ( Week 30)] + [On Order Units ( Week 31)] + [On Order Units ( Week 32)] + [On Order Units ( Week 33)] + [On Order Units ( Week 34)] + [On Order Units ( Week 35)] + [On Order Units ( Week 36)] + [On Order Units ( Week 37)] + [On Order Units ( Week 38)] + [On Order Units ( Week 39)] + [On Order Units ( Week 40)] + [On Order Units ( Week 41)] + [On Order Units ( Week 42)] + [On Order Units ( Week 43)] + [On Order Units ( Week 44)] + [On Order Units ( Week 45)] + [On Order Units ( Week 46)] + [On Order Units ( Week 47)] + [On Order Units ( Week 48)] + [On Order Units ( Week 49)] + [On Order Units ( Week 50)] + [On Order Units ( Week 51)] + [On Order Units ( Week 52)] + [On Order Units ( Week 53)]
```

### WeeklyOnOrderView.On Order Cost (Quarter 01)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 1)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 1)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) 
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Cost (Quarter 02)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 2)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 2)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) 
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Cost (Quarter 03)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 3)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 3)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) 
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Cost (Quarter 04)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 4)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 4)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) 
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Units (Quarter 01)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 1)
    )
VAR MaxDate =
    CALCULATE (
        MAXA ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 1)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Units (Quarter 02)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 2)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 2)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Units (Quarter 03)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 3)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 3)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Units (Quarter 04)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 4)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 4)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_units] ),
       DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Retail TE (Quarter 01)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 1)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 1)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) 
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Retail TE (Quarter 02)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 2)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 2)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) 
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Retail TE (Quarter 03)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 3)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 3)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) 
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Retail TE (Quarter 04)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 4)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_quarter] = 4)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) 
    )
RETURN
    Result
```

### WeeklyOnOrderView.On Order Units( Past Due Periods)

```sql
VAR SelectedDate = [Seleced Date]
 
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )

VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR PastYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )
VAR PastPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] < PastYear && 'date_dim'[fiscal_period] < PastPeriod ))

VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PastYear && 'date_dim'[fiscal_period] = PastPeriod ))

VAR Result = 
CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklyOnOrderView.+1PERIOD

```sql
[On Order Units (Next 1 Periods)]
```

### WeeklyOnOrderView.+2&3PERIODS

```sql
[On Order Units (Next 2 Periods)] + [On Order Units (Next 3 Periods)]
```

### WeeklyOnOrderView.+4&5&6PERIODS

```sql
[On Order Units (Next 4 Periods)] + [On Order Units (Next 5 Periods)] + [On Order Units (Next 6 Periods)]
```

### WeeklyOnOrderView.PAST+CURR OO

```sql

VAR SelectedDate = [Seleced Date]
 
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )

VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR PastYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )
VAR PastPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] < SelectedYear && 'date_dim'[fiscal_period] < SelectedPeriod ))

VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = SelectedPeriod ))

VAR Result = 
CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 1 Weeks)

```sql

VAR NextDate = [Seleced Date] + 7
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 2 Weeks)

```sql

VAR NextDate = [Seleced Date] + 14
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 3 Weeks)

```sql

VAR NextDate = [Seleced Date] + 21
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 4 Weeks)

```sql

VAR NextDate = [Seleced Date] + 28
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 5 Weeks)

```sql

VAR NextDate = [Seleced Date] + 35
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 6 Weeks)

```sql

VAR NextDate = [Seleced Date] + 42
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 7 Weeks)

```sql

VAR NextDate = [Seleced Date] + 49
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 8 Weeks)

```sql

VAR NextDate = [Seleced Date] + 56
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 9 Weeks)

```sql

VAR NextDate = [Seleced Date] + 63
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 10 Weeks)

```sql

VAR NextDate = [Seleced Date] + 70
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 11 Weeks)

```sql

VAR NextDate = [Seleced Date] + 77
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Next 12 Weeks)

```sql

VAR NextDate = [Seleced Date] + 84
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Current Weeks)

```sql

VAR NextDate = [Seleced Date]
VAR NextYear1 =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = NextDate )
VAR NextWeek =CALCULATE ( MAX ( 'date_dim'[fiscal_week] ) , 'date_dim'[actual_date] = NextDate )
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ),
    FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_week] = NextWeek))
VAR Result =CALCULATE (
    SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.On Order Units (Total 0-12 Weeks)

```sql

[On Order Units (Current Weeks)] + [On Order Units (Next 1 Weeks)] + [On Order Units (Next 2 Weeks)] + [On Order Units (Next 3 Weeks)]
+ [On Order Units (Next 4 Weeks)] + [On Order Units (Next 5 Weeks)] + [On Order Units (Next 6 Weeks)] + [On Order Units (Next 7 Weeks)]
+ [On Order Units (Next 8 Weeks)] + [On Order Units (Next 9 Weeks)] + [On Order Units (Next 10 Weeks)] + [On Order Units (Next 11 Weeks)]
+ [On Order Units (Next 12 Weeks)]
```

### WeeklyOnOrderView.OO Retail (month)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR Result =
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

RETURN
    Result
```

### WeeklyOnOrderView.Past due on order (month)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR Result =
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

RETURN
    Result
```

### WeeklyOnOrderView.OO Retail (month 1)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 2)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 3)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 4)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 5)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 6)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 7)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 8)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 9)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 10)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 11)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail (month 12)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 1)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 0 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 2)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 1 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 3)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 2 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 4)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 3 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 5)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 4 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 6)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 5 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 7)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 6 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 8)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 7 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 9)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 8 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 10)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 9 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 11)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 10 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order (month 12)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 11 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedFiscalYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.+4&5&6PERIODS (New)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =CALCULATE ( MAX ( 'date_dim'[fiscal_period] ) , 'date_dim'[actual_date] = SelectedDate )
VAR PeriodOffsetMin = 4 
VAR PeriodOffsetMax = 6 
VAR NextYearMin = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffsetMin - 1, 12)
VAR NextPeriodMin = 
    MOD(SelectedPeriod + PeriodOffsetMin - 1, 12) + 1
VAR NextYear1 = 
    SelectedYear + QUOTIENT(SelectedPeriod + PeriodOffsetMax - 1, 12)
VAR NextPeriod = 
    MOD(SelectedPeriod + PeriodOffsetMax - 1, 12) + 1
VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = NextYearMin && 'date_dim'[fiscal_period] = NextPeriodMin))
VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = NextYear1 && 'date_dim'[fiscal_period] = NextPeriod))
VAR Result =CALCULATE (SUM ( WeeklyOnOrderView[on_order_units] ),DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) )
RETURN Result
```

### WeeklyOnOrderView.pass due on order ( month 1 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 0 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 2 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 1 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 3 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 2 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 4 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 3 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 5 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 4 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 6 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 5 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 7 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 6 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 8 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 7 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 9 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 8 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 10 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 9 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 11 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 10 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.pass due on order ( month 12 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR BaseDate =
    EDATE ( SelectedDate, 11 )

VAR SelectedFiscalYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = BaseDate
    )

VAR SelectedMonthStart =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedFiscalYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MinDate =
    EDATE ( SelectedMonthStart, -6 )

VAR MaxDate =
    EOMONTH ( SelectedMonthStart, -1 )

RETURN
    CALCULATE (
        SUMX (
            weeklyOnOrderView,
            weeklyOnOrderView[on_order_units]
                * weeklyOnOrderView[on_order_retail]
        ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 1 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 2 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 3 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 4 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 5 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 6 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 7 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 8 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 9 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 10 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 11 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklyOnOrderView.OO Retail ( month 12 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( weeklyOnOrderView[on_order_retail_us_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Current Merch Year Week

```sql

VAR TodayDate = TODAY()
VAR Yr = YEAR ( TodayDate )
VAR Wk = WEEKNUM ( TodayDate, 2 )
RETURN Yr * 100 + Wk
```

### WeeklySalesView.Gross Sales (Last 3 Quarters)

```sql

VAR SelectedDate = [Seleced Date]
 
/* Anchor to the selected date, independent of current date filters */
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )
 
VAR SelectedQuarter =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_quarter] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )
 
/* Defensive: if SelectedDate isn't resolvable to a year/quarter, return BLANK */
VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedQuarter )
 
/* Continuous fiscal quarter index (requires fiscal_year numeric) */
VAR SelectedQIndex =
    SelectedYear * 4 + SelectedQuarter
 
RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail_us_te] ),
        FILTER (
            ALL ( 'date_dim' ),
            VAR QIndex =
                'date_dim'[fiscal_year] * 4 + 'date_dim'[fiscal_quarter]
            RETURN
                QIndex >= SelectedQIndex - 3
                    && QIndex <= SelectedQIndex - 1
        )
    )
)
```

### WeeklySalesView.Net Sales Retail (Last 3 Quarters)

```sql

VAR SelectedDate = [Seleced Date]
 
/* Anchor to the selected date, independent of current date filters */
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )
 
VAR SelectedQuarter =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_quarter] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )
 
/* Defensive: if SelectedDate isn't resolvable to a year/quarter, return BLANK */
VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedQuarter )
 
/* Continuous fiscal quarter index (requires fiscal_year numeric) */
VAR SelectedQIndex =
    SelectedYear * 4 + SelectedQuarter
 
RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),
        FILTER (
            ALL ( 'date_dim' ),
            VAR QIndex =
                'date_dim'[fiscal_year] * 4 + 'date_dim'[fiscal_quarter]
            RETURN
                QIndex >= SelectedQIndex - 3
                    && QIndex <= SelectedQIndex - 1
        )
    )
)
/*
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_quarter] ), 'date_dim'[actual_date] = SelectedDate )

VAR TargetYear =
    IF ( SelectedPeriod - 3 < 1, SelectedYear - 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod - 3 < 1, selectedPeriod - 3 + 4, SelectedPeriod - 3 )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = TargetYear, 'date_dim'[fiscal_quarter] = TargetPeriod )
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = TargetYear, 'date_dim'[fiscal_quarter] = TargetPeriod )
VAR Result =
    CALCULATE (
         SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
*/
```

### WeeklySalesView.Net Sales Units ( 1 month Ago )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR TargetYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER ( ALL ( 'date_dim' ), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER ( ALL ( 'date_dim' ), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM(WeeklySalesView[return_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units (Last 3 Quarters)

```sql

VAR SelectedDate = [Seleced Date]

/* Anchor to the selected date, independent of current date filters */
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )

VAR SelectedQuarter =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_quarter] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )

/* Defensive: if SelectedDate isn't resolvable to a year/quarter, return BLANK */
VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedQuarter )

/*
  Continuous fiscal quarter index.
  IMPORTANT: fiscal_year must be numeric for this to work.
*/
VAR SelectedQIndex =
    SelectedYear * 4 + SelectedQuarter

RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        FILTER (
            ALL ( 'date_dim' ),
            VAR QIndex = 'date_dim'[fiscal_year] * 4 + 'date_dim'[fiscal_quarter]
            RETURN
                QIndex >= SelectedQIndex - 3
                    && QIndex <= SelectedQIndex - 1
        )
    )
)
```

### WeeklySalesView.Promo Pc Total Retail (Last 3 Quarters)

```sql

VAR SelectedDate = [Seleced Date]

/* Anchor to the selected date, independent of current date filters */
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )

VAR SelectedQuarter =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_quarter] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )

/* Defensive: if SelectedDate isn't resolvable to a year/quarter, return BLANK */
VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedQuarter )

/* Continuous fiscal quarter index (requires fiscal_year numeric) */
VAR SelectedQIndex =
    SelectedYear * 4 + SelectedQuarter

RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail] ),
        FILTER (
            ALL ( 'date_dim' ),
            VAR QIndex =
                'date_dim'[fiscal_year] * 4 + 'date_dim'[fiscal_quarter]
            RETURN
                QIndex >= SelectedQIndex - 3
                    && QIndex <= SelectedQIndex - 1
        )
    )
)
```

### WeeklySalesView.Sales retail ( 1 month Ago )

```sql

VAR LastMonthDate = EOMONTH([Seleced Date], -1)
VAR MinDate = 
        CALCULATE( 
            MIN(date_dim[actual_date]),
            FILTER(ALL(date_dim),YEAR(date_dim[actual_date])= YEAR(LastMonthDate) && MONTH(date_dim[actual_date]) = MONTH(LastMonthDate))
        )
VAR MaxDate = 
        CALCULATE( 
            MAX(date_dim[actual_date]),
            FILTER(ALL(date_dim),YEAR(date_dim[actual_date]) = YEAR(LastMonthDate) && MONTH(date_dim[actual_date]) = MONTH(LastMonthDate))
        )
RETURN 
CALCULATE (
    SUM(WeeklySalesView[sales_total_retail]) * AVERAGE(WeeklySalesView[Style Attribute Set Code DISNEY ROYALTY RATE]),
    DATESBETWEEN(date_dim[actual_date],MinDate,MaxDate)
)
```

### WeeklySalesView.sales_total_retail_us_te ( 1 month Ago )

```sql

VAR SelectedDate = [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )

VAR SelectedPeriod =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )

VAR TargetYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )

VAR TargetPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = TargetYear
                && 'date_dim'[fiscal_period] = TargetPeriod
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = TargetYear
                && 'date_dim'[fiscal_period] = TargetPeriod
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail_us_te] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
```

### WeeklySalesView.Net Sales Retail TE (This week)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -0 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( 
    (SUM ( WeeklySalesView[sales_total_retail_us_te] )- sum(WeeklySalesView[return_retail_us_te]) ),  
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    ) 
    RETURN Result
```

### WeeklySalesView.Net Sales Units (This week)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevDate = CurrentDate - 0

VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = PrevDate
    )

VAR PrevWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = PrevDate
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear
                && 'date_dim'[fiscal_week] = PrevWeek
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear
                && 'date_dim'[fiscal_week] = PrevWeek
        )
    )

VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] )
            - SUM ( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (1 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -7 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM ( WeeklySalesView[sales_total_retail_us_te] )- sum(WeeklySalesView[return_retail_us_te]) ),         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (1 Week(s) ago)

```sql

VAR PrevDate = [Seleced Date] - 7
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR PrevWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR Result =
    CALCULATE (
        (
            SUM ( WeeklySalesView[sales_total_units] )
                - SUM ( WeeklySalesView[return_units] )
        ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (2 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -14 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM ( WeeklySalesView[sales_total_retail_us_te] )- sum(WeeklySalesView[return_retail_us_te]) ),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (2 Week(s) ago)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevDate = CurrentDate - 14
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR PrevWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR Result =
    CALCULATE (
        (
            SUM ( WeeklySalesView[sales_total_units] )
                - SUM ( WeeklySalesView[return_units] )
        ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (3 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -21 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM ( WeeklySalesView[sales_total_retail_us_te] )- sum(WeeklySalesView[return_retail_us_te]) ),         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (3 Week(s) ago)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevDate = CurrentDate - 21
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR PrevWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR Result =
    CALCULATE (
        (
            SUM ( WeeklySalesView[sales_total_units] )
                - SUM ( WeeklySalesView[return_units] )
        ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (4 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -28 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ((SUM ( WeeklySalesView[sales_total_retail_us_te] )- sum(WeeklySalesView[return_retail_us_te]) ),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (4 Week(s) ago)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevDate = CurrentDate - 28
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR PrevWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR Result =
    CALCULATE (
        (
            SUM ( WeeklySalesView[sales_total_units] )
                - SUM ( WeeklySalesView[return_units] )
        ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (5 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -35 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM ( WeeklySalesView[sales_total_retail_us_te] )- sum(WeeklySalesView[return_retail_us_te]) ),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (5 Week(s) ago)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevDate = CurrentDate - 35
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR PrevWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = PrevDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek
        )
    )
VAR Result =
    CALCULATE (
        (
            SUM ( WeeklySalesView[sales_total_units] )
                - SUM ( WeeklySalesView[return_units] )
        ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (6 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -42 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM ( WeeklySalesView[sales_total_retail_us_te] )- sum(WeeklySalesView[return_retail_us_te]) ),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (6 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -42 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Retail TE (7 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -49 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM ( WeeklySalesView[sales_total_retail_us_te] )- sum(WeeklySalesView[return_retail_us_te]) ),         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (7 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -49 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Retail TE (8 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -56 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM ( WeeklySalesView[sales_total_retail_us_te] )- sum(WeeklySalesView[return_retail_us_te]) ),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (8 Week(s) ago)

```sql
VAR CurrentDate =  [Seleced Date] VAR PrevDate = CurrentDate -56 VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (01)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 1
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 1
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (01)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 1)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 1))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (02)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 2
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 2
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (02)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 2)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 2))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (03)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 3
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 3
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (03)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 3)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 3))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (04)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 4
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 4
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] )  - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (04)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 4)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 4))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (05)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 5
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 5
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (05)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 5)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 5))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (06)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 6
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 6
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (06)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 6)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 6))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (07)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 7
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 7
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (07)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 7)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 7))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (08)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 8
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 8
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (08)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 8)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 8))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (09)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 9
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 9
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (09)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 9)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 9))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (10)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 10
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 10
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (10)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 10)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 10))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (11)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 11
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 11
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (11)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 11)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 11))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (12)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 12
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 12
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (12)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 12)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 12))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (13)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 13
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 13
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (13)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 13)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 13))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (14)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 14
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 14
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (14)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 14)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 14))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (15)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 15
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 15
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (15)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 15)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 15))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (16)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 16
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 16
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (16)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 16)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 16))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (17)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 17
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 17
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (17)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 17)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 17))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (18)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 18
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 18
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (18)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 18)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 18))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (19)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 19
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 19
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (19)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 19)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 19))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (20)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 20
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 20
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (20)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 20)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 20))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (21)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 21
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 21
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (21)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 21)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 21))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (22)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 22
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 22
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (22)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 22)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 22))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (23)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 23
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 23
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (23)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 23)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 23))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (24)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 24
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 24
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (24)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 24)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 24))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (25)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 25
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 25
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (25)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 25)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 25))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (26)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 26
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 26
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (26)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 26)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 26))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (27)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 27
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 27
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (27)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 27)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 27))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (28)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 28
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 28
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (28)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 28)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 28))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (29)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 29
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 29
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (29)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 29)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 29))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (30)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 30
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 30
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (30)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 30)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 30))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (31)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 31
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 31
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (31)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 31)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 31))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (32)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 32
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 32
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (32)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 32)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 32))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (33)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 33
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 33
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (33)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 33)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 33))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (34)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 34
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 34
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (34)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 34)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 34))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (35)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 35
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 35
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (35)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 35)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 35))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (36)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 36
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 36
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (36)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 36)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 36))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (37)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 37
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 37
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (37)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 37)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 37))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (38)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 38
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 38
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (38)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 38)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 38))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (39)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 39
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 39
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (39)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 39)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 39))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (40)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 40
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 40
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (40)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 40)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 40))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (41)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 41
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 41
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (41)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 41)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 41))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (42)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 42
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 42
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (42)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 42)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 42))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (43)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 43
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 43
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (43)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 43)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 43))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (44)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 44
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 44
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (44)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 44)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 44))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (45)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 45
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 45
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (45)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 45)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 45))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Net Sales Units (46)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 46
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 46
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (46)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 46)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 46))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (47)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 47
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 47
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (47)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 47)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 47))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (48)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 48
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 48
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (48)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 48)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 48))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (49)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 49
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 49
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (49)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 49)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 49))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (50)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 50
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 50
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (50)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 50)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 50))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (51)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 51
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 51
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (51)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 51)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 51))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (52)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 52
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 52
        )
    )
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE (52)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 52)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 52))  VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units (53)

```sql

VAR CurrentDate = [Seleced Date]
VAR PrevYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = CurrentDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 53
        )
    )
RETURN
    IF (
        MinDate = BLANK (),
        BLANK (),
        (
            VAR MaxDate =
                CALCULATE (
                    MAX ( 'date_dim'[actual_date] ),
                    FILTER (
                        ALL ( date_dim ),
                        'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 53
                    )
                )
            VAR Result =
                CALCULATE (
                    SUM ( WeeklySalesView[sales_total_units] ) - SUM( WeeklySalesView[return_units] ),
                    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
                )
            RETURN
                Result
        )
    )
```

### WeeklySalesView.Net Sales Retail TE (53)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 53))
RETURN IF(MinDate = BLANK(), BLANK() , (
VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 53)) 
VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result))
```

### WeeklySalesView.Net Sales Retail TE (1-53)

```sql
[Net Sales Retail TE (01)] + [Net Sales Retail TE (02)] + [Net Sales Retail TE (03)] + [Net Sales Retail TE (04)] + [Net Sales Retail TE (05)] + [Net Sales Retail TE (06)] + [Net Sales Retail TE (07)] + [Net Sales Retail TE (08)] + [Net Sales Retail TE (09)] + [Net Sales Retail TE (10)] + [Net Sales Retail TE (11)] + [Net Sales Retail TE (12)] + [Net Sales Retail TE (13)] + [Net Sales Retail TE (14)] + [Net Sales Retail TE (15)] + [Net Sales Retail TE (16)] + [Net Sales Retail TE (17)] + [Net Sales Retail TE (18)] + [Net Sales Retail TE (19)] + [Net Sales Retail TE (20)] + [Net Sales Retail TE (21)] + [Net Sales Retail TE (22)] + [Net Sales Retail TE (23)] + [Net Sales Retail TE (24)] + [Net Sales Retail TE (25)] + [Net Sales Retail TE (26)] + [Net Sales Retail TE (27)] + [Net Sales Retail TE (28)] + [Net Sales Retail TE (29)] + [Net Sales Retail TE (30)] + [Net Sales Retail TE (31)] + [Net Sales Retail TE (32)] + [Net Sales Retail TE (33)] + [Net Sales Retail TE (34)] + [Net Sales Retail TE (35)] + [Net Sales Retail TE (36)] + [Net Sales Retail TE (37)] + [Net Sales Retail TE (38)] + [Net Sales Retail TE (39)] + [Net Sales Retail TE (40)] + [Net Sales Retail TE (41)] + [Net Sales Retail TE (42)] + [Net Sales Retail TE (43)] + [Net Sales Retail TE (44)] + [Net Sales Retail TE (45)] + [Net Sales Retail TE (46)] + [Net Sales Retail TE (47)] + [Net Sales Retail TE (48)] + [Net Sales Retail TE (49)] + [Net Sales Retail TE (50)] + [Net Sales Retail TE (51)] + [Net Sales Retail TE (52)] + [Net Sales Retail TE (53)]
```

### WeeklySalesView.Net Sales Units ( Last 1 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1 


VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)


VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
       (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE ( Last 1 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1  

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)


VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
         SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.Net Sales Units ( Last 2 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1


VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)


VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2)

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.Net Sales Units ( Last 3 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 2

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear - 1, CurrentFiscalYear - 2)

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
       (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.Net Sales Units ( This Year)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR CurrentWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear))
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_week] = CurrentWeek
        )
    )
VAR Result =
    CALCULATE (
        (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units (year to Date Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR PrevYear = CurrentFiscalYear - 1

VAR YTDWeekDates =
    FILTER(
        ALL(date_dim),
        date_dim[fiscal_year] = PrevYear
        && date_dim[fiscal_week] <= CurrentFiscalWeek
    )

VAR MinDate = MINX(YTDWeekDates, date_dim[actual_date])
VAR MaxDate = MAXX(YTDWeekDates, date_dim[actual_date])

VAR Result =
    CALCULATE(
        (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.Net Sales Units ( 1 year(s) Ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear-1))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear-1))
VAR Result =
    CALCULATE (
        (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: discrepancy (1 Week(s) Ago)

```sql
0
// VAR SelectedDate = [Seleced Date]
// VAR N = 1
// VAR CurrentFiscalYear =
//     CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
// VAR CurrentFiscalWeek =
//     CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

// VAR TargetFiscalYear =
//     IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

// VAR LastWeekPrevYear =
//     MAXX (
//         FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
//         date_dim[fiscal_week]
//     )

// VAR TargetFiscalWeek =
//     IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
//         LastWeekPrevYear + ( CurrentFiscalWeek - N )
//     )


// VAR MinDate =
//     CALCULATE (
//         MIN ( date_dim[actual_date] ),
//         FILTER ( ALL ( date_dim ),
//             date_dim[fiscal_year] = TargetFiscalYear
//             && date_dim[fiscal_week] = TargetFiscalWeek
//         )
//     )
// VAR MaxDate =
//     CALCULATE (
//         MAX ( date_dim[actual_date] ),
//         FILTER ( ALL ( date_dim ),
//             date_dim[fiscal_year] = TargetFiscalYear
//             && date_dim[fiscal_week] = TargetFiscalWeek
//         )
//     )



// VAR Result =
//     CALCULATE(
//         SUM(weeklyOnHandView[on_hand_units]),
//         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
//         KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "4")
//     )

// RETURN
//     Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: Pending shrink (1 Week(s) Ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )



VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[shrink_actual_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: reserved cust order (1 Week(s) Ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )

VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[received_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: in transit ( Last 1 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[transfer_in_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: discrepancy ( Last 1 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear - 1 
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "4")
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: pending shrink ( Last 1 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[shrink_actual_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: reserved cust order ( Last 1 Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[received_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.Net Sales Units ( Periods 01 to Periods 12)

```sql
VAR SelectedDate = [Seleced Date]

VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear ))

VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear ))

VAR Result =
    CALCULATE (
         SUM ( weeklySalesView[sales_total_units] ),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )      

RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 01 to Periods 12)

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear ))

VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear ))
VAR Result =
    CALCULATE (
          SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )       
RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 01 to Periods 12)

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
   CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear ))
VAR Result =
    CALCULATE (
         SUM ( WeeklySalesView[sales_total_cost] ),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )       
RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 01)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 1))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =1))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 01)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 1 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 1 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 01)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 1 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 1 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 02)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 2))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =2))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 02)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 2 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 2 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 02)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 2 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 2 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 03)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 3))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =3))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 03)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 3 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 3 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 03)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 3 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 3 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 04)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 4))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =4))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 04)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 4 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 4 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 04)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 4 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 4 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 05)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 5))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =5))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 05)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 5 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 5 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 05)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 5 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 5 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 06)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 6))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =6))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 06)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 6 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 6 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 06)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 6 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 6 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 07)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 7))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =7))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 07)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 7 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 7 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 07)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 7 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 7 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 08)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 8))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =8))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 08)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 8 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 8 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 08)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 8 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 8 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 09)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 9))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =9))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 09)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 9 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 9 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 09)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 9 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 9 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 010)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 10))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =10))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 10)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 10 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 10 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 10)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 10 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 10 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 011)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 11))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =11))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 11)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 11 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 11 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 11)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 11 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 11 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Periods 012)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 12))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] =12))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_cost] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Units ( Periods 12)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 12 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 12 ))VAR Result =CALCULATE (SUM ( weeklySalesView[sales_total_units] ), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( Periods 12)

```sql
VAR SelectedDate = [Seleced Date]VAR SelectedYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )VAR MinDate =CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 12 ))VAR MaxDate =CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = 12 ))VAR Result =CALCULATE ( SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]), DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ))RETURN Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: in transit ( 1 Week(s) Ago )

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[transfer_in_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.Net Sales Units ( 2 year(s) Ago)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear-2))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = SelectedYear-2))
VAR Result =
    CALCULATE (
        (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Shrink Actual Units ( Period - 8 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear = CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod = CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetPeriod =
    IF ( SelectedPeriod - 8 > 0, SelectedPeriod - 8, 12 + ( SelectedPeriod - 8 ) )
VAR TargetYear =
    IF ( SelectedPeriod - 8 > 0, SelectedYear, SelectedYear - 1 )

VAR MinDate = CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod))
VAR Result =
CALCULATE (SUM ( WeeklySalesView[shrink_actual_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklySalesView.Shrink Actual Units ( Period - 7 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear = CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod = CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetPeriod =
    IF ( SelectedPeriod - 7 > 0, SelectedPeriod - 7, 12 + ( SelectedPeriod - 7 ) )
VAR TargetYear =
    IF ( SelectedPeriod - 7 > 0, SelectedYear, SelectedYear - 1 )

VAR MinDate = CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod))
VAR Result =
CALCULATE (SUM ( WeeklySalesView[shrink_actual_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklySalesView.Shrink Actual Units ( Period - 6 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear = CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod = CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetPeriod =
    IF ( SelectedPeriod - 6 > 0, SelectedPeriod - 6, 12 + ( SelectedPeriod - 6 ) )
VAR TargetYear =
    IF ( SelectedPeriod - 6 > 0, SelectedYear, SelectedYear - 1 )

VAR MinDate = CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod))
VAR Result =
CALCULATE (SUM ( WeeklySalesView[shrink_actual_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklySalesView.Shrink Actual Units ( Period - 5 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear = CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod = CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetPeriod =
    IF ( SelectedPeriod - 5 > 0, SelectedPeriod - 5, 12 + ( SelectedPeriod - 5 ) )
VAR TargetYear =
    IF ( SelectedPeriod - 5 > 0, SelectedYear, SelectedYear - 1 )

VAR MinDate = CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod))
VAR Result =
CALCULATE (SUM ( WeeklySalesView[shrink_actual_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklySalesView.Shrink Actual Units ( Period - 4 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear = CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod = CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetPeriod =
    IF ( SelectedPeriod - 4 > 0, SelectedPeriod - 4, 12 + ( SelectedPeriod - 4 ) )
VAR TargetYear =
    IF ( SelectedPeriod - 4 > 0, SelectedYear, SelectedYear - 1 )

VAR MinDate = CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod))
VAR Result =
CALCULATE (SUM ( WeeklySalesView[shrink_actual_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklySalesView.Shrink Actual Units ( Period - 3 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear = CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod = CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetPeriod =
    IF ( SelectedPeriod - 3 > 0, SelectedPeriod - 3, 12 + ( SelectedPeriod - 3 ) )
VAR TargetYear =
    IF ( SelectedPeriod - 3 > 0, SelectedYear, SelectedYear - 1 )

VAR MinDate = CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod))
VAR Result =
CALCULATE (SUM ( WeeklySalesView[shrink_actual_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklySalesView.Shrink Actual Units ( Period - 2 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear = CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod = CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetPeriod =
    IF ( SelectedPeriod - 2 > 0, SelectedPeriod - 2, 12 + ( SelectedPeriod - 2 ) )
VAR TargetYear =
    IF ( SelectedPeriod - 2 > 0, SelectedYear, SelectedYear - 1 )

VAR MinDate = CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod))
VAR Result =
CALCULATE (SUM ( WeeklySalesView[shrink_actual_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklySalesView.Shrink Actual Units ( Period - 1 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear = CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod = CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetPeriod =
    IF ( SelectedPeriod - 1 > 0, SelectedPeriod - 1, 12 + ( SelectedPeriod - 1 ) )
VAR TargetYear =
    IF ( SelectedPeriod - 1 > 0, SelectedYear, SelectedYear - 1 )

VAR MinDate = CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod))
VAR Result =
CALCULATE (SUM ( WeeklySalesView[shrink_actual_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklySalesView.Shrink Actual Units ( From Period 8 to 1)

```sql
[Shrink Actual Units ( Period - 8 )] + [Shrink Actual Units ( Period - 7 )] + [Shrink Actual Units ( Period - 6 )] + [Shrink Actual Units ( Period - 5 )] + [Shrink Actual Units ( Period - 4 )] + [Shrink Actual Units ( Period - 3 )] + [Shrink Actual Units ( Period - 2 )] + [Shrink Actual Units ( Period - 1 )]
```

### WeeklySalesView.CUR WK SLS

```sql

VAR CurrentDate = TODAY()
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX('date_dim'[fiscal_week]), 'date_dim'[actual_date] = CurrentDate)
VAR SelectedLocation = SELECTEDVALUE('d365LocationMapping_View'[LocationCode])
VAR Currentdatekey = CALCULATE(MAX('date_dim'[date_key]), FILTER( ALL(date_dim), 'date_dim'[fiscal_week] = CurrentFiscalWeek
    && 'date_dim'[fiscal_year] = CurrentFiscalYear))
VAR Result =
CALCULATE(
    SUM(WeeklySalesView[sales_total_units]),
    'date_dim'[date_key]=Currentdatekey
)
RETURN Result
```

### WeeklySalesView.Net Sales Cost ( Quarter 01 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_cost] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Cost ( Quarter 02 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_cost] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Cost ( Quarter 03 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_cost] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Cost ( Quarter 04 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_cost] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Retail ( Quarter 01 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_retail] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Retail ( Quarter 02 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_retail] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Retail ( Quarter 03 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_retail] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Retail ( Quarter 04 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_retail] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Units ( Quarter 01 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Units ( Quarter 02 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Units ( Quarter 03 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Units ( Quarter 04 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
RETURN
CALCULATE (
    SUM ( 'WeeklySalesView'[sales_total_units] ),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Cost ( Quarter 01 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
RETURN
CALCULATE (
    SUMX ('WeeklySalesView', 'WeeklySalesView'[received_units]* RELATED('product_dim_le'[costprice]) ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Cost ( Quarter 02 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
RETURN
CALCULATE (
    SUMX ('WeeklySalesView', 'WeeklySalesView'[received_units]* RELATED('product_dim_le'[costprice]) ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Cost ( Quarter 03 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
RETURN
CALCULATE (
    SUMX ('WeeklySalesView', 'WeeklySalesView'[received_units]* RELATED('product_dim_le'[costprice]) ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Cost ( Quarter 04 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
RETURN
CALCULATE (
    SUMX ('WeeklySalesView', 'WeeklySalesView'[received_units]* RELATED('product_dim_le'[costprice]) ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Retatil ( Quarter 01 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
RETURN
CALCULATE (
    SUM ('WeeklySalesView'[received_retail] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Retatil ( Quarter 02 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
RETURN
CALCULATE (
    SUM ('WeeklySalesView'[received_retail] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Retatil ( Quarter 03 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
RETURN
CALCULATE (
    SUM ('WeeklySalesView'[received_retail] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Retatil ( Quarter 04 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
RETURN
CALCULATE (
    SUM ('WeeklySalesView'[received_retail] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Units ( Quarter 01 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 1
        )
    )
RETURN
CALCULATE (
    SUM ('WeeklySalesView'[received_units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Units ( Quarter 02 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 2
        )
    )
RETURN
CALCULATE (
    SUM ('WeeklySalesView'[received_units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Units ( Quarter 03 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 3
        )
    )
RETURN
CALCULATE (
    SUM ('WeeklySalesView'[received_units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Receipts Units ( Quarter 04 )

```sql
VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER(
            ALL('date_dim'),
            'date_dim'[fiscal_year] = SelectedYear &&
            'date_dim'[fiscal_quarter] = 4
        )
    )
RETURN
CALCULATE (
    SUM ('WeeklySalesView'[received_units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
```

### WeeklySalesView.Net Sales Units ( Form Periods 1 to 8)

```sql
[Net Sales Units ( Periods 01)]  + [Net Sales Units ( Periods 02)] + [Net Sales Units ( Periods 03)] + [Net Sales Units ( Periods 04)] + [Net Sales Units ( Periods 05)] + [Net Sales Units ( Periods 06)] + [Net Sales Units ( Periods 07)] + [Net Sales Units ( Periods 08)]
```

### WeeklySalesView.Received Units ( Week 01)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 1)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 1))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 02)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 2)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 2))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 03)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 3)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 3))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 04)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 4)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 4))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 05)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 5)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 5))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 06)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 6)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 6))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 07)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 7)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 7))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 08)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 8)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 8))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 09)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 9)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 9))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 10)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 10)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 10))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 11)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 11)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 11))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 12)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 12)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 12))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Received Units ( Week 13)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 13)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 13))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 14)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 14)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 14))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 15)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 15)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 15))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 16)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 16)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 16))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 17)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 17)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 17))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 18)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 18)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 18))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 19)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 19)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 19))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 20)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 20)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 20))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 21)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 21)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 21))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 22)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 22)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 22))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 23)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 23)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 23))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 24)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 24)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 24))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 25)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 25)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 25))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 26)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 26)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 26))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 27)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 27)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 27))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 28)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 28)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 28))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Received Units ( Week 29)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 29)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 29))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 30)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 30)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 30))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 31)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 31)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 31))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 32)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 32)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 32))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 33)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 33)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 33))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 34)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 34)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 34))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 35)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 35)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 35))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 36)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 36)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 36))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 37)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 37)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 37))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 38)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 38)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 38))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 39)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 39)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 39))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 40)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 40)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 40))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 41)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 41)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 41))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 42)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 42)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 42))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 43)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 43)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 43))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 44)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 44)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 44))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Received Units ( Week 45)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 45)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 45))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 46)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 46)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 46))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) RETURN Result
```

### WeeklySalesView.Received Units ( Week 47)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 47)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 47))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 48)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 48)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 48))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 49)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 49)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 49))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 50)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 50)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 50))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 51)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 51)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 51))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 52)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 52)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 52))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Received Units ( Week 53)

```sql
VAR CurrentDate =  [Seleced Date]  
VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 53))
RETURN IF(MinDate = BLANK(), BLANK() , ( 
VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 53))  
VAR Result =  CALCULATE ( SUM ( WeeklySalesView[return_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) 
RETURN Result))
```

### WeeklySalesView.Received Units Week (1-53)

```sql
[Received Units ( Week 01)] + [Received Units ( Week 02)] + [Received Units ( Week 03)] + [Received Units ( Week 04)] + [Received Units ( Week 05)] + [Received Units ( Week 06)] + [Received Units ( Week 07)] + [Received Units ( Week 08)] + [Received Units ( Week 09)] + [Received Units ( Week 10)] + [Received Units ( Week 11)] + [Received Units ( Week 12)] + [Received Units ( Week 13)] + [Received Units ( Week 14)] + [Received Units ( Week 15)] + [Received Units ( Week 16)] + [Received Units ( Week 17)] + [Received Units ( Week 18)] + [Received Units ( Week 19)] + [Received Units ( Week 20)] + [Received Units ( Week 21)] + [Received Units ( Week 22)] + [Received Units ( Week 23)] + [Received Units ( Week 24)] + [Received Units ( Week 25)] + [Received Units ( Week 26)] + [Received Units ( Week 27)] + [Received Units ( Week 28)] + [Received Units ( Week 29)] + [Received Units ( Week 30)] + [Received Units ( Week 31)] + [Received Units ( Week 32)] + [Received Units ( Week 33)] + [Received Units ( Week 34)] + [Received Units ( Week 35)] + [Received Units ( Week 36)] + [Received Units ( Week 37)] + [Received Units ( Week 38)] + [Received Units ( Week 39)] + [Received Units ( Week 40)] + [Received Units ( Week 41)] + [Received Units ( Week 42)] + [Received Units ( Week 43)] + [Received Units ( Week 44)] + [Received Units ( Week 45)] + [Received Units ( Week 46)] + [Received Units ( Week 47)] + [Received Units ( Week 48)] + [Received Units ( Week 49)] + [Received Units ( Week 50)] + [Received Units ( Week 51)] + [Received Units ( Week 52)] + [Received Units ( Week 53)]
```

### WeeklySalesView.Net Sales Units ( Last 2 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -2))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -2))
VAR Result =
    CALCULATE(
        (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last Year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -1))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -1))
VAR Result =
    CALCULATE(
       (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units (Last 5 weeks total)

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX('date_dim'[fiscal_week]) , 'date_dim'[actual_date] = CurrentDate)
VAR LastYearWeek =
    MAXX(
    FILTER(
        ALL('date_dim'),
        'date_dim'[fiscal_year] = CurrentFiscalYear -1
    ),
    'date_dim'[fiscal_week]
)
VAR TargetDates =
    FILTER(
        ALL('date_dim'),
        ( 'date_dim'[fiscal_year] = CurrentFiscalYear &&
          'date_dim'[fiscal_week] < CurrentFiscalWeek &&
          'date_dim'[fiscal_week] >= CurrentFiscalWeek - 5 )
        ||
        ( 'date_dim'[fiscal_year] = CurrentFiscalYear - 1 &&
          'date_dim'[fiscal_week] >= LastYearWeek - (5 - CurrentFiscalWeek +1)&&
          'date_dim'[fiscal_week] < LastYearWeek )
    )
 
VAR MinDate = MINX(TargetDates, 'date_dim'[actual_date])
VAR MaxDate = MAXX(TargetDates, 'date_dim'[actual_date])
 
VAR Result =
CALCULATE(
    SUM(WeeklySalesView[sales_total_units]),
     DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### WeeklySalesView.Average Net Sale Unit (Last 5 weeks total)

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX('date_dim'[fiscal_week]) , 'date_dim'[actual_date] = CurrentDate)
VAR LastYearWeek =
    MAXX(
    FILTER(
        ALL('date_dim'),
        'date_dim'[fiscal_year] = CurrentFiscalYear -1
    ),
    'date_dim'[fiscal_week]
)
VAR TargetDates =
    FILTER(
        ALL('date_dim'),
        ( 'date_dim'[fiscal_year] = CurrentFiscalYear &&
          'date_dim'[fiscal_week] < CurrentFiscalWeek &&
          'date_dim'[fiscal_week] >= CurrentFiscalWeek - 5 )
        ||
        ( 'date_dim'[fiscal_year] = CurrentFiscalYear - 1 &&
          'date_dim'[fiscal_week] >= LastYearWeek - (5 - CurrentFiscalWeek +1)&&
          'date_dim'[fiscal_week] < LastYearWeek )
    )
 
VAR MinDate = MINX(TargetDates, 'date_dim'[actual_date])
VAR MaxDate = MAXX(TargetDates, 'date_dim'[actual_date])
 
VAR Result =
CALCULATE(
    SUM(WeeklySalesView[sales_total_units]),
   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
 
RETURN Result / 5
```

### WeeklySalesView.Net Sales Units ( Last 3 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -3))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -3))
VAR Result =
    CALCULATE(
        (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last 4 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -4))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -4))
VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[sales_total_units]),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last 5 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -5))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -5))
VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[sales_total_units]),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last 6 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -6))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -6))
VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[sales_total_units]),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last 7 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -7))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -7))
VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[sales_total_units]),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last 8 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -8))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -8))
VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[sales_total_units]),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last 9 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -9))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -9))
VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[sales_total_units]),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last 10 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -10))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -10))
VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[sales_total_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last 11 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -11))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -12))
VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[sales_total_units]),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Units ( Last 12 year )

```sql

VAR CurrentDate = [Seleced Date]
VAR CurrentFiscalYear =
    CALCULATE(MAX('date_dim'[fiscal_year]), 'date_dim'[actual_date] = CurrentDate)
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -12))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = CurrentFiscalYear -12))
VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[sales_total_units]),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Net Sales Retail TE ( From Week 07 to 09 )

```sql
[Net Sales Retail TE (07)] + [Net Sales Retail TE (08)] + [Net Sales Retail TE (09)]
```

### WeeklySalesView.Net Sales Units ( From Week 07 to 09 )

```sql
[Net Sales Units (07)] + [Net Sales Units (08)] + [Net Sales Units (09)]
```

### WeeklySalesView.Net Sales Cost (Week 01)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 1)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 1)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
        )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 02)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 2)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 2)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 03)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 3)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 3)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 04)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 4)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 4)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 05)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 5)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 5)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 06)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 6)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 6)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 07)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 7)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 7)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 08)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 8)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 8)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 09)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 9)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 9)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 10)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 10)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 10)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 11)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 11)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 11)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 12)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 12)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 12)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 13)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 13)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 13)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 14)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 14)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 14)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 15)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 15)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 15)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 16)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 16)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 16)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 17)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 17)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 17)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 18)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 18)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 18)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 19)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 19)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 19)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 20)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 20)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 20)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 21)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 21)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 21)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 22)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 22)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 22)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 23)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 23)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 23)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 24)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 24)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 24)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 25)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 25)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 25)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 26)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 26)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 26)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 27)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 27)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 27)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 28)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 28)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 28)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 29)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 29)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 29)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 30)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 30)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 30)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 31)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 31)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 31)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 32)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 32)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 32)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 33)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 33)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 33)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 34)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 34)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 34)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 35)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 35)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 35)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 36)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 36)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 36)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 37)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 37)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 37)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 38)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 38)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 38)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 39)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 39)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 39)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 40)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 40)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 40)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 41)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 41)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 41)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 42)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 42)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 42)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 43)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 43)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 43)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 44)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 44)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 44)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 45)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 45)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 45)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 46)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 46)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 46)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 47)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 47)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 47)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 48)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 48)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 48)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 49)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 49)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 49)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 50)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 50)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 50)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 51)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 51)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 51)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 52)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 52)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 52)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.Net Sales Cost (Week 53)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 53)
    )
RETURN IF(MinDate=BLANK(),BLANK(),( 
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear
            && 'date_dim'[fiscal_week] = 53)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result))
```

### WeeklySalesView.Net Sales Cost ( From Week 07 to 09 )

```sql
[Net Sales Cost (Week 07)]+[Net Sales Cost (Week 08)]+[Net Sales Cost (Week 09)]
```

### WeeklySalesView.Net Sales Retail TE ( From Week 07 to 09 Ly)

```sql

VAR CurrentDate =  [Seleced Date]  
VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate )
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear - 1 && 'date_dim'[fiscal_week] = 7)) 
VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear - 1 && 'date_dim'[fiscal_week] = 9))  
VAR Result =  CALCULATE (  SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) 
RETURN Result
```

### WeeklySalesView.Met Sales Units ( From Week 07 to 09 Ly)

```sql

VAR CurrentDate =  [Seleced Date]  
VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear - 1 && 'date_dim'[fiscal_week] = 7)) 
VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear - 1 && 'date_dim'[fiscal_week] = 9)) 
VAR Result =  CALCULATE ( SUM ( WeeklySalesView[sales_total_units] ),          DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result
```

### WeeklySalesView.Net Sales Cost ( From Week 07 to 09 Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear - 1
            && 'date_dim'[fiscal_week] = 7)
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL(date_dim),
            'date_dim'[fiscal_year] = SelectedYear - 1
            && 'date_dim'[fiscal_week] = 9)
    )
VAR Result =
    CALCULATE (
        SUM ( weeklySalesView[sales_total_cost] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN
    Result
```

### WeeklySalesView.US Web LW U SLS

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR LastWeek = 
    CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = SelectedPeriod ))

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_week] = LastWeek ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_week] = LastWeek ))
VAR Result =
    CALCULATE (
         SUM(WeeklySalesView[sales_total_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
---- MODEL MEASURES END ----
```

### WeeklySalesView.UK Web LW U SLS

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR LastWeek = 
    CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = SelectedPeriod ))

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_week] = LastWeek ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER ( ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_week] = LastWeek ))

VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ),
         DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        TREATAS ( VALUES ( product_dim_le[UK ProductKey] ), WeeklySalesView[product_key] ),
        TREATAS ( VALUES ( d365LocationMapping_View[LocationKey] ), WeeklySalesView[LocationKey] )
    )
RETURN Result
```

### WeeklySalesView.AUR US

```sql

VAR SelectedDate = [Seleced Date]  
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR SelectedWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_week] = SelectedWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_week] = SelectedWeek
        )
    )
VAR Result =
    DIVIDE (
        CALCULATE (
            SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
        ),
        CALCULATE (
            SUM ( WeeklySalesView[sales_total_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
        )
    )
RETURN
     Result
```

### WeeklySalesView.AUR UK

```sql

VAR SelectedDate = [Seleced Date]  
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR SelectedWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_week] = SelectedWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_week] = SelectedWeek
        )
    )
VAR Result =
    DIVIDE (
        CALCULATE (
            SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
            TREATAS(VALUES(product_dim_le[UK ProductKey]),WeeklySalesView[product_key])
        ),
        CALCULATE (
            SUM ( WeeklySalesView[sales_total_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
            TREATAS(VALUES(product_dim_le[UK ProductKey]),WeeklySalesView[product_key])
        )
    )
RETURN
     Result
```

### WeeklySalesView.Net Sales Retail TE ( 1 Period(s) Ago )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR TargetYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER ( ALL ( 'date_dim' ), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER ( ALL ( 'date_dim' ), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))

/*
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = TargetYear, 'date_dim'[fiscal_period] = TargetPeriod )
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), 'date_dim'[fiscal_year] = TargetYear, 'date_dim'[fiscal_period] = TargetPeriod )
*/
VAR Result =
    CALCULATE (
         SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### WeeklySalesView.Royalty Due ( 1 Period(s) Ago )

```sql

SUMX(
    VALUES(product_dim_le[product_key] ),
    VAR Rate =
        COALESCE( MAX( product_dim_le[RoyaltyPercent] ), 0 )
    VAR SalesPrev =
        CALCULATE( [sales_total_retail_us_te ( 1 month Ago )] )
    RETURN
        SalesPrev * Rate
)
```

### WeeklySalesView.Net Sales Units ( Current Week Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0


VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)


VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
       (SUM (WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units])),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.Net Sales Retail TE ( Current Week Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0

VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)


VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
         SUM ( WeeklySalesView[sales_total_retail_us_te] ) - SUM(WeeklySalesView[return_retail_us_te]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: discrepancy (Current Week)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )



VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "4")
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: Pending shrink (Current Week)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )



VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[shrink_actual_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: reserved cust order (Current Week)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 1
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear, CurrentFiscalYear - 1 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )

VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[received_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: in transit ( Current Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[transfer_in_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: discrepancy ( Current Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear -1 
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )



VAR Result =
    CALCULATE(
        SUM(weeklyOnHandView[on_hand_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ),
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "4")
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: pending shrink ( Current Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear -1 
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )


VAR Result =
    CALCULATE(
        SUM(WeeklySalesView[shrink_actual_units]),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    Result
```

### WeeklySalesView.EOP OH Units:Inv StatusUnavail: reserved cust order ( Current Weeks Ly)

```sql

VAR SelectedDate = [Seleced Date]
VAR N = 0
VAR CurrentFiscalYear =
    CALCULATE(MAX(date_dim[fiscal_year]), date_dim[actual_date] = SelectedDate)
VAR CurrentFiscalWeek =
    CALCULATE(MAX(date_dim[fiscal_week]), date_dim[actual_date] = SelectedDate)

VAR TargetFiscalYear = CurrentFiscalYear-1
    //IF ( CurrentFiscalWeek - N > 0, CurrentFiscalYear-1, CurrentFiscalYear - 2 )

VAR LastWeekPrevYear =
    MAXX (
        FILTER ( ALL ( date_dim ), date_dim[fiscal_year] = TargetFiscalYear ),
        date_dim[fiscal_week]
    )

VAR TargetFiscalWeek =
    IF ( CurrentFiscalWeek - N > 0, CurrentFiscalWeek - N,
        LastWeekPrevYear + ( CurrentFiscalWeek - N )
    )


VAR MinDate =
    CALCULATE (
        MIN ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )
VAR MaxDate =
    CALCULATE (
        MAX ( date_dim[actual_date] ),
        FILTER ( ALL ( date_dim ),
            date_dim[fiscal_year] = TargetFiscalYear
            && date_dim[fiscal_week] = TargetFiscalWeek
        )
    )

VAR Result =    
        CALCULATE( SUM(weeklyOnHandView[on_hand_units]), 
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ), 
        KEEPFILTERS(weeklyOnHandView[inventory_status_id] = "9") )       
    
RETURN
    Result
```

### WeeklySalesView.Net receipt Units ( Week 01)

```sql
VAR CurrentDate =  [Seleced Date]  VAR PrevYear =  CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = CurrentDate ) VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear && 'date_dim'[fiscal_week] = 1)) VAR MaxDate =  CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] =  PrevYear && 'date_dim'[fiscal_week] = 3))  VAR Result =  CALCULATE ( SUM ( WeeklySalesView[received_units] ),  DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )) RETURN Result
```

### WeeklySalesView.Net Sales Units ( 1 Week(s) ago )

```sql

VAR CurrentDate =  [Seleced Date] 
VAR PrevDate = CurrentDate -7 
VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) 
VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units])),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN COALESCE(Result,0)
```

### WeeklySalesView.Net Sales Units ( 2 Week(s) ago )

```sql
VAR CurrentDate =  [Seleced Date] 
VAR PrevDate = CurrentDate -14 
VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) 
VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units])),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN COALESCE(Result,0)
```

### WeeklySalesView.Net Sales Units ( 3 Week(s) ago )

```sql
VAR CurrentDate =  [Seleced Date] 
VAR PrevDate = CurrentDate -21 
VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) 
VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units])),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN COALESCE(Result,0)
```

### WeeklySalesView.Net Sales Units ( 4 Week(s) ago )

```sql
VAR CurrentDate =  [Seleced Date] 
VAR PrevDate = CurrentDate -28 
VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) 
VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units])),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN COALESCE(Result,0)
```

### WeeklySalesView.Net Sales Units ( 5 Week(s) ago )

```sql
VAR CurrentDate =  [Seleced Date] 
VAR PrevDate = CurrentDate -35 
VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) 
VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units])),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result
```

### WeeklySalesView.Net Sales Units ( 6 Week(s) ago )

```sql
VAR CurrentDate =  [Seleced Date] 
VAR PrevDate = CurrentDate -42 
VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) 
VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units])),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result
```

### WeeklySalesView.Net Sales Units ( 7 Week(s) ago )

```sql
VAR CurrentDate =  [Seleced Date] 
VAR PrevDate = CurrentDate -49 
VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) 
VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units])),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result
```

### WeeklySalesView.Net Sales Units ( 8 Week(s) ago )

```sql
VAR CurrentDate =  [Seleced Date] 
VAR PrevDate = CurrentDate -56 
VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) 
VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units])),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result
```

### WeeklySalesView.Net Sales Units ( This Week )

```sql
VAR CurrentDate =  [Seleced Date] 
VAR PrevDate = CurrentDate -0 
VAR PrevYear =CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = PrevDate) 
VAR PrevWeek = CALCULATE ( MAX ( 'date_dim'[fiscal_week] ), 'date_dim'[actual_date] = PrevDate ) 
VAR MinDate =  CALCULATE ( MIN ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR MaxDate = CALCULATE ( MAX ( 'date_dim'[actual_date] ), 
    FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PrevYear  && 'date_dim'[fiscal_week] = PrevWeek )) 
VAR Result =  CALCULATE ( (SUM (WeeklySalesView[sales_total_units])),   DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate ) ) 
RETURN Result
```

### WeeklySalesView.Net receipts retail (month)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

RETURN
    Result
```

### WeeklySalesView.Permanent markdowns (month)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

RETURN
    Result
```

### WeeklySalesView.Promo (month)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

RETURN
    Result
```

### WeeklySalesView.Shrink (month)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

RETURN
    Result
```

### WeeklySalesView.Net receipts retail (month 1)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 2)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 3)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 4)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 5)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 6)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 7)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 8)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 9)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 10)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 11)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail (month 12)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 1)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 2)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 3)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 4)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 5)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 6)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 7)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 8)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 9)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 10)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 11)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 12)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 1)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 2)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 3)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 4)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 5)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 6)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 7)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 8)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 9)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 10)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 11)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo (month 12)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 1)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 2)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 3)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 4)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 5)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 6)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 7)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 8)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 9)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 10)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 11)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink (month 12)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 1 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 2 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 3 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 4 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 5 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 6 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 7 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 8 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 9 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 10 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 11 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Shrink ( month 12 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[shrink_actual_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 1 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 2 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 3 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 4 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 5 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 6 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 7 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 8 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 9 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 10 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 11 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Promo ( month 12 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[promo_pc_total_retail_te] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 1) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 2) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 3) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 4) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 5) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 6) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 7) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 8) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 9) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 10) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 11) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Permanent markdowns (month 12) 1

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[perm_md_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 1 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 2 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 3 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 4 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 5 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 6 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 7 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 8 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 9 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 10 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 11 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net receipts retail ( month 12 )

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[received_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month)

```sql

VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[month] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[month] = SelectedMonth
        )
    )

VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )

RETURN
    Result
```

### WeeklySalesView.Sales Retail (month 1)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 1
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 2)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 2
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 3)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 3
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 4)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 4
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 5)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 5
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 6)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 6
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 7)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 7
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 8)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 8
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 9)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 9
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 10)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 10
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 11)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 11
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Sales Retail (month 12)

```sql
VAR SelectedDate =
    [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedMonth =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = 12
        )
    )

VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedMonth
        )
    )

RETURN
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail] ),
        DATESBETWEEN (
            'date_dim'[actual_date],
            MinDate,
            MaxDate
        )
    )
```

### WeeklySalesView.Net Sales Units (Last 3 Periods)

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear = LOOKUPVALUE('date_dim'[fiscal_year],'date_dim'[actual_date],SelectedDate)
VAR SelectedPeriod = LOOKUPVALUE('date_dim'[fiscal_period],'date_dim'[actual_date],SelectedDate)
VAR HasAnchor = NOT( ISBLANK(SelectedDate) || ISBLANK(SelectedYear) || ISBLANK(SelectedPeriod) )
VAR SelectedPIndex = SelectedYear*12 + SelectedPeriod
RETURN
IF( NOT HasAnchor, BLANK(),
    CALCULATE(
      SUM(WeeklySalesView[sales_total_units]) - SUM(WeeklySalesView[return_units]),
      FILTER(
         ALL('date_dim'),
         'date_dim'[fiscal_year]*12 + 'date_dim'[fiscal_period] >= SelectedPIndex - 3
         && 'date_dim'[fiscal_year]*12 + 'date_dim'[fiscal_period] <= SelectedPIndex - 1
      )
    )
)
```

### WeeklySalesView.Net Sales Retail (Last 3 Periods)

```sql

VAR SelectedDate = [Seleced Date]

/* Anchor to the selected date, independent of current date filters */
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )

VAR SelectedPeriod =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        FILTER ( ALL ( 'date_dim' ), 'date_dim'[actual_date] = SelectedDate )
    )

/* Defensive: if SelectedDate isn't resolvable to a year/period, return BLANK */
VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedPeriod )

/* Continuous fiscal period index (12 periods per fiscal year) */
VAR SelectedPIndex =
    SelectedYear * 12 + SelectedPeriod

RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail_us_te] )
            - SUM ( WeeklySalesView[return_retail_us_te] ),
        FILTER (
            ALL ( 'date_dim' ),
            VAR PIndex =
                'date_dim'[fiscal_year] * 12 + 'date_dim'[fiscal_period]
            RETURN
                PIndex >= SelectedPIndex - 3
                    && PIndex <= SelectedPIndex - 1
        )
    )
)
```

### WeeklySalesView.Net Sales Units

```sql
SUM ( WeeklySalesView[sales_total_units] ) - SUM(WeeklySalesView[return_units])
```

### WeeklySalesView.Net Sales Units ( Current Period )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR SelectedPeriod =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedPeriod )
RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] )
            - SUM ( WeeklySalesView[return_units] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedPeriod
        )
    )
)
```

### WeeklySalesView.Net Sales Retail TE ( Current Period )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR SelectedPeriod =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedPeriod )
RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail_us_te] )
            - SUM ( WeeklySalesView[return_retail_us_te] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedPeriod
        )
    )
)
```

### WeeklySalesView.sales_total_retail_us_te ( Current Period )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR SelectedPeriod =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedPeriod )
RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail_us_te] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_period] = SelectedPeriod
        )
    )
)
```

### WeeklySalesView.Royalty Due ( Current Period )

```sql

VAR RowRoyaltyDue =
    [Net Sales Retail TE ( Current Period )]
        * COALESCE ( SELECTEDVALUE ( product_dim_le[RoyaltyPercent] ), 0 )
RETURN
IF (
    ISINSCOPE ( product_dim_le[product_key] ),
    RowRoyaltyDue,
    SUMX (
        VALUES ( product_dim_le[product_key] ),
        CALCULATE (
            [Net Sales Retail TE ( Current Period )]
                * COALESCE ( SELECTEDVALUE ( product_dim_le[RoyaltyPercent] ), 0 )
        )
    )
)
```

### WeeklySalesView.Net Sales Units (Current + Prior 2 Periods)

```sql

VAR SelectedDate = [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedPeriod =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedPeriod )

VAR SelectedPIndex =
    SelectedYear * 12 + SelectedPeriod

RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] )
            - SUM ( WeeklySalesView[return_units] ),
        FILTER (
            ALL ( 'date_dim' ),
            'date_dim'[fiscal_year] * 12 + 'date_dim'[fiscal_period] >= SelectedPIndex - 2
                && 'date_dim'[fiscal_year] * 12 + 'date_dim'[fiscal_period] <= SelectedPIndex
        )
    )
)
```

### WeeklySalesView.Net Sales Retail TE (Current + Prior 2 Periods)

```sql

VAR SelectedDate = [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR SelectedPeriod =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_period] ),
        REMOVEFILTERS ( 'date_dim' ),
        'date_dim'[actual_date] = SelectedDate
    )

VAR HasAnchor =
    NOT ISBLANK ( SelectedDate )
        && NOT ISBLANK ( SelectedYear )
        && NOT ISBLANK ( SelectedPeriod )

VAR SelectedPIndex =
    SelectedYear * 12 + SelectedPeriod

RETURN
IF (
    NOT HasAnchor,
    BLANK (),
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_retail_us_te] )
            - SUM ( WeeklySalesView[return_retail_us_te] ),
        FILTER (
            ALL ( 'date_dim' ),
            VAR PIndex =
                'date_dim'[fiscal_year] * 12 + 'date_dim'[fiscal_period]
            RETURN
                PIndex >= SelectedPIndex - 2
                    && PIndex <= SelectedPIndex
        )
    )
)
```

### WeeklySalesView.Royalty Due (Current + Prior 2 Periods)

```sql

VAR RowRoyaltyDue =
    [Net Sales Retail TE (Current + Prior 2 Periods)]
        * COALESCE ( SELECTEDVALUE ( product_dim_le[RoyaltyPercent] ), 0 )
RETURN
IF (
    ISINSCOPE ( product_dim_le[product_key] ),
    RowRoyaltyDue,
    SUMX (
        VALUES ( product_dim_le[product_key] ),
        CALCULATE (
            [Net Sales Retail TE (Current + Prior 2 Periods)]
                * COALESCE ( SELECTEDVALUE ( product_dim_le[RoyaltyPercent] ), 0 )
        )
    )
)
```

### WeeklySalesView.Net Sales Units ( This Year) - DEBUG

```sql

VAR SelectedDate = [Seleced Date]

VAR SelectedYear =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_year] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR CurrentWeek =
    CALCULATE (
        MAX ( 'date_dim'[fiscal_week] ),
        'date_dim'[actual_date] = SelectedDate
    )
VAR MinDate =
    CALCULATE (
        MIN ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = SelectedYear
        )
    )

VAR MaxDate =
    CALCULATE (
        MAX ( 'date_dim'[actual_date] ),
        FILTER (
            ALL ( date_dim ),
            'date_dim'[fiscal_year] = SelectedYear
                && 'date_dim'[fiscal_week] = CurrentWeek
        )
    )

VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] )
            - SUM ( WeeklySalesView[return_units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )

RETURN
    "SelectedDate: " & FORMAT ( SelectedDate, "yyyy-mm-dd" ) &
    " | Year: " & COALESCE ( SelectedYear, -1 ) &
    " | MinDate: " & FORMAT ( MinDate, "yyyy-mm-dd" ) &
    " | MaxDate: " & FORMAT ( MaxDate, "yyyy-mm-dd" ) &
    " | Result: " & FORMAT ( Result, "#,##0" )
```

### PurchasingTransView.On Order Units ( Past Due Periods )

```sql

VAR SelectedDate =
    [Seleced Date] 
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )

VAR PastYear =
    IF ( SelectedPeriod = 1, SelectedYear - 1, SelectedYear )
VAR PastPeriod =
    IF ( SelectedPeriod = 1, 12, SelectedPeriod - 1 )

VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = PastYear && 'date_dim'[fiscal_period] = PastPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_week] = PastYear && 'date_dim'[fiscal_period] = PastPeriod ))
VAR Result = 
CALCULATE (
    SUM ( PurchasingTransView[on order units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### PurchasingTransView.On Order Units ( This Period )

```sql

VAR SelectedDate =
    [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = SelectedPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = SelectedYear && 'date_dim'[fiscal_period] = SelectedPeriod ))
VAR Result =
CALCULATE (
    SUM ( PurchasingTransView[on order units] ),
    DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
)
RETURN Result
```

### PurchasingTransView.On Order Units ( Next 1 Periods )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetYear =
    IF ( SelectedPeriod + 1 > 12, SelectedYear + 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod + 1 > 12, SelectedPeriod + 1 - 12, SelectedPeriod + 1 )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear &&  'date_dim'[fiscal_period] = TargetPeriod ))
VAR Result =
    CALCULATE (
        SUM ( PurchasingTransView[on order units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### PurchasingTransView.On Order Units ( Next 2 Periods )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetYear =
    IF ( SelectedPeriod + 2 > 12, SelectedYear + 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod + 2 > 12, SelectedPeriod + 2 - 12, SelectedPeriod + 2 )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim), 'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR Result =
    CALCULATE (
        SUM ( PurchasingTransView[on order units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### PurchasingTransView.On Order Units ( Next 3 Periods )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetYear =
    IF ( SelectedPeriod + 3 > 12, SelectedYear + 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod + 3 > 12, SelectedPeriod + 3 - 12, SelectedPeriod + 3 )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear &&'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR Result =
    CALCULATE (
        SUM ( PurchasingTransView[on order units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### PurchasingTransView.On Order Units ( Next 4 Periods )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetYear =
    IF ( SelectedPeriod + 4 > 12, SelectedYear + 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod + 4 > 12, SelectedPeriod + 4 - 12, SelectedPeriod + 4 )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR Result =
    CALCULATE (
        SUM ( PurchasingTransView[on order units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### PurchasingTransView.On Order Units ( Next 5 Periods )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetYear =
    IF ( SelectedPeriod + 5 > 12, SelectedYear + 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod + 5 > 12, SelectedPeriod + 5 - 12, SelectedPeriod + 5 )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR Result =
    CALCULATE (
        SUM ( PurchasingTransView[on order units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### PurchasingTransView.On Order Units ( Next 6 Periods )

```sql

VAR SelectedDate = [Seleced Date]
VAR SelectedYear =
    CALCULATE ( MAX ( 'date_dim'[fiscal_year] ), 'date_dim'[actual_date] = SelectedDate )
VAR SelectedPeriod =
    CALCULATE ( MAX ( 'date_dim'[fiscal_period] ), 'date_dim'[actual_date] = SelectedDate )
VAR TargetYear =
    IF ( SelectedPeriod + 6 > 12, SelectedYear + 1, SelectedYear )
VAR TargetPeriod =
    IF ( SelectedPeriod + 6 > 12, SelectedPeriod + 6 - 12, SelectedPeriod + 6 )
VAR MinDate =
    CALCULATE ( MIN ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR MaxDate =
    CALCULATE ( MAX ( 'date_dim'[actual_date] ), FILTER(ALL(date_dim),'date_dim'[fiscal_year] = TargetYear && 'date_dim'[fiscal_period] = TargetPeriod ))
VAR Result =
    CALCULATE (
        SUM ( PurchasingTransView[on order units] ),
        DATESBETWEEN ( 'date_dim'[actual_date], MinDate, MaxDate )
    )
RETURN Result
```

### PurchasingTransView.PAST + CURR OO

```sql
[On Order Units ( Past Due Periods )]+[On Order Units ( This Period )]
```

### PurchasingTransView.+1 PERIOD

```sql
[On Order Units ( Next 1 Periods )]
```

### PurchasingTransView.+2&3 PERIODS

```sql
[On Order Units ( Next 2 Periods )] + [On Order Units ( Next 3 Periods )]
```

### PurchasingTransView.+4&5&6 PERIODS

```sql
[On Order Units ( Next 4 Periods )] + [On Order Units ( Next 5 Periods )] + [On Order Units ( Next 6 Periods )]
```

### PurchasingTransView.Style Last PO Cost

```sql

VAR LastPO =
    TOPN (
        1,
        FILTER (
            PurchasingTransView,
            NOT ISBLANK ( PurchasingTransView[Receipt Date] )
        ),
        PurchasingTransView[PO number], DESC
    )
RETURN
    MAXX ( LastPO, PurchasingTransView[Cost] )
```

### InventSumCurrentView.On Order Units ( Total )

```sql

CALCULATE (
    SUM ( InventSumCurrentView[OnOrder] ),
    KEEPFILTERS ( NOT ISBLANK ( InventSumCurrentView[inventstatusid] ) )
)
```

### InventSumCurrentView.On Order Cost ( Total )

```sql

CALCULATE (
    SUMX (
        InventSumCurrentView,
        InventSumCurrentView[OnOrder] * RELATED ( product_dim_le[costprice] )
    ),
    NOT ISBLANK ( InventSumCurrentView[inventstatusid] )
)
```

### InventSumCurrentView.On Order Retail ( Total )

```sql

CALCULATE (
    SUMX (
        InventSumCurrentView,
        InventSumCurrentView[OnOrder] * RELATED ( product_dim_le[current_retail] )
    ),
    NOT ISBLANK ( InventSumCurrentView[inventstatusid] )
)
```

### InventSumCurrentView.AVAIL + INTRANS

```sql

VAR SelectedStyle = SELECTEDVALUE(product_dim_le[style_code])
       
VAR Result =
    CALCULATE(
        SUM(InventSumCurrentView[PhysicalInvent]) -
        SUM(InventSumCurrentView[ReservPhysical]) +
        SUM(InventSumCurrentView[Ordered]) -
        SUM(InventSumCurrentView[ReservOrdered]),
       
        FILTER(InventSumCurrentView,
            InventSumCurrentView[itemid] = SelectedStyle &&
            NOT ISBLANK(InventSumCurrentView[inventstatusid])
        )
    )
 
RETURN Result
```

### InventSumCurrentView.InTr Qty

```sql

VAR SelectedStyle = SELECTEDVALUE(product_dim_le[style_code])      
VAR Result =
    CALCULATE(
        SUM(InventSumCurrentView[Ordered]) -
        SUM(InventSumCurrentView[ReservOrdered]),
        FILTER(InventSumCurrentView,
            InventSumCurrentView[itemid] = SelectedStyle &&
            NOT ISBLANK(InventSumCurrentView[inventstatusid])
        )
    )
 
RETURN Result
```

### InventSumCurrentView.CUR AVAI O/H

```sql

VAR SelectedStyle = SELECTEDVALUE(product_dim_le[style_code])    
VAR Result =
    CALCULATE(
        SUM(InventSumCurrentView[PhysicalInvent]) -
        SUM(InventSumCurrentView[ReservPhysical]),
        FILTER(InventSumCurrentView,
 
           InventSumCurrentView[itemid] = SelectedStyle &&
 
            NOT ISBLANK(InventSumCurrentView[inventstatusid])
        )
 
    )
RETURN Result
```

### InventSumCurrentViewForWHSEnabledItems.Picked-AVAIL

```sql

CALCULATE(
	SUM('InventSumCurrentViewForWHSEnabledItems'[picked]),
	'InventSumCurrentViewForWHSEnabledItems'[inventstatusid]
		IN { "AVAIL" }
)
```

### InventSumCurrentViewForWHSEnabledItems.Reserved physical AVAIL

```sql

// CALCULATE (
//     SUM ( 'InventSumCurrentViewForWHSEnabledItems'[reservphysical] ),
//     FILTER (
//         'InventSumCurrentViewForWHSEnabledItems',
//         UPPER ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] ) = "AVAIL"
//     )
// )
CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[reservphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" )
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-AVAIL

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" )
)
```

### InventSumCurrentViewForWHSEnabledItems.Physical inventory AVAIL

```sql

// CALCULATE(
// 	SUM('InventSumCurrentViewForWHSEnabledItems'[physicalinvent]),
// 	'InventSumCurrentViewForWHSEnabledItems'[inventstatusid]
// 		IN { "AVAIL" }
// )
CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[physicalinvent] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" )
)
```

### InventSumCurrentViewForWHSEnabledItems.CUR AVAIL OH

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[CUR AVAI O/H] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" )
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-DAMAGED

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "DAMAGED" )
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-PENDPUT

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "PENDPUT" )
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-BLOCKED

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "BLOCKED" )
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-AVAIL STR

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" ),
    KEEPFILTERS(d365LocationMapping_View[IsDC] = 0)
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-AVAIL WH

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" ),
    KEEPFILTERS (
        d365LocationMapping_View[inventlocationid]
            IN { "8010", "9960", "9970", "9980" }
    )
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-AVAIL Cost

```sql

CALCULATE (
    SUMX (
        'InventSumCurrentViewForWHSEnabledItems',
        'InventSumCurrentViewForWHSEnabledItems'[availphysical]
            * 'InventSumCurrentViewForWHSEnabledItems'[on_hand_unit_cost]
    ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" )
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-AVAIL STR Cost

```sql

CALCULATE (
    SUMX (
        'InventSumCurrentViewForWHSEnabledItems',
        'InventSumCurrentViewForWHSEnabledItems'[availphysical]
            * 'InventSumCurrentViewForWHSEnabledItems'[on_hand_unit_cost]
    ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" ),
    KEEPFILTERS(d365LocationMapping_View[IsDC] = 0)
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-AVAIL WH Cost

```sql

CALCULATE (
    SUMX (
        'InventSumCurrentViewForWHSEnabledItems',
        'InventSumCurrentViewForWHSEnabledItems'[availphysical]
            * 'InventSumCurrentViewForWHSEnabledItems'[on_hand_unit_cost]
    ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" ),
    KEEPFILTERS (
        d365LocationMapping_View[inventlocationid]
            IN { "8010", "9960", "9970", "9980" }
    )    
)
```

### InventSumCurrentViewForWHSEnabledItems.Reserved physical AVAIL Cost

```sql

// CALCULATE (
//     SUM ( 'InventSumCurrentViewForWHSEnabledItems'[reservphysical] ),
//     FILTER (
//         'InventSumCurrentViewForWHSEnabledItems',
//         UPPER ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] ) = "AVAIL"
//     )

// )
CALCULATE (
    SUMX (
        'InventSumCurrentViewForWHSEnabledItems',
        'InventSumCurrentViewForWHSEnabledItems'[reservphysical]
            * 'InventSumCurrentViewForWHSEnabledItems'[on_hand_unit_cost]
    ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" )
)
```

### InventSumCurrentViewForWHSEnabledItems.InTransit-AVAIL

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[intransit_units] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" )    
)
```

### InventSumCurrentViewForWHSEnabledItems.ShortTermAlloc

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[CreatedNotShippedQty] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" )    
)
```

### InventSumCurrentViewForWHSEnabledItems.Physical Available-AVAIL Cost

```sql

CALCULATE (
    SUMX (
        'InventSumCurrentViewForWHSEnabledItems',
        'InventSumCurrentViewForWHSEnabledItems'[physicalinvent]
            * 'InventSumCurrentViewForWHSEnabledItems'[on_hand_unit_cost]
    ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" )
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-PENDPUT STR

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "PENDPUT" ),
    KEEPFILTERS(d365LocationMapping_View[IsDC] = 0)
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-PENDPUT WH

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "PENDPUT" ),
    KEEPFILTERS (
        d365LocationMapping_View[inventlocationid]
            IN { "8010", "9960", "9970", "9980" }
    )
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-PENDPUT DC

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "PENDPUT" ),
    KEEPFILTERS(d365LocationMapping_View[IsDC] = 1)
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-AVAIL DC

```sql

CALCULATE (
    SUM ( 'InventSumCurrentViewForWHSEnabledItems'[availphysical] ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" ),
    KEEPFILTERS(d365LocationMapping_View[IsDC] = 1)
)
```

### InventSumCurrentViewForWHSEnabledItems.Available Physical-AVAIL DC Cost

```sql

CALCULATE (
    SUMX (
        'InventSumCurrentViewForWHSEnabledItems',
        'InventSumCurrentViewForWHSEnabledItems'[availphysical]
            * 'InventSumCurrentViewForWHSEnabledItems'[on_hand_unit_cost]
    ),
    KEEPFILTERS ( 'InventSumCurrentViewForWHSEnabledItems'[inventstatusid] = "AVAIL" ),
    KEEPFILTERS(d365LocationMapping_View[IsDC] = 1)
)
```

## Power Query Source (per table)

### DateTableTemplate_4b10c522-c7e4-4ea9-8621-9face0c0a790

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### date_dim

```sql
let
    Source = Sql.Database(ServerName, "LH_Mart"),
    dbo_date_dim = Source{[Schema="dbo",Item="date_dim"]}[Data],
    #"Removed Blank Rows" = Table.SelectRows(dbo_date_dim, each ([actual_date] <> null and [actual_date] <> "") and ([fiscal_year] <> null)),
    CurrentYear = Date.Year(DateTime.LocalNow()),
    MinFY = CurrentYear - 3,
    MaxFY = CurrentYear + 1,
    #"Filtered Rows" =
        Table.SelectRows(
            #"Removed Blank Rows",            
            each 
                let fy = try Number.From([fiscal_year]) otherwise null
                in fy <> null and fy >= MinFY and fy <= MaxFY

        ),
    #"Sorted Rows" = Table.Sort(#"Filtered Rows",{{"fiscal_year", Order.Ascending}}),
    #"Filtered Rows1" = Table.SelectRows(#"Sorted Rows", each true)
in
    #"Filtered Rows1"
```

### LocalDateTable_e58886bb-220f-4db7-be70-9d550ece5351

```sql
Calendar(Date(Year(MIN('date_dim'[actual_date])), 1, 1), Date(Year(MAX('date_dim'[actual_date])), 12, 31))
```

### weeklyOnHandView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_weeklyOnHandView = Source{[Schema="dbo",Item="weeklyOnHandView"]}[Data]
in
    dbo_weeklyOnHandView
```

### LocalDateTable_f2167fd2-cd0f-4922-bc96-72d212cdcc06

```sql
Calendar(Date(Year(MIN('weeklyOnHandView'[actual_date])), 1, 1), Date(Year(MAX('weeklyOnHandView'[actual_date])), 12, 31))
```

### d365LocationMapping_View

```sql
let
    Source = Sql.Database(ServerName, "LH_D365"),
    dbo_d365LocationMapping_View = Source{[Schema="dbo",Item="d365LocationMapping_View"]}[Data]
in
    dbo_d365LocationMapping_View
```

### product_dim_le

```sql
let
    Source = Sql.Database(ServerName, "LH_D365"),
    dbo_product_dim_le = Source{[Schema="dbo",Item="product_dim_le"]}[Data]
in
    dbo_product_dim_le
```

### LocalDateTable_aaf54f7c-6bd0-4f26-9a8a-c399ae83e6db

```sql
Calendar(Date(Year(MIN('product_dim_le'[activation_date])), 1, 1), Date(Year(MAX('product_dim_le'[activation_date])), 12, 31))
```

### ProductDim_attribute

```sql
let
    Source = Sql.Database(ServerName, "LH_D365"),
    dbo_ProductDim_attribute = Source{[Schema="dbo",Item="ProductDim_attribute"]}[Data]
in
    dbo_ProductDim_attribute
```

### WeeklyAllocationView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_WeeklyAllocationView = Source{[Schema="dbo",Item="WeeklyAllocationView"]}[Data]
in
    dbo_WeeklyAllocationView
```

### WeeklyOnOrderView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_WeeklyOnOrderView = Source{[Schema="dbo",Item="WeeklyOnOrderView"]}[Data]
in
    dbo_WeeklyOnOrderView
```

### WeeklySalesView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_WeeklySalesView = Source{[Schema="dbo",Item="WeeklySalesView"]}[Data]
in
    dbo_WeeklySalesView
```

### LocalDateTable_10c9249e-d232-4e18-a167-2c5932f223de

```sql
Calendar(Date(Year(MIN('product_dim_le'[InDate])), 1, 1), Date(Year(MAX('product_dim_le'[InDate])), 12, 31))
```

### LocalDateTable_ee41d51f-9d46-4ac9-8200-f64175ecdeb0

```sql
Calendar(Date(Year(MIN('product_dim_le'[OutDate])), 1, 1), Date(Year(MAX('product_dim_le'[OutDate])), 12, 31))
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
    "DSNY-M", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "DSNY-M" 
    ),
    "DSNY-C", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "DSNY-C" 
    ),
    "OUTLET", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "OUTLET" 
    ),
    "WEB", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "WEB" 
    ),
    "WEBBUF", CALCULATE (
        MAX ( ProductDim_attribute[AttributeValue] ),
        ProductDim_attribute[AttributeName] = "WEBBUF" 
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

### suntafretailreplenactivesettingsview

```sql
let
    Source = Sql.Database(ServerName, "LH_D365"),
    LH_D365 = Source{[Name="LH_D365"]}[Data],
    dbo_suntafretailreplenactivesettingsview = Source{[Schema="dbo",Item="suntafretailreplenactivesettingsview"]}[Data]
in
    dbo_suntafretailreplenactivesettingsview
```

### VendorNameView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365"),
    dbo_VendorNameView = Source{[Schema="dbo",Item="VendorNameView"]}[Data]
in
    dbo_VendorNameView
```

### PurchasingTransView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_PurchasingTransView = Source{[Schema="dbo",Item="PurchasingTransView"]}[Data]
in
    dbo_PurchasingTransView
```

### LocalDateTable_2ee2b10b-8404-4b6e-913e-457483769a50

```sql
Calendar(Date(Year(MIN('PurchasingTransView'[Receipt Date])), 1, 1), Date(Year(MAX('PurchasingTransView'[Receipt Date])), 12, 31))
```

### LocalDateTable_b08b6a9c-a796-4fc9-9e6d-b88d2eeb184d

```sql
Calendar(Date(Year(MIN('PurchasingTransView'[Cancel date])), 1, 1), Date(Year(MAX('PurchasingTransView'[Cancel date])), 12, 31))
```

### LocalDateTable_1452680a-222b-41d5-a1bd-2e0460c19769

```sql
Calendar(Date(Year(MIN('PurchasingTransView'[Ship date])), 1, 1), Date(Year(MAX('PurchasingTransView'[Ship date])), 12, 31))
```

### LocalDateTable_b73eddbc-f285-4393-81ba-7d345736794d

```sql
Calendar(Date(Year(MIN('PurchasingTransView'[createddatetime])), 1, 1), Date(Year(MAX('PurchasingTransView'[createddatetime])), 12, 31))
```

### LocalDateTable_3d585c6d-15f6-4f36-926d-49d256ea70af

```sql
Calendar(Date(Year(MIN('WeeklyOnOrderView'[actual_date])), 1, 1), Date(Year(MAX('WeeklyOnOrderView'[actual_date])), 12, 31))
```

### LocalDateTable_f9e1d974-6a04-42a8-a0d8-335b83dbe336

```sql
Calendar(Date(Year(MIN('WeeklySalesView'[actual date])), 1, 1), Date(Year(MAX('WeeklySalesView'[actual date])), 12, 31))
```

### InventtranferView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_InventtranferView = Source{[Schema="dbo",Item="InventtranferView"]}[Data]
in
    dbo_InventtranferView
```

### InventSumCurrentView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_InventSumCurrentView = Source{[Schema="dbo",Item="InventSumCurrentView"]}[Data]
in
    dbo_InventSumCurrentView
```

### ProductCategoryHierarchyPivotView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_ProductCategoryHierarchyPivotView = Source{[Schema="dbo",Item="ProductCategoryHierarchyPivotView"]}[Data]
in
    dbo_ProductCategoryHierarchyPivotView
```

### ReceiptCostFreightFactorView

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_ReceiptCostFreightFactorView = Source{[Schema="dbo",Item="ReceiptCostFreightFactorView"]}[Data]
in
    dbo_ReceiptCostFreightFactorView
```

### LocalDateTable_9858066a-f978-47c4-a6ef-952b87e8544d

```sql
Calendar(Date(Year(MIN('ReceiptCostFreightFactorView'[Receipt Date])), 1, 1), Date(Year(MAX('ReceiptCostFreightFactorView'[Receipt Date])), 12, 31))
```

### InventSumCurrentViewForWHSEnabledItems

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 1, 0, 0)]),
    dbo_InventSumCurrentView = Source{[Schema="dbo",Item="InventSumCurrentViewForWHSEnabledItems"]}[Data]
in
    dbo_InventSumCurrentView
```

### LocalDateTable_0fd1c2bb-f5c0-4b9d-9df9-41872db3be5c

```sql
Calendar(Date(Year(MIN('date_dim'[Day])), 1, 1), Date(Year(MAX('date_dim'[Day])), 12, 31))
```

### LocalDateTable_fd47cfa2-cd82-49fb-a8e9-f9a69d2ff6bf

```sql
Calendar(Date(Year(MIN('InventSumCurrentViewForWHSEnabledItems'[Next Ordered Date])), 1, 1), Date(Year(MAX('InventSumCurrentViewForWHSEnabledItems'[Next Ordered Date])), 12, 31))
```

### LocalDateTable_0d5a504d-e3b0-4405-b642-1036c75db61e

```sql
Calendar(Date(Year(MIN('PurchasingTransView'[PO_CreateDate])), 1, 1), Date(Year(MAX('PurchasingTransView'[PO_CreateDate])), 12, 31))
```

### LocalDateTable_a23d376d-5f88-47e1-94f9-8fb237009275

```sql
Calendar(Date(Year(MIN('ReceiptCostFreightFactorView'[PO_CreateDate])), 1, 1), Date(Year(MAX('ReceiptCostFreightFactorView'[PO_CreateDate])), 12, 31))
```

### RetailSalesTransactionMerchWeekSummary

```sql
let
    Source = Sql.Database(ServerName, "LH_D365"),
    dbo_RetailSalesTransactionMerchWeekSummary = Source{[Schema="dbo",Item="RetailSalesTransactionMerchWeekSummary"]}[Data]
in
    dbo_RetailSalesTransactionMerchWeekSummary
```

## Shared Expressions

### ServerName (0)

```sql
"4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com" meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]
```

## Data Source Cross-References

_No recognized SQL data source references detected._
