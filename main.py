#Importações de bibliotecas e pastas
from time import sleep
from informações.actinio import informacoes_actinio
from informações.aluminio import informacoes_aluminio
from informações.americio import informacoes_americio
from informações.antimonio import informacoes_antimonio
from informações.argonio import informacoes_argonio
from informações.arsenio import informacoes_arsenio
from informações.bario import informacoes_bario
from informações.berilio import informacoes_berilio
from informações.bismuto import informacoes_bismuto
from informações.boro import informacoes_boro
from informações.bromo import informacoes_bromo
from informações.cadmio import informacoes_cadmio
from informações.calcio import informacoes_calcio
from informações.carbono import informacoes_carbono
from informações.cerio import informacoes_cerio
from informações.cesio import informacoes_cesio
from informações.cloro import informacoes_cloro
from informações.cobalto import informacoes_cobalto
from informações.cobre import informacoes_cobre
from informações.criptonio import informacoes_criptonio
from informações.cromo import informacoes_cromo
from informações.disprosio import informacoes_disprosio
from informações.enxofre import informacoes_enxofre
from informações.erbio import informacoes_erbio
from informações.estanho import informacoes_estanho
from informações.estroncio import informacoes_estroncio
from informações.europio import informacoes_europio
from informações.ferro import informacoes_ferro
from informações.fluor import informacoes_fluor
from informações.fosforo import informacoes_fosforo
from informações.francio import informacoes_francio
from informações.gadolinio import informacoes_gadolinio
from informações.galio import informacoes_galio
from informações.germanio import informacoes_germanio
from informações.hafnio import informacoes_hafnio
from informações.helio import informacoes_helio
from informações.hidrogenio import informacoes_hidrogenio
from informações.holmio import informacoes_holmio
from informações.indio import informacoes_indio
from informações.iodo import informacoes_iodo
from informações.iridio import informacoes_iridio
from informações.iterbio import informacoes_iterbio
from informações.latanio import informacoes_lantanio
from informações.litio import informacoes_litio
from informações.lutecio import informacoes_lutecio
from informações.magnesio import informacoes_magnesio
from informações.manganes import informacoes_manganes
from informações.molibdenio import informacoes_molibenio
from informações.neonio import informacoes_neonio
from informações.netunio import informacoes_netunio
from informações.niobio import informacoes_niobio
from informações.niquel import informacoes_niquel
from informações.nitrogenio import informacoes_nitrogenio
from informações.osmio import informacoes_osmio
from informações.ouro import informacoes_ouro
from informações.oxigenio import informacoes_oxigenio
from informações.paladio import informacoes_paladio
from informações.platina import informacoes_platina
from informações.plutonio import informacoes_plutonio
from informações.polonio import informacoes_polonio
from informações.potasio import informacoes_potassio
from informações.praseodimio import informacoes_praseodimio
from informações.prata import informacoes_prata
from informações.protactinio import informacoes_protactinio
from informações.radio import informacoes_radio
from informações.renio import informacoes_renio
from informações.rodio import informacoes_rodio
from informações.rubidio import informacoes_rubidio
from informações.rutenio import informacoes_rutenio
from informações.selenio import informacoes_selenio
from informações.silicio import informacoes_silicio
from informações.sodio import informacoes_sodio
from informações.escandio import informacoes_escandio
from informações.tantalo import informacoes_tantalo
from informações.tecnecio import informacoes_tecnecio
from informações.telurio import informacoes_telurio
from informações.terbio import informacoes_terbio
from informações.titanio import informacoes_titanio
from informações.torio import informacoes_torio
from informações.tulio import informacoes_tulio
from informações.tungstenio import informacoes_tungstenio
from informações.uranio import informacoes_uranio
from informações.vanadio import informacoes_vanadio
from informações.xenonio import informacoes_xenonio
from informações.zinco import informacoes_zinco
from informações.itrio import informacoes_itrio
from informações.zirconio import informacoes_zirconio
from informações.neodimio import informacoes_neodimio
from informações.promecio import informacoes_promecio
from informações.samario import informacoes_samario
from informações.mercurio import informacoes_mercurio
from informações.talio import informacoes_talio
from informações.chumbo import informacoes_chumbo
from informações.astato import informacoes_astato
from informações.radonio import informacoes_radonio
#Introdução 

print('''
Pesquisa em tabela periódica feita em python por:
  Ana Julia Barros e Jovêncio Neto.
''')
print()
sleep(3)
print('=' * 120)
print('                                               BEM VINDO!')
print('=' * 120)
sleep(3)
print()

#Variáveis para determinar diferentes valores a ela para depois determinar diferentes condições
print('''Escolha um desses elementos:
Actínio (Ac)
Alumínio (Al)
Amerício (Am)
Antimônio (Sb)
Argônio (Ar)
Arsênio (As)
Ástato (At)
Bário (Ba)
Berílio (Be)
Bismuto (Bi)
Boro (B)
Bromo (Br)
Cádmio (Cd)
Cálcio (Ca)
Carbono (C)
Cério (Ce)
Césio (Cs)
Chumbo (Pb)
Cloro (Cl)
Cobalto (Co)
Cobre (Cu)
Crômio(Cr)
Darmstádio (Ds)
Disprósio (Dy)
Dubnium (Db)
Érbio (Er)
Enxofre(S)
Escândio (Sc)
Estanho (Sn)
Estrôncio (Sr)
Europio (Eu)
Fermio (Fm)
Flúor (F)
Fósforo (P)
Frâncio (Fr)
Gadolínio (Gd)
Gálio (Ga)
Germânio (Ge)
Háfnio (Hf)
Hássio (Hs)
Hélio (He)
Hidrogênio (H) 
Holmio (Ho)
Índio (In)
Iodo (I)
Irídio (Ir)
Itérbio (Yb)
Ítrio (Y)
Kriptônio (Kr)
Lantânio (La)
Laurêncio (Lr)
Lítio (Li)
Livermório (Lv)
Lutécio (Lu)
Magnésio (Mg)
Manganês (Mn)
Meitnério (Mt)
Mercúrio (Hg)
Molibdênio (Mo)
Moscóvio (Mc)
Neônio (Ne)
Nihônio (Nh)
Níquel (Ni)
Nióbio (Nb)
Nitrogênio (N)
Oganésson (Og)
Osmio (Os)
Ouro (Au)
Oxigênio(O)
Paládio (Pd)
Platina (Pt) 
Plutônio (Pu)
Polônio (Po)
Potássio (K)
Praseodímio (Pr)
Prata (Ag)
Promecio (Pm)
Protactínio (Pa)
Rádio (Ra)
Radônio (Rn)
Rênio (Re)
Ródio (Rh)
Rubídio (Rb)
Rutênio (Ru)
Rutherfó(Rf)
Samário (Sm)
Seabórgio (Sg)
Selênio (Se)
Silício (Si) 
Sódio (Na)
Tálio (Tl)
Tântalo (Ta)
Telúrio (Te)
Tenessino (Ts) 
Térbio (Tb)
Titânio (Ti)
Tório (Th)
Totânio(Ti)
Túlio (Tm)
Tungstênio (W)
Urânio (U)
Vanádio (V)
Xenônio (Xe)
Zinco (Zn) 
Zircônio (Zr) 
''')

continuar = "S"
continuar2 = ''

while continuar == "S" or continuar == "SIM" or continuar2 == 'S' or continuar2 == 'SIM':
  
  elemento = str(input('Digite o símbolo ou o nome do elemento procurado:')).strip().lower()
  print() 
  print('''
Pesquise algo sobre o elemento de acordo com o número ou como as devidas opções:
-[Número atômico] = 1
-[Família] = 2
-[Peso] = 3
-[Descrição] = 4
-[Distribuição eletrônica] = 5
-[Origem Do Nome] = 6 
-[Período] = 7
''')
  print()
  pesquisa = str(input('Digite o que você deseja pesquisar aqui: ')).strip().lower()
  print()
  sleep(3)
  print('Aguarde um instante para eu identificar essas informações.')
  print()
  sleep(3)
#Uma enorme sequência de códigos a seguir para várias e várias situações de possíveis valores recebidos pelas variáveis acima, seguido de de if, elif e else...
  
#Informações sobre o hidrogênio
  if elemento =='h' or elemento == 'hidrogênio' or elemento == 'hidrogenio':
    informacoes = informacoes_hidrogenio(pesquisa)
    print(informacoes)

#Informações sobre o Helio
  elif elemento == 'he' or elemento == 'hélio' or elemento == 'helio':
    informacoes = informacoes_helio(pesquisa)
    print(informacoes)

#Informações sobre o Litio
  elif elemento == 'li' or elemento == 'lítio' or elemento == 'litio':
    informacoes = informacoes_litio(pesquisa)
    print(informacoes)

#Informações sobre o Berílio
  elif elemento == 'be' or elemento == 'berílio' or elemento == 'berilio':
    informacoes = informacoes_berilio(pesquisa)
    print(informacoes)
  
#Informações sobre o Boro
  elif elemento == 'b' or elemento == 'boro':
    informacoes = informacoes_boro(pesquisa)
    print(informacoes)

#Informações sobre o Carbono
  elif elemento == 'c' or elemento == 'carbono':
    informacoes = informacoes_carbono(pesquisa)
    print(informacoes)

#Informações sobre o Nitrogênio
  elif elemento == 'n' or elemento == 'nitrogenio' or elemento == 'nitrogênio': 
    informacoes = informacoes_nitrogenio(pesquisa)
    print(informacoes)

#Informações sobre o Oxigênio 
  elif elemento == 'o' or elemento == 'oxigenio' or elemento == 'oxigênio':
    informacoes = informacoes_oxigenio(pesquisa)
    print(informacoes)
  
#Informaçõs sobre o Flúor
  elif elemento == 'f' or elemento == 'fluor':
    informacoes = informacoes_fluor(pesquisa)
    print(informacoes)
  
#Informações do Neônio
  elif elemento == 'ne' or elemento == 'neônio' or elemento == 'neonio':
    informacoes = informacoes_neonio(pesquisa)
    print(informacoes)
  
#Informações do Sódio
  
  elif elemento == 'na' or elemento == 'sodio' or elemento == 'sódio':
    informacoes = informacoes_sodio(pesquisa)
    print(informacoes)
  
#Informações do Magnésio
  elif elemento == 'mg' or elemento == 'magnésio' or elemento == 'magnesio':
    informacoes = informacoes_magnesio(pesquisa)
    print(informacoes)
  
#Informações do alumínio 
  elif elemento == 'al' or elemento == 'alumínio' or elemento == 'aluminio':
    informacoes = informacoes_aluminio(pesquisa)
    print(informacoes)
  
#Informações do Silício
  elif elemento == 'si' or elemento == 'silício' or elemento == 'silicio':
    informacoes = informacoes_silicio(pesquisa)
    print(pesquisa)
  
#Informações do Fósforo 
  
  elif elemento == 'p' or elemento == 'fósforo' or elemento == 'fosforo':
    informacoes = informacoes_fosforo(pesquisa)
    print(informacoes)
    
#Informações do Enxofre
  elif elemento == 's' or elemento == 'enxofre':
   informacoes = informacoes_enxofre(pesquisa)
   print(informacoes)
  
#Informações do Cloro
  elif elemento == 'cl' or elemento == 'cloro':
    informacoes = informacoes_cloro(pesquisa)
    print(informacoes)
    
#Informações do Argônio
  elif elemento == 'ar' or elemento == 'argonio' or elemento == 'argônio':
    informacoes = informacoes_argonio(pesquisa)
    print(informacoes)
  
#Informações do Potássio
  
  elif elemento == 'k' or elemento == 'potássio' or elemento == 'potassio': 
    informacoes = informacoes_potassio(pesquisa)
    print(informacoes)
  
#Informação do Cálcio
  
  elif elemento == 'ca' or elemento == 'cálcio' or elemento == 'calcio':
    informacoes = informacoes_calcio(pesquisa)
    print(informacoes)
    
#Informações do Escândio
  elif elemento == 'sc' or elemento == 'escandio' or elemento == 'escândio':
    informacoes = informacoes_escandio(pesquisa)
    print(informacoes) 
  
#Informações do Titânio
  elif elemento == 'ti' or elemento == 'titanio' or elemento == 'titânio':
    informacoes = informacoes_titanio(pesquisa)
    print(informacoes)
  
#Informações do Vanádio
  elif elemento == 'v' or elemento == 'vanádio' or elemento == 'vanadio':
    informacoes = informacoes_vanadio(pesquisa)
    print(informacoes)
  
#Informações do Crômio
  
  elif elemento == 'Cr' or elemento == 'crômio' or elemento == 'cromio' or elemento == 'cromo' or elemento == 'cromita':
    informacoes = informacoes_cromo(pesquisa)
    print(informacoes)
  
#Informações do Manganês 
  elif elemento == 'mn' or elemento == 'manganês' or elemento == 'manganes':
    informacoes = informacoes_manganes(pesquisa)
    print(informacoes)
    
#Informação do Ferro
  elif elemento == 'fe' or elemento == 'ferro':
    informacoes = informacoes_ferro(pesquisa)
    print(informacoes)
    
#Informação do Cobalto
  elif elemento == 'co' or elemento == 'cobalto':
    informacoes = informacoes_cobalto(pesquisa)
    print(informacoes)
    
#Informação do Níquel
  elif elemento == 'ni' or elemento == 'níquel' or elemento == 'niquel':
    informacoes = informacoes_niquel(pesquisa)
    print(informacoes)
  
#Informação do Cobre
  elif elemento == 'cu' or elemento == 'cobre':
    informacoes = informacoes_cobre(pesquisa)
    print(informacoes)
 
#Informação do Zinco
  
  elif elemento == 'zn' or elemento == 'zinco':
    informacoes = informacoes_zinco(pesquisa)
    print(informacoes)
  
#Informação do Gálio
  
  elif elemento == 'ga' or elemento == 'gálio' or elemento == 'galio':
    informacoes = informacoes_galio(pesquisa)
    print(informacoes)
  
#Informação do Germânio
  
  elif elemento == 'ge' or elemento == 'germanio' or elemento == 'germânio':
    informacoes = informacoes_germanio(pesquisa)
    print(informacoes)
  
#Informação do Arsênio
  
  elif elemento == 'as' or elemento == 'arsênio' or elemento == 'arsenio':
    informacoes = informacoes_arsenio(pesquisa)
    print(informacoes)
  
#Informação do Selênio
  
  elif elemento == 'se' or elemento == 'selênio' or elemento == 'selenio':
    informacoes = informacoes_selenio(pesquisa)
    print(informacoes)
  
#Informação do Bromo
  
  elif elemento == 'br' or elemento == 'bromo':
    informacoes = informacoes_bromo(pesquisa)
    print(informacoes)
  
#Informação do Criptônio
  
  elif elemento == 'kr' or elemento == 'criptônio' or elemento == 'criptonio' or elemento == 'kriptônio' or elemento == 'kriptonio':
    informacoes = informacoes_criptonio(pesquisa)
    print(informacoes)
    
#Informações do Rúbidio
  
  elif elemento == 'rb' or elemento == 'rúbidio' or elemento == 'rubidio':
    informacoes = informacoes_rubidio(pesquisa)
    print(informacoes)
  
#Informação do Estrôncio 
  
  elif elemento == 'sr' or elemento == 'estrôncio' or elemento == 'estroncio':
    informacoes = informacoes_estroncio(pesquisa)
    print(informacoes)
  
#Informação do ítrio
  
  elif elemento == 'y' or elemento == 'ítrio' or elemento == 'itrio':
    informacoes = informacoes_itrio(pesquisa)
    print(informacoes)
  
#Informação do Zircônio
  
  elif elemento == 'zr' or elemento == 'zircônio' or elemento == 'zirconio':
    informacoes = informacoes_zirconio(pesquisa)
    print(informacoes)
  
#Informação do Nióbio
  
  elif elemento == 'nb' or elemento == 'nióbio' or elemento == 'niobio':
    informacoes = informacoes_niobio(pesquisa)
    print(informacoes)
   
#Informação do Molibdênio
  
  elif elemento == 'mo' or elemento == 'molibdênio' or elemento == 'molibdenio':
    informacoes = informacoes_molibenio(pesquisa)
    print(informacoes)
  
#Informação do Tecnécio
  
  elif elemento == 'tc' or elemento == 'tecnésio' or elemento == 'tecnesio':
    informacoes = informacoes_tecnecio(pesquisa)
    print(informacoes)
  
#Informação do Rutênio
  
  elif elemento == 'ru' or elemento == 'rutênio' or elemento == 'rutenio':
    informacoes = informacoes_rutenio(pesquisa)
    print(informacoes)
    
#Informação do Ródio
  
  elif elemento == 'rh' or elemento == 'ródio' or elemento == 'rodio':
    informacoes = informacoes_rodio(pesquisa)
    print(informacoes)
  
#Informação do Paládio
  
  elif elemento == 'pd' or elemento == 'paládio' or elemento == 'paladio':
    informacoes = informacoes_paladio(pesquisa)
    print(informacoes)
  
#Informação da Prata
  
  elif elemento == 'ag' or elemento == 'prata':
    informacoes = informacoes_prata(pesquisa)
    print(informacoes)
  
#Informação do Cádmio
  
  elif elemento == 'cd' or elemento == 'cádmio' or elemento == 'cadmio':
    informacoes = informacoes_cadmio(pesquisa)
    print(informacoes)
  
#Informação do Índio
  
  elif elemento == 'in' or elemento == 'índio' or elemento == 'indio':
    informacoes = informacoes_indio(pesquisa)
    print(informacoes)
  
#Informação do Estanho
  
  elif elemento == 'es' or elemento == 'estanho':
    informacoes = informacoes_estanho(pesquisa)
    print(informacoes)
  
#Informação do Antimônio
  
  elif elemento == 'sb' or elemento == 'antimônio' or elemento == 'antimonio':
    informacoes = informacoes_antimonio(pesquisa)
    print(informacoes)
  
#Informação do Telúrio
  
  elif elemento == 'te' or elemento == 'telúrio' or elemento == 'telurio':
    informacoes = informacoes_telurio(pesquisa)
    print(informacoes)
  
#Informação do Iodo
  
  elif elemento == 'i' or elemento == 'iodo':
    informacoes = informacoes_iodo(pesquisa)
    print(informacoes)
    
#Informação do Xenônio
  
  elif elemento == 'xe' or elemento == 'xenônio' or elemento == 'xenonio':
    informacoes = informacoes_xenonio(pesquisa)
    print(informacoes)
  
#Informações do Césio 
  
  elif elemento == 'cs' or elemento == 'césio' or elemento == 'cesio':
    informacoes = informacoes_cesio(pesquisa)
    print(informacoes)
  
#Informação do Bário 
  
  elif elemento == 'ba' or elemento == 'bário' or elemento == 'bario':
    informacoes = informacoes_bario(pesquisa)
    print(informacoes)
  
#Informação do Lantânio
  
  elif elemento == 'la' or elemento == 'lantânio' or elemento == 'lantanio':
    informacoes = informacoes_lantanio(pesquisa)
    print(informacoes)
  
#Informação do Cério
  
  elif elemento == 'ce' or elemento == 'cério' or elemento == 'cerio':
    informacoes = informacoes_cerio(pesquisa)
    print(informacoes)
  
#Informação do Praseodímio
  
  elif elemento == 'pr' or elemento == 'praseodímio' or elemento == 'praseodimio':
    informacoes = informacoes_praseodimio(pesquisa)
    print(informacoes)
  
#Informação do Neodímio
  
  elif elemento == 'nd' or elemento == 'neodímio' or elemento == 'neodiomio':
    informacoes = informacoes_neodimio(pesquisa)
    print(informacoes)
  
#Informação do Promécio
  
  elif elemento == 'pm' or elemento == 'promécio' or elemento == 'promecio':
    informacoes = informacoes_promecio(pesquisa)
    print(informacoes)
  
#Informação do Samário
  
  elif elemento == 'sm' or elemento == 'samário' or elemento == 'samario':
    informacoes = informacoes_samario(pesquisa)
    print(informacoes)

#Informação do Európio

  elif elemento == 'eu' or elemento == 'európio' or elemento == 'europio':
    informacoes = informacoes_europio(pesquisa)
    print(informacoes)

#Informação do Gadolínio

  elif elemento == 'gd' or elemento == 'gadolínio' or elemento == 'gadolinio':
    informacoes = informacoes_gadolinio(pesquisa)
    print(informacoes)
      
#Informação do Térbio
  elif elemento == 'tb' or elemento == 'terbio' or elemento == 'térbio':
    informacoes = informacoes_terbio(pesquisa)
    print(informacoes)

#Informação do Disprosio
  elif elemento == 'dy' or elemento == 'disprosio' or elemento == 'disprósio':
    informacoes = informacoes_disprosio(pesquisa)
    print(informacoes)
#Informação do hólmio
  elif elemento == 'ho' or elemento == 'holmio' or elemento == 'hólmio':
    informacoes = informacoes_holmio(pesquisa)
    print(informacoes)

#Informação do Érbio
  elif elemento == 'er' or elemento == 'érbio' or elemento == 'erbio':
    informacoes = informacoes_erbio(pesquisa)
    print(informacoes)

#Informações do Túlio
  elif elemento == 'tm' or elemento == 'túlio' or elemento == 'tulio':
    informacoes = informacoes_tulio(pesquisa)
    print(informacoes)

#Informação do Itérbio
  elif elemento == 'yb' or elemento == 'iterbio' or elemento == 'itérbio':
    informacoes = informacoes_iterbio(pesquisa)
    print(informacoes)

#Informação do Lutécio
  elif elemento == 'lu' or elemento == 'lutécio' or elemento == 'lutecio':
    informacoes = informacoes_lutecio(pesquisa)
    print(informacoes)
    
#Informação do Háfnio
  elif elemento == 'hf' or elemento == 'háfnio' or elemento == 'hafnio':
    informacoes = informacoes_hafnio(pesquisa)
    print(informacoes)
    
#Informação do Tântalo
  elif elemento == 'ta'  or elemento == 'tantalo' or elemento == 'tântalo':
    informacoes = informacoes_tantalo(pesquisa)
    print(informacoes)
    
#Informação do Tungstênio
  elif elemento == 'w'  or elemento == 'tungstênio' or elemento == 'tungstenio':
    informacoes = informacoes_tungstenio(pesquisa)
    print(informacoes)
#Informação do Rênio
  elif elemento == 're'  or elemento == 'rênio' or elemento == 'renio':
    informacoes = informacoes_renio(pesquisa)
    print(informacoes)

#Informação do Ósmio
  elif elemento == 'os' or elemento == 'osmio' or elemento == 'ósmio':
    informacoes = informacoes_osmio(pesquisa)
    print(informacoes)
    
#Informação do Irídio
  elif elemento == 'ir' or elemento == 'irídio' or elemento == 'iridio':
    informacoes = informacoes_iridio(pesquisa)
    print(informacoes)

#Informacação da Platina 
  elif elemento == 'pl' or elemento == 'platina':
    informacoes = informacoes_platina(pesquisa)
    print(informacoes)

#Informacação do Ouro
  elif elemento == 'au' or elemento == 'ouro':
    informacoes = informacoes_ouro(pesquisa)
    print(informacoes)

#Informacação do Mercúrio
  elif elemento == 'hg' or elemento == 'mercúrio' or elemento == 'mercurio':
    informacoes = informacoes_mercurio(pesquisa)
    print(informacoes)

#Informacação do Tálio
  elif elemento == 'ti' or elemento == 'tálio' or elemento == 'talio':
    informacoes = informacoes_talio(pesquisa)
    print(informacoes)

#Informacação do Chumbo
  elif elemento == 'pb' or elemento == 'chumbo':
    informacoes = informacoes_chumbo(pesquisa)
    print(informacoes)

#Informacação do Bismuto
  elif elemento == 'bi' or elemento == 'bismuto':
    informacoes = informacoes_bismuto(pesquisa)
    print(informacoes)

#Informações do Polônio
  elif elemento == 'po' or elemento == 'polonio' or elemento == 'polônio':
    informacoes = informacoes_polonio(pesquisa)
    print(informacoes)

#Informacação do Ástato
  elif elemento == 'as' or elemento == 'ástato' or elemento == 'astato':
    informacoes = informacoes_astato(pesquisa)
    print(informacoes)

#Informacação do Radônio
  elif elemento == 'rn' or elemento == 'radonio' or elemento == 'radônio':
    informacoes = informacoes_radonio(pesquisa)
    print(informacoes)
#Informações do Frâncio
  elif elemento == 'fr' or elemento == 'frâncio' or pesquisa == 'francio':
    informacoes = informacoes_francio(pesquisa)
    print(informacoes)
    
#Informação do Rádio
  
  elif elemento == 'ra' or elemento == 'rádio' or elemento == 'radio':
    informacoes = informacoes_radio(pesquisa)
    print(informacoes)
   
#Informação do Actínio 
  elif elemento == 'ac' or elemento == 'actínio' or elemento == 'actinio':
    informacoes = informacoes_actinio(pesquisa)
    print(informacoes)

#Informacação do Tório
  elif elemento == 'th' or elemento == 'tório' or elemento == 'torio':
    informacoes = informacoes_torio(pesquisa)
    print(informacoes)

#Informação do Protactínio
  elif elemento == 'pa' or elemento == 'protactínio' or elemento == 'protactinio':
    informacoes = informacoes_protactinio(pesquisa)
    print(informacoes)

#Informação do Urânio
  elif elemento == 'u' or elemento == 'uranio' or elemento == 'urânio':
    informacoes = informacoes_uranio(pesquisa)
    print(informacoes)

#Informações do Netúnio
  elif elemento == 'np' or elemento == 'netúnio' or elemento == 'netunio':
    informacoes = informacoes_netunio(pesquisa)
    print(informacoes)

#Informações do Plutõnio
  elif elemento == 'pu' or elemento == 'plutonio' or elemento == 'plutônio':
    informacoes = informacoes_plutonio(pesquisa)
    print(informacoes)

#Informações do Amerício
  elif elemento == 'am' or elemento ==  'amerício' or elemento == 'americio':
    informacoes = informacoes_americio(pesquisa)
    print(informacoes)



  else:
    print(f'O elemento {elemento} não foi encontrado!!')
    print()
    print('''
Tente novamente, pois ou o elemento não foi cadastrado ou não existe!!
''')
   
  print()
  continuar = str(input('Quer continuar? [S/N]')).upper()
  print()
  
  if continuar == 'N' or continuar == 'NÃO' or continuar == 'NAO':
    print('O programa foi encerrado.')
    break
  elif continuar == 'S' or continuar == 'SIM':
    print('Pois bem, vamos continuar.')
    print()
  elif continuar != 'N' or continuar != 'NÃO' or continuar != 'NAO' or continuar != 'S' or continuar != 'SIM':
    while True:
      print('Desculpe mas não reconheço esse conjunto de caracteres.')
      print()
      print('Tente novamente!')
      print()
      continuar2 = str(input('Quer continuar? [S/N]')).upper()
      print()
      if continuar2 == 'N' or continuar2 == 'NÃO' or continuar2 == 'NAO':
        print('O programa foi encerrado.')
        break 
      elif continuar2 == 'S' or continuar2 == 'SIM':
        print('Pois bem, vamos continuar.')
        print()
        break