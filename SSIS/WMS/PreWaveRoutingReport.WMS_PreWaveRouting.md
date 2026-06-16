# SSIS Package: WMS_PreWaveRouting

**Project:** PreWaveRoutingReport  
**Folder:** WMS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Dynamics_AX_Connection_Manager___Prod_conn(["Dynamics AX Connection Manager - Prod [DynamicsAX]"])
        Dynamics_AX_Connection_Manager___Test_1_conn(["Dynamics AX Connection Manager - Test 1 [DynamicsAX]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        WMS_PreWaveRouting_task["WMS_PreWaveRouting"]
        AX_Sandbox_task[/"AX Sandbox"/]
        WMS_PreWaveRouting_task --> AX_Sandbox_task
        Sequence_Container_task["Sequence Container"]
        AX_Sandbox_task --> Sequence_Container_task
        Get_Recent_TOs_and_SOs_without_HA_Data_task[/"Get Recent TOs and SOs without HA Data"/]
        Sequence_Container_task --> Get_Recent_TOs_and_SOs_without_HA_Data_task
        Summarize_and_Insert_to_Reporting_Table_task[/"Summarize and Insert to Reporting Table"/]
        Get_Recent_TOs_and_SOs_without_HA_Data_task --> Summarize_and_Insert_to_Reporting_Table_task
        Truncate_Staging_Tables_task["Truncate Staging Tables"]
        Summarize_and_Insert_to_Reporting_Table_task --> Truncate_Staging_Tables_task
        Union_SO_and_TO_tables_task[/"Union SO and TO tables"/]
        Truncate_Staging_Tables_task --> Union_SO_and_TO_tables_task
        Send_Mail_Task_task["Send Mail Task"]
        Union_SO_and_TO_tables_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| Dynamics AX Connection Manager - Prod | DynamicsAX |
| Dynamics AX Connection Manager - Test 1 | DynamicsAX |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| WMS_PreWaveRouting | Microsoft.Package |
| AX Sandbox | Microsoft.Pipeline |
| Sequence Container | STOCK:SEQUENCE |
| Get Recent TOs and SOs without HA Data | Microsoft.Pipeline |
| Summarize and Insert to Reporting Table | Microsoft.Pipeline |
| Truncate Staging Tables | Microsoft.ExecuteSQLTask |
| Union SO and TO tables | Microsoft.Pipeline |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | select distinct OrderNumber, warehouse from wms.CartonsSummaryToHA where warehouse in ('9980','8175') and left(OrderNumber,2) = 'TO' |
|  |  | select distinct OrderNumber, warehouse from wms.CartonsSummaryToHA where warehouse in ('9980','8175') and (left(OrderNumber,2) = 'SO' or left(OrderNumber,4) = '1700') |
|  |  | with uom_conv as ( select     ProductNumber,     BAG,BALE,BDL,BX,CS,IP,KT,LB,PK,PLT,RL,ROLL,[SET] from     (         select             ProductNumber,             FromUnitSymbol,             Factor as Qty         from wms.ItemsUOM         where Entity=1100         and ToUnitSymbol='ea'     ) as UOM PIVOT     (         sum(QTy)         for FromUnitSymbol in ([BAG],[BALE],[BDL],[BX],[CS],[ip],[KT],[ |

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [WMS].[TimC_AXSandbox] |
|  | [WMS].[TimC_AXSandbox_SalesOrder] |
|  | [WMS].[timc_axsandbox_hdr] |
|  | [WMS].[PreWaveSalesOrderStage] |
|  | [WMS].[PreWaveTransferOrderStage] |
|  | [WMS].[PreWaveRoutingReport] |
|  | [WMS].[PreWaveUnionSalesAndTransferOrdersSTage] |
|  | [WMS].[PreWaveTransferOrderStage] |
|  | [WMS].[PreWaveSalesOrderStage] |

