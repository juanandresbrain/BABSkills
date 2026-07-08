# dbo.DeleteRole

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteRole"]
    Roles(["Roles"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Roles |

## Stored Procedure Code

```sql
-- Delete all policies associated with this role
CREATE PROCEDURE [dbo].[DeleteRole]
@RoleName nvarchar(260)
AS
SET NOCOUNT OFF
-- if you call this, you must delete/reconstruct all policies associated with this role
DELETE FROM Roles WHERE RoleName = @RoleName
```

