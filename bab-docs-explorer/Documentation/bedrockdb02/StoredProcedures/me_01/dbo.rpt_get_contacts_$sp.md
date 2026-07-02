# dbo.rpt_get_contacts_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_get_contacts_$sp"]
    dbo_contact(["dbo.contact"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.contact |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[rpt_get_contacts_$sp] @parent_type smallint, @parent_id decimal(12, 0)

AS

/*
Proc name:		rpt_get_contacts_$sp
Description:	Gets the contact data for a single entity
*/

SELECT c.contact_description1, c.contact_description2, c.contact_number,
	c.contact_type, c.main_flag, c.contact_id
FROM contact c WITH (NOLOCK)
WHERE c.parent_type = @parent_type AND c.parent_id = @parent_id
ORDER BY c.contact_description1

RETURN 0
```

