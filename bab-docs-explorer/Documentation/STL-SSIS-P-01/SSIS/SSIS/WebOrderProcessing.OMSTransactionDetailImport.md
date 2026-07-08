# SSIS Package: OMSTransactionDetailImport

**Project:** WebOrderProcessing  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| OMSTransactionDetailReport | FLATFILE |  |  |  |
| OMSTransactionDetailReport_v2 | FLATFILE |  |  |  |
| SMTP_EMAIL | SMTP |  |  |  |
| SQL_LOG | OLEDB | stl-ssis-p-01 | msdb | Data Source=stl-ssis-p-01; Initial Catalog=msdb; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| TransactionDetailCSV | FILE |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| OMSTransactionDetailImport | Package |
| Sequence Container | SEQUENCE |
| Foreach Loop - Move Source Files to Stage | FOREACHLOOP |
| Move Files to Stage | FileSystemTask |
| Foreach Loop Container | FOREACHLOOP |
| DFT - Transaction Details | Pipeline |
| File System Task | FileSystemTask |
| File System Task 1 | FileSystemTask |
| ST - Fix Input Files | ScriptTask |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- Sequence Container [SEQUENCE]
  - Foreach Loop - Move Source Files to Stage [FOREACHLOOP]
    - Move Files to Stage [FileSystemTask]
  - Foreach Loop Container [FOREACHLOOP]
    - DFT - Transaction Details [Pipeline]
    - File System Task [FileSystemTask]
    - File System Task 1 [FileSystemTask]
    - ST - Fix Input Files [ScriptTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Sequence_Container["Sequence Container"]
    n_Package_Sequence_Container_Foreach_Loop___Move_Source_Files_to_Stage["Foreach Loop - Move Source Files to Stage"]
    n_Package_Sequence_Container_Foreach_Loop___Move_Source_Files_to_Stage_Move_Files_to_Stage["Move Files to Stage"]
    n_Package_Sequence_Container_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_Sequence_Container_Foreach_Loop_Container_DFT___Transaction_Details["DFT - Transaction Details"]
    n_Package_Sequence_Container_Foreach_Loop_Container_File_System_Task["File System Task"]
    n_Package_Sequence_Container_Foreach_Loop_Container_File_System_Task_1["File System Task 1"]
    n_Package_Sequence_Container_Foreach_Loop_Container_ST___Fix_Input_Files["ST - Fix Input Files"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_Sequence_Container_Foreach_Loop_Container_DFT___Transaction_Details --> n_Package_Sequence_Container_Foreach_Loop_Container_File_System_Task
    n_Package_Sequence_Container_Foreach_Loop_Container_ST___Fix_Input_Files --> n_Package_Sequence_Container_Foreach_Loop_Container_DFT___Transaction_Details
    n_Package_Sequence_Container_Foreach_Loop_Container_DFT___Transaction_Details --> n_Package_Sequence_Container_Foreach_Loop_Container_File_System_Task_1
    n_Package_Sequence_Container_Foreach_Loop___Move_Source_Files_to_Stage --> n_Package_Sequence_Container_Foreach_Loop_Container
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | FileStageDirectory | No |
| User | OMSFileName | No |
| User | SourceFileName | No |
| User | tmpRowCount | No |

## Execute SQL Tasks

_None detected._

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| FFS - Read Transaction Details |  | FlatFileSource | DFT - Transaction Details | OMSTransactionDetailReport_v2 |  |

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| Insert TransactionDetails |  | OLEDBDestination | DFT - Transaction Details | {6c71ac67-bc98-46e8-9678-412afb3961fd}:external |  |
| Insert TransactionDetails 1 |  | OLEDBDestination | DFT - Transaction Details | {6c71ac67-bc98-46e8-9678-412afb3961fd}:external |  |
