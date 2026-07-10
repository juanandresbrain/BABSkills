# dbo.ITSprintTaskList

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 1 |  |  |  |
| Priority | nvarchar | 510 | 1 |  |  |  |
| Status | nvarchar | 510 | 1 |  |  |  |
| PercentComplete | float | 8 | 1 |  |  |  |
| ActivityNotes | nvarchar | -1 | 1 |  |  |  |
| ActualHrs | float | 8 | 1 |  |  |  |
| ProjectedHrs | float | 8 | 1 |  |  |  |
| Category | nvarchar | 510 | 1 |  |  |  |
| SummaryNotes | nvarchar | -1 | 1 |  |  |  |
| Requestor | nvarchar | 200 | 1 |  |  |  |
| DueDate | datetime | 8 | 1 |  |  |  |
| SprintPeriod | nvarchar | 8000 | 1 |  |  |  |
| Team | nvarchar | 510 | 1 |  |  |  |
| AssignedTo | nvarchar | 200 | 1 |  |  |  |
| SprintPriority | float | 8 | 1 |  |  |  |
| Department | nvarchar | 510 | 1 |  |  |  |
| PrimarySystemImpacted | nvarchar | 510 | 1 |  |  |  |
| Modified | datetime | 8 | 1 |  |  |  |
| Created | datetime | 8 | 1 |  |  |  |
| CreatedBy | nvarchar | 200 | 1 |  |  |  |
| ModifiedBy | nvarchar | 200 | 1 |  |  |  |
| Attachments | bit | 1 | 1 |  |  |  |
| Edit | nvarchar | 8000 | 1 |  |  |  |
| Title | nvarchar | 510 | 1 |  |  |  |
| RelatedContent | nvarchar | 8000 | 1 |  |  |  |
| ExternalParticipant | nvarchar | 510 | 1 |  |  |  |
| ExternalParticipantReason | nvarchar | 510 | 1 |  |  |  |
| Outcome | nvarchar | 510 | 1 |  |  |  |
| WorkflowName | nvarchar | 510 | 1 |  |  |  |
| SprintTaskApproval | nvarchar | 200 | 1 |  |  |  |
| SprintTaskApprovalWorkflowTa0 | nvarchar | 200 | 1 |  |  |  |
| SprintTaskApprovalWorkflowTa1 | nvarchar | 200 | 1 |  |  |  |
| Feature | nvarchar | 510 | 1 |  |  |  |
| ContentType | nvarchar | 8000 | 1 |  |  |  |
| Version | nvarchar | 510 | 1 |  |  |  |
| Type | nvarchar | 8000 | 1 |  |  |  |
| ItemChildCount | nvarchar | 510 | 1 |  |  |  |
| FolderChildCount | nvarchar | 510 | 1 |  |  |  |
| INS_DT | datetime | 8 | 1 |  |  |  |
| BusinessValue | nvarchar | 8000 | 1 |  |  |  |
