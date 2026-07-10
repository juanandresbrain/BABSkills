# Azure.vwPOSOutbound_WebReturnsLocal

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_WebReturnsLocal"]
    dbo_tmpWebSalesForPOSReturns(["dbo.tmpWebSalesForPOSReturns"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmpWebSalesForPOSReturns |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_WebReturnsLocal] AS

select * 
from dbo.tmpWebSalesForPOSReturns
```

