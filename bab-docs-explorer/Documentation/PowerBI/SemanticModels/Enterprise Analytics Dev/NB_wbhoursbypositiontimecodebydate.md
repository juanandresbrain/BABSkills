# NB_wbhoursbypositiontimecodebydate

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** dd199c6e-1a90-4818-b793-1c6f7cfeaf1d  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| wbhoursbyposition_timecode_bydate | 10 | 1 |  |

## Measures

### wbhoursbyposition_timecode_bydate.Pay

```sql
SUMX(
    WBHoursByPosition_TimeCode_byDate,
    WBHoursByPosition_TimeCode_byDate[RATE] * WBHoursByPosition_TimeCode_byDate[HOURS]
)

```

## Power Query Source (per table)

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
