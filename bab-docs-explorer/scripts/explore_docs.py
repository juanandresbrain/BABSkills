#!/usr/bin/env python3
import os
import re
import sys
import json
import argparse
from pathlib import Path

# Normalization helper
def normalize_name(name):
    if not name:
        return ""
    # Strip brackets, quotes, backticks, parens, spaces
    name = re.sub(r'[\[\]`\'"()_]', '', name.strip())
    return name.lower()

def name_matches(target, query):
    t = normalize_name(target)
    q = normalize_name(query)
    if not t or not q:
        return False
    if t == q:
        return True
    if '.' in t:
        parts = t.split('.')
        if parts[-1] == q:
            return True
    if '.' in q:
        parts = q.split('.')
        if parts[-1] == t:
            return True
    return False

# Parse functions
def parse_table_file(file_path):
    try:
        content = file_path.read_text(encoding='utf-8-sig', errors='ignore')
    except Exception as e:
        return None
    
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    table_name = h1_match.group(1).strip() if h1_match else file_path.stem
    
    db_match = re.search(r'\*\*Database:\*\*\s*(.+)$', content, re.MULTILINE)
    database = db_match.group(1).strip() if db_match else "Unknown"
    
    columns = []
    columns_sec = re.search(r'## Columns\s*\n\s*\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
    if columns_sec:
        table_lines = columns_sec.group(1).strip().split('\n')
        # Skip header and separator
        if len(table_lines) > 2:
            for line in table_lines[2:]:
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if len(parts) >= 4:
                    columns.append({
                        "column": parts[0],
                        "type": parts[1],
                        "max_length": parts[2],
                        "nullable": parts[3],
                        "pk": parts[4] if len(parts) > 4 else "",
                        "fk": parts[5] if len(parts) > 5 else "",
                        "description": parts[6] if len(parts) > 6 else ""
                    })
                    
    return {
        "file_path": str(file_path),
        "table_name": table_name,
        "database": database,
        "columns": columns
    }

def parse_sp_file(file_path):
    try:
        content = file_path.read_text(encoding='utf-8-sig', errors='ignore')
    except Exception as e:
        return None
    
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    sp_name = h1_match.group(1).strip() if h1_match else file_path.stem
    
    db_match = re.search(r'\*\*Database:\*\*\s*(.+)$', content, re.MULTILINE)
    database = db_match.group(1).strip() if db_match else "Unknown"
    
    dependencies = []
    dep_sec = re.search(r'## Table Dependencies\s*\n\s*\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
    if dep_sec:
        table_lines = dep_sec.group(1).strip().split('\n')
        if len(table_lines) > 2:
            for line in table_lines[2:]:
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if parts and parts[0]:
                    dependencies.append(parts[0])
                    
    code_match = re.search(r'## Stored Procedure Code\s*\n\s*\n```sql\s*\n(.*?)\n```', content, re.DOTALL | re.IGNORECASE)
    code = code_match.group(1).strip() if code_match else ""
    
    return {
        "file_path": str(file_path),
        "sp_name": sp_name,
        "database": database,
        "dependencies": dependencies,
        "code": code
    }

def parse_view_file(file_path):
    try:
        content = file_path.read_text(encoding='utf-8-sig', errors='ignore')
    except Exception:
        return None

    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    view_name = h1_match.group(1).strip() if h1_match else file_path.stem

    db_match = re.search(r'\*\*Database:\*\*\s*(.+)$', content, re.MULTILINE)
    database = db_match.group(1).strip() if db_match else "Unknown"

    dependencies = []
    dep_sec = re.search(r'## Table Dependencies\s*\n\s*\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
    if dep_sec:
        table_lines = dep_sec.group(1).strip().split('\n')
        if len(table_lines) > 2:
            for line in table_lines[2:]:
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if parts and parts[0]:
                    dependencies.append(parts[0])

    code_match = re.search(r'## View Code\s*\n\s*\n```sql\s*\n(.*?)\n```', content, re.DOTALL | re.IGNORECASE)
    code = code_match.group(1).strip() if code_match else ""

    return {
        "file_path": str(file_path),
        "view_name": view_name,
        "database": database,
        "dependencies": dependencies,
        "code": code
    }

def parse_package_file(file_path):
    try:
        content = file_path.read_text(encoding='utf-8-sig', errors='ignore')
    except Exception as e:
        return None
    
    h1_match = re.search(r'^#\s+SSIS Package:\s*(.+)$', content, re.MULTILINE)
    package_name = h1_match.group(1).strip() if h1_match else file_path.stem
    
    proj_match = re.search(r'\*\*Project:\*\*\s*(.+)$', content, re.MULTILINE)
    project = proj_match.group(1).strip() if proj_match else "Unknown"
    
    folder_match = re.search(r'\*\*Folder:\*\*\s*(.+)$', content, re.MULTILINE)
    folder = folder_match.group(1).strip() if folder_match else "Unknown"
    
    connections = []
    conn_sec = re.search(r'## Connection Managers\s*\n\s*\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
    if conn_sec:
        table_lines = conn_sec.group(1).strip().split('\n')
        if len(table_lines) > 2:
            for line in table_lines[2:]:
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if len(parts) >= 2:
                    connections.append({
                        "name": parts[0],
                        "type": parts[1]
                    })
                    
    sources = []
    src_sec = re.search(r'## Data Flow:\s*Sources\s*\n\s*\n(.*?)(?=\n\n|\Z)', content, re.DOTALL | re.IGNORECASE)
    if src_sec:
        table_lines = src_sec.group(1).strip().split('\n')
        if len(table_lines) > 2:
            for line in table_lines[2:]:
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if parts and parts[0] and not parts[0].startswith('_') and not parts[0].startswith('|'):
                    sources.append({
                        "component": parts[0],
                        "source_table": parts[1] if len(parts) > 1 else ""
                    })
                    
    destinations = []
    dest_sec = re.search(r'## Data Flow:\s*Destinations\s*\n\s*\n(.*?)(?=\n\n|\Z)', content, re.DOTALL | re.IGNORECASE)
    if dest_sec:
        table_lines = dest_sec.group(1).strip().split('\n')
        if len(table_lines) > 2:
            for line in table_lines[2:]:
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if parts and len(parts) >= 2:
                    destinations.append({
                        "component": parts[0],
                        "destination_table": parts[1]
                    })
                    
    # Control flow tasks list (tasks and type)
    tasks = []
    tasks_sec = re.search(r'## Control Flow Tasks\s*\n\s*\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
    if tasks_sec:
        table_lines = tasks_sec.group(1).strip().split('\n')
        if len(table_lines) > 2:
            for line in table_lines[2:]:
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if len(parts) >= 2:
                    tasks.append({
                        "name": parts[0],
                        "type": parts[1]
                    })
                    
    return {
        "file_path": str(file_path),
        "package_name": package_name,
        "project": project,
        "folder": folder,
        "connections": connections,
        "sources": sources,
        "destinations": destinations,
        "tasks": tasks,
        "raw_content": content
    }

def parse_job_file(file_path):
    try:
        content = file_path.read_text(encoding='utf-8-sig', errors='ignore')
    except Exception as e:
        return None
    
    h1_match = re.search(r'^#\s+Job:\s*(.+)$', content, re.MULTILINE)
    job_name = h1_match.group(1).strip() if h1_match else file_path.stem
    
    enabled_match = re.search(r'\*\*Enabled:\*\*\s*(.+)$', content, re.MULTILINE)
    enabled = enabled_match.group(1).strip() if enabled_match else "Unknown"
    
    steps = []
    steps_sec = content.split('### Step ')
    if len(steps_sec) > 1:
        for step_text in steps_sec[1:]:
            lines = step_text.strip().split('\n')
            step_header = lines[0].strip()
            step_num = "Unknown"
            step_name = step_header
            if ':' in step_header:
                num_part, name_part = step_header.split(':', 1)
                step_num = num_part.strip()
                step_name = name_part.strip()
            
            subsystem = "Unknown"
            subsystem_match = re.search(r'\*\*Subsystem:\*\*\s*(.+)$', step_text, re.MULTILINE)
            if subsystem_match:
                subsystem = subsystem_match.group(1).strip()
                
            code = ""
            code_match = re.search(r'```(?:sql)?\s*\n(.*?)\n```', step_text, re.DOTALL | re.IGNORECASE)
            if code_match:
                code = code_match.group(1).strip()
                
            steps.append({
                "step_num": step_num,
                "step_name": step_name,
                "subsystem": subsystem,
                "command": code
            })
            
    return {
        "file_path": str(file_path),
        "job_name": job_name,
        "enabled": enabled,
        "steps": steps
    }

class DocExplorer:
    def __init__(self, docs_dir):
        self.docs_dir = Path(docs_dir).resolve()
        self.tables = {}
        self.sps = {}
        self.views = {}
        self.packages = {}
        self.jobs = {}
        self._loaded = False
        
    def load_all(self):
        if self._loaded:
            return
        
        # Load tables
        table_dir = self.docs_dir / "DataDictionary"
        if table_dir.exists():
            for f in table_dir.rglob("*.md"):
                if f.name != "_index.md":
                    tbl = parse_table_file(f)
                    if tbl:
                        self.tables[tbl["table_name"]] = tbl
                        
        # Load SPs
        sp_dir = self.docs_dir / "StoredProcedures"
        if sp_dir.exists():
            for f in sp_dir.rglob("*.md"):
                if f.name != "_index.md":
                    sp = parse_sp_file(f)
                    if sp:
                        self.sps[sp["sp_name"]] = sp

        # Load Views
        view_dir = self.docs_dir / "Views"
        if view_dir.exists():
            for f in view_dir.rglob("*.md"):
                if f.name != "_index.md":
                    view = parse_view_file(f)
                    if view:
                        self.views[view["view_name"]] = view
                        
        # Load SSIS Packages
        ssis_dir = self.docs_dir / "SSIS"
        if ssis_dir.exists():
            for f in ssis_dir.rglob("*.md"):
                if f.name != "_index.md":
                    pkg = parse_package_file(f)
                    if pkg:
                        self.packages[pkg["package_name"]] = pkg
                        
        # Load Jobs
        job_dir = self.docs_dir / "Jobs"
        if job_dir.exists():
            for f in job_dir.rglob("*.md"):
                if f.name != "_index.md" and f.name != "test.md":
                    job = parse_job_file(f)
                    if job:
                        self.jobs[job["job_name"]] = job
                        
        self._loaded = True

    def find_table(self, query):
        self.load_all()
        results = []
        for name, tbl in self.tables.items():
            if name_matches(name, query):
                results.append(tbl)
        return results

    def find_sp(self, query):
        self.load_all()
        results = []
        for name, sp in self.sps.items():
            if name_matches(name, query):
                results.append(sp)
        return results

    def find_view(self, query):
        self.load_all()
        results = []
        for name, view in self.views.items():
            if name_matches(name, query):
                results.append(view)
        return results

    def find_package(self, query):
        self.load_all()
        results = []
        for name, pkg in self.packages.items():
            if name_matches(name, query):
                results.append(pkg)
        return results

    def find_job(self, query):
        self.load_all()
        results = []
        for name, job in self.jobs.items():
            if name_matches(name, query):
                results.append(job)
        return results

    def trace_table(self, query):
        self.load_all()
        
        # 1. Matching Tables
        matching_tables = [t["table_name"] for t in self.find_table(query)]
        if not matching_tables:
            # Fallback to direct query search if no exact table found
            matching_tables = [query]
            
        trace_results = {
            "query": query,
            "matched_tables": matching_tables,
            "stored_procedures": [],
            "ssis_packages": [],
            "sql_agent_jobs": []
        }
        
        for table in matching_tables:
            # 2. Check Stored Procedures
            for sp_name, sp in self.sps.items():
                is_dep = any(name_matches(dep, table) for dep in sp["dependencies"])
                in_code = False
                if not is_dep:
                    norm_table = normalize_name(table)
                    norm_code = normalize_name(sp["code"])
                    if norm_table in norm_code:
                        in_code = True
                if is_dep or in_code:
                    trace_results["stored_procedures"].append({
                        "name": sp_name,
                        "file_path": sp["file_path"],
                        "database": sp["database"],
                        "type": "dependency_table" if is_dep else "referenced_in_code"
                    })

            # 2b. Check Views
            trace_results.setdefault("views", [])
            for view_name, view in self.views.items():
                is_dep = any(name_matches(dep, table) for dep in view["dependencies"])
                in_code = False
                if not is_dep:
                    norm_table = normalize_name(table)
                    norm_code = normalize_name(view["code"])
                    if norm_table in norm_code:
                        in_code = True
                if is_dep or in_code:
                    trace_results["views"].append({
                        "name": view_name,
                        "file_path": view["file_path"],
                        "database": view["database"],
                        "type": "dependency_table" if is_dep else "referenced_in_code"
                    })
                    
            # 3. Check SSIS Packages
            for pkg_name, pkg in self.packages.items():
                is_dest = any(name_matches(d["destination_table"], table) for d in pkg["destinations"])
                is_src = any(name_matches(s["source_table"], table) for s in pkg["sources"])
                in_content = False
                if not is_dest and not is_src:
                    norm_table = normalize_name(table)
                    norm_content = normalize_name(pkg["raw_content"])
                    if norm_table in norm_content:
                        in_content = True
                if is_dest or is_src or in_content:
                    role = []
                    if is_dest: role.append("destination")
                    if is_src: role.append("source")
                    if in_content and not role: role.append("text_reference")
                    trace_results["ssis_packages"].append({
                        "name": pkg_name,
                        "project": pkg["project"],
                        "folder": pkg["folder"],
                        "file_path": pkg["file_path"],
                        "role": ", ".join(role)
                    })
                    
            # 4. Check SQL Agent Jobs
            for job_name, job in self.jobs.items():
                matched_steps = []
                for step in job["steps"]:
                    norm_table = normalize_name(table)
                    norm_cmd = normalize_name(step["command"])
                    if norm_table in norm_cmd:
                        matched_steps.append({
                            "step_num": step["step_num"],
                            "step_name": step["step_name"],
                            "subsystem": step["subsystem"]
                        })
                if matched_steps:
                    trace_results["sql_agent_jobs"].append({
                        "name": job_name,
                        "file_path": job["file_path"],
                        "enabled": job["enabled"],
                        "steps": matched_steps
                    })
                    
        return trace_results

    def trace_lineage(self, query):
        self.load_all()
        # Full recursive mapping of what writes to/executes what upstream
        trace = self.trace_table(query)
        
        lineage_tree = {
            "target": query,
            "tables": trace["matched_tables"],
            "upstream_paths": []
        }
        
        # Helper to find which jobs run an SSIS package
        def find_jobs_running_package(pkg_name):
            runners = []
            for job_name, job in self.jobs.items():
                for step in job["steps"]:
                    if step["subsystem"].lower() == "ssis":
                        # Check command for package name
                        if pkg_name.lower() in step["command"].lower():
                            runners.append((job_name, f"Step {step['step_num']}: {step['step_name']} (SSIS)"))
                    elif step["subsystem"].lower() == "tsql":
                        # Sometimes run via DTEXEC or dynamic query, search text
                        if pkg_name.lower() in step["command"].lower():
                            runners.append((job_name, f"Step {step['step_num']}: {step['step_name']} (TSQL command)"))
            return runners

        # Helper to find which SSIS tasks run an SP
        def find_packages_running_sp(sp_name):
            runners = []
            sp_base = sp_name.split('.')[-1].lower()
            for pkg_name, pkg in self.packages.items():
                for task in pkg["tasks"]:
                    if sp_base in task["name"].lower():
                        runners.append((pkg_name, f"Task: {task['name']}"))
                # Also check destinations or raw content if not found
                if not any(sp_base in task["name"].lower() for task in pkg["tasks"]):
                    if sp_base in pkg["raw_content"].lower():
                        runners.append((pkg_name, "Reference in package text"))
            return runners

        # Helper to find which jobs run an SP directly
        def find_jobs_running_sp(sp_name):
            runners = []
            sp_base = sp_name.split('.')[-1].lower()
            for job_name, job in self.jobs.items():
                for step in job["steps"]:
                    if sp_base in step["command"].lower():
                        runners.append((job_name, f"Step {step['step_num']}: {step['step_name']} (TSQL)"))
            return runners

        # Helper to find which jobs trigger other jobs
        def find_jobs_triggering_job(target_job_name):
            triggers = []
            for job_name, job in self.jobs.items():
                if job_name == target_job_name:
                    continue
                for step in job["steps"]:
                    if "sp_start_job" in step["command"].lower() and target_job_name.lower() in step["command"].lower():
                        triggers.append((job_name, f"Step {step['step_num']}: {step['step_name']}"))
            return triggers

        # Build paths for each matching SSIS package
        for pkg in trace["ssis_packages"]:
            path = {
                "type": "SSIS Package",
                "name": pkg["name"],
                "role": pkg["role"],
                "triggers": []
            }
            # Find jobs running this package
            jobs = find_jobs_running_package(pkg["name"])
            for j_name, step_info in jobs:
                j_node = {
                    "type": "SQL Agent Job",
                    "name": j_name,
                    "trigger_step": step_info,
                    "upstream_jobs": []
                }
                # Find jobs triggering this job
                up_jobs = find_jobs_triggering_job(j_name)
                for up_name, up_step in up_jobs:
                    j_node["upstream_jobs"].append({
                        "name": up_name,
                        "step": up_step
                    })
                path["triggers"].append(j_node)
            lineage_tree["upstream_paths"].append(path)

        # Build paths for each matching Stored Procedure
        for sp in trace["stored_procedures"]:
            path = {
                "type": "Stored Procedure",
                "name": sp["name"],
                "database": sp["database"],
                "triggers": []
            }
            # Find packages running this SP
            pkgs = find_packages_running_sp(sp["name"])
            for p_name, task_info in pkgs:
                p_node = {
                    "type": "SSIS Package",
                    "name": p_name,
                    "task": task_info,
                    "jobs": []
                }
                # Find jobs running this package
                jobs = find_jobs_running_package(p_name)
                for j_name, step_info in jobs:
                    j_node = {
                        "name": j_name,
                        "step": step_info,
                        "upstream_jobs": []
                    }
                    up_jobs = find_jobs_triggering_job(j_name)
                    for up_name, up_step in up_jobs:
                        j_node["upstream_jobs"].append({
                            "name": up_name,
                            "step": up_step
                        })
                    p_node["jobs"].append(j_node)
                p_node["untriggered"] = len(jobs) == 0
                path["triggers"].append(p_node)
                
            # Find jobs running this SP directly
            direct_jobs = find_jobs_running_sp(sp["name"])
            for j_name, step_info in direct_jobs:
                j_node = {
                    "type": "Direct SQL Agent Job",
                    "name": j_name,
                    "step": step_info,
                    "upstream_jobs": []
                }
                up_jobs = find_jobs_triggering_job(j_name)
                for up_name, up_step in up_jobs:
                    j_node["upstream_jobs"].append({
                        "name": up_name,
                        "step": up_step
                    })
                path["triggers"].append(j_node)
                
            lineage_tree["upstream_paths"].append(path)

        # Direct Job steps referencing table
        for job in trace["sql_agent_jobs"]:
            # Check if this job triggers others or runs SSIS or is already listed
            already_mapped = False
            for path in lineage_tree["upstream_paths"]:
                for trigger in path.get("triggers", []):
                    if trigger.get("name") == job["name"] or any(uj["name"] == job["name"] for uj in trigger.get("upstream_jobs", [])):
                        already_mapped = True
            if not already_mapped:
                path = {
                    "type": "Direct SQL Agent Job Step Reference",
                    "name": job["name"],
                    "steps": [s["step_name"] for s in job["steps"]],
                    "triggers": []
                }
                up_jobs = find_jobs_triggering_job(job["name"])
                for up_name, up_step in up_jobs:
                    path["triggers"].append({
                        "type": "SQL Agent Job",
                        "name": up_name,
                        "trigger_step": up_step
                    })
                lineage_tree["upstream_paths"].append(path)
                
        return lineage_tree

    def search_all(self, keyword):
        self.load_all()
        results = []
        kw_lower = keyword.lower()
        
        # Search tables
        for name, tbl in self.tables.items():
            if kw_lower in name.lower() or any(kw_lower in c["column"].lower() or kw_lower in c["description"].lower() for c in tbl["columns"]):
                results.append({"type": "Table", "name": name, "file": tbl["file_path"]})
                
        # Search SPs
        for name, sp in self.sps.items():
            if kw_lower in name.lower() or kw_lower in sp["code"].lower():
                results.append({"type": "Stored Procedure", "name": name, "file": sp["file_path"]})

        # Search Views
        for name, view in self.views.items():
            if kw_lower in name.lower() or kw_lower in view["code"].lower():
                results.append({"type": "View", "name": name, "file": view["file_path"]})
                
        # Search SSIS Packages
        for name, pkg in self.packages.items():
            if kw_lower in name.lower() or kw_lower in pkg["raw_content"].lower():
                results.append({"type": "SSIS Package", "name": name, "file": pkg["file_path"]})
                
        # Search Jobs
        for name, job in self.jobs.items():
            step_match = any(kw_lower in s["step_name"].lower() or kw_lower in s["command"].lower() for s in job["steps"])
            if kw_lower in name.lower() or step_match:
                results.append({"type": "SQL Agent Job", "name": name, "file": job["file_path"]})
                
        return results

# Text output formatters
def format_table_markdown(tbl):
    md = []
    md.append(f"# Table Schema: {tbl['table_name']}")
    md.append(f"**Database:** {tbl['database']}  ")
    md.append(f"**Documentation File:** [{Path(tbl['file_path']).name}](file:///{tbl['file_path'].replace(os.sep, '/')})  \n")
    md.append("## Columns\n")
    md.append("| Column | Type | Max Length | Nullable | PK | FK | Description |")
    md.append("|---|---|---|---|---|---|---|")
    for c in tbl["columns"]:
        md.append(f"| {c['column']} | {c['type']} | {c['max_length']} | {c['nullable']} | {c['pk']} | {c['fk']} | {c['description']} |")
    return "\n".join(md)

def format_sp_markdown(sp):
    md = []
    md.append(f"# Stored Procedure: {sp['sp_name']}")
    md.append(f"**Database:** {sp['database']}  ")
    md.append(f"**Documentation File:** [{Path(sp['file_path']).name}](file:///{sp['file_path'].replace(os.sep, '/')})  \n")
    md.append("## Table Dependencies\n")
    if sp["dependencies"]:
        for dep in sp["dependencies"]:
            md.append(f"- {dep}")
    else:
        md.append("_No documented table dependencies._")
    md.append("\n## SQL Code Snippet (first 100 lines)\n")
    code_lines = sp["code"].split('\n')
    snippet = "\n".join(code_lines[:100])
    if len(code_lines) > 100:
        snippet += "\n\n... (truncated)"
    md.append(f"```sql\n{snippet}\n```")
    return "\n".join(md)

def format_view_markdown(view):
    md = []
    md.append(f"# View: {view['view_name']}")
    md.append(f"**Database:** {view['database']}  ")
    md.append(f"**Documentation File:** [{Path(view['file_path']).name}](file:///{view['file_path'].replace(os.sep, '/')})  \n")
    md.append("## Table Dependencies\n")
    if view["dependencies"]:
        for dep in view["dependencies"]:
            md.append(f"- {dep}")
    else:
        md.append("_No documented table dependencies._")
    md.append("\n## View Code Snippet (first 100 lines)\n")
    code_lines = view["code"].split('\n')
    snippet = "\n".join(code_lines[:100])
    if len(code_lines) > 100:
        snippet += "\n\n... (truncated)"
    md.append(f"```sql\n{snippet}\n```")
    return "\n".join(md)

def format_package_markdown(pkg):
    md = []
    md.append(f"# SSIS Package: {pkg['package_name']}")
    md.append(f"**Project:** {pkg['project']}  ")
    md.append(f"**Folder:** {pkg['folder']}  ")
    md.append(f"**Documentation File:** [{Path(pkg['file_path']).name}](file:///{pkg['file_path'].replace(os.sep, '/')})  \n")
    
    md.append("## Connection Managers\n")
    if pkg["connections"]:
        md.append("| Name | Type |")
        md.append("|---|---|")
        for conn in pkg["connections"]:
            md.append(f"| {conn['name']} | {conn['type']} |")
    else:
        md.append("_None detected._")
        
    md.append("\n## Data Flow: Destinations\n")
    if pkg["destinations"]:
        md.append("| Component | Destination Table |")
        md.append("|---|---|")
        for dest in pkg["destinations"]:
            md.append(f"| {dest['component']} | {dest['destination_table']} |")
    else:
        md.append("_None detected._")
        
    md.append("\n## Data Flow: Sources\n")
    if pkg["sources"]:
        md.append("| Component | Source Table |")
        md.append("|---|---|")
        for src in pkg["sources"]:
            md.append(f"| {src['component']} | {src['source_table']} |")
    else:
        md.append("_None detected._")
        
    return "\n".join(md)

def format_job_markdown(job):
    md = []
    md.append(f"# SQL Agent Job: {job['job_name']}")
    md.append(f"**Enabled:** {job['enabled']}  ")
    md.append(f"**Documentation File:** [{Path(job['file_path']).name}](file:///{job['file_path'].replace(os.sep, '/')})  \n")
    md.append("## Job Steps\n")
    for step in job["steps"]:
        md.append(f"### Step {step['step_num']}: {step['step_name']}")
        md.append(f"**Subsystem:** {step['subsystem']}  \n")
        if step['command']:
            md.append(f"```sql\n{step['command']}\n```\n")
        else:
            md.append("_No command text._\n")
    return "\n".join(md)

def format_trace_markdown(trace):
    md = []
    md.append(f"# Lineage Trace: {trace['query']}")
    md.append(f"**Matching Tables found:** {', '.join(trace['matched_tables']) if trace['matched_tables'] else 'None'}\n")

    md.append("## Stored Procedures referencing table")
    if trace["stored_procedures"]:
        for sp in trace["stored_procedures"]:
            md.append(f"- **{sp['name']}** (DB: {sp['database']}, Match: {sp['type']}) - [File]({sp['file_path']})")
    else:
        md.append("_None found._")

    md.append("\n## Views referencing table")
    for view in trace.get("views", []):
        md.append(f"- **{view['name']}** (DB: {view['database']}, Match: {view['type']}) - [File]({view['file_path']})")
    if not trace.get("views"):
        md.append("_None found._")

    md.append("\n## SSIS Packages referencing table")
    if trace["ssis_packages"]:
        for pkg in trace["ssis_packages"]:
            md.append(f"- **{pkg['name']}** (Project: {pkg['project']}, Role: {pkg['role']}) - [File]({pkg['file_path']})")
    else:
        md.append("_None found._")

    md.append("\n## SQL Agent Jobs referencing table")
    if trace["sql_agent_jobs"]:
        for job in trace["sql_agent_jobs"]:
            steps_desc = ", ".join(f"Step {s['step_num']} ({s['subsystem']})" for s in job["steps"])
            md.append(f"- **{job['name']}** (Enabled: {job['enabled']}) - steps: {steps_desc} - [File]({job['file_path']})")
    else:
        md.append("_None found._")

    return "\n".join(md)

def format_lineage_tree_markdown(tree):
    md = []
    md.append(f"# Upstream Data Lineage Tree: {tree['target']}")
    md.append(f"Traced back from matching tables: **{', '.join(tree['tables'])}**\n")
    
    if not tree["upstream_paths"]:
        md.append("_No upstream load paths detected in SSIS, SPs, or SQL Jobs._")
        return "\n".join(md)
        
    # Standard text tree builder
    def build_tree_text(paths):
        lines = []
        for path in paths:
            t_type = path["type"]
            t_name = path["name"]
            lines.append(f"├── [{t_type}] {t_name}")
            
            if t_type == "SSIS Package":
                lines.append(f"│   └── Role: {path['role']}")
                for trigger in path.get("triggers", []):
                    lines.append(f"│       └── [SQL Agent Job] {trigger['name']} ({trigger['trigger_step']})")
                    for up_job in trigger.get("upstream_jobs", []):
                        lines.append(f"│           └── Triggered by [Job] {up_job['name']} ({up_job['step']})")
            elif t_type == "Stored Procedure":
                lines.append(f"│   └── Database: {path['database']}")
                for trigger in path.get("triggers", []):
                    if trigger["type"] == "SSIS Package":
                        lines.append(f"│       └── [SSIS Package] {trigger['name']} ({trigger['task']})")
                        for job in trigger.get("jobs", []):
                            lines.append(f"│           └── [SQL Agent Job] {job['name']} ({job['step']})")
                            for up_job in job.get("upstream_jobs", []):
                                lines.append(f"│               └── Triggered by [Job] {up_job['name']} ({up_job['step']})")
                    else: # Direct SQL Job
                        lines.append(f"│       └── [Direct SQL Job] {trigger['name']} ({trigger['step']})")
                        for up_job in trigger.get("upstream_jobs", []):
                            lines.append(f"│           └── Triggered by [Job] {up_job['name']} ({up_job['step']})")
            elif t_type == "Direct SQL Agent Job Step Reference":
                lines.append(f"│   └── Step References: {', '.join(path['steps'])}")
                for trigger in path.get("triggers", []):
                    lines.append(f"│       └── Triggered by [Job] {trigger['name']} ({trigger['trigger_step']})")
        return lines

    md.append("```text")
    md.append(f"Table: {tree['target']}")
    md.extend(build_tree_text(tree["upstream_paths"]))
    md.append("```\n")
    
    # Detailed markdown description
    md.append("## Upstream Path Descriptions\n")
    for path in tree["upstream_paths"]:
        md.append(f"### {path['type']}: **{path['name']}**")
        if path.get("database"):
            md.append(f"- **Database Context**: {path['database']}")
        if path.get("role"):
            md.append(f"- **Data Flow Role**: {path['role']}")
            
        triggers = path.get("triggers", [])
        if triggers:
            md.append("- **Upstream Executions**:")
            for trig in triggers:
                if trig.get("type") == "SSIS Package":
                    md.append(f"  - SSIS Package **{trig['name']}** running task: `{trig['task']}`")
                    for job in trig.get("jobs", []):
                        md.append(f"    - SQL Agent Job **{job['name']}** step: `{job['step']}`")
                        for up_job in job.get("upstream_jobs", []):
                            md.append(f"      - Upstream Job Trigger: **{up_job['name']}** via `{up_job['step']}`")
                elif "Job" in trig.get("type", ""):
                    md.append(f"  - SQL Agent Job **{trig['name']}** step: `{trig.get('trigger_step') or trig.get('step')}`")
                    for up_job in trig.get("upstream_jobs", []):
                        md.append(f"    - Upstream Job Trigger: **{up_job['name']}** via `{up_job['step']}`")
        md.append("")
        
    return "\n".join(md)

# Main CLI execution
def main():
    parser = argparse.ArgumentParser(description="BAB Engineering Data Architecture Explorer CLI")
    parser.add_argument("--docs-dir", default=".", help="Root directory of the BAB Documentation (defaults to current dir)")
    parser.add_argument("--output", help="Path to write the results (if omitted, writes to explorer_output.md or explorer_output.json)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format rather than Markdown")
    
    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to run")
    
    # find-table
    p_find_table = subparsers.add_parser("find-table", help="Look up a table schema by name")
    p_find_table.add_argument("table_name", help="Name of the table (matches loosely, e.g. dbo.Table or just Table)")
    
    # trace-table
    p_trace_table = subparsers.add_parser("trace-table", help="Find all components referencing a table")
    p_trace_table.add_argument("table_name", help="Name of the table")
    
    # describe-sp
    p_desc_sp = subparsers.add_parser("describe-sp", help="Inspect a stored procedure by name")
    p_desc_sp.add_argument("sp_name", help="Name of the stored procedure")

    # describe-view
    p_desc_view = subparsers.add_parser("describe-view", help="Inspect a view by name")
    p_desc_view.add_argument("view_name", help="Name of the view")
    
    # describe-job
    p_desc_job = subparsers.add_parser("describe-job", help="Inspect a SQL Agent job by name")
    p_desc_job.add_argument("job_name", help="Name of the SQL Agent job")
    
    # describe-package
    p_desc_pkg = subparsers.add_parser("describe-package", help="Inspect an SSIS package by name")
    p_desc_pkg.add_argument("package_name", help="Name of the SSIS package")
    
    # search-all
    p_search = subparsers.add_parser("search-all", help="Perform a text search across all documentation files")
    p_search.add_argument("keyword", help="Term to search for")
    
    # trace-lineage
    p_lineage = subparsers.add_parser("trace-lineage", help="Generate upstream data lineage trace for a table")
    p_lineage.add_argument("table_name", help="Name of the table")
    
    args = parser.parse_args()
    
    docs_dir_path = Path(args.docs_dir).resolve()
    # Auto-fallback to the root of the BABSkills repository (grandparent of scripts folder)
    if not (docs_dir_path / "DataDictionary").exists() and not (docs_dir_path / "README.md").exists():
        fallback_path = Path(__file__).resolve().parent.parent.parent
        if (fallback_path / "DataDictionary").exists() or (fallback_path / "README.md").exists():
            docs_dir_path = fallback_path
            
    explorer = DocExplorer(docs_dir_path)
    
    # Verify documentation directory has index or structure
    if not (explorer.docs_dir / "README.md").exists() and not (explorer.docs_dir / "DataDictionary").exists():
        print(f"[ERROR] Could not find documentation folders under: {explorer.docs_dir}", file=sys.stderr)
        print("Please set --docs-dir to the absolute path of the BABEngineering/Documentation directory.", file=sys.stderr)
        sys.exit(1)
        
    result_data = None
    output_text = ""
    
    try:
        if args.command == "find-table":
            tables = explorer.find_table(args.table_name)
            if not tables:
                print(f"[WARNING] No table matched query '{args.table_name}'", file=sys.stderr)
                result_data = {"error": f"No table matched query '{args.table_name}'"}
                output_text = f"# Table Search: {args.table_name}\n\nNo matching table found."
            else:
                result_data = tables[0] if len(tables) == 1 else tables
                output_text = "\n\n---\n\n".join(format_table_markdown(t) for t in tables)
                
        elif args.command == "trace-table":
            trace = explorer.trace_table(args.table_name)
            result_data = trace
            output_text = format_trace_markdown(trace)
            
        elif args.command == "describe-sp":
            sps = explorer.find_sp(args.sp_name)
            if not sps:
                print(f"[WARNING] No stored procedure matched query '{args.sp_name}'", file=sys.stderr)
                result_data = {"error": f"No stored procedure matched query '{args.sp_name}'"}
                output_text = f"# Stored Procedure Search: {args.sp_name}\n\nNo matching stored procedure found."
            else:
                result_data = sps[0] if len(sps) == 1 else sps
                output_text = "\n\n---\n\n".join(format_sp_markdown(s) for s in sps)

        elif args.command == "describe-view":
            views = explorer.find_view(args.view_name)
            if not views:
                print(f"[WARNING] No view matched query '{args.view_name}'", file=sys.stderr)
                result_data = {"error": f"No view matched query '{args.view_name}'"}
                output_text = f"# View Search: {args.view_name}\n\nNo matching view found."
            else:
                result_data = views[0] if len(views) == 1 else views
                output_text = "\n\n---\n\n".join(format_view_markdown(v) for v in views)
                
        elif args.command == "describe-job":
            jobs = explorer.find_job(args.job_name)
            if not jobs:
                print(f"[WARNING] No SQL Agent Job matched query '{args.job_name}'", file=sys.stderr)
                result_data = {"error": f"No SQL Agent Job matched query '{args.job_name}'"}
                output_text = f"# SQL Agent Job Search: {args.job_name}\n\nNo matching job found."
            else:
                result_data = jobs[0] if len(jobs) == 1 else jobs
                output_text = "\n\n---\n\n".join(format_job_markdown(j) for j in jobs)
                
        elif args.command == "describe-package":
            pkgs = explorer.find_package(args.package_name)
            if not pkgs:
                print(f"[WARNING] No SSIS package matched query '{args.package_name}'", file=sys.stderr)
                result_data = {"error": f"No SSIS package matched query '{args.package_name}'"}
                output_text = f"# SSIS Package Search: {args.package_name}\n\nNo matching SSIS package found."
            else:
                result_data = pkgs[0] if len(pkgs) == 1 else pkgs
                output_text = "\n\n---\n\n".join(format_package_markdown(p) for p in pkgs)
                
        elif args.command == "search-all":
            search_res = explorer.search_all(args.keyword)
            result_data = search_res
            # Format search results
            md = [f"# Search Results for: '{args.keyword}'\n"]
            if search_res:
                md.append(f"Found {len(search_res)} matching documentation files:\n")
                md.append("| Type | Name | Documentation File |")
                md.append("|---|---|---|")
                for r in search_res:
                    file_url = f"file:///{r['file'].replace(os.sep, '/')}"
                    md.append(f"| {r['type']} | **{r['name']}** | [{Path(r['file']).name}]({file_url}) |")
            else:
                md.append("No matches found.")
            output_text = "\n".join(md)
            
        elif args.command == "trace-lineage":
            lineage = explorer.trace_lineage(args.table_name)
            result_data = lineage
            output_text = format_lineage_tree_markdown(lineage)
            
    except Exception as e:
        print(f"[ERROR] Exception during command execution: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
        
    # Write output to file
    out_path = args.output
    if not out_path:
        out_ext = ".json" if args.json else ".md"
        out_path = f"explorer_output{out_ext}"
        
    try:
        out_path_obj = Path(out_path)
        if args.json:
            out_path_obj.write_text(json.dumps(result_data, indent=2), encoding='utf-8')
        else:
            out_path_obj.write_text(output_text, encoding='utf-8')
        print(f"[SUCCESS] Command '{args.command}' completed. Output written to: {out_path_obj.name}")
    except Exception as e:
        print(f"[ERROR] Failed to write output to {out_path}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
