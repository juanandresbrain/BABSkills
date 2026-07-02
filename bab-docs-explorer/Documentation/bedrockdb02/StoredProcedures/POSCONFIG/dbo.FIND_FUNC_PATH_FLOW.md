# dbo.FIND_FUNC_PATH_FLOW

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FIND_FUNC_PATH_FLOW"]
    dbo_FL_FUNCTION(["dbo.FL_FUNCTION"]) --> SP
    dbo_fl_function_path(["dbo.fl_function_path"]) --> SP
    dbo_fl_function_return_target(["dbo.fl_function_return_target"]) --> SP
    dbo_UI_DFLT_EVENT_MAP(["dbo.UI_DFLT_EVENT_MAP"]) --> SP
    dbo_UI_event_map(["dbo.UI_event_map"]) --> SP
    dbo_UI_EVENT_MAP_OVRD_VALUE(["dbo.UI_EVENT_MAP_OVRD_VALUE"]) --> SP
    dbo_UI_Screen(["dbo.UI_Screen"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FL_FUNCTION |
| dbo.fl_function_path |
| dbo.fl_function_return_target |
| dbo.UI_DFLT_EVENT_MAP |
| dbo.UI_event_map |
| dbo.UI_EVENT_MAP_OVRD_VALUE |
| dbo.UI_Screen |

## Stored Procedure Code

```sql

```

