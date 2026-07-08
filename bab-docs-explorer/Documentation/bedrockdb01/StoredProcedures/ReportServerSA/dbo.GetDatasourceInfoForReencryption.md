# dbo.GetDatasourceInfoForReencryption

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDatasourceInfoForReencryption"]
    dbo_DataSource(["dbo.DataSource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DataSource |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetDatasourceInfoForReencryption]
@DSID as uniqueidentifier
AS

SELECT
    [ConnectionString],
    [OriginalConnectionString],
    [UserName],
    [Password],
    [CredentialRetrieval],
    [Version]
FROM [dbo].[DataSource]
WHERE [DSID] = @DSID
```

