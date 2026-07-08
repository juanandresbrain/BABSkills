# SSIS Package: WM_MoveInventoryFromProdToTest

**Project:** WM_MoveInventoryFromProdToTest  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| WMProd | OLEDB | wmdb01 | WMPROD | Data Source=wmdb01; Initial Catalog=WMPROD; Provider=SQLNCLI10.1; Integrated Security=SSPI; Auto Translate=False |
| WMTest | OLEDB | wmdbtest | PKMSTEST | Data Source=wmdbtest; Initial Catalog=PKMSTEST; Provider=SQLNCLI10.1; Integrated Security=SSPI; Application Name=SSIS-WM_MoveInventoryFromProdToTest-{2D6BFB12-58FB-4C79-AACC-611713E795E4}wmdbtest.PKMSTEST; Auto Translate=False |

## Control Flow Tasks

| Task | Type |
|---|---|
| WM_MoveInventoryFromProdToTest | Package |
| WM Case Detail | Pipeline |
| WM Case Header | Pipeline |

## Control Flow Outline

```text
- WM Case Detail [Pipeline]
- WM Case Header [Pipeline]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_WM_Case_Detail["WM Case Detail"]
    n_Package_WM_Case_Header["WM Case Header"]
```

## Variables

_None detected._

## Execute SQL Tasks

_None detected._

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| WM Prod Case Detail |  | OLEDBSource | WM Case Detail | WMProd | SqlCommand |
| WM Prod Case Header |  | OLEDBSource | WM Case Header | WMProd | SqlCommand |

#### WM Prod Case Detail — SqlCommand

```sql
select cd.*
from case_dtl cd with (nolock)
join case_hdr ch with (nolock) on cd.case_nbr = ch.case_nbr
join locn_hdr lh with (nolock) on ch.locn_id = lh.locn_id 
and (lh.work_grp <> 'web' or lh.work_grp is null)
where ch.stat_code = 30
```

#### WM Prod Case Header — SqlCommand

```sql
select ch.*
from case_hdr ch with (nolock) 
join locn_hdr lh with (nolock) on ch.locn_id = lh.locn_id 
and (lh.work_grp <> 'web' or lh.work_grp is null)
where ch.stat_code = 30
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| WM Test Case Detail |  | OLEDBDestination | WM Case Detail | WMTest |  |
| WM Test Case Header |  | OLEDBDestination | WM Case Header | WMTest |  |
