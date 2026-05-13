import sys, re, glob, os

os.chdir(r"d:\app\IronSyncroWealth\koreainvestment")
sys.path.insert(0, r"d:\app\IronSyncroWealth\koreainvestment\src")
from fastapi.testclient import TestClient
from app.main import create_app

print("앱 생성 중...", flush=True)
app = create_app()
client = TestClient(app)

print("OpenAPI 스펙 조회 중...", flush=True)
resp = client.get('/openapi.json')
paths = list(resp.json().get('paths', {}).keys())

quotations = sorted([p for p in paths if '/quotations/' in p and p != '/api/v1/quotations/specs'])
ranking    = sorted([p for p in paths if '/ranking/' in p and p != '/api/v1/ranking/specs'])
trading    = sorted([p for p in paths if '/trading/' in p and p != '/api/v1/trading/specs'])

print(f"[Swagger] quotations={len(quotations)}, ranking={len(ranking)}, trading={len(trading)}, total={len(quotations)+len(ranking)+len(trading)}", flush=True)

# specs_request.py 에서 URL 추출
spec_urls = []
for fpath in glob.glob(r"d:\app\IronSyncroWealth\koreainvestment\src\**\specs_request.py", recursive=True):
    content = open(fpath, encoding='utf-8').read()
    urls = re.findall(r'"url"\s*:\s*"(/[^"]+)"', content)
    spec_urls.extend(urls)

spec_urls = sorted(set(spec_urls))
print(f"[specs_request] total unique URLs: {len(spec_urls)}", flush=True)

# 마지막 세그먼트로 비교
swagger_keys = set(p.rstrip('/').split('/')[-1] for p in quotations + ranking + trading)
spec_keys    = set(u.rstrip('/').split('/')[-1] for u in spec_urls)

missing = spec_keys - swagger_keys
extra   = swagger_keys - spec_keys

print(f"[MISSING in Swagger]: {len(missing)}", flush=True)
for m in sorted(missing):
    print(f"  - {m}", flush=True)

print(f"[EXTRA in Swagger (not in specs)]: {len(extra)}", flush=True)
for e in sorted(extra):
    print(f"  + {e}", flush=True)

if not missing:
    print("\n✅ 모든 specs_request URL이 Swagger UI에 등록되어 있습니다.", flush=True)
else:
    print(f"\n❌ {len(missing)}개 항목이 Swagger UI에 누락되어 있습니다.", flush=True)
