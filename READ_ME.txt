*** Comment est structuré ce répertoire ? ***


- Un dossier ‘HTML’ qui contient les résultats de la segmentation et de l’analyse de stabilité de 
  celle ci, directement consultables

- Un dossier ‘Data’ qui contient les notebooks réalisant l’assemblage des bases de données Olist 
  et contenant l’analyse exploratoire. Un fichier permet l’assemblage en une base de données clients / produits et l’autre 
  en une base de données clients / commandes. Deux autres fichiers permettent de faire les mêmes opérations, mais en 
  séparant les données sur 2017 et 2018. L’EDA est plus complète dans le notebook ‘Assemblage_consumer_order’,
  il s’agit de celle qui sert de base pour le reste du travail effectué.

- Un dossier ’Segmentation_definition’, qui contient les notebooks permettant l’étude de la segmentation des deux points 
  de vues mentionnés précédemment.

- Un dossier ’Segmentation_stability’, qui contient le notebook d’étude de la stabilité de la segmentation.



*** Quelles librairies sont nécessaires ? ***


Le code a été rédigé en Python, les librairies suivantes doivent être installées :

- Pandas
- Numpy
- Scipy
- Matplotlib
- Seaborn
- Sklearn

A noter qu'il est également nécessaire que le fichier 'functions' soit dans le même répertoire que le notebook '‘Segmentation_definition’ .
Le fichier 'functions_extended’ doit lui être dans le même répertoire que le notebook '‘Segmentation_stability’ 

Jupiter Notebook est nécessaire pour l’ouverture des Notebook.


*** Comment utiliser ce répertoire ? ***



- Télécharger les 9 datasets à l’adresse ci dessous et les placer dans le répertoire ‘Data’ :

https://www.kaggle.com/olistbr/brazilian-ecommerce#olist_order_items_dataset.csv

- Ouvrir et lancer les notebooks suivants dans le répertoire ‘Data’ :

	- ‘Assemblage_consumer_order’
	- ‘Assemblage_consumer_order_yearly’
	- ‘Assemblage_consumer_product’
	- ‘Assemblage_consumer_product_yearly’

	Attention vérifier que la dernière ligne de code contenant l’enregistrement des datasets n’est 	pas commentée !

- Placer les fichiers obtenus suivants dans le répertoire ‘Segmentation_definition’ :

	- ‘BDD_customers_orders’
	- ‘BDD_customers_products’

- Placer les fichiers obtenus suivants dans le répertoire ‘Segmentation_stability’ :

	- ‘BDD_customers_orders_2017’
	- ‘BDD_customers_orders_2018’
	- ‘BDD_customers_products_2017’
	- ‘BDD_customers_products_2018’

- Lancer les Notebooks suivants au sein du répertoire ‘Segmentation_definition’  pour la réalisation de la segmentation 
  d’un point de vue client / produits et client / commandes :

	- Segmentation_customers_products
	- segmentation_customers_orders_VF

	Attention l’ordre des segments en sortie de clustering peut être différent à chaque exécution du code, 
	le texte ne correspondra potentiellement plus aux graphiques, il faudra probablement inverser des numéros
	de segment !

- Lancer le notebook ‘segment_stability’ au sein du répertoire éponyme pour obtenir l’analyse de la stabilité 
  de la segmentation.




