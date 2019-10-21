source venv/bin/activate


python3 run_spellcheck.py "../../_drafts/*.md" pass
python3 run_spellcheck.py "../../_posts/2019*.md" fail
python3 run_spellcheck.py "../../_posts/202*.md" fail

