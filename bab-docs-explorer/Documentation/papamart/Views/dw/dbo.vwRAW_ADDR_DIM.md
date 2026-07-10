# dbo.vwRAW_ADDR_DIM

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwRAW_ADDR_DIM"]
    dbo_RAW_ADDR_DIM(["dbo.RAW_ADDR_DIM"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RAW_ADDR_DIM |

## View Code

```sql
CREATE view [dbo].[vwRAW_ADDR_DIM] 
AS 
select r.CLNSD_ADDR_ID,r.DRVD_CNTRY_ABBRV
from dbo.RAW_ADDR_DIM r with (nolock)
group by r.CLNSD_ADDR_ID,r.DRVD_CNTRY_ABBRV
```

