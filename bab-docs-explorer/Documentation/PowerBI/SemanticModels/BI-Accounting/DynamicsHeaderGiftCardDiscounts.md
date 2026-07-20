# DynamicsHeaderGiftCardDiscounts

**Workspace:** BI-Accounting  
**Dataset ID:** f9e93a87-9a37-4fce-b5c2-be12cc983f58  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Azure vwDynamicsHeaderGiftCardDiscounts | 7 | 0 |  |

## Measures

_No measures detected._

## Power Query Source (per table)

### Azure vwDynamicsHeaderGiftCardDiscounts

```sql
let
    Source = Sql.Database("papamart", "dw"),
    Azure_vwDynamicsHeaderGiftCardDiscounts = Source{[Schema="Azure",Item="vwDynamicsHeaderGiftCardDiscounts"]}[Data],
    #"Changed Type" = Table.TransformColumnTypes(Azure_vwDynamicsHeaderGiftCardDiscounts,{{"InventLocationId", Int64.Type}})
in
    #"Changed Type"
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| papamart | dw | [papamart/dw](../../../papamart/DataDictionary/dw/) |
