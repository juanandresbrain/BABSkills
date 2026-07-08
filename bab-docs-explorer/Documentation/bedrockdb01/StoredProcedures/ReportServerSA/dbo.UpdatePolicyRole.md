# dbo.UpdatePolicyRole

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdatePolicyRole"]
    PolicyUserRole(["PolicyUserRole"]) --> SP
    Roles(["Roles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| PolicyUserRole |
| Roles |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[UpdatePolicyRole]
@PolicyID uniqueidentifier,
@PrincipalID uniqueidentifier,
@RoleName nvarchar(260),
@RoleID uniqueidentifier OUTPUT
AS 
SELECT @RoleID = (SELECT RoleID FROM Roles WHERE RoleName = @RoleName)
INSERT INTO PolicyUserRole 
(ID, RoleID, UserID, PolicyID)
VALUES (newid(), @RoleID, @PrincipalID, @PolicyID)
```

