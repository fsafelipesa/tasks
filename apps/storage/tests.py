from django.test import TestCase
from apps.storage.models import Directory, File

class StorageTestCase(TestCase):
    def setUp(self):
        dir_1 = Directory.objects.create(name="diretorio_1")
        dir_2 = Directory.objects.create(name="diretorio_2")
        subdir_1 = Directory.objects.create(name="subdiretorio_1", parent=dir_1)
        file_1 = File.objects.create(name="arquivo.txt", parent=subdir_1)

    def test_storage(self):
        dir_1 = Directory.objects.get(name="diretorio_1")
        dir_2 = Directory.objects.get(name="diretorio_2")
        subdir_1 = Directory.objects.get(name="subdiretorio_1")
        file_1 = File.objects.get(name="arquivo.txt")

        self.assertEqual(dir_1.path(), f'/diretorio_1')
        self.assertEqual(dir_2.path(), f'/diretorio_2')
        self.assertEqual(subdir_1.path(), f'/diretorio_1/subdiretorio_1')
        self.assertEqual(file_1.path(), f'/diretorio_1/subdiretorio_1/arquivo.txt')
