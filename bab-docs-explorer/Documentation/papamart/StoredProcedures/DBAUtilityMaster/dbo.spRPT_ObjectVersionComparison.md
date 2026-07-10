# dbo.spRPT_ObjectVersionComparison

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_ObjectVersionComparison"]
    dbo_tblDBA_ObjectVersionRepository(["dbo.tblDBA_ObjectVersionRepository"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_ObjectVersionRepository |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[spRPT_ObjectVersionComparison] 
@ServerName VARCHAR(100), @showSame BIT = 1
AS


--DECLARE @ServerName VARCHAR(100), @showSame BIT 
--SELECT @ServerName = 'LaborDB01', @showSame = 1

SET NOCOUNT ON 
IF @showSame = 1
BEGIN
	SELECT InstanceName, ObjectName, ObjectType, InstallDate, VersionDate, usesRevision 
	FROM DBAUtilityMaster.dbo.tblDBA_ObjectVersionRepository
	WHERE InstanceName IN ('CoreDB01', @ServerName)
END
ELSE
BEGIN
	SELECT InstanceName, ObjectName, ObjectType, InstallDate, VersionDate, usesRevision 
	FROM DBAUtilityMaster.dbo.tblDBA_ObjectVersionRepository
	WHERE InstanceName IN ('CoreDB01', @ServerName)
	AND ObjectName NOT IN (
		SELECT Core.ObjectName 
		FROM DBAUtilityMaster.dbo.tblDBA_ObjectVersionRepository Core
		INNER JOIN DBAUtilityMaster.dbo.tblDBA_ObjectVersionRepository Guest ON Core.ObjectName = guest.ObjectName and Core.ObjectType = guest.ObjectType
		AND CONVERT(VARCHAR(10),ISNULL(Core.VersionDate,'1/1/1900'), 101) = CONVERT(VARCHAR(10),ISNULL(guest.VersionDate,'1/1/1900'),101)
		AND ISNULL(CAST(core.usesRevision AS INT),2) =  ISNULL(CAST(core.usesRevision AS INT),3)
		WHERE Core.InstanceName = 'CoreDB01' AND Guest.InstanceName = @ServerName
	)
END
dbo,spRPT_SOXAuditFailedLogins,/****** Script for SelectTopNRows command from SSMS  ******/
CREATE PROCEDURE [dbo].[spRPT_SOXAuditFailedLogins]
@dteStart DATETIME = NULL, @dteEnd DATETIME = NULL
AS
-----------------------------------------------------------------------------------------------------------
--Description: Proc used as source for SOX SQL Role Security Audit report.
--
--Revisions
--	MikeP		20130417		Removed BNHDB01, added EntSCDB01
--  TimB		11/24/2015		Updated Instance Name List
--  TimB		03/16/2016		Updated Instance Name List

-----------------------------------------------------------------------------------------------------------
SET NOCOUNT ON 

SET @dteStart = ISNULL(@dteStart, DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()) - 1, 0))
SET @dteEnd = ISNULL(@dteEnd, DATEADD(MILLISECOND, -3, DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()), 0)))

SELECT [InstanceName]
      ,[LogType]
      ,[LogDate]
      ,[ProcessInfo]
      ,[MessageText]
      ,[InsertDate]
      ,@dteStart StartDate
      ,@dteEnd EndDate
  FROM [DBAUtilityMaster].[dbo].[tblDBA_ErrorLogHistoryRepository] (NOLOCK)
  WHERE InstanceName IN ('CHESDB01', 'CRMDB02', 'CRMISE02', 'LAWSONSQLCLSTR1', 'BEDROCKDB01', 'BEDROCKDB02', 'FAS01','PAPAMART','POSDBSSA','ENTSCDB01' )
  AND LogType = 'SQL Server'
  AND MessageText LIKE 'Login Failed%'
  AND [LogDate] BETWEEN @dteStart AND @dteEnd
  ORDER BY InstanceName, LogDate
```

