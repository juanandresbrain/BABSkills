# SSIS Package: AptosEStoDeckOMS

**Project:** WebOrderProcessing  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

_None detected._

## Control Flow Tasks

| Task | Type |
|---|---|
| AptosEStoDeckOMS | Package |
| Sequence Container | SEQUENCE |
| FLC - Loop through ES Orders Meta Data | FOREACHLOOP |
| Execute SQL Task | ExecuteSQLTask |
| SQL -  Log ES Order ID Exclusion (For Testing) | ExecuteSQLTask |
| SQL - Log Failure | ExecuteSQLTask |
| ST - Get EnterpriseSellingID | ScriptTask |
| ST - Load ES Order into OMS | ScriptTask |
| SQL - Get ES Order Exclusions (For Testing) | ExecuteSQLTask |
| SQL - Log Failure | ExecuteSQLTask |
| ST - Get ES Metadata | ScriptTask |
| Send Email onError | SendMailTask |

## Control Flow Outline

```text
- Send Email onError [SendMailTask]
- Sequence Container [SEQUENCE]
  - FLC - Loop through ES Orders Meta Data [FOREACHLOOP]
    - Execute SQL Task [ExecuteSQLTask]
    - SQL -  Log ES Order ID Exclusion (For Testing) [ExecuteSQLTask]
    - SQL - Log Failure [ExecuteSQLTask]
    - ST - Get EnterpriseSellingID [ScriptTask]
    - ST - Load ES Order into OMS [ScriptTask]
  - SQL - Get ES Order Exclusions (For Testing) [ExecuteSQLTask]
  - SQL - Log Failure [ExecuteSQLTask]
  - ST - Get ES Metadata [ScriptTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Sequence_Container["Sequence Container"]
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data["FLC - Loop through ES Orders Meta Data"]
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_Execute_SQL_Task["Execute SQL Task"]
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_SQL____Log_ES_Order_ID_Exclusion__For_Testing_["SQL -  Log ES Order ID Exclusion (For Testing)"]
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_SQL___Log_Failure["SQL - Log Failure"]
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_ST___Get_EnterpriseSellingID["ST - Get EnterpriseSellingID"]
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_ST___Load_ES_Order_into_OMS["ST - Load ES Order into OMS"]
    n_Package_Sequence_Container_SQL___Get_ES_Order_Exclusions__For_Testing_["SQL - Get ES Order Exclusions (For Testing)"]
    n_Package_Sequence_Container_SQL___Log_Failure["SQL - Log Failure"]
    n_Package_Sequence_Container_ST___Get_ES_Metadata["ST - Get ES Metadata"]
    n_Package_EventHandlers_OnError__Send_Email_onError["Send Email onError"]
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_ST___Load_ES_Order_into_OMS --> n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_SQL____Log_ES_Order_ID_Exclusion__For_Testing_
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_ST___Load_ES_Order_into_OMS --> n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_SQL___Log_Failure
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_ST___Get_EnterpriseSellingID --> n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_Execute_SQL_Task
    n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_Execute_SQL_Task --> n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data_ST___Load_ES_Order_into_OMS
    n_Package_Sequence_Container_ST___Get_ES_Metadata --> n_Package_Sequence_Container_FLC___Loop_through_ES_Orders_Meta_Data
    n_Package_Sequence_Container_SQL___Get_ES_Order_Exclusions__For_Testing_ --> n_Package_Sequence_Container_ST___Get_ES_Metadata
    n_Package_Sequence_Container_ST___Get_ES_Metadata --> n_Package_Sequence_Container_SQL___Log_Failure
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | AptosEnterpriseSellingAPIURL | No |
| User | DeckOrderManagementServiceAPIURL | No |
| User | ESCurrentEnterpriseSellingID | No |
| User | ESInboundOrderResponseCode | No |
| User | ESInboundOrderResponseMessage | No |
| User | ESOrderCriteria | No |
| User | ESOrderFullfillingOutledIDUK | No |
| User | ESOrderFullfillingOutledIDUS | No |
| User | ESOrderMetaData | No |
| User | ESOrderOverrideEmailAddress | No |
| User | ESOrderOverrideEmailAddressFlag | No |
| User | ESOrdersMetaData | No |
| User | GetMetaDataExceptionMessage | No |
| User | TestESOrderIDExclusions | No |
| User | TestMode | No |
| User | TestNewESOrderIDtoExclude | No |
| User | TestNumberOfOrdersToCreate | No |

## Execute SQL Tasks

### Execute SQL Task

**Path:** `Package\Sequence Container\FLC - Loop through ES Orders Meta Data\Execute SQL Task`  
**Connection:** {744FE313-1064-4E79-9385-E22229882EC8}  

```sql
EXEC ES.spMergeOMSReferenceNumberBridge ?
```

### SQL -  Log ES Order ID Exclusion (For Testing)

**Path:** `Package\Sequence Container\FLC - Loop through ES Orders Meta Data\SQL -  Log ES Order ID Exclusion (For Testing)`  
**Connection:** {744FE313-1064-4E79-9385-E22229882EC8}  

```sql
INSERT INTO ES.tmpESOrderIDsToExclude
                         (ESOrderID)
VALUES        (?)
```

### SQL - Log Failure

**Path:** `Package\Sequence Container\FLC - Loop through ES Orders Meta Data\SQL - Log Failure`  
**Connection:** {F1291F69-7277-411F-B6EC-AF91B8D3B89A}  

```sql
INSERT [dbo].[ServiceLoggingGeneralUsage] (
       [Message]
      ,[IsAnException]
      ,[ServiceID])
VALUES(?, 0, 5)
```

### SQL - Get ES Order Exclusions (For Testing)

**Path:** `Package\Sequence Container\SQL - Get ES Order Exclusions (For Testing)`  
**Connection:** {744FE313-1064-4E79-9385-E22229882EC8}  

```sql
SELECT [ESOrderID]
  FROM [ES].[tmpESOrderIDsToExclude]
```

### SQL - Log Failure

**Path:** `Package\Sequence Container\SQL - Log Failure`  
**Connection:** {F1291F69-7277-411F-B6EC-AF91B8D3B89A}  

```sql
INSERT [dbo].[ServiceLoggingGeneralUsage] (
       [Message]
      ,[IsAnException]
      ,[ServiceID])
VALUES(?, 1, 5)
```

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._
