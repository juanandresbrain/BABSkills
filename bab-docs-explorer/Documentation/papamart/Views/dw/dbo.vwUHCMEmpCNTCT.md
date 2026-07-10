# dbo.vwUHCMEmpCNTCT

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwUHCMEmpCNTCT"]
    UHCMEmp(["UHCMEmp"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| UHCMEmp |

## View Code

```sql
CREATE View [dbo].[vwUHCMEmpCNTCT]
As
	SELECT DISTINCT 
		U.JbcJobCode AS R_POSITION,
		U.EepNameFirst AS FIRST_NAME,
		U.EepNameLast AS LAST_NAME,
		U.EepNameMiddle AS MIDDLE_NAME,
		U.WorkPhoneNumber AS Lawsonphone,
		U.efoPhoneExtension AS PHONE_EXT,
		U.EfoPhoneNumber AS Lawsoncell,
		U.EepAddressEMail AS LawsonEmail,
		U.EepEEID AS LWSN_CD
		

	FROM  UHCMEmp U WITH (NOLOCK)
	--where U.EepCompanyCode <> 'BABUK'
```

