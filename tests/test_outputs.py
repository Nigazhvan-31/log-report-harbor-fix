import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "report.json was not created"

    with REPORT_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def test_report_is_valid_json():
    load_report()


def test_required_keys():
    report = load_report()

    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }


def test_report_values():
    report = load_report()

    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3
    assert report["top_path"] == "/index.html"