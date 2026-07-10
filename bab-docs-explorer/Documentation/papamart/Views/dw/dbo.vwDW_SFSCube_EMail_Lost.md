# dbo.vwDW_SFSCube_EMail_Lost

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_EMail_Lost"]
    SFSCube_EMail_Lost(["SFSCube_EMail_Lost"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| SFSCube_EMail_Lost |

## View Code

```sql
CREATE VIEW dbo.vwDW_SFSCube_EMail_Lost
AS SELECT
		  date_key
		, EMAIL_STAT_CD
		, ORIG_SRC_SYS_CD
		, daysSinceID
		, isSFSMember
		, CNTRY_ABBRV
		, numEmailsLost
		, numDaysSinceAcquisition
	 FROM queries..SFSCube_EMail_Lost A WITH (NOLOCK);
```

