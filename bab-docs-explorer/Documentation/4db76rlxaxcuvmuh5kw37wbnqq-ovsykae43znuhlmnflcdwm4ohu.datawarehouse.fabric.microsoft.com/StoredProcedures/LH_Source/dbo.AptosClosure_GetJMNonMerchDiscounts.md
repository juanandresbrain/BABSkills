# dbo.AptosClosure_GetJMNonMerchDiscounts

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_GetJMNonMerchDiscounts"]
    sls_retail_line_item(["sls_retail_line_item"]) --> SP
    sls_retail_line_item_price_mod(["sls_retail_line_item_price_mod"]) --> SP
    sls_trans(["sls_trans"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| sls_retail_line_item |
| sls_retail_line_item_price_mod |
| sls_trans |

## Stored Procedure Code

```sql
-- ============================================= -- Author:      Brandon Hickey -- Create Date: 2025-11-06 -- Description: Returns non-merchandise discount line items from JM -- =============================================  CREATE PROCEDURE [dbo].[AptosClosure_GetJMNonMerchDiscounts]     @BusinessUnitIds NVARCHAR(MAX), -- comma-separated list of IDs     @StartDate DATE,     @EndDate DATE AS BEGIN     SET NOCOUNT ON;      -- Split the comma-separated string into a table     ;WITH BusinessUnitList AS (         SELECT value AS business_unit_id         FROM STRING_SPLIT(@BusinessUnitIds, ',')         WHERE value IS NOT NULL     )      SELECT          T.business_unit_id,          T.business_date,          T.sequence_number,          lipm.description,          lipm.modification_total     FROM sls_retail_line_item li     JOIN sls_retail_line_item_price_mod lipm         ON li.business_date = lipm.business_date         AND li.sequence_number = lipm.sequence_number         AND li.line_sequence_number = lipm.line_sequence_number         AND li.device_id = lipm.device_id     JOIN sls_trans T         ON T.business_date = lipm.business_date         AND T.sequence_number = lipm.sequence_number         AND T.device_id = lipm.device_id     INNER JOIN BusinessUnitList B ON T.business_unit_id = B.business_unit_id     WHERE T.trans_status = 'COMPLETED'       AND (           li.item_type IN ('GIFTCARD', 'DONATION', 'STORE_ORDER_SHIPPING', 'SERVICE')            OR li.item_id IN ('098088', '098089', '098090', '098091', '480200', '498041', '498088')       )       AND li.voided = 0       AND TRY_CONVERT(DATE, T.business_date) BETWEEN @StartDate AND @EndDate; END
```

