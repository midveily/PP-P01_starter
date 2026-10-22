"""PP-P01 starter. Do not edit the prepared card-loading block."""
import json
from pathlib import Path
variant_number = 13
card = json.loads(Path(__file__).with_name("student_variants.json").read_text(encoding="utf-8"))["variants"][variant_number - 1]
print("Варіант:", card["number"], card["title"])
print("Дано:", card["given"])
width = card["given"]["width"]
height = card["given"]["height"]
area = width * height
perimeter = 2 * (width + height)
print("Площа прямокутника:", area)
print("Периметр прямокутника:", perimeter)