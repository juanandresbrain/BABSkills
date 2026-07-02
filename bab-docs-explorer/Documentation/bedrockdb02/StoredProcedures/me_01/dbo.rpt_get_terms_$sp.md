# dbo.rpt_get_terms_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_get_terms_$sp"]
    dbo_terms(["dbo.terms"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.terms |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[rpt_get_terms_$sp]

AS

/*
Proc name:		rpt_get_terms_$sp
Description:	Gets a list of terms from the terms table
*/

SELECT terms_id, terms_code + N'  ' + terms_description AS description
FROM terms (NOLOCK)
ORDER BY terms_id

RETURN 0
```

