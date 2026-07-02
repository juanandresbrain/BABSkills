# dbo.ReadRoleProperties

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ReadRoleProperties"]
    dbo_Roles(["dbo.Roles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Roles |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ReadRoleProperties]
@RoleName as nvarchar(260)
AS
SELECT Description, TaskMask, RoleFlags FROM Roles WHERE RoleName = @RoleName
```

