# SSIS Package: WMS_CycleCountETL

**Project:** WMS_CycleCountETL  
**Folder:** WMS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Cache_OrderLine_conn(["Cache OrderLine [CACHE]"])
        cycleCount_txt_conn(["cycleCount.txt [FILE]"])
        cycleCount_xlsx_conn(["cycleCount.xlsx [FILE]"])
        Dynamics_AX_Connection_Manager_conn(["Dynamics AX Connection Manager [DynamicsAX]"])
        Excel_Connection_Manager_conn(["Excel Connection Manager [EXCEL]"])
        Flat_File_Connection_Manager_conn(["Flat File Connection Manager [FLATFILE]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        papamart_dw_conn(["papamart.dw [OLEDB]"])
        papamart_DWStaging_conn(["papamart.DWStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        WMS_CycleCountETL_task["WMS_CycleCountETL"]
        Data_Flow_to_excel_task[/"Data Flow to excel"/]
        WMS_CycleCountETL_task --> Data_Flow_to_excel_task
        Data_Flow_to_txt_task[/"Data Flow to txt"/]
        Data_Flow_to_excel_task --> Data_Flow_to_txt_task
        SEQ___prod_filtered_task["SEQ - prod filtered"]
        Data_Flow_to_txt_task --> SEQ___prod_filtered_task
        Data_Flow_to_stage_task[/"Data Flow to stage"/]
        SEQ___prod_filtered_task --> Data_Flow_to_stage_task
        merge_stage_to_prod_task["merge stage to prod"]
        Data_Flow_to_stage_task --> merge_stage_to_prod_task
        truncate_stage_task["truncate stage"]
        merge_stage_to_prod_task --> truncate_stage_task
        SEQ___prod_unfiltered_task["SEQ - prod unfiltered"]
        truncate_stage_task --> SEQ___prod_unfiltered_task
        Data_Flow_Task_task[/"Data Flow Task"/]
        SEQ___prod_unfiltered_task --> Data_Flow_Task_task
        Data_Flow_to_stage_task[/"Data Flow to stage"/]
        Data_Flow_Task_task --> Data_Flow_to_stage_task
        merge_stage_to_prod_task["merge stage to prod"]
        Data_Flow_to_stage_task --> merge_stage_to_prod_task
        truncate_stage_task["truncate stage"]
        merge_stage_to_prod_task --> truncate_stage_task
        Send_Mail_Task_task["Send Mail Task"]
        truncate_stage_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| Cache OrderLine | CACHE |
| cycleCount.txt | FILE |
| cycleCount.xlsx | FILE |
| Dynamics AX Connection Manager | DynamicsAX |
| Excel Connection Manager | EXCEL |
| Flat File Connection Manager | FLATFILE |
| IntegrationStaging | OLEDB |
| papamart.dw | OLEDB |
| papamart.DWStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| WMS_CycleCountETL | Microsoft.Package |
| Data Flow to excel | Microsoft.Pipeline |
| Data Flow to txt | Microsoft.Pipeline |
| SEQ - prod filtered | STOCK:SEQUENCE |
| Data Flow to stage | Microsoft.Pipeline |
| merge stage to prod | Microsoft.ExecuteSQLTask |
| truncate stage | Microsoft.ExecuteSQLTask |
| SEQ - prod unfiltered | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| Data Flow to stage | Microsoft.Pipeline |
| merge stage to prod | Microsoft.ExecuteSQLTask |
| truncate stage | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_No OLE DB data flow sources detected._

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [dbo].[WMS_cycleCount_stage] |
|  | [dbo].[WMS_cycleCount_stage] |
|  | [dbo].[WMS_cycleCount_stage] |

