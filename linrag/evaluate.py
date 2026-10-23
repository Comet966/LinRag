import json
from pathlib import Path

from .index import Index


def evaluate(index: Index, cases_path: Path) -> dict:
    cases = json.loads(cases_path.read_text())
    report = {"cases": len(cases), "modes": {}}
    for mode in ("lexical", "hybrid"):
        if mode == "hybrid" and not index.vector_ready:
            report["modes"][mode] = {"status": "skipped", "reason": "需要可用的向量索引与 EMBED_* 配置"}
            continue
        details, hits, total, absent, empty = [], 0, 0, 0, 0
        for case in cases:
            result = index.search(case["query"], 5, mode=mode)
            found = {row["command"] for row in result["results"]}
            expected = set(case["expected"])
            hit = bool(expected & found) if expected else not found
            if expected:
                total += 1
                hits += hit
            else:
                absent += 1
                empty += hit
            details.append(
                {
                    **case,
                    "found": sorted(found),
                    "hit": hit,
                    "actual_mode": result["mode"],
                    "warnings": result["warnings"],
                }
            )
        degraded = sum(row["actual_mode"] != mode for row in details)
        report["modes"][mode] = {
            "status": "degraded" if degraded else "ok",
            "hit_at_5": hits / total if total else 0,
            "answerable_cases": total,
            "no_evidence_cases": absent,
            "empty_results": empty,
            "degraded_queries": degraded,
            "details": details,
        }
    return report
