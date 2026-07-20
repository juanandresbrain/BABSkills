# Model_SSRS

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** f7c84824-7a8a-4910-b4a7-8d75c82ceefb  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| RnkBy | 2 | 0 |  |
| RnkLimit | 2 | 0 |  |
| DIM_Geography | 12 | 0 |  |
| ukgiftcard_storesummary_updated | 22 | 1 |  |
| DateDim | 5 | 0 |  |
| FactActivity | 12 | 7 |  |
| wbhoursbyposition_timecode_bydate | 11 | 0 |  |

## Measures

### ukgiftcard_storesummary_updated.Cards Redeemed1

```sql
COUNTROWS(ukgiftcard_storesummary_updated)
```

### FactActivity.Row_number_by_transactionid

```sql

VAR SalesTable = 
    SUMMARIZE(
        ALLSELECTED(FactActivity),
        FactActivity[store_key],
        FactActivity[Lylty_No],
		FactActivity[party_y_n],
        // DIM_Geography[bearritory],
        // DIM_Geography[region],
        "@Amt", SUM(FactActivity[unit_gross_amount]),
		"@Tran", SUM(FactActivity[TransactionID])
    )
    // VAR SOURCETABLE = 
    // ADDCOLUMNS(
    //     ALL(FactActivity),
    //     "@Amt", [M_unit_gross_amt],
    //     "@Tran", [M_Transactions]
    // )
RETURN 
    ROWNUMBER(
        SalesTable,
        ORDERBY(
            [@Tran], DESC,
            [@Amt], DESC,
            [store_key], ASC,    -- Corrected ORDERBY for store_key
            [Lylty_No], ASC,      -- Corrected ORDERBY for Lylty_No
            [party_y_n],ASC
            // [bearritory],ASC,
            // [region],ASC
        ),
        PARTITIONBY()  -- You can fill this if you want partitioning; leave it empty if not needed
    )
// RANK(DENSE,SOURCETABLE,ORDERBY([@Amt],DESC,[@Tran],DESC))

```

### FactActivity.M_unit_gross_amt

```sql
SUM(FactActivity[unit_gross_amount])
```

### FactActivity.M_Transactions

```sql
SUM(FactActivity[TransactionID])
```

### FactActivity.SelectedRankLimit

```sql

VAR SelectedLimit = SELECTEDVALUE('RnkLimit'[Top_Count])
RETURN
IF (
    ISBLANK(SelectedLimit),
    MAX('RnkLimit'[Top_Count]), -- Default to the highest limit if nothing is selected
    SelectedLimit
)

```

### FactActivity.Row_number_by_Amt

```sql

VAR SalesTable = 
    SUMMARIZE(
        ALLSELECTED(FactActivity),
        FactActivity[store_key],
        FactActivity[Lylty_No],
		FactActivity[party_y_n],
        "@Amt", SUM(FactActivity[unit_gross_amount]),
		"@Tran", SUM(FactActivity[TransactionID])
    )
    // VAR SOURCETABLE = 
    // ADDCOLUMNS(
    //     ALL(FactActivity),
    //     "@Amt", [M_unit_gross_amt],
    //     "@Tran", [M_Transactions]
    // )
RETURN 
    ROWNUMBER(
        SalesTable,
        ORDERBY(
            [@Amt], DESC,
			[@Tran], DESC,
            [store_key], ASC,    -- Corrected ORDERBY for store_key
            [Lylty_No], ASC,      -- Corrected ORDERBY for Lylty_No
            [party_y_n],ASC
           // ,[Bearitory],ASC,
            // [Region],ASC
        ),
        PARTITIONBY()  -- You can fill this if you want partitioning; leave it empty if not needed
    )
// RANK(DENSE,SOURCETABLE,ORDERBY([@Amt],DESC,[@Tran],DESC))

```

### FactActivity.DynamicSelectedRank

```sql

VAR RankLimit = [SelectedRankLimit]
RETURN
IF (
    [Selections Based T/G] <= RankLimit,
    [Selections Based T/G],
    BLANK()
)

```

### FactActivity.SFSRank

```sql

VAR RankOrder = SELECTEDVALUE(RnkBy[Order_By])
VAR count_filter = SELECTEDVALUE(RnkLimit[Top_Count])

-- Create dynamic row number logic based on RnkBy selection
VAR RowNumber = 
    SWITCH(
        RankOrder,
        "#Transactions", [Row_number_by_transactionid],   -- Use TransactionRank measure when Order_By is #Transaction
        "Gross Amt", [Row_number_by_Amt],               -- Use Grossrnk measure when Order_By is Gross Amt
        BLANK()                      -- Default to TransactionRank if neither is selected
    )

-- Apply the filter logic where row number is <= TopCount
RETURN
    IF(
        RowNumber <= count_filter,  -- Only return rows with row number <= selected Top_Count
        RowNumber,
        BLANK()   -- Return blank for rows that do not meet the filter condition
    )

```

## Power Query Source (per table)

### RnkBy

```sql
order
```

### RnkLimit

```sql
count
```

### DIM_Geography

```sql
dsgeography
```

### ukgiftcard_storesummary_updated

```sql
ukgiftcard_storesummary_updated1
```

### DateDim

```sql
sfs_date_dim
```

### FactActivity

```sql
sfs_activity3
```

### wbhoursbyposition_timecode_bydate

```sql
wbhoursbyposition_timecode_bydate
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
