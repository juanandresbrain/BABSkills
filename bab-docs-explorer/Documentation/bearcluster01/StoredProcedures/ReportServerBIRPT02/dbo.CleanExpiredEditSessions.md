# dbo.CleanExpiredEditSessions

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanExpiredEditSessions"]
    dbo_ExecutionCache(["dbo.ExecutionCache"]) --> SP
    dbo_SessionData(["dbo.SessionData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
    dbo_TempCatalog(["dbo.TempCatalog"]) --> SP
    dbo_TempDataSets(["dbo.TempDataSets"]) --> SP
    dbo_TempDataSources(["dbo.TempDataSources"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ExecutionCache |
| dbo.SessionData |
| dbo.SnapshotData |
| dbo.TempCatalog |
| dbo.TempDataSets |
| dbo.TempDataSources |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[CleanExpiredEditSessions]
    @MaxToClean int = 10,
    @NumCleaned int OUTPUT
AS BEGIN
    SET DEADLOCK_PRIORITY LOW

    declare @now datetime;
    select @now = GETDATE();

    declare @DeletedItems table (ItemID uniqueidentifier not null primary key, Intermediate uniqueidentifier null)
    declare @DeletedCacheSnapshots table (SnapshotDataID uniqueidentifier null)

    begin transaction
        insert into @DeletedItems
        select top(@MaxToClean) TempCatalogID, Intermediate
        from [ReportServerBIRPT02TempDB].dbo.TempCatalog TC WITH(UPDLOCK)
        where ExpirationTime < @now and not exists (
            select 1
            from [ReportServerBIRPT02TempDB].dbo.SessionData SD WITH (INDEX (IX_EditSessionID))
            where SD.EditSessionID = TC.EditSessionID ) ;

        delete from [ReportServerBIRPT02TempDB].dbo.TempDataSources
        where ItemID in (
            select ItemID from @DeletedItems ) ;

        delete from [ReportServerBIRPT02TempDB].dbo.TempDataSets
        where ItemID in (
            select ItemID from @DeletedItems ) ;

        delete from [ReportServerBIRPT02TempDB].dbo.TempCatalog
        where TempCatalogID in (
            select ItemID from @DeletedItems ) ;

        delete from [ReportServerBIRPT02TempDB].dbo.ExecutionCache
        output deleted.SnapshotDataID into @DeletedCacheSnapshots(SnapshotDataID)
        where ReportID in (
            select ItemID from @DeletedItems );

        update [ReportServerBIRPT02TempDB].dbo.SnapshotData
        set PermanentRefcount = PermanentRefcount - 1
        where SnapshotData.SnapshotDataID in
            (select Intermediate from @DeletedItems
             union
             select SnapshotDataID from @DeletedCacheSnapshots) ;
    commit

    select @NumCleaned = count(1) from @DeletedItems ;
END
```

