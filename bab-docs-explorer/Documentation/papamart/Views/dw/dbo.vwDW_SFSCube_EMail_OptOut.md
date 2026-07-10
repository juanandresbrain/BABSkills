# dbo.vwDW_SFSCube_EMail_OptOut

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_EMail_OptOut"]
    SFSCube_EMail_OptOut(["SFSCube_EMail_OptOut"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| SFSCube_EMail_OptOut |

## View Code

```sql
CREATE VIEW dbo.vwDW_SFSCube_EMail_OptOut
AS SELECT
		  date_key
		, ORIG_SRC_SYS_CD
		, daysSinceID
		, isSFSMember
		, CNTRY_ABBRV
		, numEmailsUnsubscribed
		, numDaysSinceAcquisition
	 FROM queries..SFSCube_EMail_OptOut A WITH (NOLOCK);
```

