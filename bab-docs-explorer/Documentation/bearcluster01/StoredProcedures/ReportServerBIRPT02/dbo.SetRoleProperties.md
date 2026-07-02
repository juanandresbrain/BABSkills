# dbo.SetRoleProperties

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetRoleProperties"]
    dbo_Roles(["dbo.Roles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Roles |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetRoleProperties]
@RoleName as nvarchar(260),
@Description as nvarchar(512) = NULL,
@TaskMask as nvarchar(32),
@RoleFlags as tinyint
AS
SET NOCOUNT OFF
DECLARE @ExistingRoleFlags as tinyint
SET @ExistingRoleFlags = (SELECT RoleFlags FROM Roles WHERE RoleName = @RoleName)
IF @ExistingRoleFlags IS NULL
BEGIN
    RETURN
END
IF @ExistingRoleFlags <> @RoleFlags
BEGIN
    RAISERROR ('Bad role flags', 16, 1)
END
UPDATE Roles SET
Description = @Description,
TaskMask = @TaskMask,
RoleFlags = @RoleFlags
WHERE RoleName = @RoleName
```

