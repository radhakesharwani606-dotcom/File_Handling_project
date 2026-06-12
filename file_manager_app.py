import streamlit as st
from pathlib import Path
import os
 
st.set_page_config(page_title="File Manager", page_icon="📁", layout="centered")
 
# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
 
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
 
/* Page background */
.stApp {
    background: #0f1117;
    color: #e8eaf0;
}
 
/* Hide default Streamlit header decoration */
header[data-testid="stHeader"] { background: transparent; }
 
/* Title area */
.hero-title {
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #ffffff;
    margin-bottom: 0.1rem;
}
.hero-sub {
    font-size: 0.9rem;
    color: #6b7280;
    margin-bottom: 2rem;
    font-family: 'JetBrains Mono', monospace;
}
 
/* Operation cards (radio styled as cards) */
div[data-testid="stRadio"] > label {
    display: none;
}
div[data-testid="stRadio"] > div {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
}
div[data-testid="stRadio"] > div > label {
    background: #1a1d27 !important;
    border: 1px solid #2a2d3a !important;
    border-radius: 10px !important;
    padding: 1rem 1.2rem !important;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s;
    color: #c9cdd8 !important;
    font-size: 0.92rem !important;
    font-weight: 500 !important;
}
div[data-testid="stRadio"] > div > label:hover {
    border-color: #6366f1 !important;
    background: #1e2035 !important;
}
div[data-testid="stRadio"] > div > label[data-checked="true"],
div[data-testid="stRadio"] > div > label:has(input:checked) {
    border-color: #6366f1 !important;
    background: #1e2035 !important;
    color: #a5b4fc !important;
}
 
/* Input fields */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #1a1d27 !important;
    border: 1px solid #2a2d3a !important;
    border-radius: 8px !important;
    color: #e8eaf0 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.88rem !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 2px rgba(99,102,241,0.2) !important;
}
 
/* Primary button */
.stButton > button {
    background: #6366f1 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.55rem 1.4rem !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.01em !important;
    transition: background 0.2s, transform 0.1s !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: #4f46e5 !important;
    transform: translateY(-1px) !important;
}
 
/* File tree box */
.file-tree {
    background: #1a1d27;
    border: 1px solid #2a2d3a;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: #9ca3af;
    line-height: 1.8;
    max-height: 220px;
    overflow-y: auto;
}
.file-tree .item { color: #c9cdd8; }
.file-tree .idx  { color: #6b7280; margin-right: 0.5rem; }
 
/* Success / error banners */
.banner-ok  { background:#0d2a1f; border:1px solid #16a34a; border-radius:8px; padding:0.75rem 1rem; color:#4ade80; font-weight:600; font-size:0.9rem; margin-top:0.75rem; }
.banner-err { background:#2a0d0d; border:1px solid #dc2626; border-radius:8px; padding:0.75rem 1rem; color:#f87171; font-weight:600; font-size:0.9rem; margin-top:0.75rem; }
.banner-info{ background:#0d1a2a; border:1px solid #3b82f6; border-radius:8px; padding:0.75rem 1rem; color:#93c5fd; font-size:0.88rem; margin-top:0.75rem; }
 
/* Divider */
.divider { border:none; border-top:1px solid #2a2d3a; margin:1.5rem 0; }
 
/* Section label */
.sec-label { font-size:0.78rem; font-weight:600; color:#6b7280; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.5rem; }
</style>
""", unsafe_allow_html=True)
 
 
# ── Helpers ─────────────────────────────────────────────────────────────────
def get_items():
    p = Path('.')
    return list(p.rglob('*'))
 
def render_file_tree():
    items = get_items()
    if not items:
        return "<div class='file-tree' style='color:#6b7280;font-style:italic;'>No files or folders found.</div>"
    rows = ""
    for i, item in enumerate(items):
        rows += f"<div><span class='idx'>{i+1:02d}</span><span class='item'>{'📁 ' if item.is_dir() else '📄 '}{item}</span></div>"
    return f"<div class='file-tree'>{rows}</div>"
 
def banner(msg, kind="ok"):
    cls = {"ok": "banner-ok", "err": "banner-err", "info": "banner-info"}[kind]
    st.markdown(f"<div class='{cls}'>{msg}</div>", unsafe_allow_html=True)
 
 
# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("<div class='hero-title'>📁 File Manager</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-sub'>create · read · update · delete</div>", unsafe_allow_html=True)
 
# ── File tree ────────────────────────────────────────────────────────────────
st.markdown("<div class='sec-label'>Current Files &amp; Folders</div>", unsafe_allow_html=True)
st.markdown(render_file_tree(), unsafe_allow_html=True)
if st.button("🔄 Refresh"):
    st.rerun()
 
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
 
# ── Operation selector ───────────────────────────────────────────────────────
st.markdown("<div class='sec-label'>Choose Operation</div>", unsafe_allow_html=True)
op = st.radio(
    "op",
    ["➕  Create File", "👁️  Read File", "✏️  Update File", "🗑️  Delete File"],
    horizontal=False,
    label_visibility="collapsed",
)
 
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
 
# ── CREATE ───────────────────────────────────────────────────────────────────
if op == "➕  Create File":
    st.markdown("<div class='sec-label'>Create a New File</div>", unsafe_allow_html=True)
    fname = st.text_input("File name", placeholder="e.g.  notes.txt")
    content = st.text_area("Content", placeholder="Write anything here...", height=140)
    if st.button("Create File"):
        if not fname.strip():
            banner("⚠️ Please enter a file name.", "err")
        else:
            p = Path(fname.strip())
            if p.exists():
                banner(f"⚠️ '{fname}' already exists.", "err")
            else:
                try:
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(content)
                    banner(f"✅ '{fname}' created successfully!")
                    st.rerun()
                except Exception as e:
                    banner(f"Error: {e}", "err")
 
# ── READ ─────────────────────────────────────────────────────────────────────
elif op == "👁️  Read File":
    st.markdown("<div class='sec-label'>Read a File</div>", unsafe_allow_html=True)
    fname = st.text_input("File name to read", placeholder="e.g.  notes.txt")
    if st.button("Read File"):
        if not fname.strip():
            banner("⚠️ Please enter a file name.", "err")
        else:
            p = Path(fname.strip())
            if p.exists() and p.is_file():
                data = p.read_text(errors="replace")
                st.markdown("<div class='sec-label' style='margin-top:1rem;'>File Contents</div>", unsafe_allow_html=True)
                st.code(data if data.strip() else "(empty file)", language="text")
                banner(f"✅ '{fname}' read successfully!")
            else:
                banner(f"⚠️ '{fname}' does not exist or is not a file.", "err")
 
# ── UPDATE ───────────────────────────────────────────────────────────────────
elif op == "✏️  Update File":
    st.markdown("<div class='sec-label'>Update a File</div>", unsafe_allow_html=True)
    fname = st.text_input("File name to update", placeholder="e.g.  notes.txt")
 
    update_type = st.radio(
        "What do you want to do?",
        ["Rename file", "Overwrite content", "Append content"],
        horizontal=True,
    )
 
    if update_type == "Rename file":
        new_name = st.text_input("New file name", placeholder="e.g.  renamed.txt")
        if st.button("Rename"):
            if not fname.strip() or not new_name.strip():
                banner("⚠️ Both file names are required.", "err")
            else:
                p = Path(fname.strip())
                p2 = Path(new_name.strip())
                if not p.exists():
                    banner(f"⚠️ '{fname}' does not exist.", "err")
                elif p2.exists():
                    banner(f"⚠️ '{new_name}' already exists.", "err")
                else:
                    try:
                        p.rename(p2)
                        banner(f"✅ Renamed '{fname}' → '{new_name}'")
                        st.rerun()
                    except Exception as e:
                        banner(f"Error: {e}", "err")
 
    elif update_type == "Overwrite content":
        new_data = st.text_area("New content (replaces everything)", height=130)
        if st.button("Overwrite"):
            p = Path(fname.strip())
            if not p.exists() or not p.is_file():
                banner(f"⚠️ '{fname}' does not exist.", "err")
            else:
                try:
                    p.write_text(new_data)
                    banner(f"✅ '{fname}' overwritten successfully!")
                except Exception as e:
                    banner(f"Error: {e}", "err")
 
    else:  # Append
        extra = st.text_area("Text to append", height=110)
        if st.button("Append"):
            p = Path(fname.strip())
            if not p.exists() or not p.is_file():
                banner(f"⚠️ '{fname}' does not exist.", "err")
            else:
                try:
                    with open(p, 'a') as f:
                        f.write(extra)
                    banner(f"✅ Content appended to '{fname}'!")
                except Exception as e:
                    banner(f"Error: {e}", "err")
 
# ── DELETE ───────────────────────────────────────────────────────────────────
elif op == "🗑️  Delete File":
    st.markdown("<div class='sec-label'>Delete a File</div>", unsafe_allow_html=True)
    fname = st.text_input("File name to delete", placeholder="e.g.  notes.txt")
 
    if fname.strip():
        st.markdown(f"<div class='banner-err' style='margin-bottom:0.5rem;'>⚠️ This will permanently delete <strong>{fname}</strong>. This cannot be undone.</div>", unsafe_allow_html=True)
 
    if st.button("🗑️ Delete File"):
        if not fname.strip():
            banner("⚠️ Please enter a file name.", "err")
        else:
            p = Path(fname.strip())
            if p.exists() and p.is_file():
                try:
                    os.remove(p)
                    banner(f"✅ '{fname}' deleted successfully!")
                    st.rerun()
                except Exception as e:
                    banner(f"Error: {e}", "err")
            else:
                banner(f"⚠️ '{fname}' does not exist or is not a file.", "err")
 
# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#4b5563;font-size:0.78rem;'>Thank you for using File Manager ✨</div>", unsafe_allow_html=True)
