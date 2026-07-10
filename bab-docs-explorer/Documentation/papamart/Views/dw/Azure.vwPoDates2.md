# Azure.vwPoDates2

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPoDates2"]
    azure_vwPoDates(["azure.vwPoDates"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| azure.vwPoDates |

## View Code

```sql
create VIEW [Azure].[vwPoDates2]  AS
-- =============================================================================================================
-- Name: [Azure].[vwPoDates2] 
--
-- Description: 
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		John Eck		04/14/2019		Initial creation
--
-- =============================================================================================================

Select Po_NO,Expected_REceipt_date,[Vendor Ship Date] Vendor_Ship_Date,[Vendor PO Cancel Date] Vendor_PO_Cancel_Date 
from (
	select PO_NO,Expected_Receipt_Date,Date_Type_desc,User_Defined_date
	from azure.vwPoDates) d
	
	PIVOT (
	  Max(User_defined_date  )
	  	  For Date_Type_desc in ([Vendor Ship Date] ,[Vendor PO Cancel Date])
	  ) as pvt
```

