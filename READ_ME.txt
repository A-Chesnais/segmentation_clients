*** Comment est structur� ce r�pertoire ? ***


- Un dossier �HTML� qui contient les r�sultats de la segmentation et de l�analyse de stabilit� de 
  celle ci, directement consultables

- Un dossier �Data� qui contient les notebooks r�alisant l�assemblage des bases de donn�es Olist 
  et contenant l�analyse exploratoire. Un fichier permet l�assemblage en une base de donn�es clients / produits et l�autre 
  en une base de donn�es clients / commandes. Deux autres fichiers permettent de faire les m�mes op�rations, mais en 
  s�parant les donn�es sur 2017 et 2018. L�EDA est plus compl�te dans le notebook �Assemblage_consumer_order�,
  il s�agit de celle qui sert de base pour le reste du travail effectu�.

- Un dossier �Segmentation_definition�, qui contient les notebooks permettant l��tude de la segmentation des deux points 
  de vues mentionn�s pr�c�demment.

- Un dossier �Segmentation_stability�, qui contient le notebook d��tude de la stabilit� de la segmentation.



*** Quelles librairies sont n�cessaires ? ***


Le code a �t� r�dig� en Python, les librairies suivantes doivent �tre install�es :

- Pandas
- Numpy
- Scipy
- Matplotlib
- Seaborn
- Sklearn

A noter qu'il est �galement n�cessaire que le fichier 'functions' soit dans le m�me r�pertoire que le notebook '�Segmentation_definition� .
Le fichier 'functions_extended� doit lui �tre dans le m�me r�pertoire que le notebook '�Segmentation_stability� 

Jupiter Notebook est n�cessaire pour l�ouverture des Notebook.


*** Comment utiliser ce r�pertoire ? ***



- T�l�charger les 9 datasets � l�adresse ci dessous et les placer dans le r�pertoire �Data� :

https://www.kaggle.com/olistbr/brazilian-ecommerce#olist_order_items_dataset.csv

- Ouvrir et lancer les notebooks suivants dans le r�pertoire �Data� :

	- �Assemblage_consumer_order�
	- �Assemblage_consumer_order_yearly�
	- �Assemblage_consumer_product�
	- �Assemblage_consumer_product_yearly�

	Attention v�rifier que la derni�re ligne de code contenant l�enregistrement des datasets n�est 	pas comment�e !

- Placer les fichiers obtenus suivants dans le r�pertoire �Segmentation_definition� :

	- �BDD_customers_orders�
	- �BDD_customers_products�

- Placer les fichiers obtenus suivants dans le r�pertoire �Segmentation_stability� :

	- �BDD_customers_orders_2017�
	- �BDD_customers_orders_2018�
	- �BDD_customers_products_2017�
	- �BDD_customers_products_2018�

- Lancer les Notebooks suivants au sein du r�pertoire �Segmentation_definition�  pour la r�alisation de la segmentation 
  d�un point de vue client / produits et client / commandes :

	- Segmentation_customers_products
	- segmentation_customers_orders_VF

	Attention l�ordre des segments en sortie de clustering peut �tre diff�rent � chaque ex�cution du code, 
	le texte ne correspondra potentiellement plus aux graphiques, il faudra probablement inverser des num�ros
	de segment !

- Lancer le notebook �segment_stability� au sein du r�pertoire �ponyme pour obtenir l�analyse de la stabilit� 
  de la segmentation.




