# Active Employee Check for Jumpmind Stores

**Workspace:** BI-Accounting  
**Dataset ID:** e610d1e9-0844-4dea-b792-7667a2d34a9c  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Details | 9 | 3 |  |
| DateTableTemplate_165a22fd-0b20-49ee-b327-aedebbc8177a | 8 | 0 | Yes |
| StoreList | 2 | 0 |  |

## Measures

### Details.UserStatus

```sql

IF(
    MAX('Details'[user_active_flag]) = 1,
    "Active",
    "Inactive"
)
```

### Details.CombinedWorkgroup

```sql

CONCATENATEX(
    'Details',
    'Details'[workgroup_id] & " = " & 'Details'[workgroup_id2],
    ", "
)

```

### Details.FilteredUsername

```sql

IF(
    MAX('Details'[username]) <> MAX('Details'[alternate_id]),
    MAX('Details'[username]),
    BLANK()
)


```

## Power Query Source (per table)

### Details

```sql
let
    Source = Sql.Database("azsynapsewkstt3osb-ondemand.sql.azuresynapse.net", "silverdeltalake", [Query="select business_unit_id, #(lf)a.username, #(lf)first_name, #(lf)last_name, #(lf)alternate_id, #(lf)u.workgroup_id, #(lf)a.workgroup_id, #(lf)user_active_flag #(lf)from jumpmind_bab_active_user a #(lf)join jumpmind_usr_user_workgroup u#(lf)on a.username = u.username#(lf)WHERE 1=1 AND user_active_flag = 1 OR(user_active_flag = 0 AND last_login > DATEADD(Month,-6,getdate()))#(lf)order by a.business_unit_id asc, a.username"])
in
    Source
```

### DateTableTemplate_165a22fd-0b20-49ee-b327-aedebbc8177a

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### StoreList

```sql
let
    Source = Details,
    #"Removed Other Columns" = Table.SelectColumns(Source,{"business_unit_id"}),
    #"Removed Duplicates" = Table.Distinct(#"Removed Other Columns")
in
    #"Removed Duplicates"
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| azsynapsewkstt3osb-ondemand.sql.azuresynapse.net | silverdeltalake | _(not found in SQL documentation)_ |
