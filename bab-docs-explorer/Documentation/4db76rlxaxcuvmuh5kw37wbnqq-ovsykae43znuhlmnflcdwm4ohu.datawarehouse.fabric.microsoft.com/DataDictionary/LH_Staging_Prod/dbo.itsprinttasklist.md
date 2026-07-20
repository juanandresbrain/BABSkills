# dbo.itsprinttasklist

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 1 |  |  |  |
| Priority | varchar | 8000 | 1 |  |  |  |
| Status | varchar | 8000 | 1 |  |  |  |
| PercentComplete | float | 8 | 1 |  |  |  |
| ActivityNotes | varchar | 8000 | 1 |  |  |  |
| ActualHrs | float | 8 | 1 |  |  |  |
| ProjectedHrs | float | 8 | 1 |  |  |  |
| Category | varchar | 8000 | 1 |  |  |  |
| SummaryNotes | varchar | 8000 | 1 |  |  |  |
| Requestor | varchar | 8000 | 1 |  |  |  |
| DueDate | datetime2 | 8 | 1 |  |  |  |
| SprintPeriod | varchar | 8000 | 1 |  |  |  |
| Team | varchar | 8000 | 1 |  |  |  |
| AssignedTo | varchar | 8000 | 1 |  |  |  |
| SprintPriority | float | 8 | 1 |  |  |  |
| Department | varchar | 8000 | 1 |  |  |  |
| PrimarySystemImpacted | varchar | 8000 | 1 |  |  |  |
| Modified | datetime2 | 8 | 1 |  |  |  |
| Created | datetime2 | 8 | 1 |  |  |  |
| CreatedBy | varchar | 8000 | 1 |  |  |  |
| ModifiedBy | varchar | 8000 | 1 |  |  |  |
| Attachments | bit | 1 | 1 |  |  |  |
| Edit | varchar | 8000 | 1 |  |  |  |
| Title | varchar | 8000 | 1 |  |  |  |
| RelatedContent | varchar | 8000 | 1 |  |  |  |
| ExternalParticipant | varchar | 8000 | 1 |  |  |  |
| ExternalParticipantReason | varchar | 8000 | 1 |  |  |  |
| Outcome | varchar | 8000 | 1 |  |  |  |
| WorkflowName | varchar | 8000 | 1 |  |  |  |
| SprintTaskApproval | varchar | 8000 | 1 |  |  |  |
| SprintTaskApprovalWorkflowTa0 | varchar | 8000 | 1 |  |  |  |
| SprintTaskApprovalWorkflowTa1 | varchar | 8000 | 1 |  |  |  |
| Feature | varchar | 8000 | 1 |  |  |  |
| ContentType | varchar | 8000 | 1 |  |  |  |
| Version | varchar | 8000 | 1 |  |  |  |
| Type | varchar | 8000 | 1 |  |  |  |
| ItemChildCount | varchar | 8000 | 1 |  |  |  |
| FolderChildCount | varchar | 8000 | 1 |  |  |  |
| INS_DT | datetime2 | 8 | 1 |  |  |  |
| BusinessValue | varchar | 8000 | 1 |  |  |  |
