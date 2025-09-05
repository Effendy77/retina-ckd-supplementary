import json, hashlib, pathlib, time

root = pathlib.Path(__file__).resolve().parents[1]
targets = [
    root / "figures",
    root / "tables"
]

def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

manifest_path = root / "manifest.json"
manifest = {"version":"0.2.0","generated":[], "timestamp": int(time.time())}
if manifest_path.exists():
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception:
        pass

entries = []
for t in targets:
    if not t.exists(): 
        continue
    for p in t.rglob("*"):
        if p.is_file():
            entries.append({
                "path": str(p.relative_to(root)),
                "sha256": sha256(p)
            })

manifest["generated"] = entries
manifest["timestamp"] = int(time.time())
manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(f"Updated manifest with {len(entries)} entries.")
