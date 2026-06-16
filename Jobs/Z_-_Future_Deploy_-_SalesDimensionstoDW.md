# Job: Z - Future Deploy - SalesDimensionstoDW

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Z - Future Deploy - SalesDimensionstoDW"]
    JOB --> SSIS___DW_SalesDimExtracts_LineObjectDim_1["Step 1: SSIS - DW_SalesDimExtracts_LineObjectDim [SSIS]"]`n    JOB --> SSIS___DW_SalesDimExtracts_TenderDim_2["Step 2: SSIS - DW_SalesDimExtracts_TenderDim [SSIS]"]`n    JOB --> SSIS___DW_SalesDimExtracts_CurrencyDim_3["Step 3: SSIS - DW_SalesDimExtracts_CurrencyDim [SSIS]"]`n    JOB --> SSIS___DW_SalesDimExtracts_ProductDim_4["Step 4: SSIS - DW_SalesDimExtracts_ProductDim [SSIS]"]`n    JOB --> SSIS___DW_SalesDimExtracts_StoreDim_5["Step 5: SSIS - DW_SalesDimExtracts_StoreDim [SSIS]"]`n    JOB --> SSIS___DW_SalesDimExtracts_LineObj_Store_Lookup_6["Step 6: SSIS - DW_SalesDimExtracts_LineObj_Store_Lookup [SSIS]"]`n    JOB --> Update_product_dim_ScorecardCategory_7["Step 7: Update product_dim ScorecardCategory [TSQL]"]`n    JOB --> SSIS___DW_SalesDimExtracts_AttributesDim_8["Step 8: SSIS - DW_SalesDimExtracts_AttributesDim [SSIS]"]`n    JOB --> SSIS___DW_SalesDimExtracts_SyncCompanyStoreComps_9["Step 9: SSIS - DW_SalesDimExtracts_SyncCompanyStoreComps [SSIS]"]`n    JOB --> Line_Action_Dim_10["Step 10: Line Action Dim [TSQL]"]`n    JOB --> CopyStoreDim_11["Step 11: CopyStoreDim [TSQL]"]`n    JOB --> Start_Job___Process_Cube_Dimensions_12["Step 12: Start Job - Process Cube Dimensions [TSQL]"]`n```

## Steps

### Step 1: SSIS - DW_SalesDimExtracts_LineObjectDim
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DW_SalesDimExtracts_LineObjectDim\DW_SalesDimExtracts_LineObjectDim.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10128 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: SSIS - DW_SalesDimExtracts_TenderDim
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DW_SalesDimExtracts_TenderDim\DW_SalesDimExtracts_TenderDim.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10134 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: SSIS - DW_SalesDimExtracts_CurrencyDim
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DW_SalesDimExtracts_CurrencyDim\DW_SalesDimExtracts_CurrencyDim.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10131 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: SSIS - DW_SalesDimExtracts_ProductDim
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DW_SalesDimExtracts_ProductDim\DW_SalesDimExtracts_ProductDim.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10129 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: SSIS - DW_SalesDimExtracts_StoreDim
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DW_SalesDimExtracts_StoreDim\DW_SalesDimExtracts_StoreDim.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10133 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 6: SSIS - DW_SalesDimExtracts_LineObj_Store_Lookup
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DW_SalesDimExtracts_LineObj_Store_Lookup\DW_SalesDimExtracts_LineObj_Store_Lookup.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10132 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 7: Update product_dim ScorecardCategory
**Subsystem:** TSQL  

```sql
EXEC papamart.dw.dbo.spDW_ProductDim_ScorecardCategoryUpdate
```

### Step 8: SSIS - DW_SalesDimExtracts_AttributesDim
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DW_SalesDimExtracts_AttributesDim\DW_SalesDimExtracts_AttributesDim.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10130 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 9: SSIS - DW_SalesDimExtracts_SyncCompanyStoreComps
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\DW_SalesDimExtracts_SyncCompanyStoreComps\DW_SalesDimExtracts_SyncCompanyStoreComps.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10135 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 10: Line Action Dim
**Subsystem:** TSQL  

```sql
exec Papamart.DW.dbo.spDW_MergeLineActionDim
```

### Step 11: CopyStoreDim
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-01].msdb.dbo.sp_start_job @job_name='DW_StoreDimETL--CopyStoreDimOnly'
```

### Step 12: Start Job - Process Cube Dimensions
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-01].msdb.dbo.sp_start_job @job_name='ProcessCubeDimensions'
```


