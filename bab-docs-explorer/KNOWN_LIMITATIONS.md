# Known Limitations — SSIS Package Extraction

> **STATUS: RESOLVED (2026-07-06).** All six gaps below are now addressed by
> `GenerateSsisDocs.py` (repo root), which re-extracts every `.ispac` in the
> Inventory directly from the `.dtsx` XML and regenerates the SSIS package docs.
> `describe-package` and `search-all` now expose SSIS Variables and Execute SQL
> Task bodies. Verified: `search-all "SkinsUnits"` now returns
> `HR_StoreForcePosSalesExtract` (was zero matches), and the Control Flow Outline
> shows `Data Flow from Store Stage` running *before* `PreStage GiftCardBonus`
> inside each `SEQ n\Foreach Loop Container` iteration.
>
> | # | Gap | Fix |
> |---|---|---|
> | 1 | Variables not extracted | New `## Variables` section with full expression + evaluated value; scanned by `search-all` |
> | 2 | Execute SQL Task bodies missing | New `## Execute SQL Tasks` section with full `SqlStatementSource` + property-expression overrides flagged |
> | 3 | SQL truncated | Full SQL, no truncation |
> | 4 | Component name blank | `Component` column populated from `<component name>` + owning Data Flow Task |
> | 5 | No per-component connection / connstrings | Connection Managers table now shows server/catalog (credentials stripped); components list their connection |
> | 6 | Control flow flattens loop nesting | New `## Control Flow Outline` (indented by refId depth) + unique mermaid node IDs + precedence edges |
>
> To regenerate after an inventory refresh: `py GenerateSsisDocs.py` then copy
> `Documentation/<server>/SSIS` into `bab-docs-explorer/Documentation/<server>/SSIS`.
>
> _Original analysis preserved below for reference._

---

Found while investigating ticket 104344 (StoreForce daily file: incorrect `SkinsUnits`, missing Gift Card Bonus KPIs). The root cause of both bugs lived inside `HR_StoreForcePosSalesExtract.dtsx`, and none of it was reachable through `describe-package` / `search-all` — only opening the raw `.ispac` (a zip containing the real `.dtsx` XML) surfaced it. Documented here so the extraction script can be improved instead of everyone re-discovering this the hard way.

## 1. SSIS package Variables are not extracted at all (the big one)

**What's missing:** `<DTS:Variable>` elements — specifically ones with `EvaluateAsExpression="True"` and a `<DTS:VariableValue>` — are never read by the doc generator.

**Why it matters:** Several packages store their real working SQL in a variable, then bind a component's `SqlCommand` property to that variable via a property expression, rather than putting literal SQL in the component itself. In `HR_StoreForcePosSalesExtract`, the entire per-store sales computation (including the `SkinsFlag`/`SkinsUnits` department-code classification that caused the ticket's "incorrect data" bug) lived in a variable named `SQL_StoreDataFlowQuery`. It never showed up in `describe-package`'s "Data Flow: Sources" table because that table only reflects the literal `SqlCommand` property, which was blank/expression-bound in this case.

**Evidence:** `search-all "SkinsUnits"` returned **zero matches** across all 3 servers, even though the string appears 325 times in the raw `.dtsx`. The content was never indexed — no query phrasing would have found it.

**Suggested fix:** When parsing a package, also walk every `<DTS:Variable>` node. For each one with `DTS:EvaluateAsExpression="True"`, capture the `<DTS:VariableValue>` text (this is the pre-evaluated literal SQL/expression result, already HTML-entity-decoded in the XML) and include it in the package's markdown doc, e.g. under a new "## Variables" section, and make it part of what `search-all` scans.

## 2. Execute SQL Task command bodies inside packages are not captured

**What's missing:** `describe-package`'s Control Flow Tasks table lists task name + type only. For `Microsoft.ExecuteSQLTask` nodes, the actual `SQLTask:SqlStatementSource` text is never extracted.

**Why it matters:** This is where the ticket's Gift Card Bonus bug logic lived — a task named "PreStage GiftCardBonus" computes `GiftCardBonusValue`/`Units`/`Qualifying` from raw POS transaction tables using threshold values pulled from `STORE_TEXT_VARIABLE`. The task only showed up as a bare name; the SQL text (and the bug candidates in it) were invisible.

**Note:** this is inconsistent with SQL Agent Job handling — `describe-job` *does* capture full T-SQL for each job step. The same extraction logic just isn't applied to `Microsoft.ExecuteSQLTask` executables nested inside a `.dtsx`.

**Suggested fix:** Reuse the job-step SQL extraction logic for any `DTS:Executable` with `DTS:ExecutableType="Microsoft.ExecuteSQLTask"`, pulling `SQLTask:SqlStatementSource` (and noting if it's overridden by a `DTS:PropertyExpression DTS:Name="SqlStatementSource"`, which takes precedence at runtime — several tasks in this package used that pattern).

## 3. SQL previews are truncated

**What's missing:** The "SQL Preview" column in Data Flow Sources cuts off after roughly 200 characters.

**Why it matters:** Any query longer than a couple of lines (the norm here — most are 50-200+ lines with CTEs) gets cut off before reaching the meaningful logic (WHERE clauses, CASE statements, JOIN conditions).

**Suggested fix:** Either store the full SQL text (these are markdown files, not a constrained-width UI — no reason to truncate) or at minimum raise the preview limit substantially and note that it's truncated with a pointer to view the full text.

## 4. Data Flow "Component" name is blank in every package doc

**What's missing:** Every row in "Data Flow: Sources" and "Data Flow: Destinations" has an empty `Component` column, in 100% of package docs (verified across multiple unrelated packages, not just this one).

**Why it matters:** Without a component name, there's no way to associate a given SQL preview or destination table with *which* named OLE DB Source/Destination/transformation it came from, or which Data Flow Task it belongs to (a package can have several data flows, as this one does — 5 duplicate "Data Flow from Store Stage" instances plus others).

**Suggested fix:** Populate `Component` from the `name` attribute of the `<component>` XML element (e.g. `GiftCardBonus`, `Merge Join 2`, `HR_StoreForcePosSalesStage`). Also worth capturing the owning Data Flow Task's path (e.g. `SEQ 1\Foreach Loop Container\Data Flow from Store Stage`) since names repeat across loop iterations.

## 5. No per-component connection manager binding

**What's missing:** Which connection manager a specific OLE DB Source/Destination actually uses.

**Why it matters:** Needed to confirm, e.g., that the `GiftCardBonus` OLE DB Source reads via the `StoreServer1` connection manager (same one "PreStage GiftCardBonus" writes through) — this was the key fact that exposed the task-ordering bug (the consumer and producer share a connection but run in the wrong order within the same loop iteration). Also needed to resolve that this package's `DW`/`DWStaging` connection managers physically point to a server named `papamart` (`Data Source=papamart;Initial Catalog=dw`) — none of that is visible via `describe-package`, only connection manager *names*, not connection strings.

**Suggested fix:** For each connection manager, capture the resolved `DTS:ConnectionString` (server/catalog only — the extractor already handles credentials safely elsewhere, e.g. passwords are encrypted blobs in the XML). For each Data Flow component, capture which connection manager `refId` it binds to.

## 6. Control flow diagram flattens loop nesting, hiding execution order bugs

**What's missing:** The Mermaid architecture diagram dedupes nodes by label — every "Foreach Loop Container" across the whole package renders as the same visual node, regardless of actual nesting depth.

**Why it matters:** This is what hid the real ordering bug for over an hour of investigation: "PreStage GiftCardBonus" and "Data Flow from Store Stage" are siblings *inside the same per-store loop iteration*, with the data-consuming task running before the data-producing task. The diagram made it look ambiguous whether these ran once globally or once per store, and in what relative order. The only way to confirm true nesting was comparing `refId` path strings in the raw XML (e.g. `Package\SEQ - All Store Sales Stage\SEQ 1\Foreach Loop Container\Data Flow from Store Stage` vs `...\Foreach Loop Container\PreStage GiftCardBonus`).

**Suggested fix:** Give each executable a unique node ID based on its full `refId` path (not just its display label) so loop-nested siblings render distinctly, or add an indented text outline of the control flow (task name + depth) as a supplement to the Mermaid diagram.

---

**Overall takeaway:** the extractor is solid for *structural* lineage (which job runs which package, which package touches which table) but has a blind spot for *business logic* — anything living in an SSIS Variable or an Execute SQL Task body inside a `.dtsx` is currently invisible to every command in this skill. Both bugs in ticket 104344 lived in exactly those two places.
