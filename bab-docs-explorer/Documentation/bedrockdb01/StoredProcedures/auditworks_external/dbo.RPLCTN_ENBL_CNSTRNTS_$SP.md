# dbo.RPLCTN_ENBL_CNSTRNTS_$SP

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPLCTN_ENBL_CNSTRNTS_$SP"]
    CRDM_RPLCTN_LIST(["CRDM_RPLCTN_LIST"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CRDM_RPLCTN_LIST |

## Stored Procedure Code

```sql
CREATE proc [dbo].[RPLCTN_ENBL_CNSTRNTS_$SP]


AS

/*
  Procedure : RPLCTN_ENBL_CNSTRNTS_$SP
  Purpose   : Re-enable constraints after data sync

HISTORY:
Date     Name         Def# Desc
Jul14,14 Ian k             Initial Creation

*/

BEGIN

    DECLARE @cons_name varchar(100);
    DECLARE @sql       nvarchar(1000);    
    
  	DECLARE dis_cons CURSOR FAST_FORWARD FOR
      SELECT a.table_name 
        FROM CRDM_RPLCTN_LIST a;

	OPEN dis_cons;

	FETCH NEXT FROM dis_cons
	INTO @cons_name;

	WHILE @@FETCH_STATUS = 0
	BEGIN
	 
	    SELECT @sql = 'ALTER TABLE ' + @cons_name + ' WITH CHECK CHECK CONSTRAINT ALL';
	
	    EXEC sp_executesql @sql
	    
		FETCH NEXT FROM dis_cons
	     INTO @cons_name;
	     
	END;
	
	CLOSE dis_cons;
	
	DEALLOCATE dis_cons;
	
	RETURN 1;

END
```

