# Azure.vwCRMsurveyResults

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwCRMsurveyResults"]
    dbo_CRM_surveyResults(["dbo.CRM_surveyResults"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CRM_surveyResults |

## View Code

```sql
CREATE view [Azure].[vwCRMsurveyResults]

AS

select * from [dbo].[CRM_surveyResults]
```

