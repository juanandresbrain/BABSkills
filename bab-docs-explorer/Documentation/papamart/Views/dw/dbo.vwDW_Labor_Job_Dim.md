# dbo.vwDW_Labor_Job_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Labor_Job_Dim"]
    Labor_Job_Dim(["Labor_Job_Dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Labor_Job_Dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Labor_Job_Dim]
AS
-- =============================================================================================================
-- Name: [dbo].[vwDW_Labor_Job_Dim]
--
-- Description: View Job Dimension used in the Cube
-- Classifies the Work Classification of the hours.
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		5/7/2012		Initial deployment
-- =============================================================================================================
SELECT job_key
	 , descr
	 , abrv
FROM
	Labor_Job_Dim WITH (NOLOCK)
```

