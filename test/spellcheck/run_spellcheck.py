import unittest
from spellchecker import SpellChecker
import os
import re
import sys
import urllib
import json
import glob
import datetime


class SubmissionSpellChecker():
	def __init__(self):
		self.spell = SpellChecker()
		self.spell.word_frequency.load_text_file("all_mds.txt")
		ignore_words = ["aws", "#", "##", "###", "####", "#####", "devops", "http", "com", "jpg", "miica", "trello", "solutioning", "etl", "oig", "owasp", "sonarqube", "php", "website", "handoffs", "standups", "sagemaker", "talend", "nutch", "gensim", "vscode", "tf", "idf", "markdown", "wireframes", "mvp", "nosql", "dynamodb", "prototyped", "retros", "devs", "cloudfront", "lambdas", "unittest", "unittest", "jasmine", "worldspace", "prioritized", "lambdas", "tokenizing", "leverages", "paas", "microservices", "vpc", "cloudtrail", "cloudwatch", "iam", "jumpcloud", "saml", "sso", "mysql", "virtualized", "cdn", "downloads", "mdasii", "userguide", "init", "decrypt", "venv", "vpcs", "pre-signed", "priv", "url", "etls", "decryption", "dwhadmn", "ziegler", "Vectorization", "Financialmodelingprep", "backend", "initializers", "rmsprop", "overfitting", "dirichlet", "py", "optimizes", "iac"]
		for word in ignore_words:
			self.spell.word_frequency.add(word)

	def check_spelling(self, filtered_text):
		spelling_results = {}
		mispellings_list = []
		spelled_correctly = True
		line_number = 0
		for line in filtered_text:
			#print(f"checking: {line}")
			line_number = line_number + 1
			words = line.split()
			for word in words:
				if word not in self.spell:
					cor = self.spell.correction(word)
					misspelling = {"line" : line_number, "mispelling" : word, "suggestions" : cor}
					mispellings_list.append(misspelling)
					spelled_correctly = False
		spelling_results = {"spelled_correctly" : spelled_correctly, "mispellings" : mispellings_list}
		return spelling_results		

spellchecker = SubmissionSpellChecker()

def read_raw_markdown_file(filename):
	text = ""
	with open(filename, "r", encoding="utf-8") as file:
		text = file.read()
	return text


def read_markdown_filtered_file(filename):
	lines = []
	in_block = False
	with open(filename, "r", encoding="utf-8") as file:

		for line in file.readlines():
			evaluate_line = line
			if "```" in evaluate_line and not in_block:
				in_block = True
				evaluate_line = ""
			if "```" in evaluate_line and in_block:
				in_block = False
				evaluate_line = ""
			if in_block:
				evaluate_line = ""
			if evaluate_line != "":
				lines.append(evaluate_line)

	lowered_text = [i.lower() for i  in lines]
	no_links =[re.sub("http[^ ]+", "", i) for i  in lowered_text]
	filtered_text = [re.sub("[^a-zA-Z]", " ", i) for i in no_links]
	return filtered_text


print("Run")

errors_found = False
year = datetime.datetime.now().year
md_files = glob.glob(f"../../_posts/{year}*.md")
for file in md_files:
	text_lines = read_markdown_filtered_file(file)  
	line_count = len(text_lines)
	print(f"File: {file} ({line_count})")
	results = spellchecker.check_spelling(text_lines)
	for mispelling in results["mispellings"]:
		line = mispelling["line"]
		word = mispelling["mispelling"]
		suggestion = mispelling["suggestions"]
		print(f"\tLine: {line}  for '{word}' try '{suggestion}'")
		print()
		errors_found = True

if errors_found:
	sys.exit(1)


