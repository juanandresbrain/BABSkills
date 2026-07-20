# SharePoint Sites Data Usage

**Workspace:** BI-Information Technology  
**Dataset ID:** 4cc5d440-37e8-43f3-8d71-c4396ac2440c  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| SharePoint SiteOwners (2) | 10 | 0 |  |
| DateTableTemplate_6ddb454a-d7ed-46f5-a89e-17a24ede935a | 8 | 0 | Yes |
| LocalDateTable_260e9a4c-e8e0-4c95-a681-b6740b7d5d98 | 8 | 0 | Yes |
| LocalDateTable_613b5571-c6b1-40c1-b613-f2b60c9cd5f9 | 8 | 0 | Yes |
| SharePoint Sites (2) | 11 | 0 |  |
| LocalDateTable_f3018e21-3374-4621-9786-e842f03f53a6 | 8 | 0 | Yes |
| LocalDateTable_8dc3dbaa-6caa-4662-b123-bbbe06b701f0 | 8 | 0 | Yes |
| SharePoint SiteSnapshots (2) | 9 | 0 |  |
| LocalDateTable_2b2ea9dc-1e3b-4b4e-b8b9-a09667207c8c | 8 | 0 | Yes |
| LocalDateTable_0308ffc0-070c-4abe-b462-dbfe66d22c09 | 8 | 0 | Yes |

## Measures

_No measures detected._

## Power Query Source (per table)

### SharePoint SiteOwners (2)

```sql
let
  Source = Sql.Database("sql-coredb-prod-eus-01.database.windows.net", "sqldb-coredb-prod-eus-01"),
  #"Navigation 1" = Source{[Schema = "SharePoint", Item = "SiteOwners"]}[Data]
in
  #"Navigation 1"
```

### DateTableTemplate_6ddb454a-d7ed-46f5-a89e-17a24ede935a

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### LocalDateTable_260e9a4c-e8e0-4c95-a681-b6740b7d5d98

```sql
Calendar(Date(Year(MIN('SharePoint SiteOwners (2)'[FirstDiscoveredDate])), 1, 1), Date(Year(MAX('SharePoint SiteOwners (2)'[FirstDiscoveredDate])), 12, 31))
```

### LocalDateTable_613b5571-c6b1-40c1-b613-f2b60c9cd5f9

```sql
Calendar(Date(Year(MIN('SharePoint SiteOwners (2)'[LastSeenDate])), 1, 1), Date(Year(MAX('SharePoint SiteOwners (2)'[LastSeenDate])), 12, 31))
```

### SharePoint Sites (2)

```sql
let
  Source = Sql.Database("sql-coredb-prod-eus-01.database.windows.net", "sqldb-coredb-prod-eus-01"),
  #"Navigation 1" = Source{[Schema = "SharePoint", Item = "Sites"]}[Data]
in
  #"Navigation 1"
```

### LocalDateTable_f3018e21-3374-4621-9786-e842f03f53a6

```sql
Calendar(Date(Year(MIN('SharePoint Sites (2)'[FirstDiscoveredDate])), 1, 1), Date(Year(MAX('SharePoint Sites (2)'[FirstDiscoveredDate])), 12, 31))
```

### LocalDateTable_8dc3dbaa-6caa-4662-b123-bbbe06b701f0

```sql
Calendar(Date(Year(MIN('SharePoint Sites (2)'[LastUpdatedDate])), 1, 1), Date(Year(MAX('SharePoint Sites (2)'[LastUpdatedDate])), 12, 31))
```

### SharePoint SiteSnapshots (2)

```sql
let
  Source = Sql.Database("sql-coredb-prod-eus-01.database.windows.net", "sqldb-coredb-prod-eus-01"),
  #"Navigation 1" = Source{[Schema = "SharePoint", Item = "SiteSnapshots"]}[Data]
in
  #"Navigation 1"
```

### LocalDateTable_2b2ea9dc-1e3b-4b4e-b8b9-a09667207c8c

```sql
Calendar(Date(Year(MIN('SharePoint SiteSnapshots (2)'[SnapshotDate])), 1, 1), Date(Year(MAX('SharePoint SiteSnapshots (2)'[SnapshotDate])), 12, 31))
```

### LocalDateTable_0308ffc0-070c-4abe-b462-dbfe66d22c09

```sql
Calendar(Date(Year(MIN('SharePoint SiteSnapshots (2)'[LastContentModifiedDate])), 1, 1), Date(Year(MAX('SharePoint SiteSnapshots (2)'[LastContentModifiedDate])), 12, 31))
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| sql-coredb-prod-eus-01.database.windows.net | sqldb-coredb-prod-eus-01 | _(not found in SQL documentation)_ |
