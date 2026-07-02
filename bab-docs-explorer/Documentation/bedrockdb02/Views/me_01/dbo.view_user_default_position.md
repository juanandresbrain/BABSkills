# dbo.view_user_default_position

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_user_default_position"]
    dbo_entity_position(["dbo.entity_position"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.entity_position |

## View Code

```sql
CREATE view [dbo].[view_user_default_position]
AS

/* View that contains the users default or only assigned possition */

                           SELECT ep.parent_id as user_id, ep.position_id 
                             FROM (SELECT parent_id, COUNT(position_id) AS pos_count 
                                     FROM dbo.[entity_position]
                                     WHERE (parent_type = 4) 
                                     GROUP BY parent_id) AS pc INNER JOIN 
                                     dbo.[entity_position] AS ep ON ep.parent_id = pc.parent_id 
                             WHERE (pc.pos_count = 1) And (ep.parent_type = 4) And (ep.default_position_flag = 0) 
                             UNION 
                             SELECT parent_id, position_id 
                             FROM dbo.[entity_position]
                             WHERE (default_position_flag = 1) AND (parent_type = 4)
```

