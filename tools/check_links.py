"""문서 사이의 상대 링크와 #앵커가 실제로 존재하는지 검사한다.

사용법: 저장소 루트에서 `python tools/check_links.py`
깨진 링크가 있으면 목록을 출력하고 종료 코드 1을 돌려준다.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def slug(heading: str) -> str:
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def md_files():
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(d, f)


def main() -> int:
    files = list(md_files())
    anchors = {}
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        anchors[os.path.abspath(f)] = {slug(h) for h in re.findall(r"^#{1,6}\s+(.*)$", text, re.M)}

    bad = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        for link in re.findall(r"\]\(([^)\s]+)\)", text):
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, frag = link.partition("#")
            target = os.path.abspath(os.path.join(os.path.dirname(f), path)) if path else os.path.abspath(f)
            rel = os.path.relpath(f, ROOT)
            if not os.path.exists(target):
                bad.append(f"없는 파일: {rel} -> {link}")
            elif frag and os.path.isfile(target) and target.endswith(".md") and frag not in anchors.get(target, set()):
                bad.append(f"없는 앵커: {rel} -> {link}")

    print(f"검사한 문서 {len(files)}개, 깨진 링크 {len(bad)}개")
    for b in bad:
        print("  " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
