# Azure.vwCRMsurveyQuestions

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwCRMsurveyQuestions"]
    dbo_CRM_surveyQuestions(["dbo.CRM_surveyQuestions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CRM_surveyQuestions |

## View Code

```sql
CREATE view [Azure].[vwCRMsurveyQuestions]

AS

select * from [dbo].[CRM_surveyQuestions]
```

