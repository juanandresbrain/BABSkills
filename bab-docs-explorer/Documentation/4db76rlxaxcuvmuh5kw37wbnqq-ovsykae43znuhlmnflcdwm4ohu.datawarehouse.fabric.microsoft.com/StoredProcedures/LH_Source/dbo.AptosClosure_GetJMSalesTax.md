# dbo.AptosClosure_GetJMSalesTax

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_GetJMSalesTax"]
    sls_retail_line_item(["sls_retail_line_item"]) --> SP
    sls_trans(["sls_trans"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| sls_retail_line_item |
| sls_trans |

## Stored Procedure Code

```sql
-- ============================================= -- Author:      Brandon Hickey -- Create Date: 2025-11-06 -- Description: Returns sales tax line items from JM -- =============================================  CREATE PROCEDURE [dbo].[AptosClosure_GetJMSalesTax]     @BusinessUnitIds NVARCHAR(MAX), -- comma-separated list of IDs     @StartDate DATE,     @EndDate DATE AS BEGIN     SET NOCOUNT ON;      -- Split the comma-separated string into a table     ;WITH BusinessUnitList AS (         SELECT value AS business_unit_id         FROM STRING_SPLIT(@BusinessUnitIds, ',')         WHERE value IS NOT NULL     )      SELECT          T.business_unit_id,          T.business_date,          T.sequence_number,          TLI.device_id,          TLI.item_id,          TLI.item_description,          TLI.tax_amount     FROM sls_retail_line_item TLI     INNER JOIN sls_trans T         ON T.device_id = TLI.device_id         AND T.business_date = TLI.business_date         AND T.sequence_number = TLI.sequence_number     INNER JOIN BusinessUnitList B ON T.business_unit_id = B.business_unit_id     WHERE TLI.voided = 0       AND T.trans_type IN ('SALE', 'RETURN')       AND T.trans_status = 'COMPLETED'       AND TLI.tax_amount <> 0       AND TRY_CONVERT(DATE, TLI.business_date) BETWEEN @StartDate AND @EndDate; END
```

