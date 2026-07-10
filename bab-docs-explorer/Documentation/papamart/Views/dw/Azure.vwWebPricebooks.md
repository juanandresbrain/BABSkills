# Azure.vwWebPricebooks

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwWebPricebooks"]
    Azure_WebPricebooks(["Azure.WebPricebooks"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.WebPricebooks |

## View Code

```sql
create view Azure.vwWebPricebooks
as

select *
from Azure.WebPricebooks
```

