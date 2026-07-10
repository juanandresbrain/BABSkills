# dbo.vwStore_dimUK

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwStore_dimUK"]
    Store_Dim(["Store_Dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Store_Dim |

## View Code

```sql
CREATE VIEW [dbo].[vwStore_dimUK]
AS
SELECT store_key, state_province_name, demographics_bg_key
	From Store_Dim
WHERE country = 'UK'
```

