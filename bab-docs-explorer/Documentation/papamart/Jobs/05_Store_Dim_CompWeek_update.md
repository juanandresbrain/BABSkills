# Job: 05_Store_Dim_CompWeek_update

**Enabled:** Yes  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["05_Store_Dim_CompWeek_update"]
    JOB --> S1["Step 1: spMetricStoreDimComp [TSQL]"]
```

## Steps

### Step 1: spMetricStoreDimComp
**Subsystem:** TSQL  

```sql
exec spMetricStoreDimComp
```

