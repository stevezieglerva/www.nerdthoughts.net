from spellchecker import SpellChecker
spell = SpellChecker()

spell.known(['hungate', 'google'])

with open("../../_drafts/devopsdays-rdu-2019.md", "r") as file:
	line = 0
	for lines in file.readlines():
		line = line + 1
		print(line)
		words = lines.split(" ")
		misspelled = spell.unknown(words)
		for word in misspelled:
			clean_word = word.strip()
			clean_word = clean_word.replace("#", "")
			clean_word = clean_word.replace("*", "")
			clean_word = clean_word.replace("[", "")
			clean_word = clean_word.replace("]", "")
			clean_word = clean_word.replace("()", "")
			clean_word = clean_word.replace(")", "")
			clean_word = clean_word.replace("-", "")
			clean_word = clean_word.replace(".", "")			
			candidates = spell.candidates(clean_word)
			print(f"\t{line}: '{clean_word}' might be {candidates}")




import unittest
from spellchecker import SpellChecker
import os
import re
import sys
import urllib
import json


class SubmissionSpellChecker():
	def __init__(self):
		self.spell = SpellChecker()
		self.spell.word_frequency.load_text_file("rfp.txt")
		ignore_words = ["#", "##", "###", "####", "#####", "http", "com", "jpg", "miica", "trello", "solutioning", "etl", "oig", "owasp", "sonarqube", "php", "website", "handoffs", "standups", "sagemaker", "talend", "nutch", "gensim", "vscode", "tf", "idf", "markdown", "wireframes", "mvp", "nosql", "dynamodb", "prototyped", "retros", "devs", "cloudfront", "lambdas", "unittest", "unittest", "jasmine", "worldspace", "prioritized", "lambdas", "tokenizing", "leverages", "paas", "microservices", "vpc", "cloudtrail", "cloudwatch", "iam", "jumpcloud", "saml", "sso", "mysql", "virtualized", "cdn", "downloads", "mdasii", "userguide", "init", "decrypt", "venv", "vpcs", "pre-signed", "priv", "url", "etls", "decryption", "dwhadmn", "ziegler", "Vectorization", "Financialmodelingprep", "backend", "initializers", "rmsprop", "overfitting", "dirichlet", "py", "optimizes", "iac"]





		for word in ignore_words:
			self.spell.word_frequency.add(word)

	def check_spelling(self, filtered_text):
		spelling_results = {}
		mispellings_list = []
		spelled_correctly = True
		line_number = 0
		for line in filtered_text:
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
	with open(filename, "r", encoding="utf-8") as file:
		lines = file.readlines()
	lowered_text = [i.lower() for i  in lines]
	filtered_text = [re.sub("[^a-zA-Z]", " ", i) for i in lowered_text]
	return filtered_text

def count_non_space_characters(text):
	return len(text.replace(" ", ""))

def is_link_valid(relative_url):
	found = os.path.isfile(relative_url)
	return found
	
def extract_image_links(text):
	results = []
	matches = re.findall(r"!\[[^]]*\]\([^)]+\)", text)
	for match in matches:
		image = {}
		link_text = re.sub(r"\([^)]+\)$", "", match)
		link_text = re.sub(r"!\[|\]", "", link_text)

		path = re.sub(r"!\[[^]]*\]", "", match)
		path = re.sub(r" \"[^\"]*\"", "", path)
		path = re.sub(r"!|\(|\)", "", path)

		alt_text = re.sub(r"^.*\(", "", match)
		alt_text = re.sub(r"^[^\"]+", "", alt_text)
		alt_text = re.sub(r"\"", "", alt_text)	
		alt_text = re.sub(r"\)$", "", alt_text)	
		image = {
			"link_text" : link_text,
			"path" : path,
			"alt_text" : alt_text
			}
		results.append(image)
	return results


def are_all_image_links_valid(image_link_list):
	all_valid = True
	if image_link_list is not None:
		for image in image_link_list:
			if is_link_valid(os.path.join("..", image["path"])) == False:
				all_valid = False
				sys.stderr.write("\nBad image reference for: {}".format(image))
	return all_valid


def print_counts_and_images(filename, raw_file_text, image_links):
	all = len(raw_file_text)
	spaces = raw_file_text.count(" ")
	total = all - spaces
	print("\n{0:<30} characters: {1:>5} all - {2:>5} spaces = {3:>5} total (WARNING: DOES NOT INCLUDE IMAGES! COUNT THOSE ON YOUR OWN!)".format(filename, all, spaces, total))
	print("{0:<30} images    : {1:>5} images".format(filename, len(image_links)))




class Solution(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.filename = os.path.join("..", "Solution.pdf" ) 

	def test_file_exists(self):
		self.assertTrue(os.path.isfile(self.filename), "Expected to find {}".format(self.filename))
	

class Commits(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.filename = os.path.join("..", "Commits.pdf" ) 

	def test_file_exists(self):
		self.assertTrue(os.path.isfile(self.filename), "Expected to find {}".format(self.filename))


class UserStories(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.filename = os.path.join("..", "UserStories.pdf" ) 

	def test_file_exists(self):
		self.assertTrue(os.path.isfile(self.filename), "Expected to find {}".format(self.filename))


class Init(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.filename = os.path.join("..", "init.sh" ) 

	def test_file_exists(self):
		self.assertTrue(os.path.isfile(self.filename), "Expected to find {}".format(self.filename))


class InteractiveNotebook(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.filename = os.path.join("..", "InteractiveNotebook.ipynb" ) 

	def test_file_exists(self):
		self.assertTrue(os.path.isfile(self.filename), "Expected to find {}".format(self.filename))


class Models(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.filename = os.path.join("..", "models", "Models.md" ) 
		cls.character_count_limit = 10000
		cls.image_count_limit = 10
		cls.raw_file_text = read_raw_markdown_file(cls.filename)
		cls.filtered_text = read_markdown_filtered_file(cls.filename)
		cls.image_links = extract_image_links(cls.raw_file_text)
		print_counts_and_images(cls.filename, cls.raw_file_text, cls.image_links)

	def check_spelling(self, filtered_text):
		spelling_results = spellchecker.check_spelling(filtered_text)
		if spelling_results["spelled_correctly"] == False:
			sys.stderr.write("\n*** Filename: {}".format(self.filename))
			for misspelling in spelling_results["mispellings"]:
				sys.stderr.write("\n\tLine: {} , The best spelling for '{}' is '{}'".format(misspelling["line"], misspelling["mispelling"], misspelling["suggestions"]))

		return spelling_results["spelled_correctly"]


	def test_file_is_within_image_count(self):
		# Assert
		self.assertLessEqual(self.raw_file_text.count("!["), self.image_count_limit)


	def test_file_is_spelled_correctly(self):
		# Act
		spelled_correctly = self.check_spelling(self.filtered_text)

		# Assert
		self.assertTrue(spelled_correctly)


	def test_file_is_within_character_count(self):
		# Act
		result = count_non_space_characters(self.raw_file_text)

		# Assert
		self.assertLessEqual(result, self.character_count_limit)


	def test_file_has_enough_text(self):
		# Act
		result = count_non_space_characters(self.raw_file_text)

		# Assert
		self.assertGreaterEqual(result, self.character_count_limit * .5)


	def test_image_paths_are_valid(self):
		# Act
		result = are_all_image_links_valid(self.image_links)

		# Assert
		self.assertTrue(result)


class Approach(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.filename = os.path.join("..", "Approach.md" ) 
		cls.character_count_limit = 5000
		cls.image_count_limit = 10
		cls.raw_file_text = read_raw_markdown_file(cls.filename)
		cls.filtered_text = read_markdown_filtered_file(cls.filename)
		cls.image_links = extract_image_links(cls.raw_file_text)
		print_counts_and_images(cls.filename, cls.raw_file_text, cls.image_links)

	def check_spelling(self, filtered_text):
		spelling_results = spellchecker.check_spelling(filtered_text)
		if spelling_results["spelled_correctly"] == False:
			sys.stderr.write("\n*** Filename: {}".format(self.filename))
			for misspelling in spelling_results["mispellings"]:
				sys.stderr.write("\n\tLine: {} , The best spelling for '{}' is '{}'".format(misspelling["line"], misspelling["mispelling"], misspelling["suggestions"]))

		return spelling_results["spelled_correctly"]

	def test_file_is_within_image_count(self):
		# Assert
		self.assertLessEqual(self.raw_file_text.count("!["), self.image_count_limit)


	def test_file_is_spelled_correctly(self):
		# Act
		spelled_correctly = self.check_spelling(self.filtered_text)

		# Assert
		self.assertTrue(spelled_correctly)


	def test_file_is_within_character_count(self):
		# Act
		result = count_non_space_characters(self.raw_file_text)

		# Assert
		self.assertLessEqual(result, self.character_count_limit)


	def test_file_has_enough_text(self):
		# Act
		result = count_non_space_characters(self.raw_file_text)

		# Assert
		self.assertGreaterEqual(result, self.character_count_limit * .5)


	def test_image_paths_are_valid(self):
		# Act
		result = are_all_image_links_valid(self.image_links)

		# Assert
		self.assertTrue(result)


class Scans(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.filename = os.path.join("..", "Scans.md" ) 
		cls.character_count_limit = 1000
		cls.image_count_limit = 5
		cls.raw_file_text = read_raw_markdown_file(cls.filename)
		cls.filtered_text = read_markdown_filtered_file(cls.filename)
		cls.image_links = extract_image_links(cls.raw_file_text)
		print_counts_and_images(cls.filename, cls.raw_file_text, cls.image_links)

	def check_spelling(self, filtered_text):
		spelling_results = spellchecker.check_spelling(filtered_text)
		if spelling_results["spelled_correctly"] == False:
			sys.stderr.write("\n*** Filename: {}".format(self.filename))
			for misspelling in spelling_results["mispellings"]:
				sys.stderr.write("\n\tLine: {} , The best spelling for '{}' is '{}'".format(misspelling["line"], misspelling["mispelling"], misspelling["suggestions"]))

		return spelling_results["spelled_correctly"]

	def test_file_is_within_image_count(self):
		# Assert
		self.assertLessEqual(self.raw_file_text.count("!["), self.image_count_limit)


	def test_file_is_spelled_correctly(self):
		# Act
		spelled_correctly = self.check_spelling(self.filtered_text)

		# Assert
		self.assertTrue(spelled_correctly)


	def test_file_is_within_character_count(self):
		# Act
		result = count_non_space_characters(self.raw_file_text)

		# Assert
		self.assertLessEqual(result, self.character_count_limit)


	def test_image_paths_are_valid(self):
		# Act
		result = are_all_image_links_valid(self.image_links)

		# Assert
		self.assertTrue(result)


class Readme(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.filename = os.path.join("..", "ReadME.md" ) 
		cls.character_count_limit = 10000
		cls.image_count_limit = 10
		cls.raw_file_text = read_raw_markdown_file(cls.filename)
		cls.filtered_text = read_markdown_filtered_file(cls.filename)
		cls.image_links = extract_image_links(cls.raw_file_text)
		print_counts_and_images(cls.filename, cls.raw_file_text, cls.image_links)

	def check_spelling(self, filtered_text):
		spelling_results = spellchecker.check_spelling(filtered_text)
		if spelling_results["spelled_correctly"] == False:
			sys.stderr.write("\n*** Filename: {}".format(self.filename))
			for misspelling in spelling_results["mispellings"]:
				sys.stderr.write("\n\tLine: {} , The best spelling for '{}' is '{}'".format(misspelling["line"], misspelling["mispelling"], misspelling["suggestions"]))

		return spelling_results["spelled_correctly"]


	def test_file_is_within_image_count(self):
		# Assert
		self.assertLessEqual(self.raw_file_text.count("!["), self.image_count_limit)


	def test_file_is_spelled_correctly(self):
		# Act
		spelled_correctly = self.check_spelling(self.filtered_text)

		# Assert
		self.assertTrue(spelled_correctly)


	def test_file_is_within_character_count(self):
		# Act
		result = count_non_space_characters(self.raw_file_text)

		# Assert
		self.assertLessEqual(result, self.character_count_limit)


	def test_file_has_enough_text(self):
		# Act
		result = count_non_space_characters(self.raw_file_text)

		# Assert
		self.assertGreaterEqual(result, self.character_count_limit * .5)		


	def test_image_paths_are_valid(self):
		# Act
		result = are_all_image_links_valid(self.image_links)

		# Assert
		self.assertTrue(result)


	def test_single_level_architecture_diagram_exists(self):
		# Act
		diagram_filename = os.path.join("submission_images", "single_level_architecture_diagram.jpg" ) 
		found = os.path.isfile(diagram_filename)
		
		# Assert
		self.assertTrue(found, "Expected to find {}".format(diagram_filename))
	

if __name__ == '__main__':
	x = Models()


	#unittest.main()		
	# Run the tests but don't exit with system error to allow CodeBuild to trap it
	result = unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.join(".") , pattern="*.py") )
	print("\n")
	print("\tFailed: {0}  :(".format(len(result.failures)))
	count = 0
	for failure in result.failures:
		count = count + 1
		testcase = failure[0]
		test_class = type(testcase).__name__
		test = testcase.id().replace("submission_qa_unit_tests.", "").replace(test_class, "").replace(".", "")
		print("\t\t{0:>2}. {1:<20} {2}".format(count, type(testcase).__name__ , test))

	print("\n\tError: {0}  :(".format(len(result.errors)))
	for error in result.errors:
		count = count + 1
		testcase = error[0]
		test_class = type(testcase).__name__
		test = testcase.id().replace("submission_qa_unit_tests.", "").replace(test_class, "").replace(".", "")
		print("\t\t{0:>2}. {1:<20} {2}".format(count, type(testcase).__name__ , test))

	print("\n\tPassed: {0}  :)".format(result.testsRun))
	print("\n\n")
