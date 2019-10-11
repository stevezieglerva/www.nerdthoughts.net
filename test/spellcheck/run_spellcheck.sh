source venv/bin/activate

cat ../../_drafts\*.md > all_mds.txt
cat ../../_posts\*.md >> all_mds.txt


python3 run_spellcheck.py


