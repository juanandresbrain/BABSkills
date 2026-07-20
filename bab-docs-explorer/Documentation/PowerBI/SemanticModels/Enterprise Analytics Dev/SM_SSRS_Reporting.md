# SM_SSRS_Reporting

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** 81978082-713b-499e-81fa-61d37b871265  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| posbydepartment | 12 | 11 |  |
| bonusclubreport | 7 | 3 |  |
| gaap_salesreport | 17 | 10 |  |

## Measures

### posbydepartment.NetSales

```sql
SUM(posbydepartment[ActualUnitPrice])
```

### posbydepartment.UnitSold

```sql
SUM(posbydepartment[Quantity])
```

### posbydepartment.ItemRankByNetSales

```sql

RANKX(
    FILTER(
        ALL(posbydepartment[Department],posbydepartment[ItemNumber], posbydepartment[ItemDesc]), 
        posbydepartment[Department] = SELECTEDVALUE(posbydepartment[Department])
    ), 
    [NoTieColumn],
    ,
    DESC,
    DENSE
)
```

### posbydepartment.Top20NetSales

```sql

IF(
    [ItemRankByNetSales] < 21, 
    1,
    0
)

```

### posbydepartment.RowNumberByNetSales

```sql

RANKX(
    ALL(posbydepartment[Department],posbydepartment[ItemNumber],posbydepartment[ItemDesc] ),
    [NoTieColumn], 
    ,
    DESC,Dense
)

```

### posbydepartment.NoTieColumn

```sql
[NetSales]+RAND()
```

### posbydepartment.ItemRankByNetSales_test

```sql

VAR DeptRank =
    RANKX(
         ALL (posbydepartment[Department] ),
        CALCULATE ( SELECTEDVALUE ( posbydepartment[Department] ) ),
        ,
        ASC
    )

VAR ItemRank =
    RANKX ( ALL ( posbydepartment[ItemNumber] ), [NetSales] )
VAR ItemCount =
    CALCULATE(DISTINCTCOUNT(posbydepartment[ItemNumber]), ALL(posbydepartment))

VAR ItemDescRank =
    RANKX ( ALL ( posbydepartment[ItemDesc] ), [NetSales] )
VAR ItemDescCount =
    CALCULATE(DISTINCTCOUNT(posbydepartment[ItemDesc]), ALL(posbydepartment))


VAR CombinedRank = DeptRank + (ItemRank / (ItemCount + 1)) + (ItemDescRank / (ItemDescCount+1))

RETURN
    CombinedRank

```

### posbydepartment.DR

```sql

RANKX(
        ALL (posbydepartment),
        [NoTieColumn],
        ,
        DESC
    )
```

### posbydepartment.Department Rank

```sql


RANKX(

    ALL(posbydepartment[Department]),               -- The table/column you want to rank

    VALUE(CALCULATE([NoTieColumn])),   -- The expression you want to rank by

    ,                                     -- Optional: value to return for ties

    DESC,                                  -- Order: DESC for highest to lowest

    DENSE                                   -- Ranking method: DENSE or SKIP

)

 
```

### posbydepartment.Custom Rank

```sql

VAR SelectedP1 = SELECTEDVALUE(posbydepartment[Department]) 
VAR RankValue = [NoTieColumn] RETURN IF( NOT(ISBLANK(SelectedP1)), SelectedP1 & " " & RankValue, BLANK() )
```

### posbydepartment.Measure

```sql
RANK(posbydepartment,ORDERBY([NoTieColumn],desc),PARTITIONBY(posbydepartment[Department]))
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

### gaap_salesreport.NetSalesPerHour

```sql
SUMX(gaap_salesreport,
IF (
    SELECTEDVALUE(gaap_salesreport[ProductSellingGeography]) IN {"UK", "IE"},
    SUM(gaap_salesreport[extended_discounted_amount]) - SUM(gaap_salesreport[tax_amount]),
    SUM(gaap_salesreport[extended_discounted_amount])
))
```

### gaap_salesreport.Trans

```sql
DISTINCTCOUNT(gaap_salesreport[sequence_number])
```

### gaap_salesreport.DPT

```sql
DIVIDE([NetSalesPerHour],[Trans],0)
```

### gaap_salesreport.UnitsSoldPerHour

```sql
SUM(gaap_salesreport[UnitsSold])
```

### gaap_salesreport.UPT

```sql
DIVIDE([UnitsSoldPerHour],[Trans],0)
```

### gaap_salesreport.Skins

```sql

VAR TotalUnits = SUMX(FILTER(gaap_salesreport, gaap_salesreport[Department] = "Unstuffed"), gaap_salesreport[UnitsSold])
RETURN INT(TotalUnits)


```

### gaap_salesreport.ShoesPerHour

```sql

VAR TotalUnits = SUMX(FILTER(gaap_salesreport, gaap_salesreport[Department] = "Footwear"), gaap_salesreport[UnitsSold])
RETURN INT(TotalUnits)

```

### gaap_salesreport.StuffersPerHour

```sql

VAR TotalUnits = SUMX(FILTER(gaap_salesreport, gaap_salesreport[Department] = "Stuffers"), gaap_salesreport[UnitsSold])
RETURN INT(TotalUnits)

```

### gaap_salesreport.% Shoes

```sql

VAR SkinsPerHour = [Skins]
VAR ShoesPerHour = [ShoesPerHour]
RETURN 
    IF(
        SkinsPerHour = 0, 
        0, 
        DIVIDE(ShoesPerHour, SkinsPerHour, 0)
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

## Power Query Source (per table)

### posbydepartment

```sql
posbydepartment
```

### bonusclubreport

```sql
bonusclubreport
```

### gaap_salesreport

```sql
gaap_salesreport
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
