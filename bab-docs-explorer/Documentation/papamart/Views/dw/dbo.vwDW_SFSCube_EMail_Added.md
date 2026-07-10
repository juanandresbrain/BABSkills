# dbo.vwDW_SFSCube_EMail_Added

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_EMail_Added"]
    SFSCube_EMail_Added(["SFSCube_EMail_Added"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| SFSCube_EMail_Added |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_EMail_Added]
AS
	SELECT 
		   date_key,
		   ORIG_SRC_SYS_CD,
		   isSFSMember,
		   CNTRY_ABBRV,
		   numEmailsAdded
	FROM queries..SFSCube_EMail_Added A WITH (NOLOCK)
```

