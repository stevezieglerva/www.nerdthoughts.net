source venv/bin/activate

# spell check drafts but don't fail
python3 run_spellcheck.py "../../_drafts/*.md" pass

# spell check recent posts
python3 run_spellcheck.py "../../_posts/2019*.md" fail
python3 run_spellcheck.py "../../_posts/202*.md" fail

