# dbo.GetPolicyRoots

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetPolicyRoots"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetPolicyRoots]
AS
SELECT
    [Path],
    [Type]
FROM
    [Catalog]
WHERE
    [PolicyRoot] = 1
```

