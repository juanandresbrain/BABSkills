# dbo.spRPT_ServerMonitorStatus_NotHealthy

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_ServerMonitorStatus_NotHealthy"]
    dbo_Alerts(["dbo.Alerts"]) --> SP
    dbo_BaseManagedEntity(["dbo.BaseManagedEntity"]) --> SP
    dbo_MetricThresholds(["dbo.MetricThresholds"]) --> SP
    dbo_MonitoredSQLServers(["dbo.MonitoredSQLServers"]) --> SP
    dbo_MonitorView(["dbo.MonitorView"]) --> SP
    dbo_RelationshipGenericView(["dbo.RelationshipGenericView"]) --> SP
    dbo_state(["dbo.state"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Alerts |
| dbo.BaseManagedEntity |
| dbo.MetricThresholds |
| dbo.MonitoredSQLServers |
| dbo.MonitorView |
| dbo.RelationshipGenericView |
| dbo.state |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[spRPT_ServerMonitorStatus_NotHealthy]
AS
SET NOCOUNT ON 

SELECT ServerName, MIN(GroupName) GroupName, MonitoringTool, monitor, [object], Health
FROM
(
	SELECT REPLACE(qry.GroupMembers, '.buildabear.com', '') ServerName, qry.GroupName, 
	'SCOM' MonitoringTool, mon.displayName as monitor, --bme.FullName, 
	bme.DisplayName as object, 
	CASE 
	WHEN s.HealthState = 1 THEN 'Healthy'
	WHEN s.HealthState = 2 THEN 'Warning'
	WHEN s.HealthState = 3 THEN 'Critical'
	ELSE 'N/A'
	END as Health 
	FROM SCSTLOMDB01.OperationsManager.dbo.state AS s WITH (NOLOCK)
	LEFT JOIN SCSTLOMDB01.OperationsManager.dbo.BaseManagedEntity as bme WITH (NOLOCK) on s.basemanagedentityid = bme.basemanagedentityid
	LEFT JOIN SCSTLOMDB01.OperationsManager.dbo.MonitorView Mon WITH (NOLOCK) on Mon.ID = s.monitorid 
	INNER JOIN (
		SELECT MIN(SourceMonitoringObjectDisplayName ) 'GroupName', 
		TargetMonitoringObjectDisplayName  'GroupMembers' 
		FROM SCSTLOMDB01.OperationsManager.dbo.RelationshipGenericView 
		WHERE isDeleted=0  
		AND SourceMonitoringObjectDisplayName IN ('IderaDM-Monitored SQL servers', 'Non-Monitored SQL Servers', 'SQL 2000 Computers', 'SQL 2008 Computers', 'SQL Server 2005 Computers')
		--AND TargetMonitoringObjectDisplayName NOT IN 
		--(
		--	SELECT TargetMonitoringObjectDisplayName 
		--	FROM SCSTLOMDB01.OperationsManager.dbo.RelationshipGenericView 
		--	WHERE SourceMonitoringObjectDisplayName IN ('IderaDM-Monitored SQL servers', 'Monitor Exclusion Group')
		--)	
		GROUP BY TargetMonitoringObjectDisplayName
	) qry ON bme.Path = qry.GroupMembers
	WHERE s.HealthState > 1 AND mon.IsInternalRollupMonitor = 0 AND mon.IsExternalRollupMonitor = 0
	--UNION ALL
	--SELECT REPLACE(qry.GroupMembers, '.buildabear.com', '') ServerName, qry.GroupName, 
	--'SCOM' MonitoringTool, mon.displayName as monitor, --bme.FullName, 
	--bme.DisplayName as object, 
	--CASE 
	--WHEN s.HealthState = 1 THEN 'Healthy'
	--WHEN s.HealthState = 2 THEN 'Warning'
	--WHEN s.HealthState = 3 THEN 'Critical'
	--ELSE 'N/A'
	--END as Health 
	--FROM SCSTLOMDB01.OperationsManager.dbo.state AS s WITH (NOLOCK)
	--LEFT JOIN SCSTLOMDB01.OperationsManager.dbo.BaseManagedEntity as bme WITH (NOLOCK) on s.basemanagedentityid = bme.basemanagedentityid
	--LEFT JOIN SCSTLOMDB01.OperationsManager.dbo.MonitorView Mon WITH (NOLOCK) on Mon.ID = s.monitorid 
	--INNER JOIN (
	--	select SourceMonitoringObjectDisplayName as 'GroupName', 
	--	TargetMonitoringObjectDisplayName as 'GroupMembers' 
	--	from SCSTLOMDB01.OperationsManager.dbo.RelationshipGenericView 
	--	where isDeleted=0  
	--	AND SourceMonitoringObjectDisplayName IN ('IderaDM-Monitored SQL servers')
	--	--AND TargetMonitoringObjectDisplayName NOT IN 
	--	--(
	--	--	SELECT TargetMonitoringObjectDisplayName 
	--	--	FROM SCSTLOMDB01.OperationsManager.dbo.RelationshipGenericView 
	--	--	WHERE SourceMonitoringObjectDisplayName IN ('SQL 2000 Computers', 'SQL 2008 Computers', 'SQL Server 2005 Computers','Monitor Exclusion Group')
	--	--)	
	--) qry ON bme.Path = qry.GroupMembers
	--WHERE s.HealthState > 1 AND mon.IsInternalRollupMonitor = 0 AND mon.IsExternalRollupMonitor = 0
	UNION ALL
	SELECT REPLACE(TargetMonitoringObjectDisplayName , '.buildabear.com', '') ServerName, 
		SourceMonitoringObjectDisplayName 'GroupMembers', '' MonitoringTool, 'N/A' Monitor, 'N/A' [Object], 'N/A' Health
		FROM SCSTLOMDB01.OperationsManager.dbo.RelationshipGenericView 
		WHERE isDeleted=0 AND SourceMonitoringObjectDisplayName IN ('Monitor Exclusion Group')
	UNION ALL
	SELECT A.ServerName COLLATE SQL_Latin1_General_CP1_CI_AS as InstanceName, 
	'IderaDM-Monitored SQL servers' GroupName, 'Idera' MonitoringTool, 
	A.Heading COLLATE SQL_Latin1_General_CP1_CI_AS monitor, A.ServerName COLLATE SQL_Latin1_General_CP1_CI_AS [object], CASE A.Severity WHEN 8 THEN 'Critical' WHEN 4 THEN 'Warning' Else 'Healthy' END Status
	--FROM MAMAMART.SQLdmRepository.dbo.MonitoredSQLServers  S (NOLOCK)    
	--LEFT JOIN MAMAMART.SQLdmRepository.dbo.Alerts A (NOLOCK) on A.ServerName collate database_default = S.InstanceName collate database_default and 
	FROM SQLdmRepository.dbo.MonitoredSQLServers  S (NOLOCK)    
	LEFT JOIN SQLdmRepository.dbo.Alerts A (NOLOCK) on A.ServerName collate database_default = S.InstanceName collate database_default and 
		A.UTCOccurrenceDateTime = S.LastScheduledCollectionTime 
	--LEFT JOIN MAMAMART.SQLdmRepository.dbo.MetricThresholds T (nolock) on S.[SQLServerID] = T.[SQLServerID] and A.[Metric] = T.[Metric]
	LEFT JOIN SQLdmRepository.dbo.MetricThresholds T (nolock) on S.[SQLServerID] = T.[SQLServerID] and A.[Metric] = T.[Metric]
	WHERE (T.[UTCSnoozeEnd] is null or T.[UTCSnoozeEnd] < GETDATE())     
	AND S.Active = 1 AND A.Active = 1 AND A.Severity > 3 
	AND S.SQLServerID <> 25 --Oursmerchdb01  
) tbl
GROUP BY ServerName, MonitoringTool, monitor, [object], Health
```

