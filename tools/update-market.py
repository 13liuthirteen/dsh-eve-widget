# -*- coding: utf-8 -*-
"""生成/刷新 market.json（DSH 插件市场 format 1 索引）。

用法：在仓库根目录（或任意位置）执行
    python tools/update-market.py
自动读取 package.json 的 version、git 当前 commit、origin 远端 URL，
写出 market.json。发布新版本时：改版本号 → 跑本脚本 → commit + tag + push。
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKET = ROOT / "market.json"


def git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} 失败: {out.stderr.strip()}")
    return out.stdout.strip()


def main() -> None:
    pkg = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    version = pkg["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", version):
        raise SystemExit(f"version 不是精确 SemVer: {version}")

    commit = git("rev-parse", "HEAD")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise SystemExit(f"commit 不是 40 位十六进制: {commit}")

    try:
        remote = git("remote", "get-url", "origin")
    except SystemExit:
        remote = ""
    m = re.search(r"github\.com[:/]([^/]+)/(.+?)(?:\.git)?/?$", remote)
    if not m:
        raise SystemExit("未找到 github.com 形式的 origin 远端；先 git remote add origin https://github.com/<用户名>/dsh-eve-widget.git")
    repo_url = f"https://github.com/{m.group(1)}/{m.group(2)}"

    index = {
        "format": 1,
        "title": "伊薇的插件架",
        "plugins": [
            {
                "name": pkg["name"],
                "title": "伊薇余额挂件",
                "description": pkg.get("description", ""),
                "repository": {"url": repo_url},
                "versions": [
                    {
                        "version": version,
                        "publishTimestamp": int(time.time()),
                        "source": {"type": "git", "url": repo_url, "commit": commit},
                    }
                ],
            }
        ],
    }
    MARKET.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"market.json 已生成: v{version} @ {commit[:10]} ({repo_url})")


if __name__ == "__main__":
    sys.exit(main())
