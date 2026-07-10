# dbo.spscRefreshCubeDate

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spscRefreshCubeDate"]
    CubeRefreshInfo(["CubeRefreshInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CubeRefreshInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spscRefreshCubeDate] AS

SET ANSI_WARNINGS ON
SET ANSI_NULLS ON 

update BABDWConfig..CubeRefreshInfo
set refreshdate = getdate()
```

