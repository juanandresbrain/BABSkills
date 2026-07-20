# TestPBIGateway

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** 4c149c31-89dc-4ff9-9bd9-8e536186b383  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Query1 | 29 | 0 |  |
| DateTableTemplate_e5d8a3b6-408f-4644-abfe-1953aa525c6f | 8 | 0 | Yes |
| LocalDateTable_3dd29412-82bc-4a69-a86d-fd604daa37d7 | 8 | 0 | Yes |
| LocalDateTable_08e75f5b-b78e-4ea2-b2a7-84d0a9fbb940 | 8 | 0 | Yes |

## Measures

_No measures detected._

## Power Query Source (per table)

### Query1

```sql
let
    Source = Sql.Database("papamart.buildabear.com", "DW", [Query="select * from sys.tables"])
in
    Source
```

### DateTableTemplate_e5d8a3b6-408f-4644-abfe-1953aa525c6f

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### LocalDateTable_3dd29412-82bc-4a69-a86d-fd604daa37d7

```sql
Calendar(Date(Year(MIN('Query1'[create_date])), 1, 1), Date(Year(MAX('Query1'[create_date])), 12, 31))
```

### LocalDateTable_08e75f5b-b78e-4ea2-b2a7-84d0a9fbb940

```sql
Calendar(Date(Year(MIN('Query1'[modify_date])), 1, 1), Date(Year(MAX('Query1'[modify_date])), 12, 31))
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| papamart.buildabear.com | DW | [papamart/dw](../../../papamart/DataDictionary/dw/) |
