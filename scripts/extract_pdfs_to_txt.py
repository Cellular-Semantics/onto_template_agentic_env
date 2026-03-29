from pathlib import Path
from pdfminer.high_level import extract_text

pdf_dir = Path('pdfs')

pdfs = sorted([p for p in pdf_dir.iterdir() if p.suffix.lower()=='.pdf'])
print('pdf_count', len(pdfs))

for pdf in pdfs:
    txt_path = pdf.with_suffix('.txt')
    if txt_path.exists() and txt_path.stat().st_size > 1000:
        print('skip', pdf.name, '->', txt_path.name)
        continue
    try:
        text = extract_text(str(pdf))
    except Exception as e:
        print('error', pdf.name, e)
        continue
    if not text or len(text) < 1000:
        print('short', pdf.name, len(text) if text else 0)
        # still write for inspection
    txt_path.write_text(text, errors='ignore')
    print('wrote', pdf.name, '->', txt_path.name, len(text))
