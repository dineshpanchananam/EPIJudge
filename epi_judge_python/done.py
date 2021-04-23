import json
import sys
from collections import defaultdict

display = ["done", "wip", "todo"]
if len(sys.argv) > 1:
  display = sys.argv[1]
  if display not in ("done", "wip", "todo"):
    sys.exit("py done.py done|wip|todo")

with open("../problem_mapping.js") as f:
  overall = {"done": 0, "total": 0}
  content = f.read().replace("problem_mapping = ", "").replace(";", "")
  chaps = json.loads(content)
  for chap, chap_v in chaps.items():
    output = defaultdict(list)
    _chap = chap.split(": ")[1]
    done, tot = 0, 0
    for problem in chap_v.values():
      for lang, status in problem.items():
        if not lang.startswith("Py"):
          continue
        key = lang[8:]
        tot += 1
        passed, total = status["passed"], status["total"]
        if passed == total:
          done += 1
          output[key] = ("done", "✔")
        elif passed > 0:
          output[key] = ("wip", "✘")
        else:
          output[key] = ("todo", "-")
    print(f"> {_chap} ({done}/{tot})")
    overall["done"] += done
    overall["total"] += tot
    for key in output:
      status, sym = output[key]
      if status in display:
        print("  ", sym, key)

print(f"\nPROGRESS: {overall['done']}/{overall['total']}")
