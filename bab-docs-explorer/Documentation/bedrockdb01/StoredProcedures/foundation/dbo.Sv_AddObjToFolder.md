# dbo.Sv_AddObjToFolder

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_AddObjToFolder"]
    Sv_FolderItem(["Sv_FolderItem"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sv_FolderItem |

## Stored Procedure Code

```sql
create proc Sv_AddObjToFolder @TopicID int, @UserID int, @TargetFolderID int, 
@ObjectType int, @ObjectID int, 
@default_data_view varchar(1), @output_data varchar(100), 
@crosstab_data varchar(100), @graph_data varchar(100)
AS
DECLARE @NextSequence int,
	@result int
	
	SELECT @result = 0
        
	SELECT @NextSequence = ISNULL(MAX(item_sequence),0) + 1
		FROM Sv_FolderItem
		WHERE folder_id = @TargetFolderID
		
	INSERT into Sv_FolderItem (folder_id, item_sequence, item_type, item_id, 
			   default_data_view, output_data, crosstab_data, graph_data)
		Values (@TargetFolderID, @NextSequence,  @ObjectType , @ObjectID, 
			@default_data_view , @output_data, @crosstab_data , @graph_data )
				
	SELECT @result = @NextSequence
RETURN @result
```

