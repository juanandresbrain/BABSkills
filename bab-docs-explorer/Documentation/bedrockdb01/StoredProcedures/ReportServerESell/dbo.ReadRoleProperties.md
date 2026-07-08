# dbo.ReadRoleProperties

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ReadRoleProperties"]
    Roles(["Roles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Roles |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ReadRoleProperties]
@RoleName as nvarchar(260)
AS 
SELECT Description, TaskMask, RoleFlags FROM Roles WHERE RoleName = @RoleName
```

