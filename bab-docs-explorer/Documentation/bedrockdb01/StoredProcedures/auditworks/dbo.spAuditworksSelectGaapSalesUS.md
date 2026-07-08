# dbo.spAuditworksSelectGaapSalesUS

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spAuditworksSelectGaapSalesUS"]
    GaapSales(["GaapSales"]) --> SP
    store_sa(["store_sa"]) --> SP
    store_salesaudit(["store_salesaudit"]) --> SP
    dbo_transaction_header(["dbo.transaction_header"]) --> SP
    dbo_transaction_line(["dbo.transaction_line"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| GaapSales |
| store_sa |
| store_salesaudit |
| dbo.transaction_header |
| dbo.transaction_line |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[spAuditworksSelectGaapSalesUS]
as
-- =============================================================================================================
-- Name: spAuditworksSelectGaapSalesUS
--
-- Description:	captures Gaap Sales from Auditworks for US stores.
--				Modified version of usp_GAAPSales, which called sv_store view. 
--				This sv_store view is different in AW5 than in AW4, so this new proc does not use sv_view, but instead joins to the tables from that view (store_sa and store_salesaudit).
--
-- Input:		
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		10/29/2010      Sales Audit upgrade to version 5
--		Dan Tweedie		11/2/2010		Modified joins to ensure we capture stores with no sales
--		Dan Tweedie		02/21/2011		Added inclusion of Line Object 104
-- =============================================================================================================


set nocount on
    
IF (Object_ID('tempdb..#USGaapSalesAW') IS NOT NULL) DROP TABLE #USGaapSalesAW
create table #USGaapSalesAW
	(
		location_code varchar(4),
		location_name varchar(50),
		net_sales decimal (14,2),
		entry_date varchar(50)
	)

insert #USGaapSalesAW    
select	sa.store_no location_code, 
		sa.store_name location_name, 
		isnull(d.total, 0) net_sales,
		case when d.[time of last transaction polled] IS NULL 
				then 'No transactions polled' 
				else d.[time of last transaction polled]
			 end entry_date
    
    FROM store_sa sa (nolock)
    join store_salesaudit ss (nolock) on ss.store_no = sa.store_no
    left join
		( SELECT    a.store_no,
                        SUM(( (b.gross_line_amount - b.pos_discount_amount) )
                            * b.db_cr_none * b.voiding_reversal_flag) * -1 AS total,
                        LEFT(MAX(a.entry_date_time), 19) AS [time of last transaction polled]
              FROM      auditworks.dbo.transaction_header a WITH ( NOLOCK )
                        JOIN auditworks.dbo.transaction_line b WITH ( NOLOCK ) ON a.transaction_id = b.transaction_id
              WHERE     ( a.transaction_date BETWEEN CONVERT(CHAR, GETDATE(), 101)
                                             AND     CONVERT(CHAR, GETDATE(), 101)
                          AND a.transaction_void_flag = 0
                          AND a.transaction_category IN ( 1, 2 )
                          AND b.line_void_flag = 0
                          AND b.line_object IN ( 100, 102, 103, 104, 200, 202, 203, 204, 206,
                                                 210, 250, 290, 291, 293, 295,
                                                 296, 623, 640, 690, 691, 1630,
                                                 1631 )
                        ) 
            
			GROUP BY  a.store_no
            ) d on d.store_no = sa.store_no
    WHERE   ss.gl_company IN ( 100 ) -- US stores only
    ORDER BY sa.store_no



select right(('0000' + location_code), 4) as location_code,
		location_name,
		net_sales,
		entry_date,
        'Auditworks' as source
from	#USGaapSalesAW 
where	location_code in (select location_code from GaapSales where location_name = 'UTC')
order by 1
```

