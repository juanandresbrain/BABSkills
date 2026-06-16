# SSIS Package: HR_TerminationGroups

**Project:** HR_TerminationGroups  
**Folder:** HR  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Active_Directory_Connection_Manager_conn(["Active Directory Connection Manager [ActiveDirectory]"])
        DW_conn(["DW [OLEDB]"])
        EmployeesCSV_conn(["EmployeesCSV [FLATFILE]"])
        papamart_DWStaging_conn(["papamart.DWStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
        termedEmployeesGroupsFile_conn(["termedEmployeesGroupsFile [FLATFILE]"])
        termedEmployeesGroupsFile2_conn(["termedEmployeesGroupsFile2 [FLATFILE]"])
        termedEmployeesGroupsFile3_conn(["termedEmployeesGroupsFile3 [FLATFILE]"])
    end
    subgraph ControlFlow
        HR_TerminationGroups_task["HR_TerminationGroups"]
        termed_groups_file_for_SD_task["termed groups file for SD"]
        HR_TerminationGroups_task --> termed_groups_file_for_SD_task
        Foreach_Loop___group_file_task["Foreach Loop - group file"]
        termed_groups_file_for_SD_task --> Foreach_Loop___group_file_task
        2_second_pause_task["2 second pause"]
        Foreach_Loop___group_file_task --> 2_second_pause_task
        Data_Flow_Task_task[/"Data Flow Task"/]
        2_second_pause_task --> Data_Flow_Task_task
        Execute_SQL_Task_task["Execute SQL Task"]
        Data_Flow_Task_task --> Execute_SQL_Task_task
        Stage_Terminations_task["Stage Terminations"]
        Execute_SQL_Task_task --> Stage_Terminations_task
        Send_Mail_Task_task["Send Mail Task"]
        Stage_Terminations_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| Active Directory Connection Manager | ActiveDirectory |
| DW | OLEDB |
| EmployeesCSV | FLATFILE |
| papamart.DWStaging | OLEDB |
| SMTP | SMTP |
| termedEmployeesGroupsFile | FLATFILE |
| termedEmployeesGroupsFile2 | FLATFILE |
| termedEmployeesGroupsFile3 | FLATFILE |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| HR_TerminationGroups | Microsoft.Package |
| termed groups file for SD | STOCK:SEQUENCE |
| Foreach Loop - group file | STOCK:FOREACHLOOP |
| 2 second pause | STOCK:FORLOOP |
| Data Flow Task | Microsoft.Pipeline |
| Execute SQL Task | Microsoft.ExecuteSQLTask |
| Stage Terminations | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | DECLARE @s NVARCHAR(MAX)  set @s = (select MemberOf from [dbo].[ADattributes] where EmployeeID = ?);   select left(replace(Item,'CN=',''),charindex(',',replace(Item,'CN=',''),1)-1)  as groupsNames FROM dbo.SplitStrings_CTE     (@s, N';'); |

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

