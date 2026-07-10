# dbo.spRpt_DonationsbyMonthbyType

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRpt_DonationsbyMonthbyType"]
    dbo_date_dim(["dbo.date_dim"]) --> SP
    dbo_line_object_dim(["dbo.line_object_dim"]) --> SP
    dbo_transaction_detail_facts(["dbo.transaction_detail_facts"]) --> SP
    dbo_vwProduct_Dim(["dbo.vwProduct_Dim"]) --> SP
    dbo_vwstore_dimBO6(["dbo.vwstore_dimBO6"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| dbo.line_object_dim |
| dbo.transaction_detail_facts |
| dbo.vwProduct_Dim |
| dbo.vwstore_dimBO6 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spRpt_DonationsbyMonthbyType] 

	(
	 @fiscalyear INT, @BeginDate DATE
	, @EndDate DATE
	)
AS
BEGIN
SET NOCOUNT ON

/*********************************************************************************************************************************
 Author:		Mahendar Akula
 Create date:	04/07/2015
 Description:	
 Assigned by :	Kevin Shyr
 Version:		0.1
 Modified On:
 Modified By:
 Comments:		Created Proc
 Test:			EXEC [dbo].[spRpt_DonationsbyMonthbyType]  2012

***********************************************************************************************************************************/
--DECLARE  @fiscalYear INT
--Set @fiscalYear = '2015'

	SELECT
		SD.store_id
		,dd.fiscal_period
		,DD.org_fiscal_period
		,SUM(TDF.Units) AS [Units]
		,SUM(TDF.unit_gross_amount) AS [Unit Gross Amount]
		,SUM (TDF.unit_disc_amount) AS [Unit Disc Amount]
		,SD.division AS SD_Division
		,PD.sku AS [Sku]
		,PD.product_desc AS [Product Description] 
		,TDF.reference_no
		,RIGHT('000' + CAST(SD.store_id AS VARCHAR), 4) + ' ' + sd.store_name AS [StoreID]
		,COUNT(DISTINCT TDF.transaction_id) AS [No of Transaction]
		,DD.actual_date
		,DD.org_fiscal_week
		,TDF.unit_gross_amount + TDF.unit_gross_amount as [Total]
	FROM dbo.vwstore_dimBO6 SD
		JOIN dbo.transaction_detail_facts TDF WITH(READCOMMITTED)
			ON TDF.store_key = SD.store_key
		JOIN dbo.date_dim DD WITH(READCOMMITTED) 
			ON DD.date_key = TDF.date_key
		JOIN dbo.vwProduct_Dim PD 
			ON PD.product_key = TDF.product_key
		JOIN dbo.line_object_dim LOD WITH(READCOMMITTED)
			ON LOD.Line_Object_Key = tdf.line_object_key
				AND LOD.Line_Object IN (292, 101)
				AND dd.fiscal_year IN (@fiscalYear)
				AND dd.actual_date BETWEEN @BeginDate AND @EndDate
	GROUP BY 
		SD.store_id
		,dd.fiscal_period
		,DD.org_fiscal_period
		,SD.division 
		,PD.sku 
		,PD.product_desc 
		,TDF.reference_no
		,RIGHT('000' + CAST(SD.store_id AS VARCHAR), 4) + ' ' + sd.store_name 
		,DD.actual_date
		,DD.org_fiscal_week
		,TDF.unit_gross_amount + TDF.unit_gross_amount

END
```

