# Job: zRetired_05_MetricFacts_WeeklyArchive

**Enabled:** No  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_05_MetricFacts_WeeklyArchive"]
    JOB --> S1["Step 1: spMetricFactsArchive [TSQL]"]
```

## Steps

### Step 1: spMetricFactsArchive
**Subsystem:** TSQL  

```sql
exec spMetricFactsArchive
```

