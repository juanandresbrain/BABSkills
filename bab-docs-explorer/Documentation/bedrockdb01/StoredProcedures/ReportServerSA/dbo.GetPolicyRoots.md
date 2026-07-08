# dbo.GetPolicyRoots

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetPolicyRoots"]
    Catalog(["Catalog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Catalog |

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

