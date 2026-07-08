# SSIS Package: WMS_InventoryAdjustments

**Project:** WMS_InventoryAdjustments  
**Folder:** WMS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| Azure Service Bus | Azure Service Bus (KingswaySoft) |  |  |  |
| IntegrationStaging | OLEDB | STL-SSIS-P-01 | IntegrationStaging | Data Source=STL-SSIS-P-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| SMTP | SMTP |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| WMS_InventoryAdjustments | Package |
| Seq - Create Pipeline File | SEQUENCE |
| spPrintInventoryAdjustments | ExecuteSQLTask |
| Seq - Stage and Merge from Azure Service Bus | SEQUENCE |
| Data Flow - outboundinvadj-aptos | Pipeline |
| Merge InventoryAdjustments | ExecuteSQLTask |
| Truncate Stage | ExecuteSQLTask |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- Seq - Create Pipeline File [SEQUENCE]
  - spPrintInventoryAdjustments [ExecuteSQLTask]
- Seq - Stage and Merge from Azure Service Bus [SEQUENCE]
  - Data Flow - outboundinvadj-aptos [Pipeline]
  - Merge InventoryAdjustments [ExecuteSQLTask]
  - Truncate Stage [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Seq___Create_Pipeline_File["Seq - Create Pipeline File"]
    n_Package_Seq___Create_Pipeline_File_spPrintInventoryAdjustments["spPrintInventoryAdjustments"]
    n_Package_Seq___Stage_and_Merge_from_Azure_Service_Bus["Seq - Stage and Merge from Azure Service Bus"]
    n_Package_Seq___Stage_and_Merge_from_Azure_Service_Bus_Data_Flow___outboundinvadj_aptos["Data Flow - outboundinvadj-aptos"]
    n_Package_Seq___Stage_and_Merge_from_Azure_Service_Bus_Merge_InventoryAdjustments["Merge InventoryAdjustments"]
    n_Package_Seq___Stage_and_Merge_from_Azure_Service_Bus_Truncate_Stage["Truncate Stage"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
    n_Package_Seq___Stage_and_Merge_from_Azure_Service_Bus_Truncate_Stage --> n_Package_Seq___Stage_and_Merge_from_Azure_Service_Bus_Data_Flow___outboundinvadj_aptos
    n_Package_Seq___Stage_and_Merge_from_Azure_Service_Bus_Data_Flow___outboundinvadj_aptos --> n_Package_Seq___Stage_and_Merge_from_Azure_Service_Bus_Merge_InventoryAdjustments
    n_Package_Seq___Stage_and_Merge_from_Azure_Service_Bus --> n_Package_Seq___Create_Pipeline_File
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | DateTimeStamp | Yes |
| User | EndDate | Yes |
| User | EndDateAsDATE | Yes |
| User | GetDate | Yes |
| User | GetDateAsDATE | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |

### Expression-bound variable values

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
2020210125522517
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
2/10/2020
```

#### User::EndDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::EndDate])  + "-" + 
(DT_WSTR, 2) datepart("mm", @[User::EndDate])  + "-" + 
(DT_WSTR, 2) datepart("dd",  @[User::EndDate])
```

**Evaluated value:**

```sql
2020-2-10
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
2/10/2020
```

#### User::GetDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::GetDate])  + "-" + 
(DT_WSTR, 2) datepart("mm", @[User::GetDate])  + "-" + 
(DT_WSTR, 2) datepart("dd",  @[User::GetDate])
```

**Evaluated value:**

```sql
2020-2-10
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
2/9/2020
```

#### User::StartDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::StartDate])  + "-" + 
(DT_WSTR, 2) datepart("mm", @[User::StartDate])  + "-" + 
(DT_WSTR, 2) datepart("dd",  @[User::StartDate])
```

**Evaluated value:**

```sql
2020-2-9
```

## Execute SQL Tasks

### spPrintInventoryAdjustments

**Path:** `Package\Seq - Create Pipeline File\spPrintInventoryAdjustments`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

> ⚠️ `SqlStatementSource` is overridden at runtime by a property expression (shown below); the static SQL may not be what executes.

**Static SqlStatementSource:**

```sql
exec WMS.spPrintInventoryAdjustments '\\pipeapp01\Company01\Text File to IM Import Tables- Import Shrink Adj\'
```

**Property expression (runtime override):**

```sql
"exec WMS.spPrintInventoryAdjustments '" +  @[$Package::WMS_InventoryAdjustmentsFilePath] + "'"
```

### Merge InventoryAdjustments

**Path:** `Package\Seq - Stage and Merge from Azure Service Bus\Merge InventoryAdjustments`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
exec WMS.spMergeInventoryAdjustments
```

### Truncate Stage

**Path:** `Package\Seq - Stage and Merge from Azure Service Bus\Truncate Stage`  
**Connection:** IntegrationStaging (STL-SSIS-P-01/IntegrationStaging)  

```sql
TRUNCATE TABLE WMS.InventoryAdjustmentsStage
```

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| InventoryAdjustmentsStage |  | OLEDBDestination | Data Flow - outboundinvadj-aptos | IntegrationStaging |  |
