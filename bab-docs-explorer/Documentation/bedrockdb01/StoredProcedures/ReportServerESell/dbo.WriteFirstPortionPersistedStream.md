# dbo.WriteFirstPortionPersistedStream

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.WriteFirstPortionPersistedStream"]
    dbo_PersistedStream(["dbo.PersistedStream"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PersistedStream |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[WriteFirstPortionPersistedStream]
@SessionID varchar(32),
@Index int,
@Name nvarchar(260) = NULL,
@MimeType nvarchar(260) = NULL,
@Extension nvarchar(260) = NULL,
@Encoding nvarchar(260) = NULL,
@Content image
AS

UPDATE [ReportServerESellTempDB].dbo.PersistedStream set Content = @Content, [Name] = @Name, MimeType = @MimeType, Extension = @Extension WHERE SessionID = @SessionID AND [Index] = @Index

SELECT TEXTPTR(Content) FROM [ReportServerESellTempDB].dbo.PersistedStream WHERE SessionID = @SessionID AND [Index] = @Index
```

