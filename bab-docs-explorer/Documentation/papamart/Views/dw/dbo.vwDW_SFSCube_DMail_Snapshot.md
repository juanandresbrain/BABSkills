# dbo.vwDW_SFSCube_DMail_Snapshot

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSCube_DMail_Snapshot"]
    SFSCube_DMail_Snapshot(["SFSCube_DMail_Snapshot"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| SFSCube_DMail_Snapshot |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSCube_DMail_Snapshot]
AS
	SELECT date_key,
		   CNTRY_ABBRV,
		   isSFSMember,
		   dmail_stat_cd,
		   numAddresses 
	FROM queries..SFSCube_DMail_Snapshot SNAP WITH (NOLOCK)
```

