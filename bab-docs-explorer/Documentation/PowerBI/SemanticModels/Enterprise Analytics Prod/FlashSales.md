# FlashSales

**Workspace:** Enterprise Analytics Prod  
**Dataset ID:** 91d9ab94-a7c9-44dd-a33c-5199eb4b2a56  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| vwJumpMindSalesSummaryPowerBI | 44 | 0 |  |
| DateTableTemplate_b04f9ba3-85e4-4055-8fbc-4ac826c6ff3c | 8 | 0 | Yes |
| LocalDateTable_3da18d82-d3e8-4cf4-82f0-ea2786103ef8 | 8 | 0 | Yes |

## Measures

_No measures detected._

## Power Query Source (per table)

### vwJumpMindSalesSummaryPowerBI

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_vwJumpMindSalesSummaryPowerBI = Source{[Schema="dbo",Item="vwJumpMindSalesSummaryPowerBI"]}[Data]
in
    dbo_vwJumpMindSalesSummaryPowerBI
```

### DateTableTemplate_b04f9ba3-85e4-4055-8fbc-4ac826c6ff3c

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### LocalDateTable_3da18d82-d3e8-4cf4-82f0-ea2786103ef8

```sql
Calendar(Date(Year(MIN('vwJumpMindSalesSummaryPowerBI'[TransactionDate])), 1, 1), Date(Year(MAX('vwJumpMindSalesSummaryPowerBI'[TransactionDate])), 12, 31))
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com | LH_Source | [4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com/LH_Source](../../../4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Source/) |
