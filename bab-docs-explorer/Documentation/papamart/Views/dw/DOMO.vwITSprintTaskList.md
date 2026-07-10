# DOMO.vwITSprintTaskList

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["DOMO.vwITSprintTaskList"]
    dbo_ITSprintTaskList(["dbo.ITSprintTaskList"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITSprintTaskList |

## View Code

```sql
CREATE VIEW [DOMO].[vwITSprintTaskList] AS
-- =============================================================================================================
-- Name: [DOMO].[vwITSprintTaskList]
--
-- Description: View of staged Sprint Task SharePoint list.
--
--
-- Dependencies: DWStaging.dbo.ITSprintTaskList
--
-- Revision History
--		Name:				Date:			Comments:
--		Anthony Delgado		12/7/2015		Initial creation
--		Brian Byas			3/8/2016		Altered BusinessBenefit to BusinessValue
-- =============================================================================================================
SELECT [ID]
      ,CASE WHEN LEN([Priority])>4 THEN RIGHT([Priority],LEN([PRIORITY])-4) 
			ELSE [Priority] 
		END AS [Priority]
      ,CASE WHEN [Status] IN ('Complete (NEW)', 'Past Sprint') THEN 'Complete'
			WHEN [Status] IN ('Current', 'In Progress (NEW)') THEN 'In Progress'
			WHEN [Status] IN ('Deferred (NEW)') THEN 'Deferred'
			WHEN [Status] IN ('Testing (NEW)') THEN 'Testing' 
			ELSE [STATUS]
		END AS [Status]
      ,[PercentComplete]
      ,[ActivityNotes]
      ,[ActualHrs]
      ,[ProjectedHrs] AS BaselineHrs
      ,CASE WHEN RIGHT([Category],5)='(NEW)' THEN LEFT([Category], LEN([Category])-5) 
			ELSE [Category]
		END AS [Category]
      ,[SummaryNotes]
      ,[BusinessValue]
	  ,SprintTaskApproval
      ,RIGHT([Requestor],LEN([Requestor])-CHARINDEX('#',[Requestor])) AS Requestor
      ,[DueDate]
	  ,RANK() OVER (ORDER BY SprintPeriod DESC) AS SprintRecencyRank
      ,CASE WHEN [SprintPeriod] LIKE '%#%' THEN SUBSTRING([SprintPeriod],CHARINDEX('#',[SprintPeriod])+1,9)
			ELSE [SprintPeriod]
		END AS SprintPeriod
	  ,CASE WHEN [SprintPeriod] LIKE '%#%' THEN LEFT([SprintPeriod],CHARINDEX('#',[SprintPeriod])-2) 
			ELSE [SprintPeriod]
		END AS SprintNumber
	  ,RIGHT([PrimarySystemImpacted],LEN([PrimarySystemImpacted])-CHARINDEX('#',[PrimarySystemImpacted]))As SystemApplicability
      ,RIGHT([Team],LEN([Team])-CHARINDEX('#',[Team])) AS Team
      ,RIGHT([AssignedTo],LEN([AssignedTo])-CHARINDEX('#',[AssignedTo])) AS AssignedTo
      ,[SprintPriority]
      ,[Department]
      ,[PrimarySystemImpacted]
      ,[Modified]
      ,[Created]
      ,RIGHT([CreatedBy],LEN([CreatedBy])-CHARINDEX('#',[CreatedBy])) AS CreatedBy
      ,RIGHT([ModifiedBy],LEN([ModifiedBy])-CHARINDEX('#',[ModifiedBy])) AS ModifiedBy
      ,[Attachments]
      ,[Title]
      ,[Feature]
      ,[Version]
      ,RIGHT([ItemChildCount],LEN([ItemChildCount])-CHARINDEX('#',[ItemChildCount])) AS ItemChildCount
      ,RIGHT([FolderChildCount],LEN([FolderChildCount])-CHARINDEX('#',[FolderChildCount])) AS FolderChildCount
  FROM [DWStaging].[dbo].[ITSprintTaskList]
  WHERE Status<>'Cancelled'
```

