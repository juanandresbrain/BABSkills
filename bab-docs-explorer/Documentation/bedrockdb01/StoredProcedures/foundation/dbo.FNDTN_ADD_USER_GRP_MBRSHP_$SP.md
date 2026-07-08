# dbo.FNDTN_ADD_USER_GRP_MBRSHP_$SP

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_ADD_USER_GRP_MBRSHP_$SP"]
    FNDTN_SCRTY_GRP_USER(["FNDTN_SCRTY_GRP_USER"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SCRTY_GRP_USER |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_ADD_USER_GRP_MBRSHP_$SP 

(
  @i_group_id int,
  @i_user_id  int
)
AS

BEGIN

  IF NOT EXISTS (SELECT 1 
                   FROM FNDTN_SCRTY_GRP_USER 
                  WHERE GRP_ID  = @i_group_id 
                    AND USER_ID = @i_user_id)
    INSERT INTO FNDTN_SCRTY_GRP_USER (GRP_ID, USER_ID) VALUES (@i_group_id, @i_user_id)

END
```

