# GiftCardsMappedToServiceItem

**Workspace:** BI-Accounting  
**Dataset ID:** ea90321c-029a-4c62-adbb-a84cc7ba3a47  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Azure vwDynamicsGiftCardsMappedToServiceItem | 9 | 0 |  |

## Measures

_No measures detected._

## Power Query Source (per table)

### Azure vwDynamicsGiftCardsMappedToServiceItem

```sql
let
    Source = Sql.Database("papamart", "dw"),
    Azure_vwDynamicsGiftCardsMappedToServiceItem = Source{[Schema="Azure",Item="vwDynamicsGiftCardsMappedToServiceItem"]}[Data],
    #"Changed Type" = Table.TransformColumnTypes(Azure_vwDynamicsGiftCardsMappedToServiceItem,{{"Entity", Int64.Type}, {"InventLocationId", Int64.Type}})
in
    #"Changed Type"
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| papamart | dw | [papamart/dw](../../../papamart/DataDictionary/dw/) |
