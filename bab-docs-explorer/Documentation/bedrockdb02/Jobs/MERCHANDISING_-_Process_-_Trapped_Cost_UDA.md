# Job: MERCHANDISING - Process - Trapped Cost UDA

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** creates UDA for trapped cost

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Trapped Cost UDA"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputTrappedCostUDA
MERCHANDISING - Process - UK Active Pick Update	Yes	Imports CSV file \\kermode\FileRepository\MERCHANDISING\UK_Distro\ActivePick\ActivePick.csv, which contains list of UK styles that are set to Active Pick at UK warehouse.
Job will compare to Merchandising system, update styles' Active Pick attribute to either Yes or No.	1	Generate Pipeline File	TSQL	exec spMerchandisingUpdateUKActivePickSkus
MERCHANDISING - Process - UK Active Pick Update	Yes	Imports CSV file \\kermode\FileRepository\MERCHANDISING\UK_Distro\ActivePick\ActivePick.csv, which contains list of UK styles that are set to Active Pick at UK warehouse.
Job will compare to Merchandising system, update styles' Active Pick attribute to either Yes or No.	2	Run Pipeline	TSQL	exec spMerchandisingExecutePipeline_16001_17000
```


