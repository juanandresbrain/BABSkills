# Job: MERCHANDISING - Process - Nightly Sync All Whse and Web UPDATE TEST

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** compares inventories between Merch and the warehouses, posts a shrink adjustment file for discrepancies, sends emails with summaries.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Nightly Sync All Whse and Web UPDATE TEST"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectWhseInventoryShrink
MERCHANDISING - Process - Nightly Sync Post Summary	Yes	Captures and emails a summary of Nightly Sync Postings.
Allows us to quickly reference to confirm whether Nightly Sync adjustments successfully posted to Merch	1	uno	TSQL	exec me_01.dbo.spMerchandisingNightlySyncPostSummary
MERCHANDISING - Process - Pipeline Sales Posting	Yes	Runs pipelines sales posting segments 
1005
3100
5105
5100
5101
5102
5103
5104

Added 11/29/2017 replacing Pipline JOB PL0005006 (Due to conflicts between 5006 and 5105): 
After Sales Posting Segments complete kicks off:

Pipeline Segment 5006 InfoBase to Stock Ledger - Post Transactions
Pipeline Segment 5010 InfoBase to MA - Send Master Entities

Disabled PL0005006 Pipeline Schedule ID 84 (12am - 8am) due to this change

	1	Pipeline SSIS	SSIS	/FILE "\"\\kermode\d$\SSIS Packages\Pipeline\Pipeline.dtsx\"" /CHECKPOINTING OFF /REPORTING E
MERCHANDISING - Process - Pipeline Sales Posting	Yes	Runs pipelines sales posting segments 
1005
3100
5105
5100
5101
5102
5103
5104

Added 11/29/2017 replacing Pipline JOB PL0005006 (Due to conflicts between 5006 and 5105): 
After Sales Posting Segments complete kicks off:

Pipeline Segment 5006 InfoBase to Stock Ledger - Post Transactions
Pipeline Segment 5010 InfoBase to MA - Send Master Entities

Disabled PL0005006 Pipeline Schedule ID 84 (12am - 8am) due to this change

	2	Post IB to SL Segments	TSQL	EXEC pipeapp01.master..xp_cmdshell 'PipelineScheduleClient Start 5006 0' -- InfoBase to Stock Ledger - Post Transactions

EXEC pipeapp01.master..xp_cmdshell 'PipelineScheduleClient Start 5010 0' -- InfoBase to MA - Send Master Entities
```


