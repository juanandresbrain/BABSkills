# dbo.AptosClosure_GetJMMerchSales

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_GetJMMerchSales"]
    jumpmind_sls_retail_line_item(["jumpmind_sls_retail_line_item"]) --> SP
    jumpmind_sls_trans(["jumpmind_sls_trans"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| jumpmind_sls_retail_line_item |
| jumpmind_sls_trans |

## Stored Procedure Code

```sql
-- ============================================= -- Author:      Brandon Hickey -- Create Date: 2025-11-06 -- Description: Returns filtered line item data from JM -- =============================================  CREATE PROCEDURE [dbo].[AptosClosure_GetJMMerchSales]     @BusinessUnitIds NVARCHAR(MAX), -- comma-separated list of IDs     @StartDate DATE,     @EndDate DATE AS BEGIN     SET NOCOUNT ON;      -- Split the comma-separated string into a table  	;WITH BusinessUnitList AS ( 		SELECT value AS business_unit_id 		FROM STRING_SPLIT(@BusinessUnitIds, ',') 		WHERE value IS NOT NULL 	)      SELECT          T.business_unit_id,          T.business_date,          T.sequence_number,          LI.device_id,          LI.item_description,          LI.item_id,          LI.item_type,          LI.extended_amount     FROM jumpmind_sls_retail_line_item LI     JOIN jumpmind_sls_trans T          ON T.business_date = LI.business_date         AND T.sequence_number = LI.sequence_number         AND T.device_id = LI.device_id     INNER JOIN BusinessUnitList B ON T.business_unit_id = B.business_unit_id     WHERE T.trans_status = 'COMPLETED'       AND LI.voided = 0       AND LI.item_id NOT IN (           '999999990', '999999995', '899999902', '999999996', '999999997',           '098088', '098089', '098090', '098091', '480200', '498041', '498088'       )       AND LI.item_type NOT IN (           'GIFTCARD', 'DONATION', 'STORE_ORDER_SHIPPING', 'SERVICE'       )       AND TRY_CONVERT(DATE, LI.business_date) BETWEEN @StartDate AND @EndDate; END
```

