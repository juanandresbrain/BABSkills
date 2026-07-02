# dbo.Sv_UpdateNextID

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_UpdateNextID"]
    dbo_Cs_ExportReg(["dbo.Cs_ExportReg"]) --> SP
    dbo_Cs_FileStat(["dbo.Cs_FileStat"]) --> SP
    dbo_Cs_Service(["dbo.Cs_Service"]) --> SP
    dbo_Ex_ExecutionHistory(["dbo.Ex_ExecutionHistory"]) --> SP
    dbo_Ex_ServerMain(["dbo.Ex_ServerMain"]) --> SP
    dbo_Sr_History(["dbo.Sr_History"]) --> SP
    dbo_Sr_Host(["dbo.Sr_Host"]) --> SP
    dbo_Sr_Job(["dbo.Sr_Job"]) --> SP
    dbo_Sv_Categories(["dbo.Sv_Categories"]) --> SP
    dbo_Sv_Deleted(["dbo.Sv_Deleted"]) --> SP
    dbo_Sv_File(["dbo.Sv_File"]) --> SP
    dbo_Sv_Mail(["dbo.Sv_Mail"]) --> SP
    dbo_Sv_NextID(["dbo.Sv_NextID"]) --> SP
    dbo_Sv_Object(["dbo.Sv_Object"]) --> SP
    dbo_Sv_Output(["dbo.Sv_Output"]) --> SP
    dbo_Sv_OutputNote(["dbo.Sv_OutputNote"]) --> SP
    dbo_Sv_Picture(["dbo.Sv_Picture"]) --> SP
    dbo_Sv_Reminder(["dbo.Sv_Reminder"]) --> SP
    dbo_Sv_Statistic(["dbo.Sv_Statistic"]) --> SP
    dbo_Sv_User(["dbo.Sv_User"]) --> SP
    dbo_Sv_UserFolder(["dbo.Sv_UserFolder"]) --> SP
    dbo_Sv_UserGroup(["dbo.Sv_UserGroup"]) --> SP
    dbo_Tr_Directory(["dbo.Tr_Directory"]) --> SP
    dbo_Tr_Parameter(["dbo.Tr_Parameter"]) --> SP
    dbo_Tr_PollFile(["dbo.Tr_PollFile"]) --> SP
    dbo_Tr_PollFileHistory(["dbo.Tr_PollFileHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Cs_ExportReg |
| dbo.Cs_FileStat |
| dbo.Cs_Service |
| dbo.Ex_ExecutionHistory |
| dbo.Ex_ServerMain |
| dbo.Sr_History |
| dbo.Sr_Host |
| dbo.Sr_Job |
| dbo.Sv_Categories |
| dbo.Sv_Deleted |
| dbo.Sv_File |
| dbo.Sv_Mail |
| dbo.Sv_NextID |
| dbo.Sv_Object |
| dbo.Sv_Output |
| dbo.Sv_OutputNote |
| dbo.Sv_Picture |
| dbo.Sv_Reminder |
| dbo.Sv_Statistic |
| dbo.Sv_User |
| dbo.Sv_UserFolder |
| dbo.Sv_UserGroup |
| dbo.Tr_Directory |
| dbo.Tr_Parameter |
| dbo.Tr_PollFile |
| dbo.Tr_PollFileHistory |

## Stored Procedure Code

```sql

```

