# dbo.ListInfoForReencryption

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ListInfoForReencryption"]
    dbo_ConfigurationInfo(["dbo.ConfigurationInfo"]) --> SP
    dbo_DataModelDataSource(["dbo.DataModelDataSource"]) --> SP
    dbo_DataSource(["dbo.DataSource"]) --> SP
    dbo_EncryptedConfigList(["dbo.EncryptedConfigList"]) --> SP
    dbo_Keys(["dbo.Keys"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ConfigurationInfo |
| dbo.DataModelDataSource |
| dbo.DataSource |
| dbo.EncryptedConfigList |
| dbo.Keys |
| dbo.Subscriptions |
| dbo.Users |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[ListInfoForReencryption]
@ConfigNames AS [dbo].[EncryptedConfigList] READONLY
AS

SELECT [DSID]
FROM [dbo].[DataSource] WITH (XLOCK, TABLOCK)

SELECT [SubscriptionID]
FROM [dbo].[Subscriptions] WITH (XLOCK, TABLOCK)

SELECT [InstallationID], [PublicKey]
FROM [dbo].[Keys] WITH (XLOCK, TABLOCK)
WHERE [Client] = 1 AND ([SymmetricKey] IS NOT NULL)

SELECT [Name],[Value]
FROM [dbo].[ConfigurationInfo]
WHERE [Name] IN (SELECT [ConfigName] FROM @ConfigNames)

SELECT [UserID]
FROM [dbo].[Users]
WHERE ([ServiceToken] IS NOT NULL)

SELECT [DSID]
FROM [dbo].[DataModelDataSource]
```

