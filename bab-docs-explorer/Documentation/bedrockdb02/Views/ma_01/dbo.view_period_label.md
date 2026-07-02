# dbo.view_period_label

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_period_label"]
    dbo_period_label(["dbo.period_label"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.period_label |

## View Code

```sql
create view dbo.view_period_label
AS
select 1 period, period_label1 period_label
from dbo.period_label
union all
select 2 period, period_label2
from dbo.period_label
union all
select 3 period, period_label3
from dbo.period_label
union all
select 4 period, period_label4
from dbo.period_label
union all
select 5 period, period_label5
from dbo.period_label
union all
select 6 period, period_label6
from dbo.period_label
union all
select 7 period, period_label7
from dbo.period_label
union all
select 8 period, period_label8
from dbo.period_label
union all
select 9 period, period_label9
from dbo.period_label
union all
select 10 period, period_label10
from dbo.period_label
union all
select  11 period, period_label11
from dbo.period_label
union all
select 12 period, period_label12
from dbo.period_label

dbo,view_plan_group_chn_pd,/*
Feng May 21, 2010 Multi - Currency mod, add dummy column element_local_value = element_value 
					in order to match with the number of columns in view_plan_group_loc_pd

*/

create view dbo.view_plan_group_chn_pd 
AS
select  p.otb_element_id,a.hierarchy_group_id, a.merch_year_pd,
sum(a.plan_value * p.otb_operator) element_value,
sum(a.plan_local_value * p.otb_operator) element_local_value
from plan_group_chn_pd a, plan_element p , plan_version v
where
a.plan_element_id = p.plan_element_id
and p.otb_element_id is NOT NULL
and v.plan_version_id = a.plan_version_id
and v.current_plan_flag =1
group by p.otb_element_id, a.hierarchy_group_id,a.merch_year_pd
union all
select  p.otb_element_id +3,a.hierarchy_group_id,  d.merch_year_pd ,
sum(a.plan_value * p.otb_operator) element_value,
sum(a.plan_local_value * p.otb_operator) element_local_value
from plan_group_chn_pd a, plan_element p , plan_version v,
 view_calendar_merch_pd_rel c,view_calendar_merch_pd_rel d
where
p.otb_element_id between 7 and 10
and a.plan_element_id = p.plan_element_id
and p.otb_element_id is NOT NULL
and v.plan_version_id = a.plan_version_id
and v.current_plan_flag =1
and a.merch_year_pd = c.merch_year_pd
and c.relative_period = d.relative_period -1
group by p.otb_element_id, a.hierarchy_group_id,d.merch_year_pd
UNION ALL
select 13 otb_element,a.hierarchy_group_id , a.merch_year_pd, sum ( a.oh_bow_units + a.net_rcpt_wk_to_dt_units +
+ a.net_trsfrs_wk_to_dt_units + a.net_dist_wk_to_dt_units+ a.on_order_units
 - a.proj_reds_units) element_value,
sum ( a.oh_bow_units + a.net_rcpt_wk_to_dt_units +
+ a.net_trsfrs_wk_to_dt_units + a.net_dist_wk_to_dt_units+ a.on_order_units
 - a.proj_reds_units) element_local_value
from  (select a.hierarchy_group_id, a.merch_year_pd,
ISNULL ( b.oh_bow_units,0)oh_bow_units,
ISNULL (c.net_rcpt_wk_to_dt_units,0)net_rcpt_wk_to_dt_units,
ISNULL (c.net_trsfrs_wk_to_dt_units,0) net_trsfrs_wk_to_dt_units,
ISNULL (c.net_dist_wk_to_dt_units,0)net_dist_wk_to_dt_units,
ISNULL (d.on_order_units,0)on_order_units,
ISNULL (e.proj_reds_units,0)proj_reds_units
from plan_group_chn_pd a
 left join view_otb_oh_bow b
on a.hierarchy_group_id = b.hierarchy_group_id
 left join view_otb_hist c
on a.hierarchy_group_id = c.hierarchy_group_id
 left join view_otb_on_order d
on a.hierarchy_group_id = d.hierarchy_group_id
and a.merch_year_pd=d.merch_year_pd
left join view_otb_proj_reductions e
on a.hierarchy_group_id = e.hierarchy_group_id
and a.merch_year_pd = e.merch_year_pd
group by a.hierarchy_group_id ,a.merch_year_pd, b.oh_bow_units,c.net_rcpt_wk_to_dt_units,
c.net_trsfrs_wk_to_dt_units,c.net_dist_wk_to_dt_units,on_order_units,
e.proj_reds_units) a ,post_parameter p
where p.parameter_id =11
and a.merch_year_pd >= parameter_value
group by a.hierarchy_group_id ,a.merch_year_pd
UNION ALL
select 14 otb_element,a.hierarchy_group_id , a.merch_year_pd, sum ( a.oh_bow_retail + a.net_rcpt_wk_to_dt_retail +
+ a.net_trsfrs_wk_to_dt_retail + a.net_dist_wk_to_dt_retail+ a.on_order_retail
 - a.proj_reds_retail) element_value,
 sum ( a.oh_bow_retail + a.net_rcpt_wk_to_dt_retail +
+ a.net_trsfrs_wk_to_dt_retail + a.net_dist_wk_to_dt_retail+ a.on_order_retail
 - a.proj_reds_retail) element_local_value
from  (select a.hierarchy_group_id, a.merch_year_pd,
ISNULL ( b.oh_bow_retail,0)oh_bow_retail,
ISNULL (c.net_rcpt_wk_to_dt_retail,0)net_rcpt_wk_to_dt_retail,
ISNULL (c.net_trsfrs_wk_to_dt_retail,0) net_trsfrs_wk_to_dt_retail,
ISNULL (c.net_dist_wk_to_dt_retail,0)net_dist_wk_to_dt_retail,
ISNULL (d.on_order_retail,0)on_order_retail,
ISNULL (e.proj_reds_retail,0)proj_reds_retail
from plan_group_chn_pd a
 left join view_otb_oh_bow b
on a.hierarchy_group_id = b.hierarchy_group_id
 left join view_otb_hist c
on a.hierarchy_group_id = c.hierarchy_group_id
 left join view_otb_on_order d
on a.hierarchy_group_id = d.hierarchy_group_id
and a.merch_year_pd=d.merch_year_pd
left join view_otb_proj_reductions e
on a.hierarchy_group_id = e.hierarchy_group_id
and a.merch_year_pd = e.merch_year_pd
group by a.hierarchy_group_id ,a.merch_year_pd, b.oh_bow_retail,c.net_rcpt_wk_to_dt_retail,
c.net_trsfrs_wk_to_dt_retail,c.net_dist_wk_to_dt_retail,d.on_order_retail,
e.proj_reds_retail) a ,post_parameter p
where p.parameter_id =11
and a.merch_year_pd >= parameter_value
group by a.hierarchy_group_id ,a.merch_year_pd
UNION ALL
select 15 otb_element,a.hierarchy_group_id , a.merch_year_pd, sum ( a.oh_bow_cost + a.net_rcpt_wk_to_dt_cost +
+ a.net_trsfrs_wk_to_dt_cost + a.net_dist_wk_to_dt_cost+ a.on_order_cost
 - a.proj_reds_cost) element_value,
sum ( a.oh_bow_cost + a.net_rcpt_wk_to_dt_cost +
+ a.net_trsfrs_wk_to_dt_cost + a.net_dist_wk_to_dt_cost+ a.on_order_cost
 - a.proj_reds_cost) element_local_value
from  (select a.hierarchy_group_id, a.merch_year_pd,
ISNULL ( b.oh_bow_cost,0)oh_bow_cost,
ISNULL (c.net_rcpt_wk_to_dt_cost,0)net_rcpt_wk_to_dt_cost,
ISNULL (c.net_trsfrs_wk_to_dt_cost,0) net_trsfrs_wk_to_dt_cost,
ISNULL (c.net_dist_wk_to_dt_cost,0)net_dist_wk_to_dt_cost,
ISNULL (d.on_order_cost,0)on_order_cost,
ISNULL (e.proj_reds_cost,0)proj_reds_cost
from plan_group_chn_pd a
 left join view_otb_oh_bow b
on a.hierarchy_group_id = b.hierarchy_group_id
 left join view_otb_hist c
on a.hierarchy_group_id = c.hierarchy_group_id
 left join view_otb_on_order d
on a.hierarchy_group_id = d.hierarchy_group_id
and a.merch_year_pd=d.merch_year_pd
left join view_otb_proj_reductions e
on a.hierarchy_group_id = e.hierarchy_group_id
and a.merch_year_pd = e.merch_year_pd
group by a.hierarchy_group_id ,a.merch_year_pd,  b.oh_bow_cost,c.net_rcpt_wk_to_dt_cost,
c.net_trsfrs_wk_to_dt_cost,c.net_dist_wk_to_dt_cost,d.on_order_cost,
e.proj_reds_cost) a ,post_parameter p
where p.parameter_id =11
and a.merch_year_pd >= parameter_value
group by a.hierarchy_group_id ,a.merch_year_pd
UNION ALL
select 16 otb_element,a.hierarchy_group_id , a.merch_year_pd, sum ( a.oh_bow_units + a.net_rcpt_wk_to_dt_units +
+ a.net_trsfrs_wk_to_dt_units + a.net_dist_wk_to_dt_units+ a.allocation_units
 - a.proj_reds_units) element_value,
sum ( a.oh_bow_units + a.net_rcpt_wk_to_dt_units +
+ a.net_trsfrs_wk_to_dt_units + a.net_dist_wk_to_dt_units+ a.allocation_units
 - a.proj_reds_units) element_local_value
from  (select a.hierarchy_group_id, a.merch_year_pd,
ISNULL ( b.oh_bow_units,0)oh_bow_units,
ISNULL (c.net_rcpt_wk_to_dt_units,0)net_rcpt_wk_to_dt_units,
ISNULL (c.net_trsfrs_wk_to_dt_units,0) net_trsfrs_wk_to_dt_units,
ISNULL (c.net_dist_wk_to_dt_units,0)net_dist_wk_to_dt_units,
ISNULL (d.allocation_units,0)allocation_units,
ISNULL (e.proj_reds_units,0)proj_reds_units
from plan_group_chn_pd a
 left join view_otb_oh_bow b
on a.hierarchy_group_id = b.hierarchy_group_id
 left join view_otb_hist c
on a.hierarchy_group_id = c.hierarchy_group_id
 left join view_otb_on_order d
on a.hierarchy_group_id = d.hierarchy_group_id
and a.merch_year_pd=d.merch_year_pd
left join view_otb_proj_reductions e
on a.hierarchy_group_id = e.hierarchy_group_id
and a.merch_year_pd = e.merch_year_pd
group by a.hierarchy_group_id ,a.merch_year_pd, b.oh_bow_units,c.net_rcpt_wk_to_dt_units,
c.net_trsfrs_wk_to_dt_units,c.net_dist_wk_to_dt_units,allocation_units,
e.proj_reds_units) a ,post_parameter p
where p.parameter_id =11
and a.merch_year_pd >= parameter_value
group by a.hierarchy_group_id ,a.merch_year_pd
UNION ALL
select 17 otb_element,a.hierarchy_group_id , a.merch_year_pd,SUM (a.on_order_units) element_value, SUM (a.on_order_units) element_local_value
from oo_all_group_chn_pd a
group by a.hierarchy_group_id, a.merch_year_pd
UNION ALL
select 18 otb_element,a.hierarchy_group_id , a.merch_year_pd,SUM (a.on_order_retail) element_value, SUM (a.on_order_retail) element_local_value
from oo_all_group_chn_pd a
group by a.hierarchy_group_id, a.merch_year_pd
UNION ALL
select 19 otb_element,a.hierarchy_group_id , a.merch_year_pd,SUM (a.on_order_cost) element_value, SUM (a.on_order_cost) element_local_value
from oo_all_group_chn_pd a
group by a.hierarchy_group_id, a.merch_year_pd
UNION ALL
select 20 otb_element,a.hierarchy_group_id , a.merch_year_pd,SUM (a.allocation_units) element_value, SUM (a.allocation_units) element_local_value
from oo_all_group_chn_pd a
group by a.hierarchy_group_id, a.merch_year_pd
UNION ALL
select 21 otb_element,a.hierarchy_group_id , a.merch_year_pd,SUM (a.on_order_units) element_value, SUM (a.on_order_units) element_local_value
from oo_unc_group_chn_pd a
group by a.hierarchy_group_id, a.merch_year_pd
UNION ALL
select 22 otb_element,a.hierarchy_group_id , a.merch_year_pd,SUM (a.on_order_retail) element_value, SUM (a.on_order_retail) element_local_value
from oo_unc_group_chn_pd a
group by a.hierarchy_group_id, a.merch_year_pd
UNION ALL
select 23 otb_element,a.hierarchy_group_id , a.merch_year_pd,SUM (a.on_order_cost) element_value, SUM (a.on_order_cost) element_local_value
from oo_unc_group_chn_pd a
group by a.hierarchy_group_id, a.merch_year_pd
```

