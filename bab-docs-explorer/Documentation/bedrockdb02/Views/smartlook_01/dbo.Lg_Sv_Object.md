# dbo.Lg_Sv_Object

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Lg_Sv_Object"]
    dbo_Lg_DependentDesc(["dbo.Lg_DependentDesc"]) --> VIEW
    dbo_Sv_Object(["dbo.Sv_Object"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Lg_DependentDesc |
| dbo.Sv_Object |

## View Code

```sql
create view dbo.Lg_Sv_Object  AS
	SELECT a.object_id, a.topic_id, a.object_type, a.created_date, a.owner_id, 
		a.modified_date, a.modified_id, a.last_used_date, a.last_used_id, 
		a.label_1, a.label_2, ISNULL(b.first_pair_text, a.label_1) as label_3,
		a.description_1, a.description_2, ISNULL(b.second_pair_text, a.description_1) as description_3,
		a.data, a.flags, a.permission, a.object_code, 
		a.built_by_version, a.version, a.web_access, a.resource_id, b.language_id
	FROM Sv_Object a LEFT OUTER JOIN Lg_DependentDesc b ON a.resource_id = b.resource_id
```

