mydir = "/Users/analutzky/Desktop/data/scrapping_ETS/data/15_08_2017" " # je définis mon répertoire où seront créés mes fichiers scrapés // defining the directory where the scraped data will be stored 
date = "_15_08_2017"

###### PHASE 0: initialisation, lancer windmill // PHASE 0: initialization

from BeautifulSoup import BeautifulSoup
# pour scraper on va utiliser windmill. windmill va ouvrir firefox et faire semblant d'etre un utilisateur humain // In order to scrape, we're going to use windmill. windmill is going to open firefox and behave like a human
# on commence par charger les fonctions nécessaires // we start by importing the necessary modules
from windmill.authoring import setup_module, WindmillTestClient
from windmill.conf import global_settings
import sys

# On configure windmill pour qu'il utilise firefox // we configure windmill in order to have it use firefox
global_settings.START_FIREFOX = True # This makes it use Firefox
setup_module(sys.modules[__name__])
client = WindmillTestClient(__name__)

# temps avant timeout (pour ne pas bloquer si la page ne s'ouvre pas) // a certain amount of time before it gives up opening a page, so that it doesn't get stuck
timeOut=u'8000'		# 8 secondes avant time out // 8 sec before timeout
# temps de pause entre deux requêtes (pour ne pas surcharger les serveurs) // time lapse between two requests (not to overwhelm the servers)
timeSleep=u'100' 	# 0.1 seconde // 0.1 sec

# l'url qu'on va vouloir scraper // the url we want to scrape
rootServer="http://ec.europa.eu"
BASE_URL="http://ec.europa.eu/environment/ets/napMgt.do"
# la liste des pays qu'on va scrapper // the list of countries we want to scrape
cntryList=['France','Germany','Austria','Belgium','Bulgaria','Croatia','Cyprus','Czech Republic','Denmark',
'Estonia','Finland','Greece','Hungary','Iceland','Ireland','Italy','Latvia','Liechtenstein','Lithuania','Luxembourg','Malta','Netherlands','Norway','Poland','Portugal','Romania','Slovakia','Slovenia','Spain','Sweden','United Kingdom']

# ouvrir la page // open the page
client.open(url=BASE_URL)
client.waits.forPageLoad(timeout=timeOut) # et qu'elle se charge // load the page
client.waits.sleep(milliseconds=timeSleep) # attendre que la page s'ouvre // wait till the web page opens


###### PHASE 1: lister les tables qui contiennent les liens // PHASE 1: listing the tables that contain links


list_of_tables=[]

for cntry in cntryList:
	# selectionner un pays et une période et ouvrir la page // select a country and a period and open the page 
	mute=client.selectReset(name='nap.registryCodeArray') # deselectionner toutes les options pays dans le choix multiple nap.registryCodeArray parce que quand on ouvre avec client il en sélectionne plusieurs // unselect all the options about the country in multiple choice nap.registryCodeArray
	mute=client.select(name='nap.registryCodeArray',option=cntry) # selectionner l'option pays dans le choix multiple nap.registryCodeArray // selection the option country in the multiple choice nap.registryCodeArray
	mute=client.select(name='periodCode',option='All') # selectionner la periode dans le choix multiple periodCode // select period in multiple choice periodCode
	mute=client.click(value='Search') # cliquer sur search // click on search
	# attendre que la page s'update // wait till the page gets updated
	mute=client.waits.forPageLoad(timeout=timeOut)
	mute=client.waits.sleep(milliseconds=timeSleep) 
	# scraper le contenu // scrape content
	response = client.commands.getPageText() # récupérer contenu de la page en texte brut (si retour à la ligne \n, si tabulation \t... c'est illisible ! // get the page's content as a raw text (cause if there is some wrap to the next line \n, or tab \t... it gets messy and unreadable !)
	# response c'est un array avec plusieurs éléments : 'error' (est-ce que ça a marché, true/false), 'result' (le code de la page), etc. // response is an array with several elements : 'error' (did it work, true/false), 'result' (the page's code), etc.
	soup = BeautifulSoup(response['result']) # le rend lisible
	# BeautifulSoup c'est pratique parce que ça a des fonctions find (sort la 1e occurrence) et findAll (sort toutes les occurrences), qui permettent de faire pomme F avec des attributs html dans des balises // BeautifulSoup is practical because it has the 'find' function (shows the 1st occurrence) and findAll (shows all the occurrences), which allow to search for the HTML attributes in tags
	table = soup.find('table', attrs={'id':'tblNapSearchResult'}) # find the table
	table_body = table.find('tbody') # table's body
	rows = table_body.findAll('tr',recursive=False)
	for i,row in enumerate(rows):
		if i<3:
			continue # on passe le titre de la table et les noms de colonnes (2 lignes) // we pass over the table's title and the columns' names (2 rows) 
		cols = row.findAll('td',recursive=False)
		link=rootServer+(cols[4].findAll('a', attrs={"id":u"lnkNapInformation"})[1]['href'])
#		cntry=cols[0].text.strip('&nbsp;') # this seems to remove s and n at the end of country names. find out why and correct it -->  use .replace("&nbsp;", "") instead of strip()
		period=cols[1].text.replace("&nbsp;", "")
		list_of_tables.append([cntry,period,link])

f_out=open(mydir + '/list_of_tables' + date + '.txt','w')
for line in list_of_tables:
	f_out.write('\t'.join(line)+'\n')

f_out.close()


###### PHASE 2: scraper tous les liens // PHASE 2: scrape all the links

f_out=open(mydir + '/list_of_links_allCountries' + date + '.txt','a') # on ouvre le fichier en mode append afin de préserver ce qui a déjà été écrit en cas de plantage (car quand on ouvre en mode écriture, on écrase le contenu précédent). En mode append, ça ouvre le fichier, passe toutes les lignes et rajoute à la fin // we open the file in an "append' mode, in order to save what has already been written in case of bug (because when we open in a "writing" mode, we erase the former content). In an "append" mode, it opens the file, passes over all the lines and adds content at the end
f_out.write('cntry\tperiod\tpagenum\tinst_id\tpermit_id\tlink\n')

pageStart=0		# numero de page-1 // number of page -1
tabStart=0
error=True # par défaut error est à true, donc je rentre dans ma boucle, et je remets error à faulse
while error :
	error=False
	try:
		list_of_tables=open(mydir + '/list_of_tables' + date + '.txt','rU') # rU opens the file as a text file, but lines may be terminated by any of the following: the Unix end-of-line convention '\n', the Macintosh convention '\r', or the Windows convention '\r\n'
		for itab,line_tab in enumerate(list_of_tables):
			print itab, line_tab
			if itab<tabStart:
				continue
			table_to_scrap=line_tab.strip().split('\t')
			cntry=table_to_scrap[0]
			period=table_to_scrap[1]
			URL=table_to_scrap[2]
			print 'opening URL '+cntry+' '+period #pour ce qu'on fait quand le code s'exécute // that's to see what's happening when the code is running
			mute=client.open(url=URL)
			mute=client.waits.forPageLoad(timeout=timeOut)	
			mute=client.waits.sleep(milliseconds=timeSleep) 
			response=client.commands.getPageText() # recuperer contenu de la page en texte brut (si retour à la ligne \n, si tabulation \t... c'est illisible ! // grab the page's content as a raw text (cause if there is some wrap to the next line \n, or tab \t... it gets messy and unreadable !)
			# response c'est un array avec plusieurs éléments : 'error' (est-ce que ça a marché, true/false), 'result' (le code de la page), etc. // response is an array with several elements : 'error' (did it work, true/false), 'result' (the page's code), etc.
			soup = BeautifulSoup(response['result'])
			inputPageNumber=soup.findAll('input', attrs={"name":u"resultList.lastPageNumber"})
			if len(inputPageNumber)>0:
				NbPages=int(inputPageNumber[0]['value'])
			else:
				NbPages=1	
			print str(NbPages)+'page to scrap'
			for pagenum in range(0,NbPages):
				if itab==tabStart and pagenum<pageStart :
					print '\ntable'+str(itab)+', page'+str(pagenum+1)+'/'+str(NbPages)+' skipped'
					mute=client.click(value='Next>') 
					mute=client.waits.forPageLoad(timeout=timeOut)	
					mute=client.waits.sleep(milliseconds=timeSleep)
					continue
				table = soup.find('table', attrs={'id':'tblNapList'})
				print '.', # pour savoir où le pgm en est : s'il plante, on sait où il a planté (avec une virgule pour ne pas aller à la ligne et ainsi prendre moins de place) // # that's to see where the program is : if there's a bug, we now where (with a coma to avoid line wraping, not to take too much space) 
				table_body = table.find('tbody')
				print '.',
				rows = table_body.findAll('tr',recursive=False)
				for i,row in enumerate(rows):
					if i<3:
						continue
					print i,
					cols = row.findAll('td',recursive=False)
					print '.',
					findlinks=row.findAll('a', attrs={"id":u"lnkNapInformation"})
					if len(findlinks)<3:
						continue
					link=findlinks[2]['href']
					print '.',
					cols = [col.text.replace("&nbsp;", "") for col in cols]
					print '.',
					inst_id=cols[0]
					permit_id=cols[5]
					line=[cntry,period,pagenum+1,inst_id,permit_id,link]
					f_out.write('\t'.join([str(x) for x in line])+'\n')
				print 'table'+str(itab)+', page'+str(pagenum+1)+'/'+str(NbPages)+' read'
				if NbPages>1:
					mute=client.click(value='Next>') # 
					mute=client.waits.forPageLoad(timeout=timeOut)
					mute=client.waits.sleep(milliseconds=timeSleep)
					response=client.commands.getPageText()
					soup = BeautifulSoup(response['result'])
			# read last page	
			if NbPages>1:
				table = soup.find('table', attrs={'id':'tblNapList'})
				table_body = table.find('tbody')	
				rows = table_body.findAll('tr',recursive=False)
				for i,row in enumerate(rows):
					if i<3:
						continue
					cols = row.findAll('td',recursive=False)
					findlinks=row.findAll('a', attrs={"id":u"lnkNapInformation"})
					if len(findlinks)<3:
						continue
					link=findlinks[2]['href']
					cols = [col.text.replace("&nbsp;", "") for col in cols]
					inst_id=cols[0]
					permit_id=cols[5]
					line=[cntry,period,pagenum+1,inst_id,permit_id,link]
					f_out.write('\t'.join([str(x) for x in line])+'\n')
	except:
		error=True
		tabStart=itab
		pageStart=pagenum
		list_of_tables.close()

list_of_tables.close()
f_out.close()


###### PHASE 3: checker les liens qu'on a scrappé et retirer les doublons // PHASE 3: check the links we scraped and get rid of duplicates
# mergé avec la phase 4 (panda) // merged with phase 4 (panda)

################################### PHASE 4: suivre les liens qu'on a scrapé et scraper les données // PHASE 4: follow the links we scraped and scrape the data

# voir // see
# https://www.packtpub.com/books/content/web-scraping-python
# et https://www.packtpub.com/books/content/web-scraping-python-part-2 

# setup mechanize : (pour ouvrir des liens) // to open links
import mechanize
br=mechanize.Browser() # c'est comme si on avait mis client = mechanize.browser // it's as if we'd put client = mechanize.browser
br.set_handle_robots(False) # pour lire sans tenir compte de robots.txt (qui dit essentiellement que les robots ne doivent pas scraper le site) // to be able to read without taking robots.txt into account (which basically says that bots should not scrape the website)
# charger le module time (pour faire des pauses) // load the time module (to make some breaks)
import time	
# charger le module BeautifulSoup (pour lire le html) // load the module BeautifulSoup (to read html)
from BeautifulSoup import BeautifulSoup
# charger le module pandas (pour enlever les duplicates) // load the pandas module (to get rid of duplicates)
import pandas as pd	

# on lit le csv (tous les liens à scrapper) // reading csv file (which contains all the links to scrape)
DF=pd.read_csv(mydir + '/list_of_links_allCountries' + date + '.txt',sep='\t',error_bad_lines=True) # error_bad_lines c'est un argument qui existe déjà dans pd.read_casv : quand un ligne est anormale, panda plante. Ca permet de l'éviter : au lieu de planter, il dit cette ligne a un pb, je la passe. // error_bad_lines is an argument that already exists in pd.read_casv : when a line is not normal, panda bugs. This enables to prevent it : instead of bugging, panda says : ok this line has a problem, I go to the next one. 

# on enleve les liens qui sont en double // getting rid of th duplicate links 
DFunique=DF.drop_duplicates(subset='link') # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop_duplicates.html

import io
import re # pour remplacer des charactères (avec des regexpr) // replace some characters with regex
f_out=io.open(mydir + '/Emissions_allCompanies_allCountries' + date + '.txt','a', encoding='utf16') # fichier output pour écrire les résultats // output file to write the results
f_err=io.open(mydir + '/Emissions_allCompanies_allCountries_errors' + date + '.txt','w', encoding='utf16') # fichier pour écrire les lignes avec des erreurs // file to write lines with errors
for l,link in enumerate(DFunique['link']):
	print l,link
	url='http://ec.europa.eu/environment/ets/'+link[12:]
	# lire avec mechanize // read with mechanize
	print '.',
	page=br.open(url)
	html = page.read() # recuperer contenu de la page en texte brut (si retour à la ligne \n, si tabulation \t... c'est illisible ! // grab the page's content as a raw text (cause if there is some wrap to the next line \n, or tab \t... it gets messy and unreadable !)
	# make pretty with beautiful soup
	soup=BeautifulSoup(html) # ça le structure // getting structured
	# wait to avoid saturation
	time.sleep(0.1) # 0.1s = 25 minutes pour 15000 fichiers a scraper // 0.1s = 25 minutes for 15.000 files to scrape
	mycols=''
	colnames=''
	##### read account info
	print '.',
	AccountInfo=soup.find('table',attrs={"id":"tblAccountGeneralInfo"})
	tokeep=[0,1,2,3,4,5]	 # numero des colonnes a garder dans la table des account general information // number of the columns we want to keep from the account general information table
	print 'Account Info',
	rows = AccountInfo.findAll('tr',recursive=False)   # chaque ligne est en fait une table differente (AccountInfo[j]) qu'on va lire séparément // each row is actually a different table (AccountInfo[j]) that we're going to read separately
	for i,row in enumerate(rows):
		print '.',
		cols = row.findAll('td',recursive=False) # le principe : à chaque ligne, cols c'est un array. Ensuite, on va la transformer en chaîne de caractères séparés par des tabulations
		if len(cols)>1 :
			print '.',
			cols=[col.text.replace("&nbsp;", "") for col in cols] # on extrait le texte de la balise et on retire les insécables // grab the text from the tag and get rid of non-breaking spaces
			# print cols
			cols = [cols[k] for k in tokeep] # on ne garde que les colonnes qui nous intéressent // we just keep the columns we're interested in
			if i==1 : # la ligne 1 nous donne les noms des colonnes (ligne 0: titre de la table AccountInfo) // the line 1 gives us the columns' names (line 0: title of the AccountInfo table)
				colnames=colnames+'\t'.join(cols)+'\t'
			if i==2: # la ligne 2 nous donne le contenu a scraper // line 2 gives us the content to be scraped
				mycols=mycols+'\t'.join(cols)+'\t'
	ContactInfo=soup.find('table',attrs={"id":"tblAccountContactInfo"})
	tokeep=[0,1,2,3,4,5,6] # numero des colonnes a garder dans la table des account contact information // the number of the columns we want to keep from the account contact information
	print 'Contact Info',
	rows = ContactInfo.findAll('tr',recursive=False)   # chaque ligne est en fait une table differente (AccountInfo[j]) qu'on va lire séparément // each row is actually a different table (AccountInfo[j]) that we're going to read separately
	for i,row in enumerate(rows):
		print '.',
		cols = row.findAll('td',recursive=False)
		if len(cols)>1 :
			print '.',
			cols=[col.text.replace("&nbsp;", "") for col in cols] # on extrait le texte de la balise et on retire les insécables // grab the text from the tag and get rid of non-breaking spaces
			# print cols
			cols = [cols[k] for k in tokeep] # on ne garde que les colonnes qui nous intéressent // we just keep the columns we're interested in
			if i==1 : # la ligne 1 nous donne les noms des colonnes (ligne 0: titre de la table AccountInfo) // the line 1 gives us the columns' names (line 0: title of the AccountInfo table)
				colnames=colnames+'\t'.join(cols)+'\t'
			if i==2: # la ligne 2 nous donne le contenu a scraper // line 2 gives us the content to be scraped
				mycols=mycols+'\t'.join(cols)+'\t'
	##### read Other info
	Tables=soup.findAll('table',attrs={"id":"tblChildDetails"})
	##### read installation info
	InstallInfo=Tables[0].findAll('table')
	tokeep=[[0,1,2,3,4,5,6,7],	# numero des colonnes a garder dans la "ligne" (en fait table)  1 des infos installations // number of columns to be kept from the "line" (actually, table) 1 from installations info
			[0,1,2,3,4,5,6,7],	# numero des colonnes a garder dans la "ligne" 2 des infos installations // number of columns to be kept from the "line" 2 of installations info
			[0,1,2,3,4,5]]		# numero des colonnes a garder dans la "ligne" 3 des infos installations // number of columns to be kept from the "line" 2 of installations info
	for j in [0,1,2] : # pour chaque ligne des infos installations (0-2)
		rows = InstallInfo[j].findAll('tr',recursive=False) # chaque ligne est en fait une table differente (InstallInfo[j]) qu'on va lire séparément // each row is actually a different table (AccountInfo[j]) that we're going to read separately
		for i,row in enumerate(rows):
			cols = row.findAll('td',recursive=False)
			if len(cols)>1 :
				cols = [col.text.replace("&nbsp;", "") for col in cols] # on extrait le texte de la balise et on retire les insécables // grab the text from the tag and get rid of non-breaking spaces
				# print cols
				cols = [cols[k] for k in tokeep[j]] # on ne garde que les colonnes qui nous intéressent // we just keep the columns we're interested in
			if i==1 : # la ligne 1 nous donne les noms des colonnes (ligne 0: titre de la table InstallInfo[j]) // the line 1 gives us the columns' names (line 0: title of the InstallInfo[j]) table)
				colnames=colnames+'\t'.join(cols) +'\t'
			if i==2: # la ligne 2 nous donne le contenu a scraper // line 2 gives us the content to be scraped
				mycols=mycols+'\t'.join(cols)+'\t'
	##### read Emissions info
	Emission=Tables[1].table
	rows = Emission.findAll('tr',recursive=False)
	for i,row in enumerate(rows):# pour chaque ligne on regarde la colonne 1 pour avoir l'année (ajoutée au nom de colonne), et on garde les chiffres des colonnes 2 et 3 // for each line we keep column 1 in order to have the year (added to the column's name) and we keep the numbers of the columns 2 and and 3 
		if i>1:
			cols = row.findAll('td',recursive=False) # trouve-moi toutes les colonnes dans row (ligne i)
			#cols = [col.text.replace("&nbsp;", "") for col in cols] # on extrait le texte de la balise et on retire les insécables (ancienne version, remplacée depuis par une boucle) // grab the text from the tag and get rid of non-breaking spaces
			newcols=['a']*len(cols) # ici on crée un objet qui contient autant d'éléments vides que de colonnes dans le tableau d'origine (il y a autant de colonnes que de lignes de date). Car dans Python on ne peut pas (en tout cas on n'y arrive pas, il dit typeof = none) rajouter un élément à un vecteur vide. Il faut créer un vecteur ayant déjà la bonne taille. 
			for j,col in enumerate(cols):
				spans = col.findAll('span', recursive=False) # trouve-moi tous les spans dans col (colonne j)
				mytext = "" # on initialise la variable qui constituera le contenu de chaque colonne (toutes les colonnes une à une)
				for z,span in enumerate(spans):
					if z == 0 : # si c'est le premier span
						mytext = span.text.replace("&nbsp;", "") # alors insère son contenu tel quel dans la variable mytext
						# print 'yes', i,j,z, mytext
					else : # si c'est le 2e span ou les suivants, alors on va mettre des slashs et on ajoute le contenu à mytext (si celui-ci n'est pas vide) 
						if span.text.replace ("&nbsp;", "")!='': #pour ne pas avoir deux slashs de suite : seulement lorsque le span n'est pas vide, 
							mytext = mytext + "/" + span.text.replace ("&nbsp;", "") # alors son contenu est ajouté à la variable mytext
							#print 'no ', i,j,z, mytext
				newcols[j]=mytext
			cols=newcols
				#span =""
				#span[j] = [col.span[j].text]
				#cols = cols + "/" + col[j]	
			if len(cols)>1 : # en fait, les astérisques en bas du tableau constituent une ligne à une colonne => pour supprimer le cas des fins de tableau où il y a des astérisques dans une ligne supplémentaire avec col unique // remove the cases of ends of tables where there are asterisks in an additional line with a unique col
				mycols=mycols+cols[2]+'\t'+cols[3]+'\t'
				colnames=colnames+'Allowance_Allocation_'+cols[1]+'\tVerified_Emission_'+cols[1]+'\t' # les émissions vérifiées et les allocations pour chaque année
	# write output to ouput file (f_out)
	mycols=re.sub(u'\u2013','-',mycols)
	mycols=re.sub(u'&#39;',"'",mycols)
	mycols=re.sub(u'\u201c','"',mycols)
	mycols=re.sub(u'\u201d','"',mycols)
	mycols=re.sub(u'\u201e','"',mycols)
	mycols=re.sub(u'&quot;',"'",mycols)
	if l==0:
		f_out.write(colnames+'\n')
	try:
		f_out.write(mycols+'\n')
	except:
		f_err.write(str(l)+'\n')			

f_out.close()
f_err.close()