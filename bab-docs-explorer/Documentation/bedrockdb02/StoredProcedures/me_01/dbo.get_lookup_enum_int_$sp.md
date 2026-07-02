# dbo.get_lookup_enum_int_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_lookup_enum_int_$sp"]
    dbo_enum_resource(["dbo.enum_resource"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.enum_resource |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[get_lookup_enum_int_$sp]
	@enum_type		NVARCHAR(30)
AS


/*
Proc name: 	get_lookup_enum_int_$sp
Description: Get a dataset with enumerations for an enumeration type

HISTORY: 
Date            Name					Desc
March 4, 2013   Maria Van Geeteruyen	Creation
Jul  2, 2013	Maria Van Geeteruyen	Adding sort sequence 
*/


SELECT CONVERT(int, enum) AS enum, resource_name, sort_sequence 
FROM enum_resource WITH (NOLOCK)
WHERE enum_type = @enum_type


RETURN 0
```

