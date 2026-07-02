# dbo.FindItemsByDataSource

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FindItemsByDataSource"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_DataSource(["dbo.DataSource"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.DataSource |
| dbo.SecData |
| dbo.Users |

## Stored Procedure Code

```sql

```

