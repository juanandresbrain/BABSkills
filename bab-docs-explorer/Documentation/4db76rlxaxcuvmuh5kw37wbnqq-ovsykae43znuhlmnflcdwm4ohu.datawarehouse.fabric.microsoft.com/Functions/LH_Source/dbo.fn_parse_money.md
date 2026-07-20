# dbo.fn_parse_money

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  
**Function Type:** Inline Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_parse_money"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @money_string | varchar | 50 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE   FUNCTION dbo.fn_parse_money (@money_string varchar(50)) RETURNS TABLE AS RETURN SELECT     /* Amount: characters after the first space, parsed as decimal(18,2).        NULL if the string doesn't contain a space (i.e. malformed input). */     CASE         WHEN CHARINDEX(' ', @money_string) > 0 THEN              TRY_CAST(                  SUBSTRING(@money_string,                            CHARINDEX(' ', @money_string) + 1,                            LEN(@money_string))                  AS decimal(18,2))         ELSE TRY_CAST(@money_string AS decimal(18,2))     END                                                  AS amount,     /* Currency: 3-letter ISO code before the first space.        Defaults to NULL if no space (will treat the whole string as numeric). */     CASE         WHEN CHARINDEX(' ', @money_string) > 0 THEN              LEFT(@money_string, CHARINDEX(' ', @money_string) - 1)         ELSE NULL     END                                                  AS currency;
```

