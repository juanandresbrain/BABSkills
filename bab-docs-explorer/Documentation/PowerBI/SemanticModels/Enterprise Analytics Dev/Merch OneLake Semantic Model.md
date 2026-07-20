# Merch OneLake Semantic Model

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** 926061a6-85b5-424f-9c76-f7b0a59fa269  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| custinvoicejour | 156 | 0 |  |
| custinvoicetrans | 136 | 0 |  |
| inventdim | 55 | 0 |  |
| retailtransactionsalestrans | 171 | 0 |  |
| retailtransactiondiscounttrans | 46 | 0 |  |
| transformedretailsalestransactions | 20 | 0 |  |

## Measures

_No measures detected._

## Power Query Source (per table)

### custinvoicejour

```sql
custinvoicejour
```

### custinvoicetrans

```sql
custinvoicetrans
```

### inventdim

```sql
inventdim
```

### retailtransactionsalestrans

```sql
retailtransactionsalestrans
```

### retailtransactiondiscounttrans

```sql
retailtransactiondiscounttrans
```

### transformedretailsalestransactions

```sql
transformedretailsalestransactions
```

## Shared Expressions

### DirectLake - LH_D365 (0)

```sql
let
    Source = AzureStorage.DataLake("https://onelake.dfs.fabric.microsoft.com/109bd275-5f44-4366-b343-9b41b5cfb040/e5e59183-e46f-438a-b5cf-98ced7672aa4", [HierarchicalNavigation=true])
in
    Source
```

## Data Source Cross-References

_No recognized SQL data source references detected._
