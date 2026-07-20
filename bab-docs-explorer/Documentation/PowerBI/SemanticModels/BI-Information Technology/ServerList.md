# ServerList

**Workspace:** BI-Information Technology  
**Dataset ID:** d371f549-4e29-445b-b10f-30d092acb2d9  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| AllActiveServerDetails | 26 | 0 |  |
| Servers | 19 | 0 |  |
| Patching | 9 | 0 |  |
| AllActiveServers | 19 | 0 |  |

## Measures

_No measures detected._

## Power Query Source (per table)

### AllActiveServerDetails

```sql
let
    Source = Sql.Database("sql-coredb-prod-eus-01.database.windows.net", "sqldb-coredb-prod-eus-01"),
    dbo_AllActiveServerDetails = Source{[Schema="dbo",Item="AllActiveServerDetails"]}[Data]
in
    dbo_AllActiveServerDetails
```

### Servers

```sql
let
    Source = Sql.Database("sql-coredb-prod-eus-01.database.windows.net", "sqldb-coredb-prod-eus-01"),
    dbo_Servers = Source{[Schema="dbo",Item="Servers"]}[Data]
in
    dbo_Servers
```

### Patching

```sql
let
    Source = Sql.Database("sql-coredb-prod-eus-01.database.windows.net", "sqldb-coredb-prod-eus-01"),
    dbo_Patching = Source{[Schema="dbo",Item="Patching"]}[Data]
in
    dbo_Patching
```

### AllActiveServers

```sql
let
    Source = Sql.Database("sql-coredb-prod-eus-01.database.windows.net", "sqldb-coredb-prod-eus-01"),
    dbo_AllActiveServers = Source{[Schema="dbo",Item="AllActiveServers"]}[Data]
in
    dbo_AllActiveServers
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| sql-coredb-prod-eus-01.database.windows.net | sqldb-coredb-prod-eus-01 | _(not found in SQL documentation)_ |
