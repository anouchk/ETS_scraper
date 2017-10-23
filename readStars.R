
library(data.table)

# A partir de 2013, EUTL différencie 3 catégories d'allocations pour une même installation : les allocations classiques, les allocations octroyées en vertu de l'article 10c de la directive européenne (****), et les allocations octroées au titre de la réverve pour les nouveaux entrants (NER) (*****)
# From 2013, EUTL diferentiates 3 categories of allowances : classic allowances, allowances given under article 10c of the ETS directive (****), and allowances given as New entrant's reserve (NER) (*****)
# La fonction splitStars nous montre les chiffres suivis d'aucune étoile, de 4 étoiles ou de 5 étoiles 
# splitStars function shows the numbers for each of those categories

splitStars=function(x){
				x5s=substr(x,nchar(x)-4,nchar(x))
				x4s=substr(x,nchar(x)-3,nchar(x))
				x5=substr(x,1,nchar(x)-5)
				x4=substr(x,1,nchar(x)-4)
				w5s=which(x5s=='*****');
				w4s=setdiff(which(x4s=='****'),w5s);
				wns=setdiff(1:max(length(x),1),c(w4s,w5s))
				res=c(length(wns),length(w4s),length(w5s))
				if(length(wns)==0){addn=NA}else{addn=x[wns]}
				if(length(x)==0){addn=NA;res[1]=0}
				if(length(w4s)==0){add4=NA}else{add4=x4[w4s]}
				if(length(w5s)==0){add5=NA}else{add5=x5[w5s]}
				res=c(addn,add4,add5,res)
				res
				}


# On applique la fonction à chacune des installations // applying splitStars to all installations				
options(stringsAsFactors=F)				
Emis=read.table('/Users/analutzky/Desktop/data/scrapping_ETS/data/15_08_2017/Emissions_allCompanies_allCountries_15_08_2017_UTF8.txt',quote='',comment='',sep='\t',header=TRUE,stringsAsFactors=F)
x05=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2005),'/'),splitStars),1,as.numeric)
x06=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2006),'/'),splitStars),1,as.numeric)
x07=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2007),'/'),splitStars),1,as.numeric)
x08=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2008),'/'),splitStars),1,as.numeric)
x09=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2009),'/'),splitStars),1,as.numeric)
x10=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2010),'/'),splitStars),1,as.numeric)
x11=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2011),'/'),splitStars),1,as.numeric)
x12=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2012),'/'),splitStars),1,as.numeric)
x13=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2013),'/'),splitStars),1,as.numeric)
x14=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2014),'/'),splitStars),1,as.numeric)
x15=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2015),'/'),splitStars),1,as.numeric)
x16=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2016),'/'),splitStars),1,as.numeric)
x17=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2017),'/'),splitStars),1,as.numeric)
x18=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2018),'/'),splitStars),1,as.numeric)
x19=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2019),'/'),splitStars),1,as.numeric)
x20=apply(sapply(strsplit(as.character(Emis$Allowance_Allocation_2020),'/'),splitStars),1,as.numeric)

# expploratoire : on fait un tableau croisé dynamique sur les colonnes 4, 5 et 6 pour voir ce qui se passe : on a constaté que qu'il n'y a pas de chiffre avec des étoiles s'il n'y a pa s de chiffre au départ, et que des foise y'a 4 étoiles, des fois 5, des fois les deux // test to explore the data
table(x12[,5],x12[,6],x12[,4])
x12[ x12[,5]>0,]
x12[ x12[,6]>0,]

table(x13[,5],x13[,6],x13[,4])
x13[ x13[,5]>0,]
x13[ x13[,6]>0,]

table(x18[,5],x18[,6],x18[,4])
x18[ x18[,5]>0,]
x18[ x18[,6]>0,]

# On fait la somme des 3 chiffres pour avoir les allocations totales d'une installation, qu'on stocke dans une nouvelle colonne 'allocation totales' // suming up the 3 numbers to get total allowances for each installation, year by year, storing it in a new column called "total_allowances"

Emis$Total_Allowance_Allocation_2005=apply(x05[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2006=apply(x06[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2007=apply(x07[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2008=apply(x08[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2009=apply(x09[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2010=apply(x10[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2011=apply(x11[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2012=apply(x12[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2013=apply(x13[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2014=apply(x14[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2015=apply(x15[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2016=apply(x16[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2017=apply(x17[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2018=apply(x18[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2019=apply(x19[,1:3],1,sum,na.rm=T)
Emis$Total_Allowance_Allocation_2020=apply(x20[,1:3],1,sum,na.rm=T)

write.table(Emis,file='/Users/analutzky/Desktop/data/scrapping_ETS/data/15_08_2017/Emissions_allCompanies_allCountries_15_08_2017_UTF8_withTotal.txt',quote=F,sep='\t',col.names=TRUE,row.names=F)
