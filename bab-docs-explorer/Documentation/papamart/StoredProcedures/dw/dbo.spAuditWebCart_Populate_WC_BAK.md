# dbo.spAuditWebCart_Populate_WC_BAK

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spAuditWebCart_Populate_WC_BAK"]
    dbo_WCAudit_All_WC_Orders(["dbo.WCAudit_All_WC_Orders"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WCAudit_All_WC_Orders |

## Stored Procedure Code

```sql
/*
EXEC spAuditWebCart_Populate_WC
*/

CREATE        PROCEDURE spAuditWebCart_Populate_WC_BAK
AS
SET NOCOUNT ON

IF (Object_ID('queries.dbo.WCAudit_All_WC_Orders') IS NOT NULL) DROP TABLE queries.dbo.WCAudit_All_WC_Orders

CREATE TABLE queries.dbo.WCAudit_All_WC_Orders
	(order_create_date smalldatetime
	,order_number varchar(32)
	,order_status_code tinyint
	,d_DateCreated smalldatetime
	,total_lineitems int
	,saved_cy_oadjust_subtotal money
	,saved_cy_total_total money
	,SiteCode nvarchar(50)
	,SendToPMS int
	,DateSentToPMS smalldatetime
	,SendToUDADaily int
	,DateSentToUDADaily smalldatetime
	,NeedsCreditAuth int
	,SendToSettlement int
	,DateSentToSettlement smalldatetime
	,SendToSalesExport int
	,DateSentToSalesExport smalldatetime
	)
create index ix_WebCart_Orders_order_number on queries.dbo.WCAudit_All_WC_Orders(order_number)
create index ix_WebCart_Orders_SendToSalesExport on queries.dbo.WCAudit_All_WC_Orders(SendToSalesExport)


INSERT queries.dbo.WCAudit_All_WC_Orders(
	order_create_date
	,order_number
	,order_status_code
	,d_DateCreated
	,total_lineitems
	,saved_cy_oadjust_subtotal
	,saved_cy_total_total
	,SiteCode
	,SendToPMS
	,DateSentToPMS
	,SendToUDADaily
	,DateSentToUDADaily
	,NeedsCreditAuth
	,SendToSettlement
	,DateSentToSettlement
	,SendToSalesExport
	,DateSentToSalesExport 
	)
SELECT a.order_create_date
	,a.order_number
	,a.order_status_code
	,a.d_DateCreated
	,a.total_lineitems
	,a.saved_cy_oadjust_subtotal
	,a.saved_cy_total_total
	,a.SiteCode
	,a.SendToPMS
	,a.DateSentToPMS
	,a.SendToUDADaily
	,a.DateSentToUDADaily
	,a.NeedsCreditAuth
	,a.SendToSettlement
	,a.DateSentToSettlement
	,a.SendToSalesExport
	,a.DateSentToSalesExport 
FROM OPENROWSET ( 'SQLOLEDB', 'BearWebDB' ; 'CommerceServer' ; 'A1g3r#1' , 
'SELECT order_create_date
	,order_number
	,order_status_code
	,d_DateCreated
	,total_lineitems
	,saved_cy_oadjust_subtotal
	,saved_cy_total_total
	,SiteCode
	,SendToPMS
	,DateSentToPMS
	,SendToUDADaily
	,DateSentToUDADaily
	,NeedsCreditAuth
	,SendToSettlement
	,DateSentToSettlement
	,SendToSalesExport
	,DateSentToSalesExport 
from bearwebdb.webcart_commerce.dbo.OrderGroup --with(nolock)') a


-- SELECT order_create_date
-- 	,order_number
-- 	,order_status_code
-- 	,d_DateCreated
-- 	,total_lineitems
-- 	,saved_cy_oadjust_subtotal
-- 	,saved_cy_total_total
-- 	,SiteCode
-- 	,SendToPMS
-- 	,DateSentToPMS
-- 	,SendToUDADaily
-- 	,DateSentToUDADaily
-- 	,NeedsCreditAuth
-- 	,SendToSettlement
-- 	,DateSentToSettlement
-- 	,SendToSalesExport
-- 	,DateSentToSalesExport 
-- from bearwebdb.webcart_commerce.dbo.OrderGroup --with(nolock)
-- -- where DateSentToSettlement between @BeginDate and @EndDate	--##### WARNING: DateSentToSettlement gets reset if Return, Cancel! ######################
-- -- order by order_create_date
--  
-- --select * from queries.dbo.WCAudit_All_WC_Orders







dbo,sp_VoucherLookup_sfs,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_VoucherLookup_sfs]
	-- Add the parameters for the stored procedure here
	@sfs_Number varchar(20) = 'NoData',
	@refType int
AS
BEGIN

	SET NOCOUNT ON;

DECLARE @select AS VARCHAR(3000), @cntryCode AS VARCHAR(3)

IF @sfs_Number != 'NoData'
BEGIN
	SELECT DISTINCT c.reference_no AS [VoucherNumber]
			,[RedeemedDate]
			,[RedeemedAt]
			,c.date_issued AS [IssuedDate]
			,CASE WHEN expiry_date <= CONVERT(VARCHAR,DATEADD(DAY,-0,GETDATE()),111) 
				  THEN 'Yes' 
				  ELSE 'No' 
			END AS [Expired]
			,DATEADD(SECOND, -1, c.expiry_date) AS [ExpirationDate]
			,c.pos_amount_1 AS [Balance]
			,CASE WHEN (c.liability_amount != c.amount_3 AND [RedeemedDate] IS NOT NULL)
				  THEN 'Redeemed'
				  WHEN c.pos_amount_1 = 0
				  THEN 'Redeemed'
				  WHEN c.pos_status = '30' AND c.liability_amount = c.amount_3 AND c.amount_4 = 0 AND c.expiry_date > CONVERT(VARCHAR,DATEADD(DAY,-0,GETDATE()),111) 
				  THEN 'Valid' 
				  WHEN c.pos_status = '0' 
				  THEN 'Cancelled' 
				  WHEN c.pos_status = '50' 
				  THEN 'Forfeited' 
				  WHEN c.expiry_date <= CONVERT(VARCHAR,DATEADD(DAY,-0,GETDATE()),111) 
				  THEN 'Expired' 
						END AS [Status]
			,c.customer_no AS [CustomerNumber]
			,c.last_name AS [LastName]
			,c.first_name AS [FirstName]
			,c.email_address AS [EmailAddress]
			,'-' AS [Tier]
			,'UK:$11 off select FF' AS 'Title'
			,'$11 off select furry friend serialized coupon' AS 'Description'
			,522 AS 'POSTransactionNumber'
		FROM bedrockdb01.auditworks.dbo.cust_liability c (NOLOCK) 
		LEFT OUTER JOIN bedrockdb01.auditworks.dbo.cust_liability_history h (NOLOCK) ON c.reference_no = h.reference_no
		LEFT OUTER JOIN [stl-crmdb-p-01].crm.dbo.customer cc (NOLOCK) ON c.customer_no = cc.customer_no
		LEFT JOIN 
			   (
					  SELECT MIN(h2.transaction_date) [RedeemedDate], MIN(h2.store_no) [RedeemedAt], reference_no
					  FROM bedrockdb01.auditworks.dbo.cust_liability_history h2 (NOLOCK)
					  WHERE h2.store_no <> 990
					  GROUP BY reference_no
			   ) qry ON c.reference_no = qry.reference_no 

		WHERE h.store_no = 990 AND (c.reference_type = CAST(@refType AS VARCHAR(2)) OR c.reference_type = 35) AND c.customer_no = CAST(@sfs_Number AS VARCHAR(9))
		ORDER BY c.date_issued
END
END
```

