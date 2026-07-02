# dbo.GetContentCacheDetails

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetContentCacheDetails"]
    dbo_ContentCache(["dbo.ContentCache"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ContentCache |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetContentCacheDetails]
    @CatalogItemID uniqueidentifier,
    @ParamsHash int,
    @ContentType nvarchar(256)
AS
BEGIN
    DECLARE @now as DateTime
    SET @now = GETDATE()

    SELECT ContentCacheID, CatalogItemID, CreatedDate, ParamsHash, EffectiveParams, ExpirationDate, Version, ContentType
    FROM [ReportServerBIRPT02TempDB].dbo.ContentCache WITH (NOLOCK)
    WHERE
        CatalogItemID = @CatalogItemID
        AND ParamsHash = @ParamsHash
        AND ContentType = @ContentType
        AND ExpirationDate > @now
END
```

