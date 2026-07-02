# dbo.sp_ssis_listpackages

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_ssis_listpackages"]
    dbo_sysssispackages(["dbo.sysssispackages"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysssispackages |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_ssis_listpackages]
  @folderid uniqueidentifier
AS
  SELECT
      name,
      id,
      description,
      createdate,
      folderid,
      datalength(packagedata),
      vermajor,
      verminor,
      verbuild,
      vercomments,
      verid
  FROM
      sysssispackages
  WHERE
      [folderid] = @folderid
  ORDER BY
      name
```

