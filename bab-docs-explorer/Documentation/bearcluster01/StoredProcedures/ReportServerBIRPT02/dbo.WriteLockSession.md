# dbo.WriteLockSession

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.WriteLockSession"]
    dbo_SessionLock(["dbo.SessionLock"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SessionLock |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[WriteLockSession]
@SessionID as varchar(32),
@Persisted bit,
@CheckLockVersion bit = 0,
@LockVersion int
AS
SET NOCOUNT OFF ;
IF @Persisted = 1
BEGIN
    IF @CheckLockVersion = 0
    BEGIN
        UPDATE [ReportServerBIRPT02TempDB].dbo.SessionLock WITH (ROWLOCK)
        SET SessionID = SessionID
        WHERE SessionID = @SessionID;
    END
    ELSE
    BEGIN
        DECLARE @ActualLockVersion as int

        UPDATE [ReportServerBIRPT02TempDB].dbo.SessionLock WITH (ROWLOCK)
        SET SessionID = SessionID,
        LockVersion = LockVersion + 1
        WHERE SessionID = @SessionID
        AND LockVersion = @LockVersion ;

        IF (@@ROWCOUNT = 0)
        BEGIN
            SELECT @ActualLockVersion = LockVersion
            FROM [ReportServerBIRPT02TempDB].dbo.SessionLock WITH (ROWLOCK)
            WHERE SessionID = @SessionID;

            IF (@ActualLockVersion <> @LockVersion)
                RAISERROR ('Invalid version locked', 16,1)
            END
        END
    END
ELSE
BEGIN
    INSERT INTO [ReportServerBIRPT02TempDB].dbo.SessionLock WITH (ROWLOCK) (SessionID) VALUES (@SessionID)
END
```

