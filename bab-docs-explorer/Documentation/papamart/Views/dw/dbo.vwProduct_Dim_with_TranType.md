# dbo.vwProduct_Dim_with_TranType

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwProduct_Dim_with_TranType"]
    product_dim(["product_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| product_dim |

## View Code

```sql
CREATE view [dbo].[vwProduct_Dim_with_TranType]  
as
-- =============================================================================================================
-- Name: [dbo].[vwProduct_Dim_with_TranType]
--

-- Revision History
--		Name:					Date:			Comments:
--		Outside Contractor		1/14/2014		Added logic to handle changes to the hierarchy												
--		Unknown Orgin							original creation
-- =============================================================================================================

SELECT   
	ScorecardCategory AS PRODUCT_GROUP,  
      
	CASE WHEN ScorecardCategory = 'Animal' THEN 'BEAR'  
		 WHEN ScorecardCategory IN ('Clothing', 'Footwear', 'Sounds', 'Accessories', 'Prestuffed', 'Human', 'Sports') THEN 'PLUS'  
	ELSE 'OTHER'  
	END as TRAN_TYPE_GROUP,  
  
	CASE WHEN ScorecardCategory = 'Animal' THEN 1 
	  WHEN ScorecardCategory = 'Sounds' THEN 0  
	  WHEN ScorecardCategory IN ('Clothing', 'Footwear', 'Accessories', 'Prestuffed', 'Human', 'Sports')  THEN 2  
		WHEN department_code is NULL then NULL
	ELSE 4  
	END as TRAN_TYPE_NUM,  
	*  
from product_dim WITH(READCOMMITTED)
```

