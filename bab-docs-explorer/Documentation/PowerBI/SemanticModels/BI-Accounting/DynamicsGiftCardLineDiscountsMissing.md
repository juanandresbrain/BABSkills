# DynamicsGiftCardLineDiscountsMissing

**Workspace:** BI-Accounting  
**Dataset ID:** acf7ca8d-8471-4806-84ee-be32bc475d26  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Azure vwDynamicsGiftCardLineDiscountsMissing | 5 | 0 |  |

## Measures

_No measures detected._

## Power Query Source (per table)

### Azure vwDynamicsGiftCardLineDiscountsMissing

```sql
let
    Source = Sql.Database("papamart", "dw"),
    Azure_vwDynamicsGiftCardLineDiscountsMissing = Source{[Schema="Azure",Item="vwDynamicsGiftCardLineDiscountsMissing"]}[Data],
    #"Changed Type" = Table.TransformColumnTypes(Azure_vwDynamicsGiftCardLineDiscountsMissing,{{"InventLocationId", Int64.Type}, {"Entity", Int64.Type}})
in
    #"Changed Type"
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| papamart | dw | [papamart/dw](../../../papamart/DataDictionary/dw/) |
