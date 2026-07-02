# dbo.get_crnt_perm_price_no_prec_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_crnt_perm_price_no_prec_$sp"]
    dbo_get_crnt_perm_price_no_prec_out__sp(["dbo.get_crnt_perm_price_no_prec_out_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.get_crnt_perm_price_no_prec_out_$sp |

## Stored Procedure Code

```sql
/*
This Stored proc calls 'get_crnt_perm_price_no_prec_out_$sp' stored proc 
which is replacement of DoGetPermanentPrice(...) from STSIBInfobase.cpp. 
These stored proc are not using precedence rule to return permanent price.

To use start_date field to retrieve permanent price Then set @type = 1 
To use effective_date field to retrieve permanent price Then set @type = 2 

To use pricing_group_id for current retail set @check_price_group = 1 else 
set @check_price_group = 0

To retrieve temporary price, set @temp_price_flag = 1 else 
set @temp_price_flag = 0

Selecting Output Parameters at the end.  
*/
CREATE PROCEDURE [dbo].[get_crnt_perm_price_no_prec_$sp]
@jurisdiction_id SMALLINT, @style_id DECIMAL(12,0), @location_id SMALLINT,
@color_id SMALLINT, @pricing_group_id SMALLINT, @temp_price_flag BIT, 
@check_date SMALLDATETIME, @check_price_group BIT, @type SMALLINT 

AS

DECLARE @valuation_retail_price DECIMAL(14,2), @selling_retail_price DECIMAL(14,2), @price_status_id SMALLINT,
@end_date SMALLDATETIME


EXEC get_crnt_perm_price_no_prec_out_$sp @jurisdiction_id, @style_id, @location_id, 
	@color_id, @pricing_group_id, @temp_price_flag, @check_date, @check_price_group, @type, 
	@valuation_retail_price OUT, @selling_retail_price OUT, 
	@price_status_id OUT, @end_date OUT

Select @valuation_retail_price as valuation_retail_price, @selling_retail_price as selling_retail_price,
@price_status_id as price_status_id, @end_date as end_date

RETURN 0
```

