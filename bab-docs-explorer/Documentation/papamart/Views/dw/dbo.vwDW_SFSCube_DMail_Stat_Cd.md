# dbo.vwDW_SFSCube_DMail_Stat_Cd

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_DMail_Stat_Cd"]
    dbo_CLNSD_ADDR_DIM(["dbo.CLNSD_ADDR_DIM"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNSD_ADDR_DIM |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_DMail_Stat_Cd]
as

SELECT DISTINCT ISNULL(ADDR.MAIL_STAT_CD,'No Address') AS MAIL_STAT_CD
FROM dw.dbo.CLNSD_ADDR_DIM ADDR WITH (NOLOCK)
```

