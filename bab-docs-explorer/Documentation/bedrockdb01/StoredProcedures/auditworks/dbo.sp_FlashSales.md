# dbo.sp_FlashSales

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_FlashSales"]
    dbo_transaction_header(["dbo.transaction_header"]) --> SP
    dbo_transaction_line(["dbo.transaction_line"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_header |
| dbo.transaction_line |

## Stored Procedure Code

```sql
CREATE  procedure [dbo].[sp_FlashSales]
as
-- =====================================================================================================
-- Name: sp_FlashSales
--
-- Description:	Returns latest sales 
--
-- Input:	
--			N/A
--
-- Output: Resultset with the following columns:
--			
--
-- Dependencies: None
--
-- Revision History
--		Name:			Date:			Comments:
--		Garyd			08/30/2010		Initial version in source control
-- exec sp_FlashSales
-- =====================================================================================================
--------------------------------------------------------------------------------------------------------
SELECT a.store_no as store_no, a.transaction_date as transaction_date, {fn CONVERT(0,SQL_FLOAT)} as Merchandise
	, {fn CONVERT(0,SQL_FLOAT)} as Fees, {fn CONVERT(0,SQL_FLOAT)} as BB_Sale
	, {fn CONVERT(0,SQL_FLOAT)} as BB_Rdm, {fn CONVERT(0,SQL_FLOAT)} as Sales_Tax
	, {fn CONVERT(0,SQL_FLOAT)} as Net_Part_Deposits, {fn CONVERT(0,SQL_FLOAT)} as Buy_Stuff_Cards
	, {fn CONVERT(0,SQL_FLOAT)} as Invoice_Total_excl_Tax INTO #SVWORK0  
FROM auditworks.dbo.transaction_header a, auditworks.dbo.transaction_line b 
WHERE a.transaction_id=b.transaction_id 
    AND (a.transaction_void_flag = 0 
    AND a.transaction_date Between   CONVERT(char,DATEADD(day,-1,GETDATE()),101) and   CONVERT(char,DATEADD(day,-1,GETDATE()),101) 
    AND 2=2 
    AND a.transaction_category IN (1,2)) 
GROUP BY a.store_no,a.transaction_date 

SELECT a.store_no as store_no, a.transaction_date as transaction_date
	, SUM( ((b.gross_line_amount - b.pos_discount_amount) )* b.db_cr_none * b.voiding_reversal_flag) as Merchandise INTO #SVWORK3  
FROM auditworks.dbo.transaction_header a, auditworks.dbo.transaction_line b 
WHERE a.transaction_id=b.transaction_id 
    AND (a.transaction_void_flag = 0 
    AND a.transaction_date Between   CONVERT(char,DATEADD(day,-1,GETDATE()),101) and   CONVERT(char,DATEADD(day,-1,GETDATE()),101) 
    AND 2=2 
    AND a.transaction_category IN (1,2) 
    AND b.line_object_type = 1) 
GROUP BY a.store_no,a.transaction_date 

UPDATE #SVWORK0
 SET Merchandise = b.Merchandise
 
 
FROM #SVWORK0 a, #SVWORK3 b
  
WHERE a.store_no = b.store_no
 
    AND a.transaction_date = b.transaction_date 

DROP TABLE #SVWORK3  

SELECT a.store_no as store_no, a.transaction_date as transaction_date
	, SUM( ((b.gross_line_amount - b.pos_discount_amount) )* b.db_cr_none * b.voiding_reversal_flag) as Fees INTO #SVWORK4  
FROM auditworks.dbo.transaction_header a, auditworks.dbo.transaction_line b 
WHERE a.transaction_id=b.transaction_id 
    AND (a.transaction_void_flag = 0 
    AND a.transaction_date Between   CONVERT(char,DATEADD(day,-1,GETDATE()),101) and   CONVERT(char,DATEADD(day,-1,GETDATE()),101) 
    AND 2=2 
    AND a.transaction_category IN (1,2) 
    AND b.line_object_type = 2) 
GROUP BY a.store_no,a.transaction_date 

UPDATE #SVWORK0
 SET Fees = b.Fees
 
 
FROM #SVWORK0 a, #SVWORK4 b
  
WHERE a.store_no = b.store_no
 
    AND a.transaction_date = b.transaction_date 

DROP TABLE #SVWORK4  

SELECT a.store_no as store_no, a.transaction_date as transaction_date
	, SUM(b.gross_line_amount * b.db_cr_none * b.voiding_reversal_flag) as BB_Sale INTO #SVWORK5  
FROM auditworks.dbo.transaction_header a, auditworks.dbo.transaction_line b 
WHERE a.transaction_id=b.transaction_id 
    AND (a.transaction_void_flag = 0 
    AND a.transaction_date Between   CONVERT(char,DATEADD(day,-1,GETDATE()),101) and   CONVERT(char,DATEADD(day,-1,GETDATE()),101) 
    AND 2=2 
    AND a.transaction_category IN (1,2) 
    AND b.line_object_type = 4) 
GROUP BY a.store_no,a.transaction_date 

UPDATE #SVWORK0
 SET BB_Sale = b.BB_Sale
 
 
FROM #SVWORK0 a, #SVWORK5 b
  
WHERE a.store_no = b.store_no
 
    AND a.transaction_date = b.transaction_date 

DROP TABLE #SVWORK5  

SELECT a.store_no as store_no, a.transaction_date as transaction_date
	, SUM( ((b.gross_line_amount - b.pos_discount_amount) )* b.db_cr_none * b.voiding_reversal_flag) as BB_Rdm INTO #SVWORK6  
FROM auditworks.dbo.transaction_header a, auditworks.dbo.transaction_line b 
WHERE a.transaction_id=b.transaction_id 
    AND (a.transaction_void_flag = 0 
    AND a.transaction_date Between   CONVERT(char,DATEADD(day,-1,GETDATE()),101) and   CONVERT(char,DATEADD(day,-1,GETDATE()),101) 
    AND 2=2 
    AND a.transaction_category IN (1,2) 
    AND b.line_object IN (621,624,633)) 
GROUP BY a.store_no,a.transaction_date 

UPDATE #SVWORK0
 SET BB_Rdm = b.BB_Rdm
 
 
FROM #SVWORK0 a, #SVWORK6 b
  
WHERE a.store_no = b.store_no
 
    AND a.transaction_date = b.transaction_date 

DROP TABLE #SVWORK6  

SELECT a.store_no as store_no, a.transaction_date as transaction_date
	, SUM( ((b.gross_line_amount - b.pos_discount_amount) )* b.db_cr_none * b.voiding_reversal_flag) as Sales_Tax INTO #SVWORK7  
FROM auditworks.dbo.transaction_header a, auditworks.dbo.transaction_line b 
WHERE a.transaction_id=b.transaction_id 
    AND (a.transaction_void_flag = 0 
    AND a.transaction_date Between   CONVERT(char,DATEADD(day,-1,GETDATE()),101) and   CONVERT(char,DATEADD(day,-1,GETDATE()),101) 
    AND 2=2 
    AND a.transaction_category IN (1,2) 
    AND b.line_object_type = 5) 
GROUP BY a.store_no,a.transaction_date 

UPDATE #SVWORK0
 SET Sales_Tax = b.Sales_Tax
 
 
FROM #SVWORK0 a, #SVWORK7 b
  
WHERE a.store_no = b.store_no
 
    AND a.transaction_date = b.transaction_date 

DROP TABLE #SVWORK7  

SELECT a.store_no as store_no, a.transaction_date as transaction_date
	, SUM( ((b.gross_line_amount - b.pos_discount_amount) )* b.db_cr_none * b.voiding_reversal_flag) as Net_Part_Deposits INTO #SVWORK8  
FROM auditworks.dbo.transaction_header a, auditworks.dbo.transaction_line b 
WHERE a.transaction_id=b.transaction_id 
    AND (a.transaction_void_flag = 0 
    AND a.transaction_date Between   CONVERT(char,DATEADD(day,-1,GETDATE()),101) and   CONVERT(char,DATEADD(day,-1,GETDATE()),101) 
    AND 2=2 
    AND a.transaction_category IN (1,2) 
    AND b.line_object_type = 3) 
GROUP BY a.store_no,a.transaction_date 

UPDATE #SVWORK0
 SET Net_Part_Deposits = b.Net_Part_Deposits
 
 
FROM #SVWORK0 a, #SVWORK8 b
  
WHERE a.store_no = b.store_no
 
    AND a.transaction_date = b.transaction_date 

DROP TABLE #SVWORK8  

SELECT a.store_no as store_no, a.transaction_date as transaction_date
, SUM( ((b.gross_line_amount - b.pos_discount_amount) )* b.db_cr_none * b.voiding_reversal_flag) as Buy_Stuff_Cards INTO #SVWORK9  
FROM auditworks.dbo.transaction_header a, auditworks.dbo.transaction_line b 
WHERE a.transaction_id=b.transaction_id 
    AND (a.transaction_void_flag = 0 
    AND a.transaction_date Between   CONVERT(char,DATEADD(day,-1,GETDATE()),101) and   CONVERT(char,DATEADD(day,-1,GETDATE()),101) 
    AND 2=2 
    AND a.transaction_category IN (1,2) 
    AND b.line_object = 690) 
GROUP BY a.store_no,a.transaction_date 

UPDATE #SVWORK0
 SET Buy_Stuff_Cards = b.Buy_Stuff_Cards
 
 
FROM #SVWORK0 a, #SVWORK9 b
  
WHERE a.store_no = b.store_no
 
    AND a.transaction_date = b.transaction_date 

DROP TABLE #SVWORK9  

SELECT DISTINCT store_no,transaction_date,Merchandise,Fees,BB_Sale,BB_Rdm,Sales_Tax,Net_Part_Deposits,Buy_Stuff_Cards,
	(-Merchandise-Fees-BB_Sale-BB_Rdm-Net_Part_Deposits-Buy_Stuff_Cards) as Invoice_Total_excl_Tax 
FROM #SVWORK0 

DROP TABLE #SVWORK0  

--------------------------------------------------------------------------------------------------------
return
```

