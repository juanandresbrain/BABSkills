# dbo.vwDW_dim_data_status

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_dim_data_status"]
    dbo_data_status_dim(["dbo.data_status_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.data_status_dim |

## View Code

```sql
CREATE VIEW vwDW_dim_data_status
AS

	SELECT
		[data_status_key]
		,[data_status_desc]
	FROM [dw].[dbo].[data_status_dim]
```

