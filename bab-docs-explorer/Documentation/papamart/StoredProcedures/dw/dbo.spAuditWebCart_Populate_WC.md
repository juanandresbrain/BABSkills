# dbo.spAuditWebCart_Populate_WC

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spAuditWebCart_Populate_WC"]
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

CREATE        PROCEDURE spAuditWebCart_Populate_WC
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
```

