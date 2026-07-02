# Job: MERCHANDISING - Process - Update CNY Style Vendors

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Run stored procedure spMerchandisingOutputUpdateCNYStyleVendor to create pipeline file, then run pipeline jobs to process.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Update CNY Style Vendors"]
    JOB --> Query_Me_01_and_Create__GO_Files_1["Step 1: Query Me_01 and Create .GO Files [TSQL]"]`n    JOB --> Run_Pipeline_Segments_16001_and_17000_2["Step 2: Run Pipeline Segments 16001 and 17000 [TSQL]"]`n```

## Steps

### Step 1: Query Me_01 and Create .GO Files
**Subsystem:** TSQL  

```sql
EXEC [dbo].[spMerchandisingOutputUpdateCNYStyleVendor]
```

### Step 2: Run Pipeline Segments 16001 and 17000
**Subsystem:** TSQL  

```sql
EXEC [dbo].[spMerchandisingExecutePipeline_16001_17000]
```


