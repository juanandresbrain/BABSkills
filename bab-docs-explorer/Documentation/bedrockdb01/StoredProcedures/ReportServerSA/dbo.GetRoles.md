# dbo.GetRoles

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetRoles"]
    Roles(["Roles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Roles |

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

