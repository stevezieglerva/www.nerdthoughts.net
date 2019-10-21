source venv/bin/activate

cat ../../_drafts\*.md > all_mds.txt
cat ../../_posts\*.md >> all_mds.txt

python3 run_spellcheck.py "../../_drafts/*.md" pass
python3 run_spellcheck.py "../../_posts/2019*.md" fail


