# dbo.Sv_AddObjToFolderFromFolder

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sv_AddObjToFolderFromFolder"]
    Sv_FolderItem(["Sv_FolderItem"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Sv_FolderItem |

## Stored Procedure Code

```sql
create proc Sv_AddObjToFolderFromFolder @TopicID int, @UserID int, @TargetFolderID int, 
@ObjectType int, @ObjectID int, @ParentFolderID int,
@SourceSequence int
AS
DECLARE @NextSequence int,
	@result int
	
	SELECT @result = 0
        
	SELECT @NextSequence = ISNULL(MAX(item_sequence),0) + 1
		FROM Sv_FolderItem
		WHERE folder_id = @TargetFolderID
		
	INSERT into Sv_FolderItem (folder_id, item_sequence, item_type, item_id, 
			   default_data_view, output_data, crosstab_data, graph_data)
		SELECT @TargetFolderID, @NextSequence,  @ObjectType , @ObjectID, 
			a.default_data_view , a.output_data, a.crosstab_data , a.graph_data
			FROM Sv_FolderItem a
			WHERE a.folder_id = @ParentFolderID
		          AND a.item_sequence = @SourceSequence
	SELECT @result = @NextSequence
        
RETURN @result
```

