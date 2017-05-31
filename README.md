# ETS scraper 

A tool to scrape the data from the european emission trading scheme (ETS)

This script has been prepared to store in a unique file the data from 14.000 installations registered in the EU transaction log.

The information is available for 31 countries, 30 sectors, for the years 2005-2015. The content lists information like the installation name and country, the account holder's name, the verified emissions for each year and the free allocations for each year, the parent company, the address. 

**// Caveat** 

The data concernning allocations for phase 3 (2013-2015) is note acurate for certain countries (not France) : the script doesn't take into account installations under article 10c from the directive.

**// Open data**

The unique file issued from the scraping has been published on French open-government portal : <a href="https://www.data.gouv.fr/fr/datasets/donnees-2005-2015-du-marche-europeen-des-quotas-de-co2-ets/">data.gouv.fr</a>. 

**// Journalistic use**

It gave way to the publication of a **5 stories investigation**, released on May 31st and April 3d, 2017. 
<br>1. A ride into the depth of the ETS (or 12 years of impossible reforms) 
<br><a href="http://www.aef.info/depeche/libre/557532">2. Please meet the big 40 on European CO2 market</a> 
<br>3. Introducing the big 30 Frenchies and their "fat cats" 
<br>4. How the electric companies had (almost) foreseen it all, 20 years ago. 
<br>5. Challenges ahead : can the ETS horse be put inside the barn ? 
<br>The whole investigation was presented for international Datajournalism awards as **<a href="http://community.globaleditorsnetwork.org/content/big-40-european-co2-market-whos-really-control">"The big 40 on European CO2 market : who's really in control ?"</a>**.

**// Work in progress**

2016 data is available since April 3rd of 2017. It would be useful to make the script better by allowing it to take into account free allocations for countries under article 10c, on phase 3.

# ETS scraper 

Un outil pour scraper les données du marché européen de quotas de CO2

Ce script a été réalisé pour stocker dans un seul fichier les données des 14 000 installations inscrites au registre européen du marché de quotas de CO2.

L'information est disponible pour 31 pays, 30 secteurs, pour les années 2005-2015. Le contenu liste des informations telles que le nom et le pays de l'installation industrielle, le nom du teneur de compte, de la maison-mère, les émissions vérifiées pour chaque année ainsi que les allocations de quotas gratuits pour chaque année, l'adresse postale.

**// Attention** 

Les données concernant les allocations de quotas pour la 3ème phase (2013-2015) ne sont pas bonnes pour certains pays (pas la France) : l'outil n'avait pas prévu de prendre en compte les cases avec des astérisques, excluant donc les quotas gratuits pour les installations relevant de l'article 10c de la directive.

**// Open data**

Le fichier unique issu du scrapping a été publié sur le portail gouvernemental français <a href="https://www.data.gouv.fr/fr/datasets/donnees-2005-2015-du-marche-europeen-des-quotas-de-co2-ets/">data.gouv.fr</a>. 

**// Utilisation journalistique**

Cela a donné lieu à la publication d'une **enquête en 5 volets**, les 31 mai et 3 avril 2017. 
<br>1. 2005-2017 : 12 années d’impossibles réformes du marché européen du carbone EU ETS.
<br><a href="http://www.aef.info/depeche/libre/557532">2. Quels sont les grands émetteurs du marché européen du carbone et combien pèsent-ils ?</a> 
<br>3. Zoom sur la France. Quelles sont les 30 entreprises-clés ?
<br>4. Comment les électriciens européens avaient (presque) tout prévu du marché ETS voici 20 ans. 
<br>5. Les défis du marché ETS : le ver était-il dans le fruit ?
<br>L'enquête a été présentée à un prix international de datajournalisme sous l'appellation **<a href="http://community.globaleditorsnetwork.org/content/big-40-european-co2-market-whos-really-control">"The big 40 on European CO2 market : who's really in control ?"</a>**.

**// Pistes d'amélioration** 

Les données 2016 étant disponibles le 3 avril 2017, il serait utile d'améliorer l'outil afin de bien prendre en compte les quotas gratuits de la phase 3. 
