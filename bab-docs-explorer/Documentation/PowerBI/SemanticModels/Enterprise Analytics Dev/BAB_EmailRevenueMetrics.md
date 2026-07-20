# BAB_EmailRevenueMetrics

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** f31b33f8-d8ca-4b13-8f65-f0750f63b206  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| emailrevmetrics_monthly | 19 | 7 |  |
| emailrevmetrics_daily | 19 | 9 |  |
| Daily Metrics selector | 4 | 0 |  |
| Monthly Metrics Selector | 4 | 0 |  |

## Measures

### emailrevmetrics_monthly.ClickthroughRate_monthly_Measure

```sql
AVERAGE('emailrevmetrics_monthly'[Avg Click Through Rate])
```

### emailrevmetrics_monthly.OpenRate_monthly_Measure

```sql
AVERAGE('emailrevmetrics_monthly'[Avg Open Rate])
```

### emailrevmetrics_monthly.segmentcount_monthly_Measure

```sql
AVERAGE('emailrevmetrics_monthly'[Avg Segment Count])
```

### emailrevmetrics_monthly.RetRevenue_monthly_Measure

```sql
AVERAGE('emailrevmetrics_monthly'[ret Revenue])
```

### emailrevmetrics_monthly.WebRevenue_monthly_Measure

```sql
AVERAGE('emailrevmetrics_monthly'[web Revenue])
```

### emailrevmetrics_monthly.TotalRevenue_monthly_Measure

```sql
AVERAGE('emailrevmetrics_monthly'[Total Revenue])
```

### emailrevmetrics_monthly.Chk

```sql
COUNTROWS(emailrevmetrics_monthly)
```

### emailrevmetrics_daily.ClickRate_Measure

```sql
AVERAGE('emailrevmetrics_daily'[Click Rate])
```

### emailrevmetrics_daily.OpenRate_Measure

```sql
AVERAGE('emailrevmetrics_daily'[Open Rate])
```

### emailrevmetrics_daily.SegmentCount_Measure

```sql
SUM('emailrevmetrics_daily'[Segment Count])
```

### emailrevmetrics_daily.RetRev_daily_Measure

```sql
SUM('emailrevmetrics_daily'[ret Rev])
```

### emailrevmetrics_daily.WebRev_daily_Measure

```sql
SUM('emailrevmetrics_daily'[web Rev])
```

### emailrevmetrics_daily.TotalRev_daily_Measure

```sql
SUM('emailrevmetrics_daily'[Total Rev])
```

### emailrevmetrics_daily.Segment Count_M

```sql
SUM(emailrevmetrics_daily[Segment Count])
```

### emailrevmetrics_daily.Total Journeys

```sql
DISTINCTCOUNT(emailrevmetrics_daily[Journey Name])
```

### emailrevmetrics_daily.chk0

```sql
COUNTROWS(emailrevmetrics_daily)
```

## Power Query Source (per table)

### emailrevmetrics_monthly

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com", "LH_Mart"),
    dbo_emailrevmetrics_monthly = Source{[Schema="dbo",Item="emailrevmetrics_monthly"]}[Data],
    AddSpacesToHeaders = Table.TransformColumnNames(#"dbo_emailrevmetrics_monthly", each Text.Combine(Splitter.SplitTextByCharacterTransition({"a".."z"}, {"A".."Z"})(_), " "))
in
    AddSpacesToHeaders
```

### emailrevmetrics_daily

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com", "LH_Mart"),
    dbo_emailrevmetrics_daily = Source{[Schema="dbo",Item="emailrevmetrics_daily"]}[Data],
    AddSpacesToHeaders = Table.TransformColumnNames(#"dbo_emailrevmetrics_daily", each Text.Combine(Splitter.SplitTextByCharacterTransition({"a".."z"}, {"A".."Z"})(_), " "))
in
    AddSpacesToHeaders
```

### Daily Metrics selector

```sql
{
    ("Click Rate", NAMEOF('emailrevmetrics_daily'[ClickRate_Measure]), 0),
    ("Open Rate", NAMEOF('emailrevmetrics_daily'[OpenRate_Measure]), 1),
    ("Segment Count", NAMEOF('emailrevmetrics_daily'[SegmentCount_Measure]), 2),
    ("Store Revenue", NAMEOF('emailrevmetrics_daily'[RetRev_daily_Measure]), 3),
    ("Web Revenue", NAMEOF('emailrevmetrics_daily'[WebRev_daily_Measure]), 4),
    ("Total Revenue", NAMEOF('emailrevmetrics_daily'[TotalRev_daily_Measure]), 5)
}
```

### Monthly Metrics Selector

```sql
{
    ("Click-Through Rate", NAMEOF('emailrevmetrics_monthly'[ClickthroughRate_monthly_Measure]), 0),
    ("Open Rate", NAMEOF('emailrevmetrics_monthly'[OpenRate_monthly_Measure]), 1),
    ("Segments Count", NAMEOF('emailrevmetrics_monthly'[segmentcount_monthly_Measure]), 2),
    ("Retail Revenue", NAMEOF('emailrevmetrics_monthly'[RetRevenue_monthly_Measure]), 3),
    ("Web Revenue", NAMEOF('emailrevmetrics_monthly'[WebRevenue_monthly_Measure]), 4),
    ("Total Revenue", NAMEOF('emailrevmetrics_monthly'[TotalRevenue_monthly_Measure]), 5)
}
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com | LH_Mart | _(not found in SQL documentation)_ |
