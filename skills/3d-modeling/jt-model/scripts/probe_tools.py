#!/usr/bin/env python3
"""Read-only CLI discovery. MCP, project requirements and rendering need separate checks."""

import argparse
import glob
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys


def blender_candidates(explicit):
    if explicit:
        # An explicit selection must not silently fall back to a different install.
        return [os.path.expanduser(explicit)]
    candidates = [shutil.which("blender")]
    if sys.platform == "win32":
        for variable in ("ProgramW6432", "ProgramFiles", "ProgramFiles(x86)", "LOCALAPPDATA"):
            base = os.environ.get(variable)
            if base:
                pattern = str(Path(base) / "Blender Foundation" / "Blender*" / "blender.exe")
                candidates.extend(sorted(glob.glob(pattern), reverse=True))
    elif sys.platform == "darwin":
        candidates += ["/Applications/Blender.app/Contents/MacOS/Blender",
                       str(Path.home() / "Applications/Blender.app/Contents/MacOS/Blender")]
    else:
        candidates += ["/usr/bin/blender", "/usr/local/bin/blender", "/snap/bin/blender"]
    return list(dict.fromkeys(str(Path(p).absolute()) for p in candidates if p))


def probe_candidate(tool, candidate, timeout):
    path = Path(candidate).absolute()
    record = {"path": str(path), "status": "not_found"}
    if not path.is_file():
        return record
    version_flag = "-version" if tool == "ffmpeg" else "--version"
    try:
        completed = subprocess.run(
            [str(path), version_flag], capture_output=True, timeout=timeout,
            encoding="utf-8", errors="replace", check=False,
        )
        output = (completed.stdout + "\n" + completed.stderr).strip()
        record["returncode"] = completed.returncode
        patterns = {
            "blender": r"(?m)^Blender\s+\d+\.\d+",
            "ffmpeg": r"(?m)^ffmpeg version\s+\S+",
            "git": r"(?m)^git version\s+\d+",
        }
        record["status"] = (
            "available" if completed.returncode == 0 and re.search(patterns[tool], output)
            else "failed"
        )
        if record["status"] == "available":
            record["version"] = next(line for line in output.splitlines()
                                     if re.match(patterns[tool], line))
        else:
            record["output"] = output[:1000]
    except subprocess.TimeoutExpired:
        record.update(status="timed_out", error=f"Version probe exceeded {timeout:g} seconds")
    except OSError as error:
        record.update(status="failed", error=str(error))
    return record


def inspect_tool(tool, candidates, timeout):
    attempts = []
    for candidate in candidates:
        attempt = probe_candidate(tool, candidate, timeout)
        attempts.append(attempt)
        if attempt["status"] == "available":
            return {"status": "available", "path": attempt["path"], "attempts": attempts}
    status = "unavailable" if any(a["status"] != "not_found" for a in attempts) else "not_found"
    return {"status": status, "attempts": attempts}


def positive_timeout(value):
    seconds = float(value)
    if not 0 < seconds <= 30:
        raise argparse.ArgumentTypeError("timeout must be greater than 0 and at most 30 seconds")
    return seconds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blender", help="Explicit Blender executable path; no fallback if invalid")
    parser.add_argument("--timeout", type=positive_timeout, default=5.0,
                        help="Per executable version timeout in seconds (default: 5)")
    parser.add_argument("--require", action="append", default=[],
                        choices=("blender", "ffmpeg", "git"),
                        help="Exit 2 if this CLI is unavailable; repeat for multiple tools")
    args = parser.parse_args()
    candidates = {"blender": blender_candidates(args.blender)}
    for tool in ("ffmpeg", "git"):
        candidate = shutil.which(tool)
        candidates[tool] = [candidate] if candidate else []
    tools = {tool: inspect_tool(tool, paths, args.timeout) for tool, paths in candidates.items()}
    missing = [tool for tool in dict.fromkeys(args.require) if tools[tool]["status"] != "available"]
    print(json.dumps({
        "scope": "CLI version probes only; MCP, document coverage, export and render are unchecked",
        "python": {"path": sys.executable, "version": sys.version.split()[0]},
        "tools": tools,
        "missing_required_cli": missing,
    }, ensure_ascii=True, indent=2))
    return 2 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
