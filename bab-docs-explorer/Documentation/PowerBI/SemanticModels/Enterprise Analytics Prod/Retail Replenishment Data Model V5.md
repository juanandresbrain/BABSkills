# Retail Replenishment Data Model V5

**Workspace:** Enterprise Analytics Prod  
**Dataset ID:** b88c926a-a11d-42ed-8340-776565ec2cb1  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Product Attributes | 9 | 0 |  |
| Sales history - Customer invoice journals | 20 | 0 |  |
| Store Attributes | 20 | 0 |  |
| On-Hand Inventory \| Stores | 55 | 3 |  |
| Retail replenishment calculation log | 10 | 0 |  |
| Exceptions | 7 | 0 |  |
| Active replenishment settings | 20 | 2 |  |
| Calendar | 45 | 0 |  |
| Products (PLM) | 15 | 0 |  |
| Sales Volume Grades | 4 | 4 |  |
| Measure Table | 1 | 2 |  |
| DC priority and simple execution schedule | 31 | 0 |  |
| On-Hand Inventory \| DC Warehouses | 27 | 0 |  |
| Stores (Store MDM) | 24 | 0 |  |
| FedEx Transit Times | 5 | 0 |  |
| Retail store/product replenishment calculation log (Combined) | 79 | 0 |  |
| store_dim | 42 | 0 |  |
| WeeksOfSalesHistoryParameter | 2 | 1 |  |
| MinimumMultiplierParameter | 2 | 1 |  |
| MaximumMultiplierParameter | 2 | 1 |  |
| On-Hand Inventory \| DC Warehouses AvailPhy For Allocations | 14 | 1 |  |
| Invoice Summary | 12 | 19 |  |
| MinMaxBase | 8 | 9 |  |
| Replen Settings | 11 | 0 |  |

## Measures

### On-Hand Inventory | Stores.Current On-Hand

```sql
SUM('On-Hand Inventory | Stores'[Physical inventory])
```

### On-Hand Inventory | Stores.Weeks of Supply

```sql


var Result = DIVIDE([Current On-Hand],[Average Weekly Sales (Actual)])
var LowerLimit = IF([Current On-Hand]<0,0,1)

RETURN
Result * LowerLimit

```

### On-Hand Inventory | Stores.DC On Order (TO In-Transit, Shipped)

```sql
SUM('On-Hand Inventory | Stores'[DC On Order])
```

### Active replenishment settings.Week high sales (week#)

```sql

VAR WeeksOfSalesHistory =
    SELECTEDVALUE ( WeeksOfSalesHistoryParameter[Weeks of Sales History Parameter] )
VAR ThisItem =
    SELECTEDVALUE ( 'Active replenishment settings'[Product number] )
VAR ThisStore =
    SELECTEDVALUE ( 'Active replenishment settings'[Store number] )
VAR StartDate =
    IF ( WeeksOfSalesHistory = 0, TODAY(), TODAY() - ( WeeksOfSalesHistory * 7 ) )
VAR EndDate = TODAY()

VAR SalesWithWeekKey =
    SELECTCOLUMNS(
        FILTER(
            ALL('Sales history - Customer invoice journals'),
            'Sales history - Customer invoice journals'[Item number] = ThisItem &&
            'Sales history - Customer invoice journals'[Store number] = ThisStore &&
            'Sales history - Customer invoice journals'[Invoice date] >= StartDate &&
            'Sales history - Customer invoice journals'[Invoice date] <= EndDate
        ),
        "WeekKey", YEAR('Sales history - Customer invoice journals'[Invoice date]) * 100
                    + WEEKNUM('Sales history - Customer invoice journals'[Invoice date], 2),
        "InvoiceDate", 'Sales history - Customer invoice journals'[Invoice date],
        "Quantity", 'Sales history - Customer invoice journals'[Quantity]
    )


VAR WeeklySalesTable =
    GROUPBY(
        SalesWithWeekKey,
        [WeekKey],
        "WeekStartDate", MINX( CURRENTGROUP(), [InvoiceDate] ),
        "TotalQty",      SUMX( CURRENTGROUP(), [Quantity] )
    )

VAR MaxQty   = MAXX(WeeklySalesTable, [TotalQty])
VAR MaxWeek  = FILTER(WeeklySalesTable, [TotalQty] = MaxQty)
VAR WeekNo =
    CONCATENATEX(
        MaxWeek,
        DATEDIFF(StartDate, [WeekStartDate], WEEK)+1,
        ", ",
        [WeekKey],
        ASC
    )
    
RETURN 
    IF(
        ISBLANK(WeekNo),
        "0",
        WeekNo
    )
```

### Active replenishment settings.Week low sales (week#)

```sql

VAR WeeksOfSalesHistory =
    SELECTEDVALUE ( WeeksOfSalesHistoryParameter[Weeks of Sales History Parameter] )
VAR ThisItem =
    SELECTEDVALUE ( 'Active replenishment settings'[Product number] )
VAR ThisStore =
    SELECTEDVALUE ( 'Active replenishment settings'[Store number] )
VAR StartDate =
    IF ( WeeksOfSalesHistory = 0, TODAY(), TODAY() - ( WeeksOfSalesHistory * 7 ) )
VAR EndDate = TODAY()

VAR SalesWithWeekKey =
    SELECTCOLUMNS (
        FILTER (
            ALL('Sales history - Customer invoice journals'),
            'Sales history - Customer invoice journals'[Item number] = ThisItem &&
            'Sales history - Customer invoice journals'[Store number] = ThisStore &&
            'Sales history - Customer invoice journals'[Invoice date] >= StartDate &&
            'Sales history - Customer invoice journals'[Invoice date] <= EndDate
        ),
        "WeekKey", YEAR ( 'Sales history - Customer invoice journals'[Invoice date] ) * 100
                    + WEEKNUM ( 'Sales history - Customer invoice journals'[Invoice date], 2 ),
        "InvoiceDate", 'Sales history - Customer invoice journals'[Invoice date],
        "Quantity", 'Sales history - Customer invoice journals'[Quantity]
    )

VAR WeeklySalesTable =
    GROUPBY (
        SalesWithWeekKey,
        [WeekKey],
        "WeekStartDate", MINX ( CURRENTGROUP(), [InvoiceDate] ),
        "TotalQty",      SUMX ( CURRENTGROUP(), [Quantity] )
    )

VAR MinQty =
    MINX ( WeeklySalesTable, [TotalQty] )

VAR MinWeek =
    FILTER ( WeeklySalesTable, [TotalQty] = MinQty )

VAR WeekNo =
    CONCATENATEX(
        MinWeek,
        DATEDIFF(StartDate, [WeekStartDate], WEEK)+1,
        ", ",
        [WeekKey],
        ASC
    )
    
RETURN 
    IF(
        ISBLANK(WeekNo),
        "0",
        WeekNo
    )
```

### Sales Volume Grades.Volume

```sql

SUMX(
    'Sales Volume Grades',
    'Sales Volume Grades'[Multiplier] * [Average Sales Combined]
)
```

### Sales Volume Grades.Volume Total

```sql

SUMX(
    'Sales Volume Grades',
    'Sales Volume Grades'[Multiplier] * [Average Sales all Stores]
)
```

### Sales Volume Grades.Volume Quantity

```sql

SUMX(
    'Sales Volume Grades',
    'Sales Volume Grades'[Multiplier] * [Average Quantity]
)
```

### Sales Volume Grades.Volume Quantity Total

```sql

SUMX(
    'Sales Volume Grades',
    'Sales Volume Grades'[Multiplier] * [Average Quantity all Stores]
)
```

### Measure Table.Total Fiscal Weeks

```sql
DISTINCTCOUNTNOBLANK('Calendar'[Running Fiscal Week Id])
```

### Measure Table.Total Fiscal Weeks of Item

```sql

CALCULATE(
    DISTINCTCOUNTNOBLANK('Calendar'[Running Fiscal Week Id]),
    ALL('Sales history - Customer invoice journals'[Store number])
)
```

### WeeksOfSalesHistoryParameter.Weeks of Sales History Parameter Value

```sql
SELECTEDVALUE('WeeksOfSalesHistoryParameter'[Weeks of Sales History Parameter])
```

### MinimumMultiplierParameter.MinimumMultiplierParameter Value

```sql
SELECTEDVALUE('MinimumMultiplierParameter'[MinimumMultiplierParameter])
```

### MaximumMultiplierParameter.MaximumMultiplierParameter Value

```sql
SELECTEDVALUE('MaximumMultiplierParameter'[MaximumMultiplierParameter])
```

### On-Hand Inventory | DC Warehouses AvailPhy For Allocations.% Replenishing Inv.

```sql

DIVIDE(
    SUM([Firmed Replenishment]), 
    SUM([DC Effective Inventory])
)
```

### Invoice Summary.Average Weekly Sales (Actual)

```sql

DIVIDE(
    SUM('Invoice Summary'[Quantity]),
    DISTINCTCOUNT('Calendar'[Merch_Year_Week])
) + 0

```

### Invoice Summary.Sales Curve

```sql

DIVIDE(
    SUM('Invoice Summary'[AmountInUSD]),
    CALCULATE(
        SUM('Invoice Summary'[AmountInUSD]),
        ALLSELECTED('Invoice Summary')
    )
)
```

### Invoice Summary.Weeks of Sales

```sql
CALCULATE( DISTINCTCOUNT('Invoice Summary'[merch_year_wk]), FILTER( 'Invoice Summary', 'Invoice Summary'[Quantity] > 0 ) )
```

### Invoice Summary.US Sales Curve Total

```sql

VAR CatValue =
    CALCULATE(
        [Sales Curve],                                
        FILTER('Store Attributes','Store Attributes'[Country/region] = "USA"),FILTER('Invoice Summary','Invoice Summary'[fiscal_week]<=[Weeks of Sales])
    )
VAR GrandTotal =
    CALCULATE(
        [Sales Curve],                                
        FILTER('Store Attributes','Store Attributes'[Country/region] = "USA")
    )
RETURN
DIVIDE(CatValue, GrandTotal)
```

### Invoice Summary.Store USD Sales Rank

```sql

RANKX(
    ALL('Invoice Summary'),
    SUM('Invoice Summary'[AmountInUSD]),
    ,
    ASC,
    Dense
)

```

### Invoice Summary.Volume Total Grade Code

```sql

VAR CurrentSales = SUM('Invoice Summary'[AmountInUSD])

VAR GradesWithVolume =
    ADDCOLUMNS (
        ALL ( 'Sales Volume Grades'[Grade] ),
        "VolumeResult", [Volume Total]
    )

VAR AchievedGrades =
    FILTER (
        GradesWithVolume,
        [VolumeResult] <= CurrentSales
    )

VAR TopAchievedGrade =
    TOPN (
        1,
        AchievedGrades,
        [VolumeResult],
        DESC
    )

RETURN
    MAXX ( TopAchievedGrade, [Grade] )
```

### Invoice Summary.Average Sales

```sql
DIVIDE(SUM('Invoice Summary'[AmountInUSD]),DISTINCTCOUNTNOBLANK('Invoice Summary'[Store number]))
```

### Invoice Summary.Average Sales all Stores

```sql
CALCULATE(DIVIDE(SUM('Invoice Summary'[AmountInUSD]),CALCULATE(
    DISTINCTCOUNTNOBLANK('Store Attributes'[Warehouse]),
    ALLSELECTED('Store Attributes')
)), ALLSELECTED('Invoice Summary'))
```

### Invoice Summary.Volume Grade Code

```sql

VAR CurrentSales = SUM('Invoice Summary'[AmountInUSD])

VAR GradesWithVolume =
    ADDCOLUMNS (
        ALL ( 'Sales Volume Grades'[Grade] ),
        "VolumeResult", [Volume]
    )

VAR AchievedGrades =
    FILTER (
        GradesWithVolume,
        [VolumeResult] <= CurrentSales
    )

VAR TopAchievedGrade =
    TOPN (
        1,
        AchievedGrades,
        [VolumeResult],
        DESC
    )

RETURN
    MAXX ( TopAchievedGrade, [Grade] )
```

### Invoice Summary.Average Sales Combined

```sql

DIVIDE(
     CALCULATE(
        SUM('Invoice Summary'[AmountInUSD]),
        ALLSELECTED('On-Hand Inventory | Stores')
    ),
 CALCULATE(
        [Store Count],
        ALLSELECTED('On-Hand Inventory | Stores')
    )
)
```

### Invoice Summary.Store Count

```sql
DISTINCTCOUNTNOBLANK('Invoice Summary'[Store number])
```

### Invoice Summary.% of Total

```sql

DIVIDE(
    SUM('Invoice Summary'[Quantity]),
    CALCULATE(
        SUM('Invoice Summary'[Quantity]),
        ALLSELECTED('Invoice Summary')
    )
)
```

### Invoice Summary.Average Quantity Combined

```sql

DIVIDE(
     CALCULATE(
        SUM('Invoice Summary'[Quantity]),
        ALLSELECTED('On-Hand Inventory | Stores')
    ),
 CALCULATE(
        [Store Count],
        ALLSELECTED('On-Hand Inventory | Stores')
    )
)
```

### Invoice Summary.Average Quantity

```sql
DIVIDE(SUM('Invoice Summary'[Quantity]),DISTINCTCOUNTNOBLANK('Invoice Summary'[Store number]))
```

### Invoice Summary.Average Quantity all Stores

```sql
CALCULATE(DIVIDE(SUM('Invoice Summary'[Quantity]),CALCULATE(
    DISTINCTCOUNTNOBLANK('Invoice Summary'[Store number]),
    ALLSELECTED('Invoice Summary'
))), ALLSELECTED('Invoice Summary'))
```

### Invoice Summary.Volume Total Quantity Grade Code

```sql

VAR CurrentSales = SUM('Invoice Summary'[Quantity])

VAR GradesWithVolume =
    ADDCOLUMNS (
        ALL ( 'Sales Volume Grades'[Grade] ),
        "VolumeResult", [Volume Quantity Total]
    )

VAR AchievedGrades =
    FILTER (
        GradesWithVolume,
        [VolumeResult] <= CurrentSales
    )

VAR TopAchievedGrade =
    TOPN (
        1,
        AchievedGrades,
        [VolumeResult],
        DESC
    )

RETURN
    MAXX ( TopAchievedGrade, [Grade] )
```

### Invoice Summary.Weeks of Quantity

```sql

CALCULATE(
    DISTINCTCOUNT('Invoice Summary'[fiscal_week]),
    FILTER(
        'Invoice Summary',
        'Invoice Summary'[Quantity] > 0
    )
)
```

### Invoice Summary.Store Count Quantity

```sql
CALCULATE(
    DISTINCTCOUNTNOBLANK('Invoice Summary'[Store number]),
    ALLSELECTED('Invoice Summary')
)
```

### Invoice Summary.xx

```sql
DISTINCTCOUNT('Calendar'[Fiscal Week])
```

### MinMaxBase.Number of Weeks with 0 Sales

```sql

VAR SelectedWeeks = SELECTEDVALUE(WeeksOfSalesHistoryParameter[Weeks of Sales History Parameter]) 
RETURN
    CALCULATE(
        DISTINCTCOUNT(MinMaxBase[WeeksAgo]),
        FILTER(MinMaxBase,MinMaxBase[WeeksAgo] <= SelectedWeeks
        )
    )
```

### MinMaxBase.Number of weeks with sales

```sql

VAR SelectedWeeks = SELECTEDVALUE(WeeksOfSalesHistoryParameter[Weeks of Sales History Parameter]) 
RETURN 
IF(
        ISBLANK([Number of Weeks with 0 Sales]),
        BLANK(),
        SelectedWeeks-[Number of Weeks with 0 Sales]
    )
```

### MinMaxBase.Average weekly sales

```sql

VAR SelectedWeeks = SELECTEDVALUE(WeeksOfSalesHistoryParameter[Weeks of Sales History Parameter]) 
RETURN
    DIVIDE(CALCULATE(
        SUM(MinMaxBase[TotalQuantity]),
        FILTER(MinMaxBase,MinMaxBase[WeeksAgo] <= SelectedWeeks
        )
    ),SelectedWeeks)
```

### MinMaxBase.Max weekly sales

```sql

VAR Maximum = SELECTEDVALUE(MaximumMultiplierParameter[MaximumMultiplierParameter])
VAR AverageWeeklySales = [Average weekly sales]
RETURN IF(Maximum = 0 ,0 ,Maximum * AverageWeeklySales)
```

### MinMaxBase.Min weekly sales

```sql

VAR Minimum = SELECTEDVALUE(MinimumMultiplierParameter[MinimumMultiplierParameter])
VAR AverageWeeklySales = [Average weekly sales]
RETURN IF(Minimum = 0 ,0 ,Minimum * AverageWeeklySales)
```

### MinMaxBase.Week high sales (quantity)

```sql

VAR SelectedWeeks = SELECTEDVALUE(WeeksOfSalesHistoryParameter[Weeks of Sales History Parameter]) 
VAR FilteredBaseTable = 
    FILTER(
        MinMaxBase,
        MinMaxBase[WeeksAgo] <= SelectedWeeks
    )
VAR WeeklySalesTable =
    GROUPBY (
        FilteredBaseTable, 
        MinMaxBase[Product],
        MinMaxBase[Store],
        MinMaxBase[WeeksAgo],
        "TotalQty", SUMX ( CURRENTGROUP(), [TotalQuantity] )
    )
VAR MaxQty =
    MAXX ( WeeklySalesTable, [TotalQty] )
RETURN
    MaxQty
```

### MinMaxBase.Week low sales (quantity)

```sql

VAR SelectedWeeks = SELECTEDVALUE(WeeksOfSalesHistoryParameter[Weeks of Sales History Parameter]) 
VAR FilteredBaseTable = 
    FILTER(
        MinMaxBase,
        MinMaxBase[WeeksAgo] <= SelectedWeeks
    )
VAR WeeklySalesTable =
    GROUPBY (
        FilteredBaseTable, 
        MinMaxBase[Product],
        MinMaxBase[Store],
        MinMaxBase[WeeksAgo],
        "TotalQty", SUMX ( CURRENTGROUP(), [TotalQuantity] )
    )
VAR MinQty =
    MINX ( WeeklySalesTable, [TotalQty] )
RETURN
    MinQty
```

### MinMaxBase.Min variance %

```sql

VAR CurrentMin = SELECTEDVALUE('Replen Settings'[Current Min])
RETURN IF(ISBLANK([Min weekly sales]), BLANK(),
    DIVIDE(
    [Min weekly sales] - CurrentMin,
    CurrentMin
))
```

### MinMaxBase.Max variance %

```sql

VAR CurrentMax = SELECTEDVALUE('Replen Settings'[Current Max])
RETURN IF(ISBLANK([Max weekly sales]), BLANK(),
    DIVIDE(
    [Max weekly sales] - CurrentMax,
    CurrentMax
))
```

## Power Query Source (per table)

### Product Attributes

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="WITH ProductCTE AS (
     SELECT DISTINCT style_code
        FROM [dbo].[product_dim_le]
        )
     , attributes AS (   
SELECT	
		DISTINCT
        ecoresproduct.[displayproductnumber]                                     AS [Product number],
        ecoresproducttranslation.[name]                                          AS [Name],
        ecoresproducttranslation.[description]                                   AS [Description],
        ecoresproduct.[searchname]                                               AS [Search name],
        ecoresproduct_producttype_GlobalOptionsetMetadata.[LocalizedLabel]       AS [Product type],
        ecoresproduct.[displayproductnumber] + ' | ' + ecoresproducttranslation.[name] AS [Product line],
        RIGHT(ecoresproduct.[displayproductnumber], 5)                           AS [Product number (Core)],
        RIGHT(ecoresproduct.[displayproductnumber], 5) + ' | ' + ecoresproducttranslation.[name] AS [Product line (Core)]
    FROM
        [ecoresproductcategory]
    INNER JOIN
        [ecoresproduct]
        ON ecoresproductcategory.[product] = ecoresproduct.[recid]
    LEFT JOIN
        [ecoresproducttranslation]
        ON ecoresproduct.[recid] = ecoresproducttranslation.[product]
    LEFT JOIN
        (
            SELECT
                [OptionSetName],
                [Option],
                [LocalizedLabel],
                [EntityName]
            FROM
                [dbo].[globaloptionsetmetadata] AS GlobalOptionsetMetadata
            WHERE
                GlobalOptionsetMetadata.[EntityName] = 'ecoresproduct'
                AND GlobalOptionsetMetadata.[OptionSetName] = 'producttype'
        ) AS ecoresproduct_producttype_GlobalOptionsetMetadata
        ON ecoresproduct.[producttype] = ecoresproduct_producttype_GlobalOptionsetMetadata.[Option]
    WHERE
		(ecoresproduct.[IsDelete] IS NULL OR ecoresproduct.[IsDelete] = 0)
        AND (ecoresproductcategory.[IsDelete] IS NULL OR ecoresproductcategory.[IsDelete] = 0)
        AND (ecoresproducttranslation.[IsDelete] IS NULL OR ecoresproducttranslation.[IsDelete] = 0)
        )

        SELECT 
        style_code AS [Product number],
        attrib.[Name],
        attrib.[Description],
        attrib.[Search name],
        attrib.[Product type],
        attrib.[Product line],
        attrib.[Product number (Core)],
        attrib.[Product line (Core)]
        FROM 
        ProductCTE
        LEFT JOIN attributes AS attrib
        ON ProductCTE.style_code = attrib.[Product number]
", CommandTimeout=#duration(0, 2, 0, 0)])
in
    #"Source"
```

### Sales history - Customer invoice journals

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="WITH distinct_products AS 
 (
     SELECT
        MIN(products.[product_key]) AS [product_key],
        products.[style_code]         
		FROM [dbo].[product_dim_le] products
		GROUP BY products.[style_code]      
 )
, productAttruibutes AS (
 SELECT
 products.[style_code] AS [Style Code],
     products.[style_desc]                            AS [Style Description],
    products.[department]                                  AS [Department],
    products.[class]                                       AS [Class],
    products.[consumer_group]                               AS [Consumer Group],
    products.[KeyStory]                                    AS [Key Story]
  FROM distinct_products
	INNER JOIN [dbo].[product_dim_le] products
		ON distinct_products.product_key = products.product_key 
)

SELECT 
    cit.salesid                                      AS [Sales order],
    CAST(cit.invoicedate AS DATE)                   AS [Invoice date],
    CAST(cit.invoicedate AS DATETIME)               AS [Invoice Datetime],
	CAST(FORMAT(GETDATE(), 'yyyyMMdd') AS INT) AS [DateAsInteger],
    cit.itemid                                      AS [Item number],
    cit.qty                                         AS [Quantity],
    cit.dataareaid                                  AS [Company],
    il.name                                         AS [Warehouse name],
    erp.searchname                                  AS [Product name],
    erp.babcolordescription                         AS [Color],
    idim.inventlocationid                           AS [Store number],
    plm.[Style Description]                            AS [Style Description],
    plm.[Department]                                  AS [Department],
    plm.[Class]                                       AS [Class],
    plm.[Consumer Group]                               AS [Consumer Group],
    plm.[Key Story]                                    AS [Key Story],
    CONCAT(cit.itemid, ' | ', plm.[Style Description]) AS [Product line],
    CONCAT(idim.inventlocationid, ' | ', il.name)   AS [Store line],
    CONCAT(idim.inventlocationid, '-', cit.itemid)  AS [StoreItemKey]

FROM [custinvoicetrans] AS cit
    LEFT JOIN [inventdim] AS idim 
        ON cit.inventdimid = idim.inventdimid
       AND cit.dataareaid  = idim.dataareaid
    LEFT JOIN [inventlocation] AS il 
        ON idim.inventlocationid = il.inventlocationid
       AND idim.dataareaid      = il.dataareaid
    LEFT JOIN [ecoresproduct] AS erp 
        ON cit.itemid     = erp.displayproductnumber
       AND cit.dataareaid = erp.dataareaid
    LEFT JOIN productAttruibutes AS plm 
        ON cit.itemid = plm.[Style Code]
WHERE 
    cit.invoicedate >= CAST(DATEADD(WEEK, DATEDIFF(WEEK, 0, DATEADD(WEEK, -52, GETDATE())), 0) AS DATE)
    AND il.name NOT LIKE '%DO NOT USE%'
    AND il.name NOT LIKE '%OLD%'
    AND (cit.IsDelete IS NULL OR cit.IsDelete = 0)
    AND (idim.IsDelete IS NULL OR idim.IsDelete = 0)
    AND (il.IsDelete IS NULL OR il.IsDelete = 0)
    AND (erp.IsDelete IS NULL OR erp.IsDelete = 0)
", CommandTimeout=#duration(0, 2, 0, 0)]),
    #"Filtered Rows" = Table.SelectRows(Source, each [Invoice date] >= RangeStart and [Invoice date] < RangeEnd)
in
    #"Filtered Rows"
```

### Store Attributes

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="WITH RankedData AS (
    SELECT
        inventlocation.inventlocationid,
        inventlocation.inventlocationidtransit,
        inventlocation.name,
        inventlocation.babestimatedpalletvolume,
        inventlocation.babdefaulttomodeofdelivery,
        inventlocation.babcontainerizebyvolumeonly,
        inventlocation.babretailstore,
        logisticspostaladdress.address,
        logisticspostaladdress.city,
        logisticspostaladdress.countryregionid,
        logisticspostaladdress.state,
        logisticspostaladdress.street,
        logisticspostaladdress.validfrom,
        logisticspostaladdress.validto,
        logisticspostaladdress.zipcode,
        retstore.babconcept,
        retstore.babvolume,
        sunTAF.inventlocationid AS [PrimaryDC],
		ROW_NUMBER() OVER(PARTITION BY inventlocation.inventlocationid ORDER BY logisticspostaladdress.validto DESC) AS rn
    FROM
        [inventlocation] AS inventlocation
    LEFT JOIN
        [inventlocationlogisticslocation] AS inventlocationlogisticslocation
        ON inventlocation.recid = inventlocationlogisticslocation.inventlocation
    LEFT JOIN
        [logisticspostaladdress] AS logisticspostaladdress
        ON inventlocationlogisticslocation.location = logisticspostaladdress.location
    LEFT JOIN
        [retailstoretable] AS retstore
        ON inventlocation.inventlocationid = retstore.storenumber
	LEFT JOIN 
	suntafretailreplenstoredcsettings AS sunTAF
	ON inventlocation.inventlocationid = sunTAF.storenumber
    WHERE
        inventlocationlogisticslocation.isprimary = 1
        AND inventlocation.IsDelete IS NULL
		AND sunTAF.IsDelete IS NULL		
)
SELECT
    rd.inventlocationid AS [Warehouse],
    rd.name AS [Location name],
    rd.address AS [Address],
    rd.city AS [City],
    rd.countryregionid AS [Country/region],
    rd.state AS [State/province],
    rd.street AS [Street],
    rd.validfrom AS [Valid from],
    rd.validto AS [Valid to],
    rd.zipcode AS [Postal code],
    rd.inventlocationidtransit AS [Transit warehouse],
    CAST(rd.babretailstore AS bit) AS [BAB Retail store?],
    rd.babdefaulttomodeofdelivery AS [Mode of delivery],
    CAST(rd.babcontainerizebyvolumeonly AS bit) AS [Containerize by volume only?],
    rd.babconcept AS [Store Concept],
    rd.babvolume AS [Store Volume],
    CONCAT(rd.inventlocationid, ' | ', rd.name) AS [Location line],
    CAST(CASE WHEN rd.inventlocationid LIKE '%-T' THEN 1 ELSE 0 END AS bit) AS [Transit?],
	[PrimaryDC]
FROM
    RankedData rd
WHERE
    rd.rn = 1
    AND rd.name NOT LIKE '%DO NOT USE%'
    AND rd.inventlocationid NOT LIKE '%OLD'
    AND rd.inventlocationidtransit IS NOT NULL", CommandTimeout=#duration(0, 2, 0, 0)])
in
    #"Source"
```

### On-Hand Inventory | Stores

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="WITH SUM_Store AS
     (
             SELECT
                     [isum].[dataareaid] AS [inventsum_dataareaid]                             ,
                     [isum].[inventsiteid]                                                     ,
                     [isum].[inventlocationid]                 AS [inventsum_inventlocationid] ,
                     [isum].[inventstatusid]                   AS [inventsum_inventstatusid]   ,
                     [isum].[itemid]                           AS [inventsum_itemid]           ,
                     SUM([isum].[availordered])                AS [inventsum_availordered]     ,
                     SUM([isum].[AvailablePhysicalCalculated]) AS [inventsum_availphysical]    ,
                     SUM([isum].[deducted])                    AS [inventsum_deducted]         ,
                     SUM(
                             CASE
                             WHEN
                                     [isum].[inventstatusid] = 'AVAIL'
                             THEN
                                     [isum].[AvailablePhysicalCalculated]
                             ELSE
                                     0
                             END) AS [availphysical_Avail],
                     SUM(
                             CASE
                             WHEN
                                     [isum].[inventstatusid] = 'PendPut'
                             THEN
                                     [isum].[AvailablePhysicalCalculated]
                             ELSE
                                     0
                             END)                 AS [availphysical_PendPut]   ,
                     SUM([isum].[onorder])        AS [inventsum_onorder]       ,
                     SUM([isum].[ordered])        AS [inventsum_ordered]       ,
                     SUM([isum].[physicalinvent]) AS [inventsum_physicalinvent],
                     SUM([isum].[reservordered])  AS [inventsum_reservordered] ,
                     SUM(
                             CASE
                             WHEN
                                     [isum].[inventstatusid] = 'AVAIL'
                             THEN
                                     [isum].[reservphysical]
                             ELSE
                                     0
                             END) AS [reservphysical_AVAIL],
                     SUM(
                             CASE
                             WHEN
                                     [isum].[inventstatusid] = 'PendPut'
                             THEN
                                     [isum].[reservphysical]
                             ELSE
                                     0
                             END)                 AS [reservphysical_PendPut]                                ,
                     SUM([isum].[reservphysical]) AS [inventsum_reservphysical]                              ,
                     T2.name                      AS inventlocation_name                                     ,
                     T3.searchname                AS ecoresproduct_searchname                                ,
                     T3.babcolordescription       AS ecoresproduct_babcolordescription                       ,
                     T4.babstoreproducteligible   AS suntafretailreplenactivesettings_babstoreproducteligible,
                     T4.maximumsupply             AS suntafretailreplenactivesettings_maximumsupply          ,
                     T4.minimumsupply             AS suntafretailreplenactivesettings_minimumsupply          ,
                     T4.targetweekssupply         AS suntafretailreplenactivesettings_targetweekssupply      ,
                     T4.orderminimum              AS suntafretailreplenactivesettings_orderminimum           ,
                     T4.ordermultiple             AS suntafretailreplenactivesettings_ordermultiple          ,
                     T5.inventlocationid          AS suntafretailreplenstoredcsettings_inventlocationid      ,
                     T5.priority                  AS suntafretailreplenstoredcsettings_priority              ,
                     retstore.[babconcept]        AS [Store Concept],
                     SUM([isum].CreatedNotShippedQty) AS [Documents Created],
                     SUM([isum].ShippedNotReceivedQty) AS [Documents In Transit (Inbound)],
                     SUM(COALESCE([isum].[InTr Qty],0)) - SUM(COALESCE([isum].CreatedNotShippedQty,0)) - SUM(COALESCE([isum].ShippedNotReceivedQty,0)) AS [Documents Received],
                     SUM(COALESCE([isum].CreatedNotShippedQty,0)) + SUM(COALESCE([isum].ShippedNotReceivedQty,0)) + (SUM(COALESCE([isum].[InTr Qty],0)) - SUM(COALESCE([isum].CreatedNotShippedQty,0)) - SUM(COALESCE([isum].ShippedNotReceivedQty,0))) AS [Ordered In Total],
                     SUM([isum].[CUR AVAI O/H Sellable]) AS [O/H Sellable],
                     SUM([isum].[CUR AVAI O/H Non-Sellable]) AS [O/H Non-Sellable],
                     SUM([isum].[CUR AVAI O/H]) AS [Store Available Physical]
             FROM
                     [dbo].[InventSumCurrentViewForWHSEnabledItems] AS [isum]
             LEFT JOIN
                     inventlocation AS T2
             ON
                     [isum].inventlocationid = T2.inventlocationid
             LEFT JOIN
                     ecoresproduct AS T3
             ON
                     [isum].itemid = T3.displayproductnumber
             LEFT JOIN
                     suntafretailreplenactivesettings AS T4
             ON
                     T3.recid                = T4.distinctproduct
             AND     [isum].inventlocationid = T4.storenumber
             LEFT JOIN
                     suntafretailreplenstoredcsettings AS T5
             ON
                     [isum].inventlocationid = T5.storenumber
             LEFT JOIN
                     [retailstoretable] AS retstore
             ON
                     T2.[inventlocationid] = retstore.[storenumber]
             WHERE
                     [isum].[inventlocationid] NOT IN ('9980',
                                                       '9970',
                                                       '9960',
                                                       '9942',
                                                       '9941',
                                                       '8175')
             --AND     [isum].[inventstatusid]  = 'AVAIL'
             AND     COALESCE(T2.IsDelete, 0) = 0
             AND     COALESCE(T3.IsDelete, 0) = 0
             AND     COALESCE(T4.IsDelete, 0) = 0
             AND     COALESCE(T5.IsDelete, 0) = 0
             GROUP BY
                     [isum].[dataareaid]       ,
                     [isum].[inventsiteid]     ,
                     [isum].[inventlocationid] ,
                     [isum].[inventstatusid]   ,
                     [isum].[itemid]           ,
                     T2.name                   ,
                     T3.searchname             ,
                     T3.babcolordescription    ,
                     T4.babstoreproducteligible,
                     T4.maximumsupply          ,
                     T4.minimumsupply          ,
                     T4.targetweekssupply      ,
                     T4.orderminimum           ,
                     T4.ordermultiple          ,
                     T5.inventlocationid       ,
                     T5.priority               ,
                     retstore.[babconcept]) ,
     SUM_DC AS
     (
             SELECT
                     [isum].[dataareaid]                                                       ,
                     [isum].[inventsiteid]                                                     ,
                     [isum].[inventlocationid]                                                 ,
                     [isum].[itemid]                                                           ,
                     SUM([isum].[AvailablePhysicalCalculated]) AS [AvailablePhysicalCalculated],
                     SUM(
                             CASE
                             WHEN
                                     [isum].[inventstatusid] = 'AVAIL'
                             THEN
                                     [isum].[AvailablePhysicalCalculated]
                             ELSE
                                     0
                             END) AS [availphysical_Avail],
                     SUM(
                             CASE
                             WHEN
                                     [isum].[inventstatusid] = 'PendPut'
                             THEN
                                     [isum].[AvailablePhysicalCalculated]
                             ELSE
                                     0
                             END)                 AS [availphysical_PendPut],
                     SUM([isum].[ordered])        AS [ordered]              ,
                     SUM([isum].[onorder])        AS [onorder]              ,
                     SUM([isum].[reservordered])  AS [ordered reserved]     ,
                     SUM([isum].[reservphysical]) AS [reservphysical]
             FROM
                     [dbo].[InventSumCurrentViewForWHSEnabledItems] AS [isum]
             WHERE
                     [isum].[inventlocationid] IN ('9980',
                                                   '9970',
                                                   '9960',
                                                   '9942',
                                                   '9941',
                                                   '8175')
             GROUP BY
                     [isum].[dataareaid]       ,
                     [isum].[inventsiteid]     ,
                     [isum].[inventlocationid] ,
                     [isum].[itemid]) ,
     distinct_products AS
     (
             SELECT
                     MIN(products.[product_key]) AS [product_key],
                     products.[style_code]
             FROM
                     [dbo].[product_dim_le] products
             GROUP BY
                     products.[style_code] ) ,
     attributes AS
     (
             SELECT
                     products.[style_code]     AS [Style Code]       ,
                     products.[style_desc]     AS [Style Description],
                     products.[consumer_group] AS [Consumer Group]   ,
                     products.[department]     AS [Department]       ,
                     products.[class]          AS [Class]            ,
                     products.[subclass]       AS [Subclass]         ,
                     products.[KeyStory]       AS [Key Story]        ,
                     products.[concept]        AS [Concept]          ,
                     attributes.[OrderMultiple]                      ,
                     attributes.[DistributionMultiple] AS [Distribution Multiple]
             FROM
                     distinct_products
             INNER JOIN
                     [dbo].[product_dim_le] products
             ON
                     distinct_products.product_key = products.product_key
             LEFT JOIN
                     (
                             SELECT DISTINCT
                                     [StyleCode]    ,
                                     [OrderMultiple],
                                     [DistributionMultiple]
                             FROM
                                     [LH_Mart].[dbo].[productcatalogmasterattributes]) AS attributes
             ON
                     products.[style_code] = attributes.[StyleCode] )
SELECT
        StoreInv.inventsum_availordered                                   AS [Total available]                                 ,
        StoreInv.inventsum_availphysical                                  AS [Available physical]                              ,
        StoreInv.inventsum_deducted                                       AS [Deducted]                                        ,
        StoreInv.inventsum_itemid                                         AS [Item number]                                     ,
        StoreInv.inventsum_onorder                                        AS [On order]                                        ,
        StoreInv.inventsum_ordered                                        AS [Ordered]                                         ,
        StoreInv.inventsum_physicalinvent                                 AS [Physical inventory]                              ,
        StoreInv.inventsum_reservordered                                  AS [Ordered reserved]                                ,
        StoreInv.inventsum_reservphysical                                 AS [Physical reserved]                               ,
        StoreInv.inventsum_inventlocationid                               AS [Store number]                                    ,
        StoreInv.inventsum_inventlocationid                               AS [Warehouse]                                       ,
        StoreInv.inventsum_inventstatusid                                 AS [Inventory status]                                ,
        StoreInv.inventsum_dataareaid                                     AS [Company]                                         ,
        StoreInv.inventlocation_name                                      AS [Store name]                                      ,
        StoreInv.ecoresproduct_searchname                                 AS [Product name]                                    ,
        StoreInv.ecoresproduct_babcolordescription                        AS [Color]                                           ,
        StoreInv.suntafretailreplenactivesettings_babstoreproducteligible AS [Store/product eligible?]                         ,
        StoreInv.suntafretailreplenactivesettings_maximumsupply           AS [Maximum supply]                                  ,
        StoreInv.suntafretailreplenactivesettings_minimumsupply           AS [Minimum supply]                                  ,
        StoreInv.suntafretailreplenactivesettings_targetweekssupply       AS [Target weeks supply]                             ,
        StoreInv.suntafretailreplenactivesettings_orderminimum            AS [Order minimum]                                   ,
        StoreInv.suntafretailreplenactivesettings_ordermultiple           AS [Order multiple]                                  ,
        StoreInv.suntafretailreplenstoredcsettings_inventlocationid       AS [Primary DC]                                      ,
        StoreInv.suntafretailreplenstoredcsettings_priority               AS [DC Warehouse Priority]                           ,
        StoreInv.[Store Concept]                                                                                               ,
        DCInv.[availphysical_Avail]                                                      AS [DC Available Physical]            ,
        DCInv.[availphysical_PendPut]                                                    AS [DC Available Physical PendPut]    ,
        DCInv.ordered                                                                    AS [DC Ordered]                       ,
        DCInv.[onorder]                                                                  AS [DC On Order]                      ,
        DCInv.[ordered reserved]                                                         AS [DC Ordered Reserved]              ,
        DCInv.[availphysical_Avail] +  DCInv.[availphysical_PendPut] - DCInv.[onorder]   AS [DC Available for Replenishment]   ,
        CONCAT(StoreInv.inventsum_inventlocationid, '-', StoreInv.inventsum_itemid)      AS [StoreItemKey]                     ,
        (StoreInv.inventsum_availphysical - StoreInv.inventsum_onorder)                  AS [Available for replenishments]     ,
        CONCAT(StoreInv.inventsum_inventlocationid, ' | ', StoreInv.inventlocation_name) AS [Store line]                       ,
        plm.[Style Description]                                                                                                ,
        plm.[Department]                                                                                                       ,
        plm.[Class]                                                                                                            ,
        plm.[Consumer Group]                                                                                                   ,
        plm.[Key Story]                                                                                                        ,
        plm.[OrderMultiple]                                                                                 AS [Outer casepack],
        plm.[Distribution Multiple]                                                                         AS [Inner casepack],
        CONCAT(StoreInv.inventsum_itemid, ' | ', plm.[Style Description])                                   AS [Product line]  ,
        CONCAT(StoreInv.suntafretailreplenstoredcsettings_inventlocationid, '-', StoreInv.inventsum_itemid) AS [DCStoreItemKey],
        COALESCE(StoreInv.[Documents Created],0) AS [Documents Created],
        COALESCE(StoreInv.[Documents In Transit (Inbound)],0) AS [Documents In Transit (Inbound)],
        COALESCE(StoreInv.[Documents Received],0) AS [Documents Received],
        COALESCE(StoreInv.[Ordered In Total],0) AS [Ordered In Total],
        COALESCE(StoreInv.[O/H Sellable],0) AS [O/H Sellable],
        COALESCE(StoreInv.[O/H Non-Sellable],0) AS[O/H Non-Sellable],
        COALESCE(StoreInv.[Store Available Physical],0) AS [Store Available Physical]
FROM
        SUM_Store AS StoreInv
LEFT JOIN
        SUM_DC AS DCInv
ON
        StoreInv.inventsum_itemid                                   = DCInv.itemid
AND     StoreInv.suntafretailreplenstoredcsettings_inventlocationid = DCInv.inventlocationid
LEFT JOIN
        attributes AS plm
ON
        StoreInv.inventsum_itemid = plm.[Style Code]", CommandTimeout=#duration(0, 2, 0, 0)])
in
    #"Source"
```

### Retail replenishment calculation log

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="SELECT
    suntafretailreplencalclog.[processid],
    suntafretailreplencalclog.[startdatetime],
    suntafretailreplencalclog.[enddatetime],
    suntafretailreplencalclog.[calctype],
    suntafretailreplencalclog.[ignoreschedule],
    suntafretailreplencalclog.[simulation]
FROM
    [suntafretailreplencalclog] AS suntafretailreplencalclog
WHERE suntafretailreplencalclog.IsDelete IS NULL", CommandTimeout=#duration(0, 2, 0, 0)]),
    #"Inserted Date | Date" = Table.AddColumn(Source, "Date", each DateTime.Date([startdatetime]), type date),
    #"Renamed Columns" = Table.RenameColumns(#"Inserted Date | Date",{{"processid", "Process ID"}, {"startdatetime", "Start datetime"}, {"enddatetime", "End datetime"}, {"calctype", "Calculation type"}, {"ignoreschedule", "Ignore schedule"}, {"simulation", "Simulation"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Ignore schedule", type logical}, {"Simulation", type logical}}),
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(#"Changed Type", each [Start datetime] >= RangeStart and [Start datetime] < RangeEnd),
    #"Renamed Columns1" = Table.RenameColumns(#"Filtered Rows | Incremental Refresh",{{"Ignore schedule", "Ignore schedule?"}, {"Simulation", "Simulation?"}})
in
    #"Renamed Columns1"
```

### Exceptions

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="SELECT
        suntafretailreplenexceptions.[parmid]                                                                                                                                                                                                                                                                                               ,
        [GlobalOptionsetMetadata].[LocalizedLabel] AS [exceptiontype]                                                                                                                                                                                                                                                                       ,
        suntafretailreplenexceptions.[message]                                                                                                                                                                                                                                                                                              ,
        suntafretailreplencalclog.[startdatetime]                                                                                                                                                                                                                                                                                           ,
        SUBSTRING( suntafretailreplenexceptions.[message], CHARINDEX('store ', suntafretailreplenexceptions.[message])   + 6, CHARINDEX(',', suntafretailreplenexceptions.[message]) - (CHARINDEX('store ', suntafretailreplenexceptions.[message]) + 6) )                                                                       AS store_id,
        SUBSTRING( suntafretailreplenexceptions.[message], CHARINDEX('product ', suntafretailreplenexceptions.[message]) + 8, CHARINDEX(' ', suntafretailreplenexceptions.[message], CHARINDEX('product ', suntafretailreplenexceptions.[message])  + 8) - (CHARINDEX('product ', suntafretailreplenexceptions.[message]) + 8) ) AS product_id
FROM
        [suntafretailreplenexceptions] suntafretailreplenexceptions
INNER JOIN
        [suntafretailreplencalclog] suntafretailreplencalclog
ON
        suntafretailreplenexceptions.[parmid] = suntafretailreplencalclog.[processid]
LEFT JOIN
        [dbo].[globaloptionsetmetadata] AS [GlobalOptionsetMetadata]
ON
        [EntityName]                                 = 'suntafretailreplenexceptions'
AND     [OptionSetName]                              = 'exceptiontype'
AND     [LocalizedLabelLanguageCode]                 = '1033'
AND     suntafretailreplenexceptions.[exceptiontype] = [GlobalOptionsetMetadata].[Option]
WHERE
        suntafretailreplenexceptions.IsDelete IS NULL", CommandTimeout=#duration(0, 2, 0, 0)]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"parmid", "Parameter ID"}, {"exceptiontype", "Exception type"}, {"message", "Message"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"startdatetime", type date}})
in
    #"Changed Type"
```

### Active replenishment settings

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="SELECT    suntafretailreplenactivesettings.storenumber,
    suntafretailreplenactivesettings.weekshistory,
    suntafretailreplenactivesettings.seasonalitycurveid,
    suntafretailreplenactivesettings.maximumsupply,
    suntafretailreplenactivesettings.minimumsupply,
    suntafretailreplenactivesettings.targetweekssupply,
    suntafretailreplenactivesettings.orderminimum,
    suntafretailreplenactivesettings.ordermultiple,
    suntafretailreplenactivesettings.replenishmentmethod,
    suntafretailreplenactivesettings.enabled,
    suntafretailreplenactivesettings.babstoreproducteligible,
    ecoresproduct.displayproductnumber,
    ecoresproduct.searchname,
    historyreplen.description AS historyreplenconfigsource,
    stockreplen.description AS stockreplenconfigsource,
    orderreplen.description AS orderreplenconfigsource,
	erptranslation.name AS [Product Name],
	products.[style_desc] AS [Style Description]
FROM
    suntafretailreplenactivesettings AS suntafretailreplenactivesettings
INNER JOIN
    ecoresproduct AS ecoresproduct
    ON suntafretailreplenactivesettings.distinctproduct = ecoresproduct.recid
INNER JOIN
    suntafretailreplenconfig AS historyreplen
    ON suntafretailreplenactivesettings.historyreplenconfigsource = historyreplen.recid
INNER JOIN
    suntafretailreplenconfig AS stockreplen
    ON suntafretailreplenactivesettings.stockreplenconfigsource = stockreplen.recid
INNER JOIN
    suntafretailreplenconfig AS orderreplen
    ON suntafretailreplenactivesettings.orderreplenconfigsource = orderreplen.recid
LEFT JOIN
        [ecoresproducttranslation] AS erptranslation
ON
        ecoresproduct.[recid] = erptranslation.[product]
LEFT JOIN (
SELECT 
[style_code],MIN([style_desc]) AS [style_desc]
FROM
[LH_Mart].[dbo].[product_dim] 
GROUP BY [style_code] ) AS products
ON  products.[style_code] = ecoresproduct.displayproductnumber
WHERE suntafretailreplenactivesettings.IsDelete IS NULL", CommandTimeout=#duration(0, 2, 0, 0)]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"storenumber", "Store number"}, {"babstoreproducteligible", "Store/product eligible?"}, {"weekshistory", "Weeks history"}, {"seasonalitycurveid", "Seasonality curve"}, {"maximumsupply", "Maximum supply"}, {"minimumsupply", "Minimum supply"}, {"targetweekssupply", "Target weeks supply"}, {"orderminimum", "Order minimum"}, {"ordermultiple", "Order multiple"}, {"replenishmentmethod", "Replenishment method"}, {"displayproductnumber", "Product number"}, {"enabled", "Enabled?"}, {"historyreplenconfigsource", "Historical replenishment source"}, {"orderreplenconfigsource", "Order replenishment source"}, {"stockreplenconfigsource", "Stock replenishment source"}, {"searchname", "Search name"}}),
    #"Added Custom | StoreItemKey" = Table.AddColumn(#"Renamed Columns", "StoreItemKey", each [Store number] & "-" & [Product number]),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | StoreItemKey",{{"Enabled?", type logical}, {"StoreItemKey", type text}, {"Store/product eligible?", type logical}})
in
    #"Changed Type"
```

### Calendar

```sql
let
    Source = Sql.Database(ServerName, "LH_Mart", [CommandTimeout=#duration(0, 2, 0, 0)]),
    dbo_date_dim = Source{[Schema="dbo",Item="date_dim"]}[Data],
    #"Filtered Rows" = Table.SelectRows(dbo_date_dim, each [fiscal_year] >= 2024),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows",{{"actual_date", "Actual Datetime"}, {"fiscal_year", "Fiscal Year"}, {"season", "Season"}, {"fiscal_quarter", "Fiscal Quarter"}, {"fiscal_period", "Fiscal Month"}, {"fiscal_week", "Fiscal Week"}, {"month", "Calendar Month Id"}, {"year", "Calendar Year"}, {"month_name", "Calendar Month Name"}, {"day_of_month", "Day of Calendar Month"}, {"day_of_year", "Day of Calendar Year"}, {"day_name", "Day Name"}, {"weekend_y_n", "Is Weekend"}, {"day_of_week", "Day of Week"}, {"day_id", "Running Fiscal Day Id"}, {"week_of_period", "Week of Fiscal Month"}, {"week_of_quarter", "Week of Fiscal Quarter"}, {"period_of_quarter", "Month of Fiscal Quarter"}, {"holiday_period_code", "Holiday Period Code"}, {"week_id", "Running Fiscal Week Id"}, {"period_id", "Running Fiscal Month Id"}, {"quarter_id", "Running Fiscal Quarter Id"}, {"org_fiscal_quarter", "Fiscal Quarter 2"}, {"org_fiscal_period", "Fiscal Month 2"}, {"org_fiscal_week", "Fiscal Week 2"}, {"org_week_of_period", "Week of Fiscal Month 2"}, {"org_week_of_quarter", "Week of Fiscal Quarter 2"}, {"org_period_of_quarter", "Month of Fiscal Quarter 2"}}),
    #"Filtered Rows | Fiscal Year > 2018" = Table.SelectRows(#"Renamed Columns", each ([Fiscal Year] > 2018)),
    #"Inserted Date | Actual Date" = Table.AddColumn(#"Filtered Rows | Fiscal Year > 2018", "Actual Date", each Date.From([Actual Datetime]), type date),
    #"Removed Columns | Duplicates" = Table.RemoveColumns(#"Inserted Date | Actual Date",{"Fiscal Quarter 2", "Fiscal Month 2", "Fiscal Week 2", "Week of Fiscal Month 2", "Week of Fiscal Quarter 2", "Month of Fiscal Quarter 2", "Calendar Month Name", "Calendar Month Id"}),
    #"Sorted Rows | Actual Datetime ASC" = Table.Sort(#"Removed Columns | Duplicates",{{"Actual Datetime", Order.Ascending}}),
    #"Added Custom | Fiscal Year (Header)" = Table.AddColumn(#"Sorted Rows | Actual Datetime ASC", "Fiscal Year (Header)", each "FY" & Text.From([Fiscal Year])),
    #"Added Custom | Fiscal Quarter (Header)" = Table.AddColumn(#"Added Custom | Fiscal Year (Header)", "Fiscal Quarter (Header)", each "FQ" & Text.From([Fiscal Quarter])),
    #"Added Conditional Column | Fiscal Month (Name)" = Table.AddColumn(#"Added Custom | Fiscal Quarter (Header)", "Fiscal Month (Name)", each if [Fiscal Month] = 1 then "Febuary" else if [Fiscal Month] = 2 then "March" else if [Fiscal Month] = 3 then "April" else if [Fiscal Month] = 4 then "May" else if [Fiscal Month] = 5 then "June" else if [Fiscal Month] = 6 then "July" else if [Fiscal Month] = 7 then "August" else if [Fiscal Month] = 8 then "September" else if [Fiscal Month] = 9 then "October" else if [Fiscal Month] = 10 then "November" else if [Fiscal Month] = 11 then "December" else if [Fiscal Month] = 12 then "January" else null),
    #"Inserted Month Name | Calendar Month (Name)" = Table.AddColumn(#"Added Conditional Column | Fiscal Month (Name)", "Calendar Month (Name)", each Date.MonthName([Actual Datetime]), type text),
    #"Inserted Month | Calendar Month INT" = Table.AddColumn(#"Inserted Month Name | Calendar Month (Name)", "Calendar Month", each Date.Month([Actual Datetime]), Int64.Type),
    #"Added Custom | Fiscal Month (Header)" = Table.AddColumn(#"Inserted Month | Calendar Month INT", "Fiscal Month (Header)", each Text.PadStart(Text.From([Fiscal Month]),2,"0") & "-" & [#"Fiscal Month (Name)"]),
    #"Added Custom | Calendar Month (Header)" = Table.AddColumn(#"Added Custom | Fiscal Month (Header)", "Calendar Month (Header)", each Text.PadStart(Text.From([#"Calendar Month"]),2,"0") & "-" & [#"Calendar Month (Name)"]),
    #"Added Custom | Fiscal Week (Header)" = Table.AddColumn(#"Added Custom | Calendar Month (Header)", "Fiscal Week (Header)", each "FW" & Text.PadStart(Text.From([Fiscal Week]),2,"0")),
    #"Inserted Quarter | Calendar Quarter INT" = Table.AddColumn(#"Added Custom | Fiscal Week (Header)", "Calendar Quarter", each Date.QuarterOfYear([Actual Datetime]), Int64.Type),
    #"Added Custom | Calendar Quarter (Header)" = Table.AddColumn(#"Inserted Quarter | Calendar Quarter INT", "Calendar Quarter (Header)", each "CQ" & Text.From([#"Calendar Quarter"])),
    #"Added Custom | Calendar Year (Header)" = Table.AddColumn(#"Added Custom | Calendar Quarter (Header)", "Calendar Year (Header)", each "CY" & Text.From([Calendar Year])),
    #"Inserted Week of Year | Calendar Week INT" = Table.AddColumn(#"Added Custom | Calendar Year (Header)", "Calendar Week", each Date.WeekOfYear([Actual Datetime]), Int64.Type),
    #"Added Custom | Calendar Week (Header)" = Table.AddColumn(#"Inserted Week of Year | Calendar Week INT", "Calendar Week (Header)", each "CW" & Text.PadStart(Text.From([Calendar Week]),2,"0")),
    #"Replaced Value | """" with NULL" = Table.ReplaceValue(#"Added Custom | Calendar Week (Header)","",null,Replacer.ReplaceValue,{"Holiday Period Code"}),
    #"Reordered Columns" = Table.ReorderColumns(#"Replaced Value | """" with NULL",{"date_key", "Actual Datetime", "Actual Date", "Fiscal Year", "Fiscal Quarter", "Fiscal Month", "Fiscal Month (Name)", "Fiscal Week", "Calendar Year", "Calendar Quarter", "Calendar Month", "Calendar Month (Name)", "Calendar Week", "Day Name", "Is Weekend", "Holiday Period Code", "Season", "Day of Week", "Day of Calendar Month", "Day of Calendar Year", "Week of Fiscal Month", "Week of Fiscal Quarter", "Month of Fiscal Quarter", "Running Fiscal Day Id", "Running Fiscal Week Id", "Running Fiscal Month Id", "Running Fiscal Quarter Id", "Fiscal Year (Header)", "Fiscal Quarter (Header)",  "Fiscal Month (Header)", "Fiscal Week (Header)", "Calendar Year (Header)", "Calendar Quarter (Header)", "Calendar Month (Header)", "Calendar Week (Header)"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Reordered Columns",{{"Calendar Week (Header)", type text}, {"Calendar Month (Header)", type text}, {"Calendar Quarter (Header)", type text}, {"Calendar Year (Header)", type text}, {"Fiscal Week (Header)", type text}, {"Fiscal Month (Header)", type text}, {"Fiscal Quarter (Header)", type text}, {"Fiscal Year (Header)", type text}, {"Fiscal Month (Name)", type text}}),
    #"Added Custom" = Table.AddColumn(#"Changed Type", "Merch_Year_Week", each Number.ToText([Fiscal Year]) & Text.PadStart(Number.ToText([Fiscal Week]),2,"0")),
    #"Sorted Rows" = Table.Sort(#"Added Custom",{{"Actual Datetime", Order.Ascending}})
in
    #"Sorted Rows"
```

### Products (PLM)

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="WITH distinct_products AS 
 (
     SELECT
        MIN(products.[product_key]) AS [product_key],
        products.[style_code]         
		FROM [dbo].[product_dim_le] products
		GROUP BY products.[style_code]      
 )

 SELECT
 products.[style_code] AS [Style Code],
 products.[style_desc] AS [Style Description],
 products.[consumer_group] AS [Consumer Group],
 products.[department] AS [Department],
 products.[class] AS [Class],
 products.[subclass] AS [Subclass],
 products.[KeyStory] AS [Key Story],
 products.[LicensedCollection] AS [Licensed Collection],
products.[product_desc]                                 AS [Product Description],
products.[merch_status]                                 AS [Merch Status],
TRY_CAST(attributes.[MerchInDate] AS DATE) AS [Merch In Date],
COALESCE(TRY_CAST(attributes.[merchOutDate] AS DATE), TRY_CAST(attributes.[ODATE] AS DATE)) AS [Merch Out Date],
CAST(CASE WHEN attributes.[LICEN] = 'NO' THEN 0 WHEN attributes.[LICEN] IS NULL THEN NULL ELSE 1 END AS BIT) AS [Licensed],
attributes.[OccasionCode]                               AS [Occasion Code]

  FROM distinct_products
	INNER JOIN [dbo].[product_dim_le] products
		ON distinct_products.product_key = products.product_key 
		LEFT JOIN (SELECT DISTINCT
[StyleCode],[MerchInDate],[merchOutDate],[LICEN],[OccasionCode],[ODATE]
  FROM [LH_Mart].[dbo].[productcatalogmasterattributes]) AS attributes
  ON products.[style_code] = attributes.[StyleCode]
", CommandTimeout=#duration(0, 2, 0, 0)])
in
    #"Source"
```

### Sales Volume Grades

```sql
let
    Source = SharePoint.Files("https://babw.sharepoint.com/sites/ReportMaster", [ApiVersion = 15]),
    #"Sales Volume Grades xlsx_https://babw sharepoint com/sites/ReportMaster/Shared Documents/Report Master/Retail Replen PBI Report Excel Files/" = Source{[Name="Sales Volume Grades.xlsx",#"Folder Path"="https://babw.sharepoint.com/sites/ReportMaster/Shared Documents/Report Master/Retail Replen PBI Report Excel Files/"]}[Content],
    #"Imported Excel Workbook" = Excel.Workbook(#"Sales Volume Grades xlsx_https://babw sharepoint com/sites/ReportMaster/Shared Documents/Report Master/Retail Replen PBI Report Excel Files/"),
    Query1_Sheet = #"Imported Excel Workbook"{[Item="Query1",Kind="Sheet"]}[Data],
    #"Promoted Headers" = Table.PromoteHeaders(Query1_Sheet, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"Grade", type text}, {"Multiplier", type number}, {"Index", Int64.Type}})
in
    #"Changed Type"
```

### Measure Table

```sql
let
    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
in
    #"Removed Columns"
```

### DC priority and simple execution schedule

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [CommandTimeout=#duration(0, 2, 0, 0)]),
    dbo_suntafretailreplenstoredcsettings = Source{[Schema="dbo",Item="suntafretailreplenstoredcsettings"]}[Data],
    #"Filtered Rows" = Table.SelectRows(dbo_suntafretailreplenstoredcsettings, each ([IsDelete] = null)),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows",{{"replenishfriday", "Replenish Friday?"}, {"replenishmonday", "Replenish Monday?"}, {"replenishsaturday", "Replenish Saturday?"}, {"replenishsunday", "Replenish Sunday?"}, {"replenishthursday", "Replenish Thursday?"}, {"replenishtuesday", "Replenish Tuesday?"}, {"replenishwednesday", "Replenish Wednesday?"}, {"generateplannedtransfers", "Generate planned transfers?"}, {"storenumber", "Store number"}, {"inventlocationdataareaid", "Warehouse company"}, {"inventlocationid", "Warehouse"}, {"priority", "Priority"}, {"nextexecutionstorepriority", "Next execution store priority"}, {"modifieddatetime", "Modified datetime"}, {"modifiedby", "Modified by"}, {"modifiedtransactionid", "Modified transaction Id"}, {"createddatetime", "Created datetime"}, {"createdby", "Created by"}, {"createdtransactionid", "Created transaction Id"}, {"dataareaid", "Company"}, {"recid", "RecId"}, {"tableid", "TableId"}, {"versionnumber", "Version number"}, {"createdon", "Created on"}, {"modifiedon", "Modified on"}, {"IsDelete", "Is Delete?"}, {"createdonpartition", "Created on partition"}, {"PartitionId", "Partition Id"}}),
    #"Removed Columns" = Table.RemoveColumns(#"Renamed Columns",{"recversion", "partition", "sysrowversion", "Version number", "sysdatastatecode"}),
    #"Sorted Rows" = Table.Sort(#"Removed Columns",{{"Priority", Order.Ascending}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Sorted Rows",{{"Replenish Friday?", type logical}, {"Replenish Monday?", type logical}, {"Replenish Saturday?", type logical}, {"Replenish Sunday?", type logical}, {"Replenish Thursday?", type logical}, {"Replenish Tuesday?", type logical}, {"Replenish Wednesday?", type logical}, {"Generate planned transfers?", type logical}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Changed Type",{"Id", "SinkCreatedOn", "SinkModifiedOn", "Replenish Sunday?", "Replenish Monday?", "Replenish Tuesday?", "Replenish Wednesday?", "Replenish Thursday?", "Replenish Friday?", "Replenish Saturday?", "Generate planned transfers?", "Store number", "Warehouse company", "Warehouse", "Priority", "Next execution store priority", "Modified datetime", "Modified by", "Modified transaction Id", "Created datetime", "Created by", "Created transaction Id", "Company", "RecId", "TableId", "Created on", "Modified on", "Is Delete?", "Created on partition", "Partition Id"}),
    #"Removed Duplicates" = Table.Distinct(#"Reordered Columns", {"Store number"})
in
    #"Removed Duplicates"
```

### On-Hand Inventory | DC Warehouses

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="WITH PhysicalInventory AS (
    SELECT 
        [isum].[inventlocationid], 
        [isum].[itemid], 
        SUM(CASE WHEN [isum].[inventstatusid] = 'AVAIL' THEN [physicalinvent] ELSE 0 END) AS [physicalinvent_AVAIL],
        SUM(CASE WHEN [isum].[inventstatusid] = 'PendPut' THEN [physicalinvent] ELSE 0 END) AS [physicalinvent_PendPut]
    FROM [inventsum] AS [isum]
    INNER JOIN [inventdim] AS [idim]
        ON [isum].[inventdimid] = [idim].[inventdimid]
    WHERE
        [isum].[inventlocationid] IN ('9980', '9970', '9960', '9942', '9941', '8175')
        AND [isum].[closed] = 0
        AND ([isum].[IsDelete] IS NULL OR [isum].[IsDelete] = 0)
    GROUP BY 
        [isum].[inventlocationid], 
        [isum].[itemid]
),
ReservedPhysical AS (
    SELECT 
        [isum].[inventlocationid], 
        [isum].[itemid], 
        SUM(CASE WHEN [isum].[inventstatusid] = 'AVAIL' THEN [reservphysical] ELSE 0 END) AS [reservphysical_AVAIL],
        SUM(CASE WHEN [isum].[inventstatusid] = 'PendPut' THEN [reservphysical] ELSE 0 END) AS [reservphysical_PendPut]
    FROM [inventsum] AS [isum]
    INNER JOIN [inventdim] AS [idim]
        ON [isum].[inventdimid] = [idim].[inventdimid]
    WHERE
        [isum].[inventlocationid] IN ('9980', '9970', '9960', '9942', '9941', '8175')
        AND [isum].[inventstatusid] IN ('AVAIL', 'PendPut')
        AND [isum].[closed] = 0
        AND ([isum].[IsDelete] IS NULL OR [isum].[IsDelete] = 0)
        AND ([idim].[wmslocationid] IS NULL OR ([isum].[inventlocationid] = '9960' AND [idim].[wmslocationid] = 'Main'))
        AND [idim].[licenseplateid] IS NULL
        AND [idim].[wmspalletid] IS NULL
    GROUP BY 
        [isum].[inventlocationid], 
        [isum].[itemid]
),
CombinedInventory AS (
    SELECT 
        piv.inventlocationid,
        piv.itemid,
        piv.physicalinvent_AVAIL,
        ISNULL(rsv.reservphysical_AVAIL, 0) AS [reservphysical_AVAIL],
        (piv.physicalinvent_AVAIL - ISNULL(rsv.reservphysical_AVAIL, 0)) AS [availphysical_AVAIL],
        piv.physicalinvent_PendPut,
        ISNULL(rsv.reservphysical_PendPut, 0) AS [reservphysical_PendPut],
        (piv.physicalinvent_PendPut - ISNULL(rsv.reservphysical_PendPut, 0)) AS [availphysical_PendPut]
    FROM PhysicalInventory AS piv
    LEFT JOIN ReservedPhysical AS rsv
        ON piv.inventlocationid = rsv.inventlocationid
        AND piv.itemid = rsv.itemid
)
SELECT DISTINCT
        SUM(inventsum.[availordered])                                               AS [Total available]             ,
        SUM(ci.[availphysical_AVAIL])                                               AS [Available physical]          ,
        SUM(inventsum.[onorder])                                                    AS [On order]                    ,
        SUM(CASE WHEN (inventsum.wmslocationid IS NOT NULL AND inventsum.wmslocationid != 'PACK' AND inventsum.wmslocationid != 'DOOR') THEN inventsum.[ordered] ELSE 0 END)                                                   AS [Ordered]                     ,
        SUM(inventsum.[physicalinvent])                                             AS [Physical inventory]          ,
        SUM(inventsum.[reservordered])                                              AS [Ordered reserved]            ,
        SUM(inventsum.[reservphysical])                                             AS [Physical reserved]           ,
        inventsum.[itemid]                                                          AS [Item number]                 ,
        inventsum.[inventlocationid]                                                AS [Warehouse]                   ,
        UPPER(inventsum.[inventstatusid])                                           AS [Inventory status]            ,
        inventsum.[dataareaid]                                                      AS [Company]                     ,
        suntafretailreplenactivesettings.[babstoreproducteligible]                  AS [Store/product eligible?]     ,
        suntafretailreplenactivesettings.[maximumsupply]                            AS [Maximum supply]              ,
        suntafretailreplenactivesettings.[minimumsupply]                            AS [Minimum supply]              ,
        suntafretailreplenactivesettings.[orderminimum]                             AS [Order minimum]               ,
        suntafretailreplenactivesettings.[ordermultiple]                            AS [Order multiple]              ,
        CONCAT(inventsum.[inventlocationid] , '-', inventsum.[itemid])              AS [StoreItemKey]                ,
        CONCAT(inventsum.[inventlocationid] , '-', inventsum.[itemid])              AS [AvailableStoreItemKey]       ,
        CAST((SUM(ci.[availphysical_AVAIL]) - SUM(inventsum.[onorder])) AS BIGINT) AS [Available for replenishments],
        plm.[Style Description]                                                                                      ,
        plm.[Department]                                                                                             ,
        plm.[Class]                                                                                                  ,
        plm.[Consumer Group]                                                                                         ,
        plm.[Key Story]                                                                                              ,
        plm.[OrderMultiple] AS [Order Multiple]                                                                      ,
        plm.[Distribution Multiple]
FROM
        [inventsum]
LEFT JOIN
        CombinedInventory AS ci
ON
        inventsum.[inventlocationid] = ci.[inventlocationid]
AND     inventsum.[itemid] = ci.[itemid]
LEFT JOIN
        [inventlocation]
ON
        inventsum.[inventlocationid] = inventlocation.[inventlocationid]
AND     inventsum.[dataareaid]       = inventlocation.[dataareaid]
LEFT JOIN
        [ecoresproduct]
ON
        inventsum.[itemid] = ecoresproduct.[displayproductnumber]
LEFT JOIN
        [suntafretailreplenactivesettings]
ON
        ecoresproduct.[recid]        = suntafretailreplenactivesettings.[distinctproduct]
AND     inventsum.[inventlocationid] = suntafretailreplenactivesettings.[storenumber]
LEFT JOIN
        (
       SELECT DISTINCT
                        attributes.[ProductNumber] AS [Product Number]   ,
                        products.[style_desc]      AS [Style Description],
                        products.[department]      AS [Department]       ,
                        products.[class]           AS [Class]            ,
                        attributes.[ConsumerGroup] AS [Consumer Group]   ,
                        products.[concept]         AS [Concept]          ,
                        attributes.[KeyStory]      AS [Key Story]        ,
                        attributes.[OrderMultiple]                       ,
                        attributes.[DistributionMultiple] AS [Distribution Multiple]
                FROM
                        [LH_Mart].[dbo].[product_dim] products
                LEFT JOIN
                        [LH_Mart].[dbo].[productcatalogmasterattributes] attributes
                ON
                        products.[jurisdiction_code] = attributes.[ProductSellingGeography]
                AND     products.[style_code]        = attributes.[StyleCode]
				AND     products.[subclass_code]        = attributes.[SubClassCode]
                                	   AND     products.[subclass_code]        = attributes.[SubClassCode]
                WHERE
                        products.[style_code] IS NOT NULL
                AND     attributes.[ProductNumber] IS NOT NULL
                AND     products.[product_key] > 0
                OR      (
                                attributes.[StyleCode]        = '333697'
                                AND attributes.[FriendHeight] = '16') ) AS plm
ON
        inventsum.[itemid] = plm.[Product Number]
WHERE
        inventsum.[inventlocationid] IN ('9980',
                                         '9970',
                                         '9960',
                                         '9942',
                                         '9941',
                                         '8175')
AND     inventsum.[inventstatusid] IS NOT NULL
AND     (
                inventsum.[IsDelete] IS NULL
                OR inventsum.[IsDelete] = 0)
AND     (
                inventlocation.[IsDelete] IS NULL
                OR inventlocation.[IsDelete] = 0)
AND     (
                ecoresproduct.[IsDelete] IS NULL
                OR ecoresproduct.[IsDelete] = 0)
AND     (
                suntafretailreplenactivesettings.[IsDelete] IS NULL
                OR suntafretailreplenactivesettings.[IsDelete] = 0)
AND     UPPER(inventsum.[inventstatusid]) = 'AVAIL'
AND    inventsum.[closed] = 0
GROUP BY
        inventsum.[itemid]                                        ,
        inventsum.[inventlocationid]                              ,
        UPPER(inventsum.[inventstatusid])                         ,
        inventsum.[dataareaid]                                    ,
        inventlocation.[name]                                     ,
        ecoresproduct.[searchname]                                ,
        ecoresproduct.[babcolordescription]                       ,
        suntafretailreplenactivesettings.[babstoreproducteligible],
        suntafretailreplenactivesettings.[maximumsupply]          ,
        suntafretailreplenactivesettings.[minimumsupply]          ,
        suntafretailreplenactivesettings.[targetweekssupply]      ,
        suntafretailreplenactivesettings.[orderminimum]           ,
        suntafretailreplenactivesettings.[ordermultiple]          ,
        plm.[Style Description]                                   ,
        plm.[Department]                                          ,
        plm.[Class]                                               ,
        plm.[Consumer Group]                                      ,
        plm.[Key Story]                                           ,
        plm.[OrderMultiple]                                       ,
        plm.[Distribution Multiple]
", CommandTimeout=#duration(0, 2, 0, 0)])
in
    #"Source"
```

### Stores (Store MDM)

```sql
let
    Source = Sql.Database(ServerName, "LH_Mart", [Query="select#(lf)s.store_name as Store,#(lf)s.store_id as Number,#(lf)v.inventsiteid as 'Store Number',#(lf)s.state_province as State,#(lf)null as Layout,                                             -- not in LH_Mart.dbo.store_dim source#(lf)s.opening_date as 'First Day of Trade',#(lf)s.store_type as Design,                               -- same field but most values are null in LH_Mart.dbo.store_dim#(lf)case when v.JurisidictionCode = 'US' then 'USD'#(lf)       when v.JurisidictionCode = 'UK' then 'GBP'#(lf)       when v.JurisidictionCode = 'IE' then 'EUR'#(lf)       when v.JurisidictionCode = 'CA' then 'CAD'#(lf)       else null end as 'Currency',#(lf)s.email as 'Email Address',                           -- stores have 2 options for email, LH_Mart.dbo.store_dim source uses this format#(lf)address1 as 'Address Line 1',#(lf)address2 as 'Address Line 2',#(lf)city as 'City',#(lf)county as 'County',#(lf)country as 'Country Code',#(lf)postal_code as 'Postal Code',               -- LH_Mart.dbo.store_dim source values include hyphen and last 4 digits#(lf)null as 'ZIP+4',                                      -- can extract from postal_code if necessary#(lf)phone as 'Phone Number',#(lf)bearritory as 'District',#(lf)square_feet as 'Total Sq Footage',          -- same field but most values are null in LH_Mart.dbo.store_dim source#(lf)null as 'Amusement Park (Y/N)',             -- not in Store MDM source  #(lf)null as 'Temp Space (Y/N)',                           -- not in Store MDM source#(lf)null as 'Seasonal (Y/N)',                             -- not in Store MDM source#(lf)null as 'UK Territory Store (Y/N)'              -- not in Store MDM source#(lf)from LH_Mart.dbo.store_dim s#(lf)join LH_D365.dbo.d365LocationMapping_View v on s.store_key = v.store_key#(lf)where v.JurisidictionCode in ('US','IE','UK','CA')#(lf)order by store_id asc", CommandTimeout=#duration(0, 2, 0, 0)])
in
    Source
```

### FedEx Transit Times

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="SELECT
        [cvtppl].[toinventlocation] AS [Store number] ,
        CASE
        WHEN
                [cvtppl].[frominventlocation] = '9980'
        THEN
                [cvtppt].[transportdays]
        ELSE
                0
        END AS [Ground From 9980] ,
        CASE
        WHEN
                [cvtppl].[frominventlocation] = '9960'
        THEN
                [cvtppt].[transportdays]
        ELSE
                0
        END      AS [Ground From 9960] ,
        'Actual' AS [Estimate Type]
FROM
        [dbo].[custvendtransportpointline] AS [cvtppl]
INNER JOIN
        [dbo].[custvendtransporttime] AS [cvtppt]
ON
        [cvtppt].[transportpointlinerecid] = [cvtppl].[recid]
AND     [cvtppt].[dataareaid]              = [cvtppl].[dataareaid]
WHERE
        [cvtppl].[toinventlocation] NOT IN ('9980',
                                            '9960')
AND     [cvtppl].[frominventlocation] IN ('9980',
                                          '9960')
AND     [cvtppl].[totransportpointtype] = 0
AND     [cvtppt].[dlvmode]              = 1
AND		[cvtppl].[IsDelete] IS NULL", CommandTimeout=#duration(0, 2, 0, 0)])
in
    Source
```

### Retail store/product replenishment calculation log (Combined)

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="WITH distinct_products AS 
 (
     SELECT
        MIN(products.[product_key]) AS [product_key],
        products.[style_code]         
		FROM [dbo].[product_dim_le] products
		GROUP BY products.[style_code]      
 )
, productAttruibutes AS (
 SELECT
 products.[style_code] AS [Style Code],
 products.[concept] AS [Concept],
 products.[KeyStory] AS [Key Story],
 products.[consumer_group] AS [Consumer Group]
  FROM distinct_products
	INNER JOIN [dbo].[product_dim_le] products
		ON distinct_products.product_key = products.product_key 
)
, baseData AS (
SELECT
    suntafretailreplenstoredistinctproductcalclog.[parmid] AS [Parameter ID]
  , suntafretailreplenstoredistinctproductcalclog.[storenumber] AS [Store number]
  , suntafretailreplenstoredistinctproductcalclog.[weekshistory] AS [Weeks history]
  , NULLIF(suntafretailreplenstoredistinctproductcalclog.[seasonalitycurveid], '') AS [Seasonality curve]
  , suntafretailreplenstoredistinctproductcalclog.[avgweeklysales] AS [Average weekly sales]
  , suntafretailreplenstoredistinctproductcalclog.[nonseasonalavgweeklysales] AS [Non-seasonal average weekly sales]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[minimumsupply] AS BIGINT) AS [Minimum supply]
  , suntafretailreplenstoredistinctproductcalclog.[targetweekssupply] AS [Target weeks supply]
  , suntafretailreplenstoredistinctproductcalclog.[targetweeksforecast] AS [Target weeks forecast]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[maximumsupply] AS BIGINT) AS [Maximum supply]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[storeonhand] AS BIGINT) AS [Store on-hand inventory]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[storeopenreplenishment] AS BIGINT) AS [Store open replenishment]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[suggestedreplenishment] AS BIGINT) AS [Suggested replenishment]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[actualreplenishment] AS BIGINT) AS [Actual replenishment]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[orderminimum] AS BIGINT) AS [Order minimum]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[ordermultiple] AS BIGINT) AS [Order multiple]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[firmedreplenishment] AS BIGINT) AS [Firmed replenishment]
  , CASE
        WHEN CAST(suntafretailreplenstoredistinctproductcalclog.[historystartdate] AS DATE) = '1900-01-01' THEN
            NULL
        ELSE
            CAST(suntafretailreplenstoredistinctproductcalclog.[historystartdate] AS DATE)
    END AS [History start date]
  , suntafretailreplenstoredistinctproductcalclog.[createddatetime] AS [Created datetime]
  , suntafretailreplenstoredistinctproductcalclog.[modifieddatetime] AS [Modified datetime]
  , ecoresproduct.[babcolordescription] AS [Color Description]
  , ecoresproduct.[displayproductnumber] AS [Product number]
  , ecoresproduct.[searchname] AS [Search name]
  , CAST(ecoresproduct.[sunplmsyncwithplm] AS BIT) AS [Sync with PLM?]
  , suntafretailreplenstoredistinctproductcalclog.[babinitialcartoncount] AS [Initial carton count]
  , CAST(inventlocation.[babcontainerizebyvolumeonly] AS BIT) AS [Containerize by volume only?]
  , inventlocation.[babdefaulttomodeofdelivery] AS [Mode of Delivery]
  , inventlocation.[babestimatedpalletvolume] AS [Estimated pallet volume by warehouse]
  , CAST(inventlocation.[babretailstore] AS BIT) AS [BAB Retail Store?]
  , CAST(inventlocation.[cyclecountallowpalletmove] AS BIT) AS [Allow license plate moves during cycle counting?]
  , CAST(inventlocation.[decrementloadline] AS BIT) AS [Decrement load line?]
  , inventlocation.[defaultstatusid] AS [Default inventory status ID]
  , inventlocation.[fshstore] AS [Store]
  , inventlocation.[inventlocationid] AS [Warehouse]
  , inventlocation.[inventlocationidtransit] AS [Transit warehouse]
  , inventlocation.[inventlocationlevel] AS [Warehouse level]
  , inventlocation.[inventsiteid] AS [Site]
  , inventlocation.[name] AS [Name]
  , inventlocation.[rbodefaultwmslocationid] AS [Default location]
  , CAST(inventlocation.[removeinventblockingonstatuschange] AS BIT) AS [Remove inventory blocking?]
  , inventlocation.[retailwmslocationiddefaultreturn] AS [Default return location]
  , CAST(inventlocation.[whsenabled] AS BIT) AS [Use warehouse management processes?]
  , CAST(inventlocation.[wmsaislenameactive] AS BIT) AS [Include aisle?]
  , inventlocation.[wmslocationiddefaultissue] AS [Default issue location]
  , inventlocation.[wmslocationiddefaultreceipt] AS [Default receipt location]
  , babsuntafretailreplendcstoredistinctproductcalclog.[inventlocationid] AS [DC Warehouse]
  , babsuntafretailreplendcstoredistinctproductcalclog.[inventlocationpriority] AS [Warehouse priority]
  , NULLIF(babsuntafretailreplendcstoredistinctproductcalclog.[vendaccount], '') AS [Vendor account]
  , CAST(babsuntafretailreplendcstoredistinctproductcalclog.[firmed] AS BIT) AS [Firmed?]
  , babsuntafretailreplendcstoredistinctproductcalclog.[createddatetime] AS [DC Created datetime]
  , babsuntafretailreplendcstoredistinctproductcalclog.[babfirmedcartoncount] AS [Firmed carton count]
  , babsuntafretailreplendcstoredistinctproductcalclog.[baborderreleaseddate] AS [Order released date]
  , babsuntafretailreplendcstoredistinctproductcalclog.[firmingkeyorg] AS [FirmingKeyOrg]
  , CAST(babsuntafretailreplendcstoredistinctproductcalclog.[spilted] AS BIT) AS [Split?]
  , babsuntafretailreplendcstoredistinctproductcalclog.[babdlvmode] AS [Delivery mode]
  , babsuntafretailreplendcstoredistinctproductcalclog.[babadjustedorderquantity] AS [Adjusted order quantity]
  , CAST(babsuntafretailreplendcstoredistinctproductcalclog.[isparent] AS BIT) AS [Parent?]
  , CAST(babsuntafretailreplendcstoredistinctproductcalclog.[isplanoverride] AS BIT) AS [Plan Override?]
  , ecoresproducttranslation.[name] AS [Product name]
  , ecoresproduct_producttype_GlobalOptionsetMetadata.[LocalizedLabel] AS [Product type]
  , ecoresproduct_servicetype_GlobalOptionsetMetadata.[LocalizedLabel] AS [Service type]
  , babsuntafretailreplendcstoredistinctproductcalclog_ordertype_GlobalOptionsetMetadata.[LocalizedLabel] AS [Replenishment order type]
  , babsuntafretailreplendcstoredistinctproductcalclog_babadjustmentstatus_GlobalOptionsetMetadata.[LocalizedLabel] AS [Adjustment status]
  , babsuntafretailreplendcstoredistinctproductcalclog.[suggestedreplenishment] AS [Adj. suggested replenishment]
  , suntafretailreplenstoredistinctproductcalclog_replenishmentmethod_GlobalOptionsetMetadata.[LocalizedLabel] AS [Replenishment method]
  , suntafretailreplenstoredistinctproductcalclog_replenqtymethod_GlobalOptionsetMetadata.[LocalizedLabel] AS [Replenishment quantity method]
  , [Stores].[name] AS [DC Location name]
  , CONCAT(suntafretailreplenstoredistinctproductcalclog.[storenumber], ' | ', inventlocation.[name]) AS [Store line]
  , CONCAT(ecoresproduct.[displayproductnumber], ' | ', ecoresproducttranslation.[name]) AS [Product line]
  , CONCAT(babsuntafretailreplendcstoredistinctproductcalclog.[inventlocationid], ' | ', [Stores].[name]) AS [DC Allocation line]
  , CAST(suntafretailreplenstoredistinctproductcalclog.[createddatetime] AS DATE) AS [Created date]
  , [Products (PLM)].[Concept] AS [Concept]
  , [Products (PLM)].[Key Story] AS [Key Story]
  , [Products (PLM)].[Consumer Group] AS [Consumer Group]
FROM
    [suntafretailreplenstoredistinctproductcalclog]
    LEFT JOIN [babsuntafretailreplendcstoredistinctproductcalclog] AS [babsuntafretailreplendcstoredistinctproductcalclog]
        ON suntafretailreplenstoredistinctproductcalclog.[parmid] = babsuntafretailreplendcstoredistinctproductcalclog.[parmid]
        AND suntafretailreplenstoredistinctproductcalclog.[storenumber] = babsuntafretailreplendcstoredistinctproductcalclog.[storenumber]
        AND suntafretailreplenstoredistinctproductcalclog.[distinctproduct] = babsuntafretailreplendcstoredistinctproductcalclog.[distinctproduct]
    LEFT JOIN [ecoresproduct]
        ON suntafretailreplenstoredistinctproductcalclog.[distinctproduct] = ecoresproduct.[recid]
    LEFT JOIN [inventlocation]
        ON suntafretailreplenstoredistinctproductcalclog.[storenumber] = inventlocation.[inventlocationid]
    LEFT JOIN [ecoresproducttranslation]
        ON ecoresproduct.[recid] = ecoresproducttranslation.[product]
    LEFT JOIN (
        SELECT
            [Option]
          , [LocalizedLabel]
        FROM
            [dbo].[globaloptionsetmetadata] AS [GlobalOptionsetMetadata]
        WHERE
            [EntityName] = 'suntafretailreplenstoredistinctproductcalclog'
            AND [OptionSetName] = 'replenishmentmethod'
    ) AS suntafretailreplenstoredistinctproductcalclog_replenishmentmethod_GlobalOptionsetMetadata
        ON suntafretailreplenstoredistinctproductcalclog.[replenishmentmethod] = suntafretailreplenstoredistinctproductcalclog_replenishmentmethod_GlobalOptionsetMetadata.[Option]
    LEFT JOIN (
        SELECT
            [Option]
          , [LocalizedLabel]
        FROM
            [dbo].[globaloptionsetmetadata] AS [GlobalOptionsetMetadata]
        WHERE
            [EntityName] = 'suntafretailreplenstoredistinctproductcalclog'
            AND [OptionSetName] = 'replenqtymethod'
    ) AS suntafretailreplenstoredistinctproductcalclog_replenqtymethod_GlobalOptionsetMetadata
        ON suntafretailreplenstoredistinctproductcalclog.[replenqtymethod] = suntafretailreplenstoredistinctproductcalclog_replenqtymethod_GlobalOptionsetMetadata.[Option]
    LEFT JOIN (
        SELECT
            [Option]
          , [LocalizedLabel]
        FROM
            [dbo].[globaloptionsetmetadata] AS [GlobalOptionsetMetadata]
        WHERE
            [EntityName] = 'babsuntafretailreplendcstoredistinctproductcalclog'
            AND [OptionSetName] = 'babadjustmentstatus'
    ) AS babsuntafretailreplendcstoredistinctproductcalclog_babadjustmentstatus_GlobalOptionsetMetadata
        ON babsuntafretailreplendcstoredistinctproductcalclog.[babadjustmentstatus] = babsuntafretailreplendcstoredistinctproductcalclog_babadjustmentstatus_GlobalOptionsetMetadata.[Option]
    LEFT JOIN (
        SELECT
            [Option]
          , [LocalizedLabel]
        FROM
            [dbo].[globaloptionsetmetadata] AS [GlobalOptionsetMetadata]
        WHERE
            [EntityName] = 'babsuntafretailreplendcstoredistinctproductcalclog'
            AND [OptionSetName] = 'reftype'
    ) AS babsuntafretailreplendcstoredistinctproductcalclog_reftype_GlobalOptionsetMetadata
        ON babsuntafretailreplendcstoredistinctproductcalclog.[reftype] = babsuntafretailreplendcstoredistinctproductcalclog_reftype_GlobalOptionsetMetadata.[Option]
    LEFT JOIN (
        SELECT
            [Option]
          , [LocalizedLabel]
        FROM
            [dbo].[globaloptionsetmetadata] AS [GlobalOptionsetMetadata]
        WHERE
            [EntityName] = 'babsuntafretailreplendcstoredistinctproductcalclog'
            AND [OptionSetName] = 'ordertype'
    ) AS babsuntafretailreplendcstoredistinctproductcalclog_ordertype_GlobalOptionsetMetadata
        ON babsuntafretailreplendcstoredistinctproductcalclog.[ordertype] = babsuntafretailreplendcstoredistinctproductcalclog_ordertype_GlobalOptionsetMetadata.[Option]
    LEFT JOIN (
        SELECT
            [Option]
          , [LocalizedLabel]
        FROM
            [dbo].[globaloptionsetmetadata] AS [GlobalOptionsetMetadata]
        WHERE
            [EntityName] = 'ecoresproduct'
            AND [OptionSetName] = 'producttype'
    ) AS ecoresproduct_producttype_GlobalOptionsetMetadata
        ON ecoresproduct.[producttype] = ecoresproduct_producttype_GlobalOptionsetMetadata.[Option]
    LEFT JOIN (
        SELECT
            [Option]
          , [LocalizedLabel]
        FROM
            [dbo].[globaloptionsetmetadata] AS [GlobalOptionsetMetadata]
        WHERE
            [EntityName] = 'ecoresproduct'
            AND [OptionSetName] = 'servicetype'
    ) AS ecoresproduct_servicetype_GlobalOptionsetMetadata
        ON ecoresproduct.[servicetype] = ecoresproduct_servicetype_GlobalOptionsetMetadata.[Option]
    LEFT JOIN [inventlocation] AS [Stores]
        ON babsuntafretailreplendcstoredistinctproductcalclog.[inventlocationid] = [Stores].[inventlocationid]
			AND babsuntafretailreplendcstoredistinctproductcalclog.dataareaid = [Stores].dataareaid
    LEFT JOIN productAttruibutes AS [Products (PLM)]
        ON ecoresproduct.[displayproductnumber] = [Products (PLM)].[Style Code]
WHERE
    suntafretailreplenstoredistinctproductcalclog.[modifieddatetime] >= CAST(DATEADD(WEEK, DATEDIFF(WEEK, 0, DATEADD(WEEK, -52, GETDATE())), 0) AS DATE)
    AND (suntafretailreplenstoredistinctproductcalclog.[IsDelete] IS NULL OR suntafretailreplenstoredistinctproductcalclog.[IsDelete] = 0)
    AND (ecoresproduct.[IsDelete] IS NULL OR ecoresproduct.[IsDelete] = 0)
    AND (babsuntafretailreplendcstoredistinctproductcalclog.[IsDelete] IS NULL OR babsuntafretailreplendcstoredistinctproductcalclog.[IsDelete] = 0)
)

SELECT
[Parameter ID],
[Store number],
[Weeks history],
[Seasonality curve],
[Average weekly sales],
[Non-seasonal average weekly sales],
[Minimum supply],
[Target weeks supply],
[Target weeks forecast],
[Maximum supply],
[Store on-hand inventory],
[Store open replenishment],
[Suggested replenishment],
[Actual replenishment],
[Order minimum],
[Order multiple],
[Firmed replenishment],
[History start date],
[Created datetime],
[Modified datetime],
[Color Description],
[Product number],
[Search name],
[Sync with PLM?],
[Initial carton count],
[Containerize by volume only?],
[Mode of Delivery],
[Estimated pallet volume by warehouse],
[BAB Retail Store?],
[Allow license plate moves during cycle counting?],
[Decrement load line?],
[Default inventory status ID],
[Store],
[Warehouse],
[Transit warehouse],
[Warehouse level],
[Site],
[Name],
[Default location],
[Remove inventory blocking?],
[Default return location],
[Use warehouse management processes?],
[Include aisle?],
[Default issue location],
[Default receipt location],
[DC Warehouse],
[Warehouse priority],
[Vendor account],
[Firmed?],
[DC Created datetime],
SUM([Firmed carton count]) AS [Firmed carton count],
[Order released date],
[FirmingKeyOrg],
[Split?],
[Delivery mode],
[Adjusted order quantity],
[Parent?],
[Plan Override?],
[Product name],
[Product type],
[Service type],
[Replenishment order type],
[Adjustment status],
COALESCE(SUM([Adj. suggested replenishment]),0) AS [Adj. suggested replenishment],
[Replenishment method],
[Replenishment quantity method],
[DC Location name],
[Store line],
[Product line],
[DC Allocation line],
[Created date],
[Concept],
[Key Story],
[Consumer Group]
FROM baseData
GROUP BY [Parameter ID],
[Store number],
[Weeks history],
[Seasonality curve],
[Average weekly sales],
[Non-seasonal average weekly sales],
[Minimum supply],
[Target weeks supply],
[Target weeks forecast],
[Maximum supply],
[Store on-hand inventory],
[Store open replenishment],
[Suggested replenishment],
[Actual replenishment],
[Order minimum],
[Order multiple],
[Firmed replenishment],
[History start date],
[Created datetime],
[Modified datetime],
[Color Description],
[Product number],
[Search name],
[Sync with PLM?],
[Initial carton count],
[Containerize by volume only?],
[Mode of Delivery],
[Estimated pallet volume by warehouse],
[BAB Retail Store?],
[Allow license plate moves during cycle counting?],
[Decrement load line?],
[Default inventory status ID],
[Store],
[Warehouse],
[Transit warehouse],
[Warehouse level],
[Site],
[Name],
[Default location],
[Remove inventory blocking?],
[Default return location],
[Use warehouse management processes?],
[Include aisle?],
[Default issue location],
[Default receipt location],
[DC Warehouse],
[Warehouse priority],
[Vendor account],
[Firmed?],
[DC Created datetime],
[Order released date],
[FirmingKeyOrg],
[Split?],
[Delivery mode],
[Adjusted order quantity],
[Parent?],
[Plan Override?],
[Product name],
[Product type],
[Service type],
[Replenishment order type],
[Adjustment status],
[Replenishment method],
[Replenishment quantity method],
[DC Location name],
[Store line],
[Product line],
[DC Allocation line],
[Created date],
[Concept],
[Key Story],
[Consumer Group]
", CommandTimeout=#duration(0, 2, 0, 0)]),
    #"Filtered Rows" = Table.SelectRows(Source, each [Modified datetime] >= RangeStart and [Modified datetime] < RangeEnd)
in
    #"Filtered Rows"
```

### store_dim

```sql
let
    Source = Sql.Database(ServerName, "LH_Mart", [CommandTimeout=#duration(0, 2, 0, 0)]),
    dbo_store_dim = Source{[Schema="dbo",Item="store_dim"]}[Data],
    #"Renamed Columns" = Table.RenameColumns(dbo_store_dim,{{"store_id", "Location Number"}, {"bearea", "Bearea"}, {"store_name", "Location Name"}, {"bearritory", "District"}, {"address1", "Address line 1"}, {"store_name_abbrv", "Abbrev"}, {"region", "Region"}, {"zone", "Zone"}, {"address2", "Address line 2"}, {"state_province_name", "State/Province name"}, {"business_type", "Business type"}, {"city", "City"}, {"division", "Division"}, {"state_province", "State/Province"}, {"county", "County"}, {"business_unit", "Business unit"}, {"country", "Country"}, {"country_name", "Country name"}, {"postal_code", "Postal code"}, {"phone", "Phone"}, {"email", "Email"}, {"opening_date", "Opening date"}, {"active", "Active"}, {"latitude", "Latitude"}, {"longitude", "Longitude"}, {"volume_group", "Volume group"}, {"store_mgr", "Store manager"}, {"bearea_mgr", "Bearea manager"}, {"bearitory_mgr", "Bearritory manager"}, {"region_mgr", "Region manager"}, {"store_type", "Store type"}, {"closing_date", "Closing date"}, {"comp_date", "Comp date"}, {"store_group_id", "Store group Id"}, {"address3", "Address line 3"}, {"address4", "Address line 4"}, {"square_feet", "Square feet"}, {"num_of_pos", "POS count"}, {"num_of_kiosks", "Kiosk count"}, {"postal_plus4", "Postal +4"}, {"Legal_Description", "Legal description"}, {"comp_week_id", "Comp week Id"}, {"bearea_id", "Bearea Id"}, {"bearitory_id", "Bearittory Id"}, {"region_id", "Region Id"}, {"division_code", "Division code"}, {"language", "Language"}, {"demographics_bg_key", "Demographics key"}, {"fax", "Fax"}}),
    #"Filtered Rows | ETL_LOG_ID <> -1" = Table.SelectRows(#"Renamed Columns", each ([ETL_LOG_ID] <> -1)),
    #"Filtered Rows | Store Key > 0" = Table.SelectRows(#"Filtered Rows | ETL_LOG_ID <> -1", each [store_key] >= 0),
    #"Filtered Rows | Email IS NOT NULL" = Table.SelectRows(#"Filtered Rows | Store Key > 0", each ([Email] <> null)),
    #"Removed Columns | System Fields" = Table.RemoveColumns(#"Filtered Rows | Email IS NOT NULL",{"INS_DT", "UPDT_DT", "ETL_LOG_ID", "ETL_EVNT_ID"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | System Fields",{"Zone", "Business type", "County", "Business unit", "Fax", "Address line 3", "Address line 4", "Kiosk count", "Postal +4", "Bearea Id", "Bearittory Id", "Region Id", "Division code", "Language"}),
    #"Sorted Rows | Location Number ASC" = Table.Sort(#"Removed Columns | Empty Columns",{{"Location Number", Order.Ascending}}),
    #"Added Custom | Location Number (Standard)" = Table.AddColumn(#"Sorted Rows | Location Number ASC", "Location Number (Standard)", each Text.PadStart(Text.PadStart(Number.ToText([Location Number]),3,"0"),4,"1")),
    #"Added Custom | Location Line" = Table.AddColumn(#"Added Custom | Location Number (Standard)", "Location Line", each [#"Location Number (Standard)"] & " | " & [Location Name]),
    #"Added Conditional Column | Legal Entity (D365)" = Table.AddColumn(#"Added Custom | Location Line", "Legal Entity (D365)", each if [Country] = "US" then 1100 else if [Country] = "CA" then 1700 else if [Country] = "IE" then 2110 else if [Country] = "UK" then 2110 else null),
    #"Cleaned Text" = Table.TransformColumns(#"Added Conditional Column | Legal Entity (D365)",{{"Location Name", Text.Clean, type text}, {"Abbrev", Text.Clean, type text}, {"District", Text.Clean, type text}, {"Address line 1", Text.Clean, type text}, {"Bearea", Text.Clean, type text}, {"Region", Text.Clean, type text}, {"Address line 2", Text.Clean, type text}, {"State/Province name", Text.Clean, type text}, {"City", Text.Clean, type text}, {"Division", Text.Clean, type text}, {"State/Province", Text.Clean, type text}, {"Country", Text.Clean, type text}, {"Country name", Text.Clean, type text}, {"Postal code", Text.Clean, type text}, {"Phone", Text.Clean, type text}, {"Email", Text.Clean, type text}, {"Store manager", Text.Clean, type text}, {"Bearea manager", Text.Clean, type text}, {"Bearritory manager", Text.Clean, type text}, {"Region manager", Text.Clean, type text}, {"Store type", Text.Clean, type text}, {"Abbreviation", Text.Clean, type text}, {"Legal description", Text.Clean, type text}}),
    #"Trimmed Text" = Table.TransformColumns(#"Cleaned Text",{{"Location Name", Text.Trim, type text}, {"Abbrev", Text.Trim, type text}, {"District", Text.Trim, type text}, {"Address line 1", Text.Trim, type text}, {"Bearea", Text.Trim, type text}, {"Region", Text.Trim, type text}, {"Address line 2", Text.Trim, type text}, {"State/Province name", Text.Trim, type text}, {"City", Text.Trim, type text}, {"Division", Text.Trim, type text}, {"State/Province", Text.Trim, type text}, {"Country", Text.Trim, type text}, {"Country name", Text.Trim, type text}, {"Postal code", Text.Trim, type text}, {"Phone", Text.Trim, type text}, {"Email", Text.Trim, type text}, {"Store manager", Text.Trim, type text}, {"Bearea manager", Text.Trim, type text}, {"Bearritory manager", Text.Trim, type text}, {"Region manager", Text.Trim, type text}, {"Store type", Text.Trim, type text}, {"Abbreviation", Text.Trim, type text}, {"Legal description", Text.Trim, type text}}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Trimmed Text",{{"State/Province name", Text.Proper, type text}}),
    #"Added Custom | City State" = Table.AddColumn(#"Capitalized Each Word", "City, State", each [City] & ", " & [#"State/Province name"]),
    #"Replaced Value | ? with NULL" = Table.ReplaceValue(#"Added Custom | City State","?","",Replacer.ReplaceText,{"State/Province name"}),
    #"Replaced Value | """" with NULL" = Table.ReplaceValue(#"Replaced Value | ? with NULL","",null,Replacer.ReplaceValue,{"Address line 2", "Legal description", "Demographics key","State/Province name"}),
    #"Replaced Value | ( with NULL" = Table.ReplaceValue(#"Replaced Value | """" with NULL","(","",Replacer.ReplaceText,{"Phone"}),
    #"Replaced Value | ) with NULL" = Table.ReplaceValue(#"Replaced Value | ( with NULL",")","",Replacer.ReplaceText,{"Phone"}),
    #"Replaced Value | - with NULL" = Table.ReplaceValue(#"Replaced Value | ) with NULL","-","",Replacer.ReplaceText,{"Phone"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Value | - with NULL",{{"Legal Entity (D365)", type text}, {"Active", type logical}, {"Location Number (Standard)", type text}, {"Location Line", type text}, {"City, State", type text}})
in
    #"Changed Type"
```

### WeeksOfSalesHistoryParameter

```sql
GENERATESERIES(0, 9999, 1)
```

### MinimumMultiplierParameter

```sql
GENERATESERIES(0, 9999, 1)
```

### MaximumMultiplierParameter

```sql
GENERATESERIES(0, 9999, 1)
```

### On-Hand Inventory | DC Warehouses AvailPhy For Allocations

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="WITH replenSuggested AS 
(
SELECT
     suntafretailreplenstoredistinctproductcalclog.[parmid]                             AS [parmid]
    , suntafretailreplenstoredcsettings.inventlocationid        AS DC   
    , suntafretailreplenstoredistinctproductcalclog.[distinctproduct]                    AS [distinctproduct]
    , SUM(suntafretailreplenstoredistinctproductcalclog.[suggestedreplenishment])             AS [suggestedreplenishment]
	, SUM(suntafretailreplenstoredistinctproductcalclog.[actualreplenishment])             AS [actualreplenishment]
	, SUM(suntafretailreplenstoredistinctproductcalclog.[firmedreplenishment])             AS [firmedreplenishment]
    , ecoresproduct.[displayproductnumber]                AS [displayproductnumber]
FROM
    [suntafretailreplenstoredistinctproductcalclog]
LEFT JOIN
    [ecoresproduct]
    ON suntafretailreplenstoredistinctproductcalclog.[distinctproduct] = ecoresproduct.[recid]
LEFT JOIN
    [inventlocation]
    ON suntafretailreplenstoredistinctproductcalclog.[storenumber] = inventlocation.[inventlocationid]
LEFT JOIN
        suntafretailreplenstoredcsettings
ON
        [suntafretailreplenstoredistinctproductcalclog].storenumber = suntafretailreplenstoredcsettings.storenumber
WHERE
    suntafretailreplenstoredistinctproductcalclog.[modifieddatetime] >= '2025-06-01 00:00:00'
    AND (suntafretailreplenstoredistinctproductcalclog.[IsDelete] IS NULL OR suntafretailreplenstoredistinctproductcalclog.[IsDelete] = 0)
    AND (ecoresproduct.[IsDelete] IS NULL OR ecoresproduct.[IsDelete] = 0)
	AND (suntafretailreplenstoredcsettings.[IsDelete] IS NULL OR suntafretailreplenstoredcsettings.[IsDelete] = 0)
GROUP BY suntafretailreplenstoredistinctproductcalclog.[parmid]  
,suntafretailreplenstoredcsettings.inventlocationid
,  suntafretailreplenstoredistinctproductcalclog.[distinctproduct]
,ecoresproduct.[displayproductnumber]
)
, relpenAdj AS (
SELECT
	babsuntafretailreplendcstoredistinctproductcalclog.[parmid] AS [parmid]
	, babsuntafretailreplendcstoredistinctproductcalclog.[inventlocationid]              AS [DC]
	, babsuntafretailreplendcstoredistinctproductcalclog.[distinctproduct] AS [distinctproduct]
    , SUM(babsuntafretailreplendcstoredistinctproductcalclog.[suggestedreplenishment])        AS [adjsuggestedreplenishment]
FROM
    [babsuntafretailreplendcstoredistinctproductcalclog] AS [babsuntafretailreplendcstoredistinctproductcalclog]
LEFT JOIN
    [ecoresproduct]
    ON babsuntafretailreplendcstoredistinctproductcalclog.[distinctproduct] = ecoresproduct.[recid]

 WHERE (babsuntafretailreplendcstoredistinctproductcalclog.[IsDelete] IS NULL OR babsuntafretailreplendcstoredistinctproductcalclog.[IsDelete] = 0)
 	    AND (ecoresproduct.[IsDelete] IS NULL OR ecoresproduct.[IsDelete] = 0)
GROUP BY 	babsuntafretailreplendcstoredistinctproductcalclog.[parmid] 
	, babsuntafretailreplendcstoredistinctproductcalclog.[distinctproduct]
	, babsuntafretailreplendcstoredistinctproductcalclog.[inventlocationid]
), inventSumDC AS (
	SELECT
        [isum].[dataareaid]                                                       ,
        [isum].[inventsiteid]                                                     ,
        [isum].[inventlocationid]                                                 ,
        [isum].[itemid]                                                           ,
        SUM([isum].[AvailablePhysicalCalculated]) AS [AvailablePhysicalCalculated],
        SUM(
                CASE
                WHEN
                        [isum].[inventstatusid] = 'AVAIL'
                THEN
                        [isum].[AvailablePhysicalCalculated]
                ELSE
                        0
                END) AS [availphysical_AVAIL],
        SUM(
                CASE
                WHEN
                        [isum].[inventstatusid] = 'PendPut'
                THEN
                        [isum].[AvailablePhysicalCalculated]
                ELSE
                        0
                END)          AS [availphysical_PendPut],
        SUM([isum].[onorder]) AS [onorder]
FROM
        [dbo].[InventSumCurrentViewForWHSEnabledItems] AS [isum]
WHERE
        [isum].[inventlocationid] IN ('9980', '9970', '9960', '9942', '9941', '8175')
GROUP BY
        [isum].[dataareaid]       ,
        [isum].[inventsiteid]     ,
        [isum].[inventlocationid] ,
        [isum].[itemid]
)
SELECT 
replenSuggested.parmid
,replenSuggested.DC AS [Distro Center]
,replenSuggested.displayproductnumber AS [Product Number]
,replenSuggested.suggestedreplenishment AS [Suggested Replenishment]
,replenSuggested.actualreplenishment AS [Actual Replenishment] 
,replenSuggested.firmedreplenishment AS [Firmed Replenishment] 
,relpenAdj.adjsuggestedreplenishment AS [Adj. Suggested Replenishment]
,NULL AS [Adj. Suggested Replenishment]
,COALESCE(inventSumDC.[availphysical_AVAIL],0) AS [DC Available Physical]
,COALESCE(inventSumDC.[availphysical_PendPut],0) AS [DC PendPut Available Physical]
,COALESCE(inventSumDC.[onorder],0) AS [DC On Order]
,COALESCE(replenSuggested.firmedreplenishment,0) + COALESCE(inventSumDC.[availphysical_AVAIL],0) + COALESCE(inventSumDC.[availphysical_PendPut],0)-COALESCE(inventSumDC.[onorder],0) AS [DC Effective Inventory]
,CASE WHEN COALESCE(replenSuggested.firmedreplenishment,0) + COALESCE(inventSumDC.[availphysical_AVAIL],0) + COALESCE(inventSumDC.[availphysical_PendPut],0)-COALESCE(inventSumDC.[onorder],0) = 0 THEN 0 ELSE COALESCE(replenSuggested.firmedreplenishment / (COALESCE(replenSuggested.firmedreplenishment,0) + COALESCE(inventSumDC.[availphysical_AVAIL],0) + COALESCE(inventSumDC.[availphysical_PendPut],0) - COALESCE(inventSumDC.[onorder],0)),0)
END AS [Effective Inventory Percent]
FROM replenSuggested
LEFT JOIN relpenAdj
ON replenSuggested.parmid = relpenAdj.parmid
AND replenSuggested.distinctproduct = relpenAdj.distinctproduct
AND replenSuggested.DC = relpenAdj.DC
LEFT JOIN inventSumDC
ON  replenSuggested.displayproductnumber = inventSumDC.itemid
AND replenSuggested.DC = inventSumDC.[inventlocationid]
", CommandTimeout=#duration(0, 2, 0, 0)]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"Effective Inventory Percent", "Replenishing Inventory Percent"}})
in
    #"Renamed Columns"
```

### Invoice Summary

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="SELECT 
    [style_code] AS [Item number],
    locationmapping.[inventlocationid] AS [Store number],
    locationmapping.[name] AS [Store Name],
    CONCAT(locationmapping.[inventlocationid], '-', [style_code]) AS [StoreItemKey],
    DD.[actual_date] AS [Invoice date],
    [merch_year_wk],
    [sales_total_units] AS [Quantity],
    [sales_total_retail] AS [AmountInUSD],
    RIGHT([merch_year_wk], 2) AS [fiscal_week],
    [jurisdiction_code]
FROM [dbo].[WeeklySalesView] AS WSV
LEFT JOIN LH_D365.dbo.d365LocationMapping_View AS locationmapping
    ON locationmapping.[LocationKey] = WSV.[LocationKey]
LEFT JOIN [LH_Mart].[dbo].[date_dim] AS DD
    ON WSV.[date_key] = DD.[date_key]
WHERE WSV.[date_key] >= (
    SELECT MIN([date_key])
    FROM [LH_Mart].[dbo].[date_dim]
    WHERE fiscal_year = 2024
)", CommandTimeout=#duration(0, 2, 0, 0)]),
    #"Inserted Date/Time" = Table.AddColumn(#"Source", "Invoice Datetime", each DateTime.From([Invoice date]), type datetime),
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(#"Inserted Date/Time", each [Invoice Datetime] >= RangeStart and [Invoice Datetime] < RangeEnd)
in
    #"Filtered Rows | Incremental Refresh"
```

### MinMaxBase

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="WITH Dates AS 
(
SELECT actual_date,
DATEDIFF(WEEK, actual_date, GETDATE()) AS [WeeksAgo]
FROM [LH_Mart].dbo.date_dim
WHERE actual_date BETWEEN CAST(DATEADD(WEEK, DATEDIFF(WEEK, 0, DATEADD(WEEK, -52, GETDATE())), 0) AS DATE) AND GETDATE()
)
SELECT 
    CONCAT(idim.inventlocationid, '-', cit.itemid)  AS [StoreItemKey],
    cit.dataareaid                                  AS [Company],
	idim.inventlocationid AS [Store],
	cit.itemid AS [Product],
	 Dates.[actual_date],
	 Dates.[WeeksAgo],
    COALESCE(cit.qty,0)                                  AS [TotalQuantity]
FROM Dates
LEFT JOIN [custinvoicetrans] AS cit
ON cit.invoicedate = Dates.actual_date
    LEFT JOIN [inventdim] AS idim 
        ON cit.inventdimid = idim.inventdimid
        AND cit.dataareaid  = idim.dataareaid
    LEFT JOIN [inventlocation] AS il 
        ON idim.inventlocationid = il.inventlocationid
        AND idim.dataareaid      = il.dataareaid
WHERE 
    cit.invoicedate >= CAST(DATEADD(WEEK, DATEDIFF(WEEK, 0, DATEADD(WEEK, -52, GETDATE())), 0) AS DATE)
    AND il.name NOT LIKE '%DO NOT USE%'
    AND il.name NOT LIKE '%OLD%'
    AND (cit.IsDelete IS NULL OR cit.IsDelete = 0)
    AND (idim.IsDelete IS NULL OR idim.IsDelete = 0)
    AND (il.IsDelete IS NULL OR il.IsDelete = 0)
", CommandTimeout=#duration(0, 2, 0, 0)])
in
    Source
```

### Replen Settings

```sql
let
    Source = Sql.Database(ServerName, "LH_D365", [Query="SELECT
CONCAT(suntafretailreplenactivesettings.storenumber, '-', ecoresproduct.displayproductnumber)  AS [StoreItemKey],
        ecoresproduct.displayproductnumber                       AS [Item]                   ,
        erptranslation.name                                      AS [Product Name]           ,
        products.[ScorecardCategory]                             AS [Product Category]       ,
        suntafretailreplenactivesettings.storenumber             AS [Location/Store]         ,
        inventlocation.name                                      AS [Location Name]          ,
        suntafretailreplenactivesettings.babstoreproducteligible AS [Store Location Eligible],
        suntafretailreplenactivesettings.minimumsupply           AS [Current Min]            ,
        suntafretailreplenactivesettings.maximumsupply           AS [Current Max]            ,
        suntafretailreplenactivesettings.targetweekssupply       AS [Target Weeks of Supply]
FROM
        suntafretailreplenactivesettings AS suntafretailreplenactivesettings
INNER JOIN
        ecoresproduct AS ecoresproduct
ON
        suntafretailreplenactivesettings.distinctproduct = ecoresproduct.recid
LEFT JOIN
        [ecoresproducttranslation] AS erptranslation
ON
        ecoresproduct.[recid] = erptranslation.[product]
LEFT JOIN
        (
                SELECT DISTINCT
                        [style_code],
                        [ScorecardCategory]
                FROM
                        [LH_Mart].[dbo].[product_dim] ) AS products
ON
        products.[style_code] = ecoresproduct.displayproductnumber
LEFT JOIN
        [inventlocation] AS inventlocation
ON
        inventlocation.inventlocationid = suntafretailreplenactivesettings.storenumber
WHERE
        suntafretailreplenactivesettings.IsDelete IS NULL
AND     ecoresproduct.IsDelete IS NULL
AND     erptranslation.IsDelete IS NULL
AND     [inventlocation].IsDelete IS NULL
", CommandTimeout=#duration(0, 2, 0, 0)])
in
    Source
```

## Shared Expressions

### RangeStart (0)

```sql
#datetime(2024, 2, 4, 0, 0, 0) meta [IsParameterQuery=true, Type="DateTime", IsParameterQueryRequired=true]
```

### RangeEnd (0)

```sql
#datetime(2099, 12, 31, 0, 0, 0) meta [IsParameterQuery=true, Type="DateTime", IsParameterQueryRequired=true]
```

### ServerName (0)

```sql
"4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com" meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]
```

## Data Source Cross-References

_No recognized SQL data source references detected._
