# ETS scraper 

A tool to scrape the data from the european emission trading scheme (ETS)

This script has been prepared to store in a unique file the data from 14.000 installations registered in the EU transaction log.

The information is available for 31 countries, 30 sectors, for the years 2005-2016. The content lists information like the installation name and country, the account holder's name, the verified emissions for each year and the free allocations for each year, the parent company, the address. 

**// Open data**

The unique file issued from the scraping has been published on French open-government portal : <a href="https://www.data.gouv.fr/fr/datasets/donnees-2005-2016-du-marche-europeen-des-quotas-de-co2-ets-2005-2016-data-from-the-european-emissions-trading-scheme-ets/">data.gouv.fr</a>. You can also download it on <a href="https://github.com/anouchk/ETS_data">Github</a>.

**// Journalistic use**

It gave way to the publication of a **5 stories investigation**, released on May 31st and April 3d, 2017. 
<br>1.<a href="https://www.aefinfo.fr/depeche/559180"> A ride into the depth of the ETS (or 12 years of impossible reforms) </a> 
<br>2.<a href="https://www.aefinfo.fr/depeche/557532"> Please meet the big 40 on European CO2 market</a> 
<br>3.<a href="https://www.aefinfo.fr/depeche/559634"> Introducing the big 30 Frenchies and their "fat cats" </a> 
<br>4.<a href="https://www.aefinfo.fr/depeche/557519"> How the electric companies had (almost) foreseen it all, 20 years ago. </a> 
<br>5.<a href="https://www.aefinfo.fr/depeche/557538"> Challenges ahead : can the ETS horse be put inside the barn ? </a> 
<br>The whole investigation was presented for international Datajournalism awards as **<a href="http://community.globaleditorsnetwork.org/content/big-40-european-co2-market-whos-really-control">"The big 40 on European CO2 market : who's really in control ?"</a>**.


**// Stories published in the Netherlands and Germany**

Marcel Pauly's story released in Der Spiegel (Germany) November 16th
<br>http://www.spiegel.de/wissenschaft/mensch/deutschland-das-sind-die-groessten-klimasuender-a-1178207.html

De Groene Amsterdammer's story from Luuk Sengers released September 6th (Netherlands), were they quote AEF (my news outlet)
<br>http://bit.ly/2yMkWUc

**// 2018 update and caveat**

This scraper parses the "Allocations to stationary installations" part of the EU transactions log. We realized with a few European journalists that some plants were missing, that were included in the "Operator Holding Accounts" part of the EUTL. 

Lucilky, the world is full of helping hands. Nathann Cohen, a skilled computer scientist, took some of his spare time to give a hand scraping the **236 missing plants**. The result is here ("All Operator Holding accounts") : https://www.steinertriples.fr/ncohen/data/EU_CO2_LOG/ 
<br>… 15 505 plants. \o/

# ETS scraper 

Un outil pour scraper les données du marché européen de quotas de CO2

Ce script a été réalisé pour stocker dans un seul fichier les données des 14 000 installations inscrites au registre européen du marché de quotas de CO2.

L'information est disponible pour 31 pays, 30 secteurs, pour les années 2005-2016. Le contenu liste des informations telles que le nom et le pays de l'installation industrielle, le nom du teneur de compte, de la maison-mère, les émissions vérifiées pour chaque année ainsi que les allocations de quotas gratuits pour chaque année, l'adresse postale.

**// Open data**

Le fichier unique issu du scrapping a été publié sur le portail gouvernemental français <a href="https://www.data.gouv.fr/fr/datasets/donnees-2005-2016-du-marche-europeen-des-quotas-de-co2-ets-2005-2016-data-from-the-european-emissions-trading-scheme-ets/">data.gouv.fr</a>. Vous pouvez aussi le télécharger sur <a href="https://github.com/anouchk/ETS_data">Github</a>.

**// Utilisation journalistique**

Cela a donné lieu à la publication d'une **enquête en 5 volets**, les 31 mai et 3 avril 2017. 
<br>1.<a href="https://www.aefinfo.fr/depeche/559180"> 2005-2017 : 12 années d’impossibles réformes du marché européen du carbone EU ETS. </a>
<br>2.<a href="https://www.aefinfo.fr/depeche/557532"> Quels sont les grands émetteurs du marché européen du carbone et combien pèsent-ils ?</a> 
<br>3.<a href="https://www.aefinfo.fr/depeche/559634"> Zoom sur la France. Quelles sont les 30 entreprises-clés ?</a> 
<br>4.<a href="https://www.aefinfo.fr/depeche/557519"> Comment les électriciens européens avaient (presque) tout prévu du marché ETS voici 20 ans. </a> 
<br>5.<a href="https://www.aefinfo.fr/depeche/557538"> Les défis du marché ETS : le ver était-il dans le fruit ?</a> 
<br>L'enquête a été présentée à un prix international de datajournalisme sous l'appellation **<a href="http://community.globaleditorsnetwork.org/content/big-40-european-co2-market-whos-really-control">"The big 40 on European CO2 market : who's really in control ?"</a>**.

**// Enquêtes publiées aux Pays-Bas et en Allemagne**

Un papier de Marcel Pauly a été publié dans Der Spiegel (Allemagne) le 16 novembre 2017
<br><a href="http://www.spiegel.de/wissenschaft/mensch/deutschland-das-sind-die-groessten-klimasuender-a-1178207.html">http://www.spiegel.de/wissenschaft/mensch/deutschland-das-sind-die-groessten-klimasuender-a-1178207.html</a> 

Un papier de plusieurs journalistes dont Luuk Sengers a été publié dans De Groene Amsterdammer's (Pays-Bas) le 6 septembre 2017 
<br><a href="http://bit.ly/2yMkWUc">"The industrial lobby is incredibly strong"</a>

**// Actualisation 2018 et mise en garde**

Ce scraper parcourt la partie "Allocations to stationary installations" du EU transactions log. Or nous nous sommes rendu compte avec quelques journalistes européens que plusieurs installations manquaient à l'appel, qui étaient inclues dans la partie "Operator Holding Accounts" du EUTL. 

Heureusement, le monde est rempli de talents généreux. Nathann Cohen, un chercheur en informatique, a pris un peu de son temps libre pour scraper les **236 installations manquantes**. Le résultat est ici ("All Operator Holding accounts") : <a href="https://www.steinertriples.fr/ncohen/data/EU_CO2_LOG/">https://www.steinertriples.fr/ncohen/data/EU_CO2_LOG/</a> 
<br>… 15 505 installations. \o/
