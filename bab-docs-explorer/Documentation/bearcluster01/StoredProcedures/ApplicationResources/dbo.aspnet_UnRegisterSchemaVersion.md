# dbo.aspnet_UnRegisterSchemaVersion

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.aspnet_UnRegisterSchemaVersion"]
    dbo_aspnet_SchemaVersions(["dbo.aspnet_SchemaVersions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.aspnet_SchemaVersions |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].aspnet_UnRegisterSchemaVersion
    @Feature                   nvarchar(128),
    @CompatibleSchemaVersion   nvarchar(128)
AS
BEGIN
    DELETE FROM dbo.aspnet_SchemaVersions
        WHERE   Feature = LOWER(@Feature) AND @CompatibleSchemaVersion = CompatibleSchemaVersion
END
```

