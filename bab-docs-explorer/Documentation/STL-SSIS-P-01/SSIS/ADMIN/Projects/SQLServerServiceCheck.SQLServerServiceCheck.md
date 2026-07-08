# SSIS Package: SQLServerServiceCheck

**Project:** SQLServerServiceCheck  
**Folder:** ADMIN/Projects  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| IntegrationStaging | OLEDB | stl-ssis-p-01 | IntegrationStaging | Data Source=stl-ssis-p-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| SMTP | SMTP |  |  |  |
| master | OLEDB | AVeryLongServenameJustToIncreaseMetaData | master | Data Source=AVeryLongServenameJustToIncreaseMetaData; Initial Catalog=master; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| master - NowOnline | OLEDB | AVeryLongServenameJustToIncreaseMetaData | master | Data Source=AVeryLongServenameJustToIncreaseMetaData; Initial Catalog=master; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| master - PostRestart | OLEDB | AVeryLongServenameJustToIncreaseMetaData | master | Data Source=AVeryLongServenameJustToIncreaseMetaData; Initial Catalog=master; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| master - SQL Agent | OLEDB | AVeryLongServenameJustToIncreaseMetaData | master | Data Source=AVeryLongServenameJustToIncreaseMetaData; Initial Catalog=master; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |

## Control Flow Tasks

| Task | Type |
|---|---|
| SQLServerServiceCheck | Package |
| Offline Row Count Check | ExecuteSQLTask |
| Sequence Container  - Start SQL Agent Service on Eligible Servers | SEQUENCE |
| Execute SQL Task - Load Target Server Names Sql Agent After Start Attempt | ExecuteSQLTask |
| Execute SQL Task - Load Target Server Names Sql Agent Start | ExecuteSQLTask |
| FEL - Check SQL Agent Status | FOREACHLOOP |
| Data Flow Task - Load SQL Agent Status | Pipeline |
| Execute SQL Task - Query Target Server for SQL Agent Status | ExecuteSQLTask |
| FEL - Start SQL Agent Service | FOREACHLOOP |
| Execute Process Task - Start Sql Agent Svc | ExecuteProcess |
| Execute SQL Task - Wait X Seconds | ExecuteSQLTask |
| Sequence Container  - Validate Service Is Now Running and Load SQL Agent Start Eligibility | SEQUENCE |
| Execute SQL Task - Wait for 10 Seconds - Testing Only | ExecuteSQLTask |
| Sequence Container - Get Server Status Post Restart | SEQUENCE |
| Execute SQL Task  - Load Target Server Names | ExecuteSQLTask |
| Execute SQL Task - Trucate Stage | ExecuteSQLTask |
| FEL - Query Target Server - Post Restart | FOREACHLOOP |
| Data Flow Task - Reload SqlServerStatusCheck | Pipeline |
| Execute SQL Task - Query Target Server | ExecuteSQLTask |
| Sequence Container - Load SQL Agent Start Eligibility | SEQUENCE |
| Data Flow Task - Load Curr Status | Pipeline |
| Execute SQL Task - Load Servers Now Online | ExecuteSQLTask |
| FEL - Load SQL Agent Start Eligibility | FOREACHLOOP |
| Data Flow Task - Load SQL Agent Elig Status | Pipeline |
| Execute SQL Task - Query Target Server for SQL Agent Elig | ExecuteSQLTask |
| Sequence Container - Get Server Status | SEQUENCE |
| Data Flow Task - Load Target Server Control Table | Pipeline |
| Execute SQL Task  - Load Target Server Names | ExecuteSQLTask |
| Execute SQL Task - Truncate Stage | ExecuteSQLTask |
| FEL - Query Target Server | FOREACHLOOP |
| Data Flow Task - Load SqlServerStatusCheck | Pipeline |
| Execute SQL Task - Query Target Server | ExecuteSQLTask |
| Sequence Container - Send Emails | SEQUENCE |
| Check Hour - Only Send at 6, 12, 18 Hours | ExecuteSQLTask |
| Offline Row Count Check After Restart | ExecuteSQLTask |
| Online Row Count  Check After Restart | ExecuteSQLTask |
| Sequence Container - Send Email Action Taken | SEQUENCE |
| Execute SQL Task - SEnd No Problem Email | ExecuteSQLTask |
| Sequence Container - Send Email No Action | SEQUENCE |
| Execute SQL Task - Send No Problem Email | ExecuteSQLTask |
| Sequence Container - Send Problem Email | SEQUENCE |
| Execute SQL Task - Send Problem Email | ExecuteSQLTask |
| Sequence Container - Start SQL on Server | SEQUENCE |
| Data Flow Task - Load Server Status to Reporting Table | Pipeline |
| Execute SQL Task - Load Offline Server Names | ExecuteSQLTask |
| Execute SQL Task - Truncate Reporting Table | ExecuteSQLTask |
| Foreach Loop Container - Issue Start Command | FOREACHLOOP |
| Execute Process Task - Start SQL Agent Service | ExecuteProcess |
| Execute Process Task - Start SQL Server Service | ExecuteProcess |
| Execute Process Task - Stop SQL Agent Service | ExecuteProcess |
| Execute Process Task - Stop SQL Server Service | ExecuteProcess |
| Execute SQL Task - Wait for 10 Seconds  - 1 | ExecuteSQLTask |
| Execute SQL Task - Wait for 10 Seconds - 2 | ExecuteSQLTask |
| Execute SQL Task - Wait for 10 Seconds - 3 | ExecuteSQLTask |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- Offline Row Count Check [ExecuteSQLTask]
- Sequence Container  - Start SQL Agent Service on Eligible Servers [SEQUENCE]
  - Execute SQL Task - Load Target Server Names Sql Agent After Start Attempt [ExecuteSQLTask]
  - Execute SQL Task - Load Target Server Names Sql Agent Start [ExecuteSQLTask]
  - FEL - Check SQL Agent Status [FOREACHLOOP]
    - Data Flow Task - Load SQL Agent Status [Pipeline]
    - Execute SQL Task - Query Target Server for SQL Agent Status [ExecuteSQLTask]
  - FEL - Start SQL Agent Service [FOREACHLOOP]
    - Execute Process Task - Start Sql Agent Svc [ExecuteProcess]
    - Execute SQL Task - Wait X Seconds [ExecuteSQLTask]
- Sequence Container  - Validate Service Is Now Running and Load SQL Agent Start Eligibility [SEQUENCE]
  - Execute SQL Task - Wait for 10 Seconds - Testing Only [ExecuteSQLTask]
  - Sequence Container - Get Server Status Post Restart [SEQUENCE]
    - Execute SQL Task  - Load Target Server Names [ExecuteSQLTask]
    - Execute SQL Task - Trucate Stage [ExecuteSQLTask]
    - FEL - Query Target Server - Post Restart [FOREACHLOOP]
      - Data Flow Task - Reload SqlServerStatusCheck [Pipeline]
      - Execute SQL Task - Query Target Server [ExecuteSQLTask]
  - Sequence Container - Load SQL Agent Start Eligibility [SEQUENCE]
    - Data Flow Task - Load Curr Status [Pipeline]
    - Execute SQL Task - Load Servers Now Online [ExecuteSQLTask]
    - FEL - Load SQL Agent Start Eligibility [FOREACHLOOP]
      - Data Flow Task - Load SQL Agent Elig Status [Pipeline]
      - Execute SQL Task - Query Target Server for SQL Agent Elig [ExecuteSQLTask]
- Sequence Container - Get Server Status [SEQUENCE]
  - Data Flow Task - Load Target Server Control Table [Pipeline]
  - Execute SQL Task  - Load Target Server Names [ExecuteSQLTask]
  - Execute SQL Task - Truncate Stage [ExecuteSQLTask]
  - FEL - Query Target Server [FOREACHLOOP]
    - Data Flow Task - Load SqlServerStatusCheck [Pipeline]
    - Execute SQL Task - Query Target Server [ExecuteSQLTask]
- Sequence Container - Send Emails [SEQUENCE]
  - Check Hour - Only Send at 6, 12, 18 Hours [ExecuteSQLTask]
  - Offline Row Count Check After Restart [ExecuteSQLTask]
  - Online Row Count  Check After Restart [ExecuteSQLTask]
  - Sequence Container - Send Email Action Taken [SEQUENCE]
    - Execute SQL Task - SEnd No Problem Email [ExecuteSQLTask]
  - Sequence Container - Send Email No Action [SEQUENCE]
    - Execute SQL Task - Send No Problem Email [ExecuteSQLTask]
  - Sequence Container - Send Problem Email [SEQUENCE]
    - Execute SQL Task - Send Problem Email [ExecuteSQLTask]
- Sequence Container - Start SQL on Server [SEQUENCE]
  - Data Flow Task - Load Server Status to Reporting Table [Pipeline]
  - Execute SQL Task - Load Offline Server Names [ExecuteSQLTask]
  - Execute SQL Task - Truncate Reporting Table [ExecuteSQLTask]
  - Foreach Loop Container - Issue Start Command [FOREACHLOOP]
    - Execute Process Task - Start SQL Agent Service [ExecuteProcess]
    - Execute Process Task - Start SQL Server Service [ExecuteProcess]
    - Execute Process Task - Stop SQL Agent Service [ExecuteProcess]
    - Execute Process Task - Stop SQL Server Service [ExecuteProcess]
    - Execute SQL Task - Wait for 10 Seconds  - 1 [ExecuteSQLTask]
    - Execute SQL Task - Wait for 10 Seconds - 2 [ExecuteSQLTask]
    - Execute SQL Task - Wait for 10 Seconds - 3 [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Offline_Row_Count_Check["Offline Row Count Check"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers["Sequence Container  - Start SQL Agent Service on Eligible Servers"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_Execute_SQL_Task___Load_Target_Server_Names_Sql_Agent_After_Start_Attempt["Execute SQL Task - Load Target Server Names Sql Agent After Start Attempt"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_Execute_SQL_Task___Load_Target_Server_Names_Sql_Agent_Start["Execute SQL Task - Load Target Server Names Sql Agent Start"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Check_SQL_Agent_Status["FEL - Check SQL Agent Status"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Check_SQL_Agent_Status_Data_Flow_Task___Load_SQL_Agent_Status["Data Flow Task - Load SQL Agent Status"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Check_SQL_Agent_Status_Execute_SQL_Task___Query_Target_Server_for_SQL_Agent_Status["Execute SQL Task - Query Target Server for SQL Agent Status"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Start_SQL_Agent_Service["FEL - Start SQL Agent Service"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Start_SQL_Agent_Service_Execute_Process_Task___Start_Sql_Agent_Svc["Execute Process Task - Start Sql Agent Svc"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Start_SQL_Agent_Service_Execute_SQL_Task___Wait_X_Seconds["Execute SQL Task - Wait X Seconds"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility["Sequence Container  - Validate Service Is Now Running and Load SQL Agent Start Eligibility"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Execute_SQL_Task___Wait_for_10_Seconds___Testing_Only["Execute SQL Task - Wait for 10 Seconds - Testing Only"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart["Sequence Container - Get Server Status Post Restart"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_Execute_SQL_Task____Load_Target_Server_Names["Execute SQL Task  - Load Target Server Names"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_Execute_SQL_Task___Trucate_Stage["Execute SQL Task - Trucate Stage"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_FEL___Query_Target_Server___Post_Restart["FEL - Query Target Server - Post Restart"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_FEL___Query_Target_Server___Post_Restart_Data_Flow_Task___Reload_SqlServerStatusCheck["Data Flow Task - Reload SqlServerStatusCheck"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_FEL___Query_Target_Server___Post_Restart_Execute_SQL_Task___Query_Target_Server["Execute SQL Task - Query Target Server"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility["Sequence Container - Load SQL Agent Start Eligibility"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_Data_Flow_Task___Load_Curr_Status["Data Flow Task - Load Curr Status"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_Execute_SQL_Task___Load_Servers_Now_Online["Execute SQL Task - Load Servers Now Online"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_FEL___Load_SQL_Agent_Start_Eligibility["FEL - Load SQL Agent Start Eligibility"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_FEL___Load_SQL_Agent_Start_Eligibility_Data_Flow_Task___Load_SQL_Agent_Elig_Status["Data Flow Task - Load SQL Agent Elig Status"]
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_FEL___Load_SQL_Agent_Start_Eligibility_Execute_SQL_Task___Query_Target_Server_for_SQL_Agent_Elig["Execute SQL Task - Query Target Server for SQL Agent Elig"]
    n_Package_Sequence_Container___Get_Server_Status["Sequence Container - Get Server Status"]
    n_Package_Sequence_Container___Get_Server_Status_Data_Flow_Task___Load_Target_Server_Control_Table["Data Flow Task - Load Target Server Control Table"]
    n_Package_Sequence_Container___Get_Server_Status_Execute_SQL_Task____Load_Target_Server_Names["Execute SQL Task  - Load Target Server Names"]
    n_Package_Sequence_Container___Get_Server_Status_Execute_SQL_Task___Truncate_Stage["Execute SQL Task - Truncate Stage"]
    n_Package_Sequence_Container___Get_Server_Status_FEL___Query_Target_Server["FEL - Query Target Server"]
    n_Package_Sequence_Container___Get_Server_Status_FEL___Query_Target_Server_Data_Flow_Task___Load_SqlServerStatusCheck["Data Flow Task - Load SqlServerStatusCheck"]
    n_Package_Sequence_Container___Get_Server_Status_FEL___Query_Target_Server_Execute_SQL_Task___Query_Target_Server["Execute SQL Task - Query Target Server"]
    n_Package_Sequence_Container___Send_Emails["Sequence Container - Send Emails"]
    n_Package_Sequence_Container___Send_Emails_Check_Hour___Only_Send_at_6__12__18_Hours["Check Hour - Only Send at 6, 12, 18 Hours"]
    n_Package_Sequence_Container___Send_Emails_Offline_Row_Count_Check_After_Restart["Offline Row Count Check After Restart"]
    n_Package_Sequence_Container___Send_Emails_Online_Row_Count__Check_After_Restart["Online Row Count  Check After Restart"]
    n_Package_Sequence_Container___Send_Emails_Sequence_Container___Send_Email_Action_Taken["Sequence Container - Send Email Action Taken"]
    n_Package_Sequence_Container___Send_Emails_Sequence_Container___Send_Email_Action_Taken_Execute_SQL_Task___SEnd_No_Problem_Email["Execute SQL Task - SEnd No Problem Email"]
    n_Package_Sequence_Container___Send_Emails_Sequence_Container___Send_Email_No_Action["Sequence Container - Send Email No Action"]
    n_Package_Sequence_Container___Send_Emails_Sequence_Container___Send_Email_No_Action_Execute_SQL_Task___Send_No_Problem_Email["Execute SQL Task - Send No Problem Email"]
    n_Package_Sequence_Container___Send_Emails_Sequence_Container___Send_Problem_Email["Sequence Container - Send Problem Email"]
    n_Package_Sequence_Container___Send_Emails_Sequence_Container___Send_Problem_Email_Execute_SQL_Task___Send_Problem_Email["Execute SQL Task - Send Problem Email"]
    n_Package_Sequence_Container___Start_SQL_on_Server["Sequence Container - Start SQL on Server"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Data_Flow_Task___Load_Server_Status_to_Reporting_Table["Data Flow Task - Load Server Status to Reporting Table"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Execute_SQL_Task___Load_Offline_Server_Names["Execute SQL Task - Load Offline Server Names"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Execute_SQL_Task___Truncate_Reporting_Table["Execute SQL Task - Truncate Reporting Table"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command["Foreach Loop Container - Issue Start Command"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Start_SQL_Agent_Service["Execute Process Task - Start SQL Agent Service"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Start_SQL_Server_Service["Execute Process Task - Start SQL Server Service"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Stop_SQL_Agent_Service["Execute Process Task - Stop SQL Agent Service"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Stop_SQL_Server_Service["Execute Process Task - Stop SQL Server Service"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_SQL_Task___Wait_for_10_Seconds____1["Execute SQL Task - Wait for 10 Seconds  - 1"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_SQL_Task___Wait_for_10_Seconds___2["Execute SQL Task - Wait for 10 Seconds - 2"]
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_SQL_Task___Wait_for_10_Seconds___3["Execute SQL Task - Wait for 10 Seconds - 3"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Check_SQL_Agent_Status_Execute_SQL_Task___Query_Target_Server_for_SQL_Agent_Status --> n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Check_SQL_Agent_Status_Data_Flow_Task___Load_SQL_Agent_Status
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Start_SQL_Agent_Service_Execute_Process_Task___Start_Sql_Agent_Svc --> n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Start_SQL_Agent_Service_Execute_SQL_Task___Wait_X_Seconds
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_Execute_SQL_Task___Load_Target_Server_Names_Sql_Agent_Start --> n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Start_SQL_Agent_Service
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Start_SQL_Agent_Service --> n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_Execute_SQL_Task___Load_Target_Server_Names_Sql_Agent_After_Start_Attempt
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_Execute_SQL_Task___Load_Target_Server_Names_Sql_Agent_After_Start_Attempt --> n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers_FEL___Check_SQL_Agent_Status
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_FEL___Query_Target_Server___Post_Restart_Execute_SQL_Task___Query_Target_Server --> n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_FEL___Query_Target_Server___Post_Restart_Data_Flow_Task___Reload_SqlServerStatusCheck
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_Execute_SQL_Task___Trucate_Stage --> n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_Execute_SQL_Task____Load_Target_Server_Names
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_Execute_SQL_Task____Load_Target_Server_Names --> n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart_FEL___Query_Target_Server___Post_Restart
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_FEL___Load_SQL_Agent_Start_Eligibility_Execute_SQL_Task___Query_Target_Server_for_SQL_Agent_Elig --> n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_FEL___Load_SQL_Agent_Start_Eligibility_Data_Flow_Task___Load_SQL_Agent_Elig_Status
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_Data_Flow_Task___Load_Curr_Status --> n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_Execute_SQL_Task___Load_Servers_Now_Online
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_Execute_SQL_Task___Load_Servers_Now_Online --> n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility_FEL___Load_SQL_Agent_Start_Eligibility
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart --> n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Load_SQL_Agent_Start_Eligibility
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Execute_SQL_Task___Wait_for_10_Seconds___Testing_Only --> n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility_Sequence_Container___Get_Server_Status_Post_Restart
    n_Package_Sequence_Container___Get_Server_Status_FEL___Query_Target_Server_Execute_SQL_Task___Query_Target_Server --> n_Package_Sequence_Container___Get_Server_Status_FEL___Query_Target_Server_Data_Flow_Task___Load_SqlServerStatusCheck
    n_Package_Sequence_Container___Get_Server_Status_Execute_SQL_Task____Load_Target_Server_Names --> n_Package_Sequence_Container___Get_Server_Status_FEL___Query_Target_Server
    n_Package_Sequence_Container___Get_Server_Status_Execute_SQL_Task___Truncate_Stage --> n_Package_Sequence_Container___Get_Server_Status_Data_Flow_Task___Load_Target_Server_Control_Table
    n_Package_Sequence_Container___Get_Server_Status_Data_Flow_Task___Load_Target_Server_Control_Table --> n_Package_Sequence_Container___Get_Server_Status_Execute_SQL_Task____Load_Target_Server_Names
    n_Package_Sequence_Container___Send_Emails_Online_Row_Count__Check_After_Restart --> n_Package_Sequence_Container___Send_Emails_Sequence_Container___Send_Email_Action_Taken
    n_Package_Sequence_Container___Send_Emails_Check_Hour___Only_Send_at_6__12__18_Hours --> n_Package_Sequence_Container___Send_Emails_Sequence_Container___Send_Email_No_Action
    n_Package_Sequence_Container___Send_Emails_Offline_Row_Count_Check_After_Restart --> n_Package_Sequence_Container___Send_Emails_Sequence_Container___Send_Problem_Email
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Stop_SQL_Agent_Service --> n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_SQL_Task___Wait_for_10_Seconds____1
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Stop_SQL_Server_Service --> n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_SQL_Task___Wait_for_10_Seconds___2
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Start_SQL_Server_Service --> n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_SQL_Task___Wait_for_10_Seconds___3
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_SQL_Task___Wait_for_10_Seconds___2 --> n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Start_SQL_Server_Service
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_SQL_Task___Wait_for_10_Seconds____1 --> n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Stop_SQL_Server_Service
    n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_SQL_Task___Wait_for_10_Seconds___3 --> n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command_Execute_Process_Task___Start_SQL_Agent_Service
    n_Package_Sequence_Container___Start_SQL_on_Server_Execute_SQL_Task___Load_Offline_Server_Names --> n_Package_Sequence_Container___Start_SQL_on_Server_Foreach_Loop_Container___Issue_Start_Command
    n_Package_Sequence_Container___Start_SQL_on_Server_Data_Flow_Task___Load_Server_Status_to_Reporting_Table --> n_Package_Sequence_Container___Start_SQL_on_Server_Execute_SQL_Task___Load_Offline_Server_Names
    n_Package_Sequence_Container___Start_SQL_on_Server_Execute_SQL_Task___Truncate_Reporting_Table --> n_Package_Sequence_Container___Start_SQL_on_Server_Data_Flow_Task___Load_Server_Status_to_Reporting_Table
    n_Package_Sequence_Container___Get_Server_Status --> n_Package_Sequence_Container___Start_SQL_on_Server
    n_Package_Sequence_Container___Start_SQL_on_Server --> n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility
    n_Package_Sequence_Container____Validate_Service_Is_Now_Running_and_Load_SQL_Agent_Start_Eligibility --> n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers
    n_Package_Sequence_Container____Start_SQL_Agent_Service_on_Eligible_Servers --> n_Package_Sequence_Container___Send_Emails
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | BatchDestFilePath | Yes |
| User | BatchDestFilePath2 | No |
| User | BatchSourceFilePath | No |
| User | BatchSourceShortcutFilePath | No |
| User | DateTimeStamp | Yes |
| User | EndDate | Yes |
| User | EndDateAsDATE | Yes |
| User | GetDate | Yes |
| User | GetDateAsDATE | Yes |
| User | NoProblemEmailTimeCheck | No |
| User | QueryResult | No |
| User | QueryResultAfterRestart | No |
| User | QueryResultSqlAgentCheck | No |
| User | ServerNameAfterRestart | No |
| User | ServerNameEligibleForSqlAgentStart | No |
| User | ServerNameNew | No |
| User | ServerNameNowOnline | No |
| User | ServerNameOffline | No |
| User | ServerNameSqlAgentSvcCheck | No |
| User | ServerNamesAfterRestart | No |
| User | ServerNamesCheckSqlAgentStatus | No |
| User | ServerNamesEligibleForSqlAgentStart | No |
| User | ServerNamesNew | No |
| User | ServerNamesNowOnline | No |
| User | ServerNamesOffline | No |
| User | ServersOfflineCountVar | No |
| User | ServersOfflineCountVarAfterRestart | No |
| User | ServersOnlineCountVarAfterRestart | No |
| User | SqlAgentEligibility | No |
| User | SqlSourceString | Yes |
| User | SqlVariableString | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |

### Expression-bound variable values

#### User::BatchDestFilePath

**Expression:**

```sql
"\\\\"+ @[User::ServerNameOffline]+"\\"+"C$"+"\\"+"Temp"+"\\"
```

**Evaluated value:**

```sql
\\PipeTestApp01\C$\Temp\
```

#### User::DateTimeStamp

**Expression:**

```sql
(DT_WSTR,4)DATEPART("yyyy",GetDate()) 
+ (DT_WSTR,4)DATEPART("mm",GetDate()) 
+ (DT_WSTR,4)DATEPART("dd",GetDate()) 
+ (DT_WSTR,4)DATEPART("hh",GetDate()) 
+ (DT_WSTR,4)DATEPART("mi",GetDate()) 
+ (DT_WSTR,4)DATEPART("ss",GetDate()) 
+ (DT_WSTR,4)DATEPART("ms",GetDate())
```

**Evaluated value:**

```sql
2026521101423393
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
5/21/2026
```

#### User::EndDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::EndDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::EndDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::EndDate]),2)
```

**Evaluated value:**

```sql
2026-05-21
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
5/21/2026
```

#### User::GetDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::GetDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::GetDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::GetDate]),2)
```

**Evaluated value:**

```sql
2026-05-21
```

#### User::SqlSourceString

**Expression:**

```sql
"select "+
"'"
+
@[User::ServerNameNew]+
"'"
+
" as ServerName,
" +
"'"
+
 
 (DT_STR, 20,1252) @[User::QueryResult]
+

"'"
+
" as SQLServerStatus"
```

**Evaluated value:**

```sql
select 'AVeryLongServenameJustToIncreaseMetaData' as ServerName,
'' as SQLServerStatus
```

#### User::SqlVariableString

**Expression:**

```sql
"SELECT ? AS Message
FROM (SELECT 1 AS N)t"
```

**Evaluated value:**

```sql
SELECT ? AS Message
FROM (SELECT 1 AS N)t
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
5/20/2026
```

#### User::StartDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::StartDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::StartDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::StartDate]),2)
```

**Evaluated value:**

```sql
2026-05-20
```

## Execute SQL Tasks

### Offline Row Count Check

**Path:** `Package\Offline Row Count Check`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select count (*) ServersOfflineCount
from [dbo].[SqlServerStatusCheck]
where SQLServerStatus = 'Offline'
order by 1
```

### Execute SQL Task - Load Target Server Names Sql Agent After Start Attempt

**Path:** `Package\Sequence Container  - Start SQL Agent Service on Eligible Servers\Execute SQL Task - Load Target Server Names Sql Agent After Start Attempt`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql

select distinct ServerName
from [Reporting].[SqlServerStatusCheck]
--where SQLServerStatus = 'Offline' 
--and SQLServerStatusAfterStartAttempt = 'Online'
where SQLServerAgentStartEligible = 'Yes'
order by 1

```

### Execute SQL Task - Load Target Server Names Sql Agent Start

**Path:** `Package\Sequence Container  - Start SQL Agent Service on Eligible Servers\Execute SQL Task - Load Target Server Names Sql Agent Start`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql

select distinct ServerName
from [Reporting].[SqlServerStatusCheck]
where SQLServerStatus = 'Offline' 
and SQLServerStatusAfterStartAttempt = 'Online'
and SQLServerAgentStartEligible = 'Yes'
order by 1

```

### Execute SQL Task - Query Target Server for SQL Agent Status

**Path:** `Package\Sequence Container  - Start SQL Agent Service on Eligible Servers\FEL - Check SQL Agent Status\Execute SQL Task - Query Target Server for SQL Agent Status`  
**Connection:** master - SQL Agent (AVeryLongServenameJustToIncreaseMetaData/master)  

```sql
select status_desc as SQLAgentServiceStatus 
FROM   sys.dm_server_services dss
WHERE  dss.[servicename] LIKE N'SQL Server Agent (%';

```

### Execute SQL Task - Wait X Seconds

**Path:** `Package\Sequence Container  - Start SQL Agent Service on Eligible Servers\FEL - Start SQL Agent Service\Execute SQL Task - Wait X Seconds`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
WAITFOR DELAY '0:00:10'
```

### Execute SQL Task - Wait for 10 Seconds - Testing Only

**Path:** `Package\Sequence Container  - Validate Service Is Now Running and Load SQL Agent Start Eligibility\Execute SQL Task - Wait for 10 Seconds - Testing Only`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
WAITFOR DELAY '0:00:10'
```

### Execute SQL Task  - Load Target Server Names

**Path:** `Package\Sequence Container  - Validate Service Is Now Running and Load SQL Agent Start Eligibility\Sequence Container - Get Server Status Post Restart\Execute SQL Task  - Load Target Server Names`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select distinct ServerName
from SqlServerStatusCheckControl
order by 1

```

### Execute SQL Task - Trucate Stage

**Path:** `Package\Sequence Container  - Validate Service Is Now Running and Load SQL Agent Start Eligibility\Sequence Container - Get Server Status Post Restart\Execute SQL Task - Trucate Stage`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table [SqlServerStatusCheck]
```

### Execute SQL Task - Query Target Server

**Path:** `Package\Sequence Container  - Validate Service Is Now Running and Load SQL Agent Start Eligibility\Sequence Container - Get Server Status Post Restart\FEL - Query Target Server - Post Restart\Execute SQL Task - Query Target Server`  
**Connection:** master - PostRestart (AVeryLongServenameJustToIncreaseMetaData/master)  

```sql
select cast (@@SERVERNAME as varchar) as ReturnedServerName 
```

### Execute SQL Task - Load Servers Now Online

**Path:** `Package\Sequence Container  - Validate Service Is Now Running and Load SQL Agent Start Eligibility\Sequence Container - Load SQL Agent Start Eligibility\Execute SQL Task - Load Servers Now Online`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select distinct ServerName
from [Reporting].[SqlServerStatusCheck]
--where SQLServerStatus = 'Offline' 
where SQLServerStatusAfterStartAttempt = 'Online'
order by 1

```

### Execute SQL Task - Query Target Server for SQL Agent Elig

**Path:** `Package\Sequence Container  - Validate Service Is Now Running and Load SQL Agent Start Eligibility\Sequence Container - Load SQL Agent Start Eligibility\FEL - Load SQL Agent Start Eligibility\Execute SQL Task - Query Target Server for SQL Agent Elig`  
**Connection:** master - NowOnline (AVeryLongServenameJustToIncreaseMetaData/master)  

```sql
select case when startup_type_desc = 'Automatic' Then 'Yes '
Else 'No' end as SqlAgentEligibility
FROM   sys.dm_server_services dss
WHERE  dss.[servicename] LIKE N'SQL Server Agent (%';

```

### Execute SQL Task  - Load Target Server Names

**Path:** `Package\Sequence Container - Get Server Status\Execute SQL Task  - Load Target Server Names`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select distinct ServerName
from SqlServerStatusCheckControl
order by 1

```

### Execute SQL Task - Truncate Stage

**Path:** `Package\Sequence Container - Get Server Status\Execute SQL Task - Truncate Stage`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table [SqlServerStatusCheck]
truncate table [SqlServerStatusCheckControl]
```

### Execute SQL Task - Query Target Server

**Path:** `Package\Sequence Container - Get Server Status\FEL - Query Target Server\Execute SQL Task - Query Target Server`  
**Connection:** master (AVeryLongServenameJustToIncreaseMetaData/master)  

```sql
select cast (@@SERVERNAME as varchar) as ReturnedServerName 
```

### Check Hour - Only Send at 6, 12, 18 Hours

**Path:** `Package\Sequence Container - Send Emails\Check Hour - Only Send at 6, 12, 18 Hours`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select case when datepart(hh, GETDATE()) in (6,12,18)
	then 'Send'
	else 'DoNotSend'
	end as SendEmail

```

### Offline Row Count Check After Restart

**Path:** `Package\Sequence Container - Send Emails\Offline Row Count Check After Restart`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select count (*) ServersOfflineCountAfterRestart
from reporting.SqlServerStatusCheck 
where SQLServerStatusAfterStartAttempt = 'Offline'
order by 1

```

### Online Row Count  Check After Restart

**Path:** `Package\Sequence Container - Send Emails\Online Row Count  Check After Restart`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select count (*) ServersOnlineCountAfterRestart
from reporting.SqlServerStatusCheck 
where SQLServerStatusAfterStartAttempt  = 'Online'					  
and SQLServerStatus = 'Offline'
order by 1

```

### Execute SQL Task - SEnd No Problem Email

**Path:** `Package\Sequence Container - Send Emails\Sequence Container - Send Email Action Taken\Execute SQL Task - SEnd No Problem Email`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
declare @text nvarchar(max)

	set @text = 
		'<font face =arial size = 2><B>SQL Server Service Restart Report</B><br><br></font>' +
			'<table border="1">' +
				'<tr><th><font face =arial size = 2>ServerName</font></th>' +
					'<th><font face =arial size = 2>SQLServerStatus</font></th>' +
					'<th><font face =arial size = 2>SQLServerStatusAfterStartAttempt</font></th>' +
					'<th><font face =arial size = 2>SQLServerAgentStartEligible</font></th>' +
					'<th><font face =arial size = 2>SQLServerAgentStatus</font></th>' +
		'<font face =arial size = 2>' +
			CAST ( ( SELECT td = ServerName,'',
							td = SQLServerStatus, '',
							td = SQLServerStatusAfterStartAttempt, '',
							td = SQLServerAgentStartEligible, '',
							td = SQLServerAgentStatus, ''
					  from reporting.SqlServerStatusCheck 
					  where SQLServerStatusAfterStartAttempt  = 'Online'					  
					  and SQLServerStatus = 'Offline'
					  order by ServerName
					  FOR XML PATH('tr'), TYPE 
					) AS NVARCHAR(MAX) ) +
			'</font></table></font></p></p>
			<br>
			<font face =arial size = 1><B>This report was run from SSIS Package SQLServerServiceCheck </B></font>
			<br>
			<br>
		<font face =arial size = 1><i>The information in this message may be privileged, â€œconfidentialâ€ and protected from disclosure and/or intended only for the addressee(s) named above.  If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, please notify us immediately by replying to the message and deleting it from your computer.  Thank you beary much.</i></font>'

		exec msdb.dbo.sp_send_dbmail
		@profile_name = 'biadmin',
		@recipients = 'biadmin@buildabear.com',
		@body = @text,
		@subject = 'SQL Server Status Check - No Problem - SQL Server is Running After A Restart Command',
		@body_format = 'HTML'

```

### Execute SQL Task - Send No Problem Email

**Path:** `Package\Sequence Container - Send Emails\Sequence Container - Send Email No Action\Execute SQL Task - Send No Problem Email`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
declare @text nvarchar(max)

	set @text = 
		'<font face =arial size = 2><B>SQL Server Service Report</B><br><br></font>' +
			'<table border="1">' +
				'<tr><th><font face =arial size = 2>ServerName</font></th>' +
					'<th><font face =arial size = 2>SQLServerStatus</font></th>' +
					--'<th><font face =arial size = 2>SQLServerStatusAfterStartAttempt</font></th>' +
					--'<th><font face =arial size = 2>SQLServerAgentStartEligible</font></th>' +
					'<th><font face =arial size = 2>SQLServerAgentStatus</font></th>' +
		'<font face =arial size = 2>' +
			CAST ( ( SELECT td = ServerName,'',
							td = SQLServerStatus, '',
							--td = SQLServerStatusAfterStartAttempt, '',
							--td = SQLServerAgentStartEligible, '',
							td = isnull(SQLServerAgentStatus,'Not Eligible'), ''
					  from reporting.SqlServerStatusCheck 
					  where SQLServerStatusAfterStartAttempt  = 'Online'					  
					  and SQLServerStatus = 'Online'
					  order by ServerName
					  FOR XML PATH('tr'), TYPE 
					) AS NVARCHAR(MAX) ) +
			'</font></table></font></p></p>
			<br>
			<font face =arial size = 1><B>This report was run from SSIS Package SQLServerServiceCheck </B></font>
			<br>
			<br>
		<font face =arial size = 1><i>The information in this message may be privileged, â€œconfidentialâ€ and protected from disclosure and/or intended only for the addressee(s) named above.  If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, please notify us immediately by replying to the message and deleting it from your computer.  Thank you beary much.</i></font>'

		exec msdb.dbo.sp_send_dbmail
		@profile_name = 'biadmin',
		@recipients = 'biadmin@buildabear.com',
		@body = @text,
		@subject = 'SQL Server Status Check - No Problem - SQL Server is Running',
		@body_format = 'HTML'

```

### Execute SQL Task - Send Problem Email

**Path:** `Package\Sequence Container - Send Emails\Sequence Container - Send Problem Email\Execute SQL Task - Send Problem Email`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
declare @text nvarchar(max)

	set @text = 
		'<font face =arial size = 2><B>SQL Server Service Restart Report</B><br><br></font>' +
			'<table border="1">' +
				'<tr><th><font face =arial size = 2>ServerName</font></th>' +
					'<th><font face =arial size = 2>SQLServerStatus</font></th>' +
					'<th><font face =arial size = 2>SQLServerStatusAfterStartAttempt</font></th>' +
					--'<th><font face =arial size = 2>SQLServerAgentStartEligible</font></th>' +
					--'<th><font face =arial size = 2>SQLServerAgentStatusAfterStartAttempt</font></th>' +
		'<font face =arial size = 2>' +
			CAST ( ( SELECT td = ServerName,'',
							td = SQLServerStatus, '',
							td = SQLServerStatusAfterStartAttempt, ''
							--,td = SQLServerAgentStartEligible, ''
							--,td = SQLServerAgentStatusAfterStartAttempt, ''
					  from reporting.SqlServerStatusCheck 
					  where SQLServerStatusAfterStartAttempt  = 'Offline'					  
					  --and HasError='NO' 
					  order by ServerName
					  FOR XML PATH('tr'), TYPE 
					) AS NVARCHAR(MAX) ) +
			'</font></table></font></p></p>
			<br>
			<font face =arial size = 1><B>This report was run from SSIS Package SQLServerServiceCheck </B></font>
			<br>
			<br>
		<font face =arial size = 1><i>The information in this message may be privileged, â€œconfidentialâ€ and protected from disclosure and/or intended only for the addressee(s) named above.  If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, please notify us immediately by replying to the message and deleting it from your computer.  Thank you beary much.</i></font>'

		exec msdb.dbo.sp_send_dbmail
		@profile_name = 'biadmin',
		@recipients = 'biadmin@buildabear.com',
		@body = @text,
		@subject = 'SQL Server Status Check - PROBLEM - SQL Server(s) Offline After Attempted SQL Service Restart',
		@body_format = 'HTML'

```

### Execute SQL Task - Load Offline Server Names

**Path:** `Package\Sequence Container - Start SQL on Server\Execute SQL Task - Load Offline Server Names`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select distinct sc.ServerName
from SqlServerStatusCheck sc
left join SqlServerStatusCheckControl scc on sc.ServerName=scc.Servername
where scc.ServiceStartEligible = 'Yes'
and sc.SQLServerStatus = 'Offline'
order by 1

```

### Execute SQL Task - Truncate Reporting Table

**Path:** `Package\Sequence Container - Start SQL on Server\Execute SQL Task - Truncate Reporting Table`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table [Reporting].[SqlServerStatusCheck]
```

### Execute SQL Task - Wait for 10 Seconds  - 1

**Path:** `Package\Sequence Container - Start SQL on Server\Foreach Loop Container - Issue Start Command\Execute SQL Task - Wait for 10 Seconds  - 1`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
WAITFOR DELAY '0:00:10'
```

### Execute SQL Task - Wait for 10 Seconds - 2

**Path:** `Package\Sequence Container - Start SQL on Server\Foreach Loop Container - Issue Start Command\Execute SQL Task - Wait for 10 Seconds - 2`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
WAITFOR DELAY '0:00:10'
```

### Execute SQL Task - Wait for 10 Seconds - 3

**Path:** `Package\Sequence Container - Start SQL on Server\Foreach Loop Container - Issue Start Command\Execute SQL Task - Wait for 10 Seconds - 3`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
WAITFOR DELAY '0:00:10'
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Source |  | OLEDBSource | Data Flow Task - Load SQL Agent Status | IntegrationStaging | SqlCommand |
| OLE DB Source |  | OLEDBSource | Data Flow Task - Reload SqlServerStatusCheck | IntegrationStaging | SqlCommand |
| OLE DB Source - Reporting Table |  | OLEDBSource | Data Flow Task - Load Curr Status | IntegrationStaging | SqlCommand |
| OLE DB Source |  | OLEDBSource | Data Flow Task - Load SQL Agent Elig Status | IntegrationStaging | SqlCommand |
| OLE DB Source |  | OLEDBSource | Data Flow Task - Load Target Server Control Table | IntegrationStaging | SqlCommand |
| OLE DB Source |  | OLEDBSource | Data Flow Task - Load SqlServerStatusCheck | IntegrationStaging | SqlCommand |
| OLE DB Source |  | OLEDBSource | Data Flow Task - Load Server Status to Reporting Table | IntegrationStaging | SqlCommand |

#### OLE DB Source — SqlCommand

```sql
select getdate() as DateCapture
```

#### OLE DB Source - Reporting Table — SqlCommand

```sql
select ServerName, 
SQLServerStatus
from [Reporting].[SqlServerStatusCheck]
```

#### OLE DB Source — SqlCommand

```sql
select cast (	'stl-sql-p-02'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION 
select cast (	'stl-sql-p-03'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION 
select cast (	'papamart'	 as nvarchar)	as ServerName 	, cast ('No' as nvarchar) as ServiceStartEligible	UNION
select cast (	'stl-ssis-p-01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION
select cast (	'kermode'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION
select cast (	'stl-sql-p-04\sql2008r2'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION
select cast (	'stl-sql-p-04'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION
select cast (	'kodiak'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION
select cast (	'BEDROCKDB01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION--CASE SENSITIVE
select cast (	'bedrockdb02'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION
--select cast (	'stl-crmdb-p-01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION -- Remarked out on 9/30/2024 due to Decomission of Server
select cast (	'stl-plmdb-p-01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION
select cast (	'stl-sql-p-01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION -- THIS IS SAME as  as PLMDB01
--select cast (	'txtdb01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION -- Remarked out on 2/18/2025
--select cast (	'LAWSONDB01V'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION --CASE SENSITIVE now Decommisioned 
--select cast (	'spdb10'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION -- Removed on 3/12/2024 due to Decommision of Server 
--select cast (	'posdbs'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION -- FYI  Routine connectivty issues with this server
--select cast (	'coredb01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION -- Remarked out on 2/18/2025
--select cast (	'coredb02'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION
--select cast (	'BEARWEBDB\SQL2008'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION -- Remarked out on 11/22/2022
select cast (	'clb-sql-p-01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION
--select cast (	'labordb01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION -- Decommisioned 
select cast (	'STL-AVALDB-P-01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION 
select cast (	'esdmdb01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	UNION 
select cast (	'pipeapp01'	 as nvarchar)	as ServerName 	, cast ('Yes' as nvarchar) as ServiceStartEligible	 UNION 
select cast('stl-ssis-p-02' as nvarchar) ServerName, cast ('Yes' as nvarchar) ServiceStartEligible -- For Testing SSIS
--union select cast('stl-sql-t-01' as nvarchar) ServerName, cast ('Yes' as nvarchar) ServiceStartEligible -- For Testing SSIS
order by 1
```

#### OLE DB Source — SqlCommand

```sql
select sc.ServerName, 
sc.SQLServerStatus, 
scc.ServiceStartEligible
from [dbo].[SqlServerStatusCheck] sc
left join SqlServerStatusCheckControl scc on sc.ServerName=scc.Servername
--where SQLServerStatus = 'Offline'
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Destination |  | OLEDBDestination | Data Flow Task - Reload SqlServerStatusCheck | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Data Flow Task - Load Target Server Control Table | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Data Flow Task - Load SqlServerStatusCheck | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Data Flow Task - Load Server Status to Reporting Table | IntegrationStaging |  |
