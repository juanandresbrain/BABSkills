# Job: MERCHANDISING - Process - Enable View of SKU\Location Qtys on External Distro Docs

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** There is a bug in the Aptos Merchandising application that will not allow users to view SKU\Location quantities on completed\cancelled Distribution Documents that were created from an External Source (i.e. Dan upload files). Aptos provided a stored proc workaround until the bug is resolved.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Enable View of SKU\Location Qtys on External Distro Docs"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.zzz_set_dist_method_$sp
MERCHANDISING - Process - ERD Email Notices and Auto Receipts	No	Checks for unreceived store shipments 2 days past ERD, sends email warning to store and BL. Checks for unreceived store shipments 3 days past ERD, automates the receipts via carton batch file to pipeline, sends email to store and BL.
Update 06/25/2020, LT - Added step "ERD Plus 1" (spMerchandisingEmail1DaysPastERDWarning) to send alerts to BOSFS particpating locations 1 day after their shipments' expected receipt date.  These locations are also excluded from arton batch files to pipeline.	1	ERD Plus 1	TSQL	EXEC me_01.dbo.spMerchandisingEmail1DaysPastERDWarning
MERCHANDISING - Process - ERD Email Notices and Auto Receipts	No	Checks for unreceived store shipments 2 days past ERD, sends email warning to store and BL. Checks for unreceived store shipments 3 days past ERD, automates the receipts via carton batch file to pipeline, sends email to store and BL.
Update 06/25/2020, LT - Added step "ERD Plus 1" (spMerchandisingEmail1DaysPastERDWarning) to send alerts to BOSFS particpating locations 1 day after their shipments' expected receipt date.  These locations are also excluded from arton batch files to pipeline.	2	ERD Plus 2	TSQL	exec me_01.dbo.spMerchandisingEmail2DaysPastERDWarning
MERCHANDISING - Process - ERD Email Notices and Auto Receipts	No	Checks for unreceived store shipments 2 days past ERD, sends email warning to store and BL. Checks for unreceived store shipments 3 days past ERD, automates the receipts via carton batch file to pipeline, sends email to store and BL.
Update 06/25/2020, LT - Added step "ERD Plus 1" (spMerchandisingEmail1DaysPastERDWarning) to send alerts to BOSFS particpating locations 1 day after their shipments' expected receipt date.  These locations are also excluded from arton batch files to pipeline.	3	ERD Plus 3	TSQL	exec me_01.dbo.spMerchandisingEmail3DaysPastERDNotice
```


