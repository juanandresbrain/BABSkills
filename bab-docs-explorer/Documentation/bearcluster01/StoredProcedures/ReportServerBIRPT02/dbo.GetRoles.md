# dbo.GetRoles

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetRoles"]
    dbo_Roles(["dbo.Roles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Roles |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetRoles]
@RoleFlags as tinyint = NULL
AS
SELECT
    RoleName,
    Description,
    TaskMask
FROM
    Roles
WHERE
    (@RoleFlags is NULL) OR
    (RoleFlags = @RoleFlags)
```

