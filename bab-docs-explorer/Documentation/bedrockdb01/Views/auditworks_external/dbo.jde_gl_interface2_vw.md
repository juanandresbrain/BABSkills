# dbo.jde_gl_interface2_vw

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.jde_gl_interface2_vw"]
    jde_gl_interface2(["jde_gl_interface2"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| jde_gl_interface2 |

## View Code

```sql
create view dbo.jde_gl_interface2_vw  AS
SELECT
  vnone, vnedus, vnedty, vnedsq, vnedtn, vnedct, vnedln, vnedts, vnedft, vneddt, vneder, vneddl,
  vnedsp, vnedtc, vnedtr, vnedbt, vnedgl, vnedan, vnkco, vndct, vndoc, vndgj, vnjeln,
  vnextl, vnpost, vnicu, vnicut, vndicj, vndsyj, vnticu, vnco, vnani, vnam, vnaid, vnmcu,
  vnobj, vnsub, vnsbl, vnsblt, vnlt, vnpn, vnctry, vnfy, vnfq, vncrcd, vncrr, vnhcrr,
  vnhdgj, vnaa, vnu, vnum, vnglc, vnre, vnexa, vnexr, vnr1, vnr2, vnr3,
  vnsfx, vnodoc, vnodct, vnosfx, vnpkco, vnokco, vnpdct, vnan8, vncn, vndkj, vndkc,
  vnasid, vnbre, vnrcnd, vnsumm, vnprge, vntnn, vnalt1, vnalt2, vnalt3, vnalt4, vnalt5,
  vnalt6, vnalt7, vnalt8, vnalt9, vnalt0, vnaltt, vnaltu, vnaltv, vnaltw, vnaltx, vnaltz,
  vndlna, vncff1, vncff2, vnasm, vnbc, vnvinv, vnivd, vnwr01, vnpo, vnpsfx, vndcto,
  vnlnid, vnwy, vnwn, vnfnlp, vnopsq, vnjbcd, vnjbst, vnhmcu, vndoi, vnalid, vnalty,
  vndsvj, vntorg, vnregnum, vnpyid, vnuser, vnpid, vnjobn, vnupmj, vnupmt, vncrrm
FROM jde_gl_interface2
```

