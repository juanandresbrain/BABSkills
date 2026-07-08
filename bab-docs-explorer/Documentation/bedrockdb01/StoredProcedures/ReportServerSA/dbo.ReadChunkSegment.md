# dbo.ReadChunkSegment

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ReadChunkSegment"]
    ChunkSegmentMapping(["ChunkSegmentMapping"]) --> SP
    dbo_ChunkSegmentMapping(["dbo.ChunkSegmentMapping"]) --> SP
    Segment(["Segment"]) --> SP
    dbo_Segment(["dbo.Segment"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ChunkSegmentMapping |
| dbo.ChunkSegmentMapping |
| Segment |
| dbo.Segment |

## Stored Procedure Code

```sql
create proc [dbo].[ReadChunkSegment]
	@ChunkId		uniqueidentifier,
	@SegmentId		uniqueidentifier,
	@IsPermanent	bit, 
	@DataIndex		int,
	@Length			int
as begin
	if(@IsPermanent = 1) begin	
		select substring(seg.Content, @DataIndex + 1, @Length) as [Content]
		from Segment seg
		join ChunkSegmentMapping csm on (csm.SegmentId = seg.SegmentId)
		where csm.ChunkId = @ChunkId and csm.SegmentId = @SegmentId
	end
	else begin
		select substring(seg.Content, @DataIndex + 1, @Length) as [Content]
		from [ReportServerSATempDB].dbo.Segment seg
		join [ReportServerSATempDB].dbo.ChunkSegmentMapping csm on (csm.SegmentId = seg.SegmentId)
		where csm.ChunkId = @ChunkId and csm.SegmentId = @SegmentId
	end
end
```

