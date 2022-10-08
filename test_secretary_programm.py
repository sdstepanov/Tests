import unittest.mock
import pytest
from main import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, get_doc_shelf, add_new_shelf, \
	delete_doc


class TestProgram:
	number = ["2207 876234", "11-2", "10006"]
	num_name = [
		("2207 876234", "Василий Гупкин"),
		("11-2", "Геннадий Покемонов"),
		("10006", "Аристарх Павлов")
	]
	directories = [
		('2207 876234', '1'),
		('11-2', '1'),
		('5455 028765', None),
		('10006', '2')
	]
	shelf = [
		('1', ('1', False)),
		('2', ('2', False)),
		('3', ('3', False)),
		('4', ('4', True)),
		('5', ('5', True))
	]
	numbers = [
		("2207 876234", ("2207 876234", True)),
		("11-2", ("11-2", True)),
		("10006", ("10006", True)),
		("1245", None)
	]

	@pytest.mark.parametrize('data', number)
	def test_check_document_existance(self, data):
		result = check_document_existance(data)
		assert result

	@pytest.mark.parametrize('data, res', num_name)
	def test_get_doc_owner_name(self, data, res):
		with unittest.mock.patch('builtins.input', return_value=data):
			result = get_doc_owner_name()
			assert result == res

	def test_get_all_doc_owners_names(self):
		result = get_all_doc_owners_names()
		assert result == {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'}

	@pytest.mark.parametrize('data, res', directories)
	def test_get_doc_shelf(self, data, res):
		with unittest.mock.patch('builtins.input', return_value=data):
			result = get_doc_shelf()
			assert result == res

	@pytest.mark.parametrize('data, res', shelf)
	def test_add_new_shelf(self, data, res):
		with unittest.mock.patch('builtins.input', return_value=data):
			result = add_new_shelf()
			assert result == res

	@pytest.mark.parametrize('data, res', numbers)
	def test_delete_doc(self, data, res):
		with unittest.mock.patch('builtins.input', return_value=data):
			result = delete_doc()
			assert result == res
