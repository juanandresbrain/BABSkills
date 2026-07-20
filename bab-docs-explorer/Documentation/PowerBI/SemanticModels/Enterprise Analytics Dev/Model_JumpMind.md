# Model_JumpMind

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** a1252ce2-8da6-413c-9c33-339c492e8506  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| rawtransdata | 12 | 3 |  |
| gctransdata | 10 | 1 |  |
| gaap_salesreport | 17 | 10 |  |
| bonusclubreport | 7 | 4 |  |
| jumpmind_posbydepartment | 14 | 16 |  |
| jumpmind_active_employee | 9 | 0 |  |

## Measures

### rawtransdata.TotalTrans_RW

```sql
DISTINCTCOUNT(rawtransdata[sequence_number])
```

### rawtransdata.TotalQualifyingTrans

```sql

SUMX(
    rawtransdata, 
    SWITCH(
        TRUE(),
        rawtransdata[subtotal] >= 25 && LEFT(rawtransdata[business_unit_id], 1) = "1", 1,
        rawtransdata[subtotal] >= 20 && LEFT(rawtransdata[business_unit_id], 1) = "2", 1,
        0
    )
)

```

### rawtransdata.% Transactions W/ GC Bonus

```sql
DIVIDE([TotalTransWithGcPromo],[TotalQualifyingTrans],0)
```

### gctransdata.TotalTransWithGcPromo

```sql
DISTINCTCOUNT(gctransdata[sequence_number])
```

### gaap_salesreport.NetSalesPerHour

```sql
SUMX(gaap_salesreport,
IF (
    UPPER(gaap_salesreport[ProductSellingGeography]) IN {"UK", "IE"},
    gaap_salesreport[extended_discounted_amount] - gaap_salesreport[tax_amount],
    gaap_salesreport[extended_discounted_amount]
)
)
```

### gaap_salesreport.UnitsSoldPerHour

```sql
SUM(gaap_salesreport[UnitsSold])
```

### gaap_salesreport.Trans

```sql
DISTINCTCOUNT(gaap_salesreport[sequence_number])
```

### gaap_salesreport.Skins

```sql

VAR TotalUnits = SUMX(FILTER(gaap_salesreport, LOWER(gaap_salesreport[Department] = "unstuffed")), gaap_salesreport[UnitsSold])
RETURN INT(TotalUnits)


```

### gaap_salesreport.ShoesPerHour

```sql

VAR TotalUnits = SUMX(FILTER(gaap_salesreport, lower(gaap_salesreport[Department] = "footwear")), gaap_salesreport[UnitsSold])
RETURN INT(TotalUnits)

```

### gaap_salesreport.DPT

```sql
DIVIDE([NetSalesPerHour],[Trans],0)
```

### gaap_salesreport.StuffersPerHour

```sql

VAR TotalUnits = SUMX(FILTER(gaap_salesreport, lower(gaap_salesreport[Department] = "stuffers")), gaap_salesreport[UnitsSold])
RETURN INT(TotalUnits)

```

### gaap_salesreport.UPT

```sql
DIVIDE([UnitsSoldPerHour],[Trans],0)
```

### gaap_salesreport.% Shoes

```sql

    IF(
        [Skins] = 0, 
        0, 
        DIVIDE([ShoesPerHour], [Skins], 0)
    )
```

### gaap_salesreport.% Stuffer

```sql
IF(
    [Skins] = 0, 
    0, 
    DIVIDE(
        [StuffersPerHour], 
        [Skins], 
        0
    )
)

```

### bonusclubreport.TransNumberCount

```sql
DISTINCTCOUNT(bonusclubreport[TransactionNumber])
```

### bonusclubreport.TotalTransNumberWithClubNumber

```sql

SUMX(
    bonusclubreport, 
    IF(
        ISBLANK(bonusclubreport[CustomerNumber]), 
        0, 
        1
    )
)
```

### bonusclubreport.BCCR %

```sql
([TotalTransNumberWithClubNumber]/[TransNumberCount])
```

### bonusclubreport.Measure

```sql
-- (no expression)
```

### jumpmind_posbydepartment.ItemRankByNetSales

```sql

RANKX(
    FILTER(
        ALL(jumpmind_posbydepartment[Department],jumpmind_posbydepartment[ItemNumber],jumpmind_posbydepartment[ItemDesc]), 
        jumpmind_posbydepartment[Department] = SELECTEDVALUE(jumpmind_posbydepartment[Department])
    ), 
    [NoTieColumn],
    ,
    DESC,
    DENSE
)
```

### jumpmind_posbydepartment.TotalNetSales

```sql
SUM(jumpmind_posbydepartment[NetSales])
```

### jumpmind_posbydepartment.NoTieColumn

```sql
[TotalNetSales]+RAND()
```

### jumpmind_posbydepartment.Top20NetSales

```sql

IF(
    [ItemRankByNetSales] < 21, 
    1,
    0
)

```

### jumpmind_posbydepartment.TotalUnitSold

```sql
SUM(jumpmind_posbydepartment[UnitsSold])
```

### jumpmind_posbydepartment.CUST_SORT

```sql

    VAR SelectedP1 = SELECTEDVALUE(jumpmind_posbydepartment[Department])
    VAR RankValue = FORMAT([ItemRankByNetSales], "00")
    VAR FormatRankValue  =FORMAT(RAND() * 0.0198, "0.000")

    RETURN
        IF(
            NOT(ISBLANK(SelectedP1)),
            SelectedP1 & " " & RankValue & " " & FormatRankValue,
            BLANK()
        )
```

### jumpmind_posbydepartment.M_Rows

```sql

var Cat=MAX(jumpmind_posbydepartment[Department])
var Pro=MAX(jumpmind_posbydepartment[ItemNumber])
return
CALCULATE(countrows(ALLSELECTED(jumpmind_posbydepartment)),jumpmind_posbydepartment[Department]=Cat,jumpmind_posbydepartment[ItemNumber]<=Pro)
```

### jumpmind_posbydepartment.M_Salt

```sql

var rnk = RANKX(
        FILTER(
        ALL(jumpmind_posbydepartment[Department],jumpmind_posbydepartment[ItemNumber]),
        jumpmind_posbydepartment[Department] = MAX(jumpmind_posbydepartment[Department])  -- Change 'Category' to your category column
    ),
   ABS(RAND()),  -- Change 'Sales' to the metric you are ranking on
    ,
    DESC,
    DENSE
)
return 1-(rnk/100.00)
```

### jumpmind_posbydepartment.M_Sales_Salted

```sql
[TotalNetSales] + [M_Salt]
```

### jumpmind_posbydepartment.ranknumber

```sql
RANKX(
    FILTER(
        ALL(jumpmind_posbydepartment[Department]),
        jumpmind_posbydepartment[Department] = MAX(jumpmind_posbydepartment[Department])  -- Change 'Category' to your category column
    ),
    [M_Sales_Salted],  -- Change 'Sales' to the metric you are ranking on
    ,
    DESC,
    DENSE
)
```

### jumpmind_posbydepartment.M_Item

```sql
max(jumpmind_posbydepartment[ItemNumber])
```

### jumpmind_posbydepartment.Rank_By_dept

```sql

RANKX(
        ALLSELECTED(jumpmind_posbydepartment[Department]),
        CALCULATE(SUM(jumpmind_posbydepartment[NetSales])),
    ,
    DESC,
    DENSE
)
```

### jumpmind_posbydepartment.Item_Rnk_by_dept

```sql

VAR CurrentDept = SELECTEDVALUE(jumpmind_posbydepartment[Department])
VAR SalesTable = 
    SUMMARIZE(
        ALLSELECTED(jumpmind_posbydepartment),
        jumpmind_posbydepartment[Department],
        jumpmind_posbydepartment[ItemNumber],
        "TotalNetSales", SUM(jumpmind_posbydepartment[NetSales])
    )
RETURN
RANKX(
    FILTER(
        SalesTable,
        [Department] = CurrentDept
    ),
    [TotalNetSales],
    ,
    DESC,
    SKIP
)
```

### jumpmind_posbydepartment.Sort_Data

```sql
CONCATENATE(SELECTEDVALUE(jumpmind_posbydepartment[Department]),RIGHT(CONCATENATE(0,jumpmind_posbydepartment[Item_Rnk_by_dept]),2))
```

### jumpmind_posbydepartment.Item_Row_by_dept

```sql

VAR CurrentDept = SELECTEDVALUE(jumpmind_posbydepartment[Department])
VAR SalesTable = 
    SUMMARIZE(
        ALLSELECTED(jumpmind_posbydepartment),
        jumpmind_posbydepartment[Department],
        jumpmind_posbydepartment[ItemNumber],
        "TotalNetSales", SUM(jumpmind_posbydepartment[NetSales])
    )
RETURN
// RANKX(
//     FILTER(
//         SalesTable,
//         [Department] = CurrentDept
//     ),
//     [TotalNetSales],
//     ,
//     DESC,
//     SKIP
// )
ROWNUMBER(FILTER(
        SalesTable,
        [Department] = CurrentDept
),
ORDERBY([TotalNetSales],desc,
    		jumpmind_posbydepartment[ItemNumber], asc
),
PARTITIONBY(jumpmind_posbydepartment[Department]))
```

### jumpmind_posbydepartment.IsSameDate

```sql
IF(DATEVALUE(jumpmind_posbydepartment[Shcreate_time]) = DATEVALUE(jumpmind_posbydepartment[Slcreate_time]), 1, 0)

```

## Power Query Source (per table)

### rawtransdata

```sql
rawtransdata
```

### gctransdata

```sql
gctransdata
```

### gaap_salesreport

```sql
gaap_salesreport
```

### bonusclubreport

```sql
bonusclubreport
```

### jumpmind_posbydepartment

```sql
jumpmind_posbydepartment
```

### jumpmind_active_employee

```sql
jumpmindactiveemployee
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
