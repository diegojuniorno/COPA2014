from django.db import models


class Jogos(models.Model):

	
	Brasil = models.CharField(db_index=True, max_length='50', null=False)
	Croacia = models.CharField(db_index=True, max_length='50', null=False)
	Placar1 = models.CharField(db_index=True, max_length='50', null=False)
	Placar2 = models.CharField(db_index=True, max_length='50', null=False)

	Brasil = models.CharField(db_index=True, max_length='50', null=False)
	Mexico = models.CharField(db_index=True, max_length='50', null=False)
	Placar1 = models.CharField(db_index=True, max_length='50', null=False)
	Placar2 = models.CharField(db_index=True, max_length='50', null=False)

	Brasil = models.CharField(db_index=True, max_length='50', null=False)
	Camaroes = models.CharField(db_index=True, max_length='50', null=False)
	Placar1 = models.CharField(db_index=True, max_length='50', null=False)
	Placar2 = models.CharField(db_index=True, max_length='50', null=False)