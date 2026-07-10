# dbo.vwValueLink_StoreDim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwValueLink_StoreDim"]
    store_dim(["store_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| store_dim |

## View Code

```sql
create view dbo.vwValueLink_StoreDim
as
select store_key,store_id,store_name from store_dim
union
select -50,-50,'Unspecified/Not Applicable'
```

