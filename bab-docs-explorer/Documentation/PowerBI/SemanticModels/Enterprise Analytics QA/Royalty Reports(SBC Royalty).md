# Royalty Reports(SBC Royalty)

**Workspace:** Enterprise Analytics QA  
**Dataset ID:** db97a715-e547-4ba9-9bc2-db9dffeaf12b  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| date_dim | 30 | 0 |  |
| weeklyOnHandView | 16 | 0 |  |
| d365LocationMapping_View | 12 | 0 |  |
| product_dim | 45 | 0 |  |
| ProductDim_attribute | 8 | 0 |  |
| WeeklyAllocationView | 10 | 0 |  |
| WeeklyOnOrderView | 14 | 0 |  |
| WeeklySalesView | 42 | 8 |  |
| LocalDateTable_e58886bb-220f-4db7-be70-9d550ece5351 | 8 | 0 |  |
| LocalDateTable_f2167fd2-cd0f-4922-bc96-72d212cdcc06 | 8 | 0 |  |
| LocalDateTable_aaf54f7c-6bd0-4f26-9a8a-c399ae83e6db | 8 | 0 |  |
| LocalDateTable_14654b87-d4f1-48fb-b43b-c3cc28900700 | 8 | 0 |  |
| LocalDateTable_78fc1d9f-63f4-4c29-8efd-901518b0fc66 | 8 | 0 |  |

## Measures

### WeeklySalesView.Current Merch Year Week

```sql

VAR TodayDate = TODAY()
VAR Yr = YEAR ( TodayDate )
VAR Wk = WEEKNUM ( TodayDate, 2 )
RETURN Yr * 100 + Wk
```

### WeeklySalesView.Net Sales Units ( 1 month Ago )

```sql

VAR LastMonthDate = EOMONTH(TODAY(), -1) 
RETURN
CALCULATE (
    SUM(WeeklySalesView[sales_total_units]),
    FILTER (
        WeeklySalesView,
        YEAR(WeeklySalesView[actual date]) = YEAR(LastMonthDate) &&
        MONTH(WeeklySalesView[actual date]) = MONTH(LastMonthDate)
    )
)
```

### WeeklySalesView.sales_total_retail_us_te ( 1 month Ago )

```sql

VAR LastMonthDate = EOMONTH(TODAY(), -1) 
RETURN
CALCULATE (
    SUM(WeeklySalesView[sales_total_retail_us_te]),
    FILTER (
        WeeklySalesView,
        YEAR(WeeklySalesView[actual date]) = YEAR(LastMonthDate) &&
        MONTH(WeeklySalesView[actual date]) = MONTH(LastMonthDate)
    )
)
```

### WeeklySalesView.Sales retail ( 1 month Ago )

```sql

VAR LastMonthDate = EOMONTH(TODAY(), -1) 
RETURN
CALCULATE (
    SUM(WeeklySalesView[sales_total_retail]) * AVERAGE(WeeklySalesView[Style Attribute Set Code DISNEY ROYALTY RATE]),
    FILTER (
        WeeklySalesView,
        YEAR(WeeklySalesView[actual date]) = YEAR(LastMonthDate) &&
        MONTH(WeeklySalesView[actual date]) = MONTH(LastMonthDate)
    )
)
```

### WeeklySalesView.Net Sales Units (Last 3 Quarters)

```sql

CALCULATE(
    SUM(WeeklySalesView[sales_total_units]),
    DATESINPERIOD(
        WeeklySalesView[actual date],
        LASTDATE(WeeklySalesView[actual date]),
        -3,
        QUARTER
    )
)
```

### WeeklySalesView.Gross Sales (Last 3 Quarters)

```sql

CALCULATE(
    SUM(WeeklySalesView[sales_total_retail]),
    DATESINPERIOD(
        WeeklySalesView[actual date],
        LASTDATE(WeeklySalesView[actual date]),
        -3,
        QUARTER
    )
)
```

### WeeklySalesView.Promo Pc Total Retail (Last 3 Quarters)

```sql

CALCULATE(
    SUM(WeeklySalesView[promo_pc_total_retail]),
    DATESINPERIOD(
        WeeklySalesView[actual date],
        LASTDATE(WeeklySalesView[actual date]),
        -3,
        QUARTER
    )
)
```

### WeeklySalesView.Net Sales Retail (Last 3 Quarters)

```sql

CALCULATE(
    SUM(WeeklySalesView[sales_total_retail_us_te]),
    DATESINPERIOD(
        WeeklySalesView[actual date],
        LASTDATE(WeeklySalesView[actual date]),
        -3,
        QUARTER
    )
)
```

## Power Query Source (per table)

### date_dim

```sql
date_dim
```

### weeklyOnHandView

```sql
weeklyOnHandView
```

### d365LocationMapping_View

```sql
d365LocationMapping_View
```

### product_dim

```sql
product_dim_le
```

### ProductDim_attribute

```sql
ProductDim_attribute
```

### WeeklyAllocationView

```sql
WeeklyAllocationView
```

### WeeklyOnOrderView

```sql
WeeklyOnOrderView
```

### WeeklySalesView

```sql
WeeklySalesView
```

### LocalDateTable_e58886bb-220f-4db7-be70-9d550ece5351

```sql
LocalDateTable_e58886bb-220f-4db7-be70-9d550ece5351
```

### LocalDateTable_f2167fd2-cd0f-4922-bc96-72d212cdcc06

```sql
LocalDateTable_f2167fd2-cd0f-4922-bc96-72d212cdcc06
```

### LocalDateTable_aaf54f7c-6bd0-4f26-9a8a-c399ae83e6db

```sql
LocalDateTable_aaf54f7c-6bd0-4f26-9a8a-c399ae83e6db
```

### LocalDateTable_14654b87-d4f1-48fb-b43b-c3cc28900700

```sql
LocalDateTable_14654b87-d4f1-48fb-b43b-c3cc28900700
```

### LocalDateTable_78fc1d9f-63f4-4c29-8efd-901518b0fc66

```sql
LocalDateTable_78fc1d9f-63f4-4c29-8efd-901518b0fc66
```

## Shared Expressions

### RangeStart (0)

```sql
#datetime(2024, 2, 4, 0, 0, 0) meta [IsParameterQuery=true, Type="DateTime", IsParameterQueryRequired=true]
```

### RangeEnd (0)

```sql
#datetime(2025, 6, 1, 0, 0, 0) meta [IsParameterQuery=true, Type="DateTime", IsParameterQueryRequired=true]
```

### DirectQuery to AS - Merchandise Aggregate Semantic Model (0)

```sql
let
    Source = AnalysisServices.Database("powerbi://api.powerbi.com/v1.0/myorg/Enterprise%20Analytics%20QA", "Merchandise Aggregate Semantic Model"),
    Cubes = Table.Combine(Source[Data]),
    Cube = Cubes{[Id="Model", Kind="Cube"]}[Data]
in
    Cube
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| powerbi://api.powerbi.com/v1.0/myorg/Enterprise%20Analytics%20QA | Merchandise Aggregate Semantic Model | _(not found in SQL documentation)_ |
