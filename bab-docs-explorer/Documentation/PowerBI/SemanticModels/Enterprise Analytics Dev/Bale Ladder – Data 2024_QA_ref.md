# Bale Ladder – Data 2024_QA_ref

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** f2c3e4c5-7356-4b05-a20e-d6ad2c510919  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| date_dim | 30 | 0 |  |
| weeklyOnHandView | 16 | 0 |  |
| d365LocationMapping_View | 12 | 0 |  |
| product_dim | 45 | 0 |  |
| WeeklySalesView | 38 | 6 |  |
| LocalDateTable_e58886bb-220f-4db7-be70-9d550ece5351 | 8 | 0 |  |
| LocalDateTable_f2167fd2-cd0f-4922-bc96-72d212cdcc06 | 8 | 0 |  |
| LocalDateTable_aaf54f7c-6bd0-4f26-9a8a-c399ae83e6db | 8 | 0 |  |

## Measures

### WeeklySalesView.Current Merch Year Week

```sql

VAR TodayDate = TODAY()
VAR Yr = YEAR ( TodayDate )
VAR Wk = WEEKNUM ( TodayDate, 2 )
RETURN Yr * 100 + Wk
```

### WeeklySalesView.Net SalesUnits (This Week)

```sql

VAR CurrentWk = [Current Merch Year Week]
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ),
        WeeklySalesView[merch_year_wk] = CurrentWk
    )
RETURN
    COALESCE ( Result, 0 )

```

### WeeklySalesView.Net SalesUnits (01 Week(s) ago)

```sql

VAR CurrentWk = [Current Merch Year Week]
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ),
        WeeklySalesView[merch_year_wk] = CurrentWk - 1
    )
RETURN
    COALESCE ( Result, 0 )
```

### WeeklySalesView.Net SalesUnits (02 Week(s) ago)

```sql

VAR CurrentWk = [Current Merch Year Week]
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ),
        WeeklySalesView[merch_year_wk] = CurrentWk - 2
    )
RETURN
    COALESCE ( Result, 0 )
```

### WeeklySalesView.Net SalesUnits (03 Week(s) ago)

```sql

VAR CurrentWk = [Current Merch Year Week]
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ),
        WeeklySalesView[merch_year_wk] = CurrentWk - 3
    )
RETURN
    COALESCE ( Result, 0 )
```

### WeeklySalesView.Net SalesUnits (04 Week(s) ago)

```sql

VAR CurrentWk = [Current Merch Year Week]
VAR Result =
    CALCULATE (
        SUM ( WeeklySalesView[sales_total_units] ),
        WeeklySalesView[merch_year_wk] = CurrentWk - 4
    )
RETURN
    COALESCE ( Result, 0 )
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
