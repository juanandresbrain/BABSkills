# Azure.vwPCHealthChecks

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPCHealthChecks"]
    Azure_PCHealthChecks(["Azure.PCHealthChecks"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.PCHealthChecks |

## View Code

```sql
CREATE view [Azure].[vwPCHealthChecks]

AS
-- =============================================================================================================
-- Name: [Azure].[vwPCHealthChecks]
--
-- Description: This view is filtered to only show current and two previous fiscal years it is used to limit the data that shows up in Power BI views.
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:

--
-- =============================================================================================================

select *
from [Azure].[PCHealthChecks]
```

