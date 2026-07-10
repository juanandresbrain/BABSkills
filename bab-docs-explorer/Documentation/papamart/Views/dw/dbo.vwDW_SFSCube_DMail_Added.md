# dbo.vwDW_SFSCube_DMail_Added

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_DMail_Added"]
    SFSCube_DMail_Added(["SFSCube_DMail_Added"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| SFSCube_DMail_Added |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_DMail_Added]
AS
	SELECT 
		   date_key,
		   ORIG_SRC_SYS_CD,
		   isSFSMember,
		   CNTRY_ABBRV,
		   numDmailsAdded
	FROM queries..SFSCube_DMail_Added A WITH (NOLOCK)
```

