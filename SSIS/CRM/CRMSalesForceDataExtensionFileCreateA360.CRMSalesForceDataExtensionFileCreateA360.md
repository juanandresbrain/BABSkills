# SSIS Package: CRMSalesForceDataExtensionFileCreateA360

**Project:** CRMSalesForceDataExtensionFileCreateA360  
**Folder:** CRM  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        12M_conn(["12M [CACHE]"])
        18M_conn(["18M [CACHE]"])
        1M_conn(["1M [CACHE]"])
        24M_conn(["24M [CACHE]"])
        3M_conn(["3M [CACHE]"])
        6M_conn(["6M [CACHE]"])
        ADLS_raw_conn(["ADLS raw [Azure Data Lake Storage (KingswaySoft)]"])
        archive_conn(["archive [FILE]"])
        birthday_export_csv_conn(["birthday_export.csv [FILE]"])
        cDim_conn(["cDim [CACHE]"])
        CRM_conn(["CRM [OLEDB]"])
        delta_conn(["delta [EXCEL]"])
        DW_conn(["DW [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        Flat_File_Connection_Manager_conn(["Flat File Connection Manager [FLATFILE]"])
        SMTP_conn(["SMTP [SMTP]"])
        STL_SSIS_P_01_IntegrationStaging_conn(["STL-SSIS-P-01.IntegrationStaging [OLEDB]"])
    end
    subgraph ControlFlow
        CRMSalesForceDataExtensionFileCreateA360_task["CRMSalesForceDataExtensionFileCreateA360"]
        discounts_task["discounts"]
        CRMSalesForceDataExtensionFileCreateA360_task --> discounts_task
        insert_task["insert"]
        discounts_task --> insert_task
        output_task["output"]
        insert_task --> output_task
        remove_any_nulls_task["remove any nulls"]
        output_task --> remove_any_nulls_task
        truncate_task["truncate"]
        remove_any_nulls_task --> truncate_task
        products_task["products"]
        truncate_task --> products_task
        Data_Flow_Task_task[/"Data Flow Task"/]
        products_task --> Data_Flow_Task_task
        output_task["output"]
        Data_Flow_Task_task --> output_task
        truncate_task["truncate"]
        output_task --> truncate_task
        Sequence_Container_task["Sequence Container"]
        truncate_task --> Sequence_Container_task
        ADLS_detail_task[/"ADLS detail"/]
        Sequence_Container_task --> ADLS_detail_task
        ADLS_discounts_task[/"ADLS discounts"/]
        ADLS_detail_task --> ADLS_discounts_task
        ADLS_header_task[/"ADLS header"/]
        ADLS_discounts_task --> ADLS_header_task
        ADLS_products_task[/"ADLS products"/]
        ADLS_header_task --> ADLS_products_task
        ADLS_store_task[/"ADLS store"/]
        ADLS_products_task --> ADLS_store_task
        stores_task["stores"]
        ADLS_store_task --> stores_task
        output_task["output"]
        stores_task --> output_task
        transaction_detail_task["transaction detail"]
        output_task --> transaction_detail_task
        insert_task["insert"]
        transaction_detail_task --> insert_task
        output_task["output"]
        insert_task --> output_task
        truncate_task["truncate"]
        output_task --> truncate_task
        transaction_header_task["transaction header"]
        truncate_task --> transaction_header_task
        insert_task["insert"]
        transaction_header_task --> insert_task
        output_task["output"]
        insert_task --> output_task
        truncate_task["truncate"]
        output_task --> truncate_task
        Send_Mail_Task_task["Send Mail Task"]
        truncate_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| 12M | CACHE |
| 18M | CACHE |
| 1M | CACHE |
| 24M | CACHE |
| 3M | CACHE |
| 6M | CACHE |
| ADLS raw | Azure Data Lake Storage (KingswaySoft) |
| archive | FILE |
| birthday_export.csv | FILE |
| cDim | CACHE |
| CRM | OLEDB |
| delta | EXCEL |
| DW | OLEDB |
| DWStaging | OLEDB |
| Flat File Connection Manager | FLATFILE |
| SMTP | SMTP |
| STL-SSIS-P-01.IntegrationStaging | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| CRMSalesForceDataExtensionFileCreateA360 | Microsoft.Package |
| discounts | STOCK:SEQUENCE |
| insert | Microsoft.ExecuteSQLTask |
| output | Microsoft.ExecuteSQLTask |
| remove any nulls | Microsoft.ExecuteSQLTask |
| truncate | Microsoft.ExecuteSQLTask |
| products | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| output | Microsoft.ExecuteSQLTask |
| truncate | Microsoft.ExecuteSQLTask |
| Sequence Container | STOCK:SEQUENCE |
| ADLS detail | Microsoft.Pipeline |
| ADLS discounts | Microsoft.Pipeline |
| ADLS header | Microsoft.Pipeline |
| ADLS products | Microsoft.Pipeline |
| ADLS store | Microsoft.Pipeline |
| stores | STOCK:SEQUENCE |
| output | Microsoft.ExecuteSQLTask |
| transaction detail | STOCK:SEQUENCE |
| insert | Microsoft.ExecuteSQLTask |
| output | Microsoft.ExecuteSQLTask |
| truncate | Microsoft.ExecuteSQLTask |
| transaction header | STOCK:SEQUENCE |
| insert | Microsoft.ExecuteSQLTask |
| output | Microsoft.ExecuteSQLTask |
| truncate | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | with  products as ( select p.* from [Azure].[vwPOSOutbound_Products] p ), chain as ( select style, max(Chain) as consumerGroup from  [Azure].[vwProducts]  group by style  ) select products.*, chain.consumerGroup from products join chain on products.ProductNumber = chain.style |

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [dbo].[A360_product_dim] |

