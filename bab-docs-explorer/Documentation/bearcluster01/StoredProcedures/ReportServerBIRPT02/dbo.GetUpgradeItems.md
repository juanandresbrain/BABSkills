# dbo.GetUpgradeItems

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetUpgradeItems"]
    dbo_UpgradeInfo(["dbo.UpgradeInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.UpgradeInfo |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetUpgradeItems]
AS
SELECT
    [Item],
    [Status]
FROM
    [UpgradeInfo]
```

