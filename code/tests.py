from main import write_dict_to_csv

def test_write_dict_to_csv():
	test_dict = {"A": {"followers": ["B", "C"], "friends": ["D", "E"]}}
	write_dict_to_csv(test_dict)

test_write_dict_to_csv()