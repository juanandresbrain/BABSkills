# dbo.AptosClosure_GetMissingSequences_Old

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AptosClosure_GetMissingSequences_Old"]
    jumpmind_sls_trans_summary(["jumpmind_sls_trans_summary"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| jumpmind_sls_trans_summary |

## Stored Procedure Code

```sql
-- ============================================= -- Author:      Brandon Hickey -- Create Date: 2025-11-04 -- Description: Pulls missing sequence numbers between Aptos and GLTest1 -- =============================================  CREATE PROCEDURE [dbo].[AptosClosure_GetMissingSequences_Old]     @BusinessUnitIds NVARCHAR(MAX), -- comma-separated list of IDs     @StartDate DATE,     @EndDate DATE AS BEGIN     SET NOCOUNT ON;      -- Split the comma-separated string into a table if not null     WITH BusinessUnitList AS (         SELECT TRY_CAST(TRIM(value) AS INT) AS business_unit_id         FROM STRING_SPLIT(@BusinessUnitIds, ',')         WHERE TRY_CAST(TRIM(value) AS INT) IS NOT NULL     ),          filtered_data AS (         SELECT              s.business_unit_id,             s.business_date,             s.device_id,             s.sequence_number         FROM jumpmind_sls_trans_summary s         WHERE TRY_CONVERT(DATE, s.business_date) BETWEEN @StartDate AND @EndDate         AND (             @BusinessUnitIds IS NULL             OR s.business_unit_id IN (SELECT business_unit_id FROM BusinessUnitList)         )     ),      sequenced AS (         SELECT              business_unit_id,             business_date,             device_id,             sequence_number,             LAG(sequence_number) OVER (                 PARTITION BY business_unit_id, business_date, device_id                  ORDER BY sequence_number             ) AS prev_sequence         FROM filtered_data     ),      missing_sequences AS (         SELECT              business_unit_id,             business_date,             device_id,             prev_sequence + 1 AS missing_sequence_start,             sequence_number - 1 AS missing_sequence_end         FROM sequenced         WHERE sequence_number - prev_sequence > 1     )      SELECT          business_unit_id,         business_date,         device_id,         missing_sequence_start,         missing_sequence_end     FROM missing_sequences     ORDER BY business_unit_id, business_date, device_id, missing_sequence_start; END
```

