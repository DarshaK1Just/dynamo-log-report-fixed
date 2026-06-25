import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

EXPECTED_TOTAL = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load():
    assert REPORT_PATH.exists(), "report.json not found at /app/report.json"
    raw = REPORT_PATH.read_text().strip()
    assert raw, "report.json is empty"
    return json.loads(raw)


def test_report_exists():
    """The agent produced report.json at the required path."""
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"


def test_total_requests():
    """total_requests equals the number of log lines (6)."""
    data = _load()
    assert "total_requests" in data, "missing key: total_requests"
    assert data["total_requests"] == EXPECTED_TOTAL, (
        f"total_requests: expected {EXPECTED_TOTAL}, got {data['total_requests']}"
    )


def test_unique_ips():
    """unique_ips equals the number of distinct client IPs (3)."""
    data = _load()
    assert "unique_ips" in data, "missing key: unique_ips"
    assert data["unique_ips"] == EXPECTED_UNIQUE_IPS, (
        f"unique_ips: expected {EXPECTED_UNIQUE_IPS}, got {data['unique_ips']}"
    )


def test_top_path():
    """top_path is the most-requested URL path (/index.html, 3 hits)."""
    data = _load()
    assert "top_path" in data, "missing key: top_path"
    assert data["top_path"] == EXPECTED_TOP_PATH, (
        f"top_path: expected {EXPECTED_TOP_PATH!r}, got {data['top_path']!r}"
    )
