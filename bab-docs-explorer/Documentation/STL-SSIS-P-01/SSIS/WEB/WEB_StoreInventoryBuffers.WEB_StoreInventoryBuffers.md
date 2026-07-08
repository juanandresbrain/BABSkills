# SSIS Package: WEB_StoreInventoryBuffers

**Project:** WEB_StoreInventoryBuffers  
**Folder:** WEB  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| BuffersCSV | FLATFILE |  |  |  |
| IntegrationStaging | OLEDB | stl-ssis-p-01 | IntegrationStaging | Data Source=stl-ssis-p-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| SMTP | SMTP |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| WEB_StoreInventoryBuffers | Package |
| SEQ - Stage Buffer Data | SEQUENCE |
| Foreach Loop Container | FOREACHLOOP |
| DataFlow - Load Buffers | Pipeline |
| Merge StoreInventoryBuffers | ExecuteSQLTask |
| Truncate Stage | ExecuteSQLTask |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- SEQ - Stage Buffer Data [SEQUENCE]
  - Foreach Loop Container [FOREACHLOOP]
    - DataFlow - Load Buffers [Pipeline]
    - Merge StoreInventoryBuffers [ExecuteSQLTask]
  - Truncate Stage [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_SEQ___Stage_Buffer_Data["SEQ - Stage Buffer Data"]
    n_Package_SEQ___Stage_Buffer_Data_Foreach_Loop_Container["Foreach Loop Container"]
    n_Package_SEQ___Stage_Buffer_Data_Foreach_Loop_Container_DataFlow___Load_Buffers["DataFlow - Load Buffers"]
    n_Package_SEQ___Stage_Buffer_Data_Foreach_Loop_Container_Merge_StoreInventoryBuffers["Merge StoreInventoryBuffers"]
    n_Package_SEQ___Stage_Buffer_Data_Truncate_Stage["Truncate Stage"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
    n_Package_SEQ___Stage_Buffer_Data_Foreach_Loop_Container_DataFlow___Load_Buffers --> n_Package_SEQ___Stage_Buffer_Data_Foreach_Loop_Container_Merge_StoreInventoryBuffers
    n_Package_SEQ___Stage_Buffer_Data_Truncate_Stage --> n_Package_SEQ___Stage_Buffer_Data_Foreach_Loop_Container
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | BuffersFileForLoop | No |
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
202042813528923
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
4/28/2020
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
2020-4-28
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
4/28/2020
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
2020-4-28
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
4/27/2020
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
2020-4-27
```

## Execute SQL Tasks

### Merge StoreInventoryBuffers

**Path:** `Package\SEQ - Stage Buffer Data\Foreach Loop Container\Merge StoreInventoryBuffers`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
exec WEB.spMergeStoreInventoryBuffers 
```

### Truncate Stage

**Path:** `Package\SEQ - Stage Buffer Data\Truncate Stage`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
TRUNCATE TABLE WEB.StoreInventoryBuffersStage
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| Buffers CSV |  | FlatFileSource | DataFlow - Load Buffers | BuffersCSV |  |

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| Web StoreInventoryBuffers |  | OLEDBDestination | DataFlow - Load Buffers | IntegrationStaging |  |
