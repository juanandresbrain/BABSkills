# SSIS Package: ManageD36WaveMessages

**Project:** WebOrderProcessing  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| Azure Service Bus Connection Manager | Azure Service Bus (KingswaySoft) |  |  |  |
| HTTP Connection Manager | HTTP (KingswaySoft) |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| ManageD36WaveMessages | Package |
| Sequence Container | SEQUENCE |
| Data Flow Task | Pipeline |
| DFT - Import new waved messages | Pipeline |
| DFT - Process new waved messages | Pipeline |
| DFT - Process new waves | Pipeline |
| SQL - Set MessageTypeId | ExecuteSQLTask |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- SQL - Set MessageTypeId [ExecuteSQLTask]
- Sequence Container [SEQUENCE]
  - DFT - Import new waved messages [Pipeline]
  - DFT - Process new waved messages [Pipeline]
  - DFT - Process new waves [Pipeline]
  - Data Flow Task [Pipeline]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Sequence_Container["Sequence Container"]
    n_Package_Sequence_Container_Data_Flow_Task["Data Flow Task"]
    n_Package_Sequence_Container_DFT___Import_new_waved_messages["DFT - Import new waved messages"]
    n_Package_Sequence_Container_DFT___Process_new_waved_messages["DFT - Process new waved messages"]
    n_Package_Sequence_Container_DFT___Process_new_waves["DFT - Process new waves"]
    n_Package_SQL___Set_MessageTypeId["SQL - Set MessageTypeId"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
    n_Package_Sequence_Container_DFT___Process_new_waved_messages --> n_Package_Sequence_Container_DFT___Process_new_waves
    n_Package_Sequence_Container_DFT___Process_new_waves --> n_Package_Sequence_Container_Data_Flow_Task
    n_Package_Sequence_Container_DFT___Import_new_waved_messages --> n_Package_Sequence_Container_DFT___Process_new_waved_messages
    n_Package_SQL___Set_MessageTypeId --> n_Package_Sequence_Container
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
| User | MessageTypeId | No |
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
20222248383010
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
2/24/2022
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
2022-2-24
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
2/24/2022
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
2022-2-24
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
2/23/2022
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
2022-2-23
```

## Execute SQL Tasks

### SQL - Set MessageTypeId

**Path:** `Package\SQL - Set MessageTypeId`  
**Connection:** {744FE313-1064-4E79-9385-E22229882EC8}  

```sql
SELECT [MessageTypeId]
FROM [IntegrationStaging].[WMS].[WMServiceBusMessageType]
  WHERE [Description] = 'outboundso-wave'
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Source |  | OLEDBSource | Data Flow Task | {744FE313-1064-4E79-9385-E22229882EC8}:external | SqlCommand |
| OLE DB Source 1 |  | OLEDBSource | Data Flow Task | {744FE313-1064-4E79-9385-E22229882EC8}:external |  |
| OLE DB Source |  | OLEDBSource | DFT - Process new waved messages | {744FE313-1064-4E79-9385-E22229882EC8}:external | SqlCommand |
| OLE DB Source |  | OLEDBSource | DFT - Process new waves | {744FE313-1064-4E79-9385-E22229882EC8}:external | SqlCommand |

#### OLE DB Source — SqlCommand

```sql
SELECT *
FROM [IntegrationStaging].[WMS].[eCommWaveStatus]
WHERE isWaved = 0
```

#### OLE DB Source — SqlCommand

```sql
SELECT [ServiceBusMessageId]
      ,[MessageId]
      ,[Message]
      ,[Sequence]
      ,[MessageTypeId]
      ,[EnqueuedTimeUTC]
  FROM [IntegrationStaging].[WMS].[WMServiceBusMessage] WITH(NOLOCK)
  WHERE ServiceBusMessageId IN (SELECT MAX(ServiceBusMessageID) FROM [IntegrationStaging].[WMS].[WMServiceBusMessage] WITH(NOLOCK) WHERE MessageTypeId = ? 
--AND EnqueuedTimeUTC BETWEEN '2020-09-11 00:00:00' AND '2020-09-12 00:00:00'
AND DATEDIFF(MINUTE, EnqueuedTimeUTC, GETUTCDATE()) < ? 
GROUP BY MessageId)
```

#### OLE DB Source — SqlCommand

```sql
SELECT v.[WaveId]
FROM [IntegrationStaging].[WMS].[vwSalesOrderStatusUpdateWaved] v
LEFT JOIN [IntegrationStaging].[WMS].[eCommWaveStatus] e WITH(NOLOCK) ON v.WaveId = e.WaveID
WHERE e.WaveId IS NULL AND v.WaveId IS NOT NULL
GROUP BY v.WaveId
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Destination |  | OLEDBDestination | DFT - Import new waved messages | {744FE313-1064-4E79-9385-E22229882EC8}:external |  |
| OLE DB Destination |  | OLEDBDestination | DFT - Process new waved messages | {744FE313-1064-4E79-9385-E22229882EC8}:external |  |
| OLE DB Destination 1 |  | OLEDBDestination | DFT - Process new waved messages | {744FE313-1064-4E79-9385-E22229882EC8}:external |  |
| OLE DB Destination |  | OLEDBDestination | DFT - Process new waves | {744FE313-1064-4E79-9385-E22229882EC8}:external |  |
