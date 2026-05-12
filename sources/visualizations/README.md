# Temats: Datu vizualizācija - vēsture, mērķis un prakse

Datu vizualizācija nav noformējums. Tā ir metode, kā spriest par datiem, atklāt likumsakarības un komunicēt pierādījumus. Svarīgākais ieradums ir vispirms definēt mērķi: kas auditorijai pēc vizualizācijas apskates ir jāsaprot, jāsalīdzina, jāapšauba vai jāizlemj?

## Mācību mērķi

Temata beigās studentiem jāspēj:

- izskaidrot, kāpēc vizualizācijas ir bijušas svarīgas zinātnē, sabiedriskajā politikā, žurnālistikā un statistikā;
- atpazīt vairākus vēsturiskus datu vizualizācijas atskaites punktus;
- izvēlēties biežāk lietotos diagrammu (chart) tipus pēc uzdevuma, nevis pēc tā, kas izskatās iespaidīgi;
- pirms diagrammas veidošanas uzrakstīt skaidru vizualizācijas mērķi;
- uzlabot diagrammas, izmantojot skaidrus apzīmējumus, piemērotus mērogus, jēgpilnu krāsu lietojumu un samazinot nevajadzīgus traucēkļus;
- izvēlēties piemērotas Python vizualizācijas bibliotēkas izpētošajai analīzei, publicējamām diagrammām, interaktīvām diagrammām, kartēm un teksta analīzes vizualizācijām.

## Vēsturiskie pamati

Mūsdienu vizualizācijas prakse ir veidojusies no kartogrāfijas, statistikas, sabiedrības veselības, ekonomikas, socioloģijas un grafiskā dizaina. Tālāk minētie piemēri ir vērti izpētei, jo katrs no tiem risināja īstu komunikācijas problēmu.

| Laikposms | Persona vai darbs | Kāpēc tas ir svarīgi |
| --- | --- | --- |
| 1780. gadi | Viljams Pleifērs (William Playfair), *The Commercial and Political Atlas* | Pleifērs palīdzēja nostiprināt statistiskās diagrammas, piemēram, līniju diagrammas, stabiņu diagrammas un vēlāk sektoru diagrammas (pie chart), kā ekonomiska argumenta rīkus. Viņš parādīja, ka kvantitatīvas pārmaiņas var lasīt vizuāli, ne tikai tabulās. |
| 1854 | Džona Snova (John Snow) Brodstrītas holeras kartes | Snova kartes sasaistīja nāves gadījumus ar ūdens sūkņu atrašanās vietām holeras uzliesmojuma laikā Londonā. Tas joprojām ir klasisks telpisku pierādījumu piemērs sabiedrības veselības analīzē. |
| 1858 | Florensas Naitingeilas (Florence Nightingale) polārā laukuma mirstības diagrammas | Naitingeila izmantoja statistiskās diagrammas, lai argumentētu par sanitārijas reformu militārajās slimnīcās. Viņas darbs rāda, ka vizualizācija var atbalstīt politikas maiņu, ja tā padara problēmu redzamu. |
| 1869 | Šarla Žozefa Mināra (Charles Joseph Minard) Napoleona 1812. gada gājiena uz Maskavu un atkāpšanās grafiskais attēlojums | Minārs vienā attēlā apvienoja ģeogrāfiju, virzienu, armijas lielumu, laiku un temperatūru. Šī karte ir slavena tāpēc, ka sarežģītu vēsturisku katastrofu padara uztveramu vienā skatienā, nesamazinot to līdz vienam skaitlim. |
| 1900 | V. E. B. Dibuā (W. E. B. Du Bois) un Atlantas Universitātes datu portreti | Dibuā un viņa kolēģi Parīzes izstādei izveidoja ar roku zīmētas diagrammas par melnādaino amerikāņu dzīvi, izglītību, darbu un sociālajiem apstākļiem. Šīs diagrammas rāda vizualizāciju kā pierādījumu, dizainu un pilsonisku argumentu. |
| 1967 | Žaks Bertēns (Jacques Bertin), *Semiology of Graphics* | Bertēns formalizēja ideju, ka vizuālās zīmes un kanāli, piemēram, novietojums, izmērs, forma, vērtība, faktūra, orientācija un krāsa, pārnes atšķirīgus informācijas tipus. |
| No 1983. gada | Edvards Tafti (Edward Tufte), *The Visual Display of Quantitative Information* un vēlākās grāmatas | Tafti popularizēja stingru dizaina vārdnīcu par grafisko godīgumu, augstu informācijas blīvumu, datu tinti (data-ink) un izvairīšanos no diagrammu liekā noformējuma (chartjunk). Viņa darbs arī palīdzēja Mināra Napoleona grafiku ieviest mūsdienu vizualizācijas mācīšanā. |
| No 1984. gada | Viljama Klīvlenda (William Cleveland) un Roberta Makgila (Robert McGill) grafiskās uztveres pētījumi | Viņu eksperimenti deva vizualizācijas dizainam empīrisku pamatu: cilvēki dažus vizuālos kodējumus atšifrē precīzāk nekā citus, īpaši novietojumu uz kopīgas skalas. |

Galvenā vēstures mācība ir tāda, ka spēcīgas vizualizācijas sākas ar problēmu: izskaidrot tirdzniecību, atrast slimības izplatības modeļus, argumentēt par reformu, dokumentēt sociālos apstākļus, salīdzināt pierādījumus vai atbalstīt lēmumu.

## Definējiet mērķi pirms diagrammas izvēles

Pirms diagrammas veidošanas uzrakstiet vienu teikumu:

> Es vēlos, lai šī auditorija ierauga, ka ____, lai tā varētu ____.

Pēc tam atbildiet uz šiem jautājumiem:

- Kas ir auditorija: kursabiedri, analītiķi, vadītāji, sabiedrība vai nozares eksperti?
- Kāds ir uzdevums: salīdzināt, ranžēt, atrast tendenci, izpētīt sadalījumu, parādīt sakarību, atrast vietu kartē, parādīt daļu un veseluma attiecību vai parādīt nenoteiktību?
- Kāda ir mērvienība un saucējs: skaits, procents, rādītājs uz iedzīvotāju, indekss, valūta, laika intervāls?
- Kādu lēmumu vai interpretāciju diagrammai jāatbalsta?
- Ko varētu pārprast, ja diagrammu lasa ātri?
- Kāds datu avots, filtrēšana, agregēšana vai trūkstošās vērtības ir jānorāda?

Ja mērķis ir neskaidrs, arī diagramma parasti būs neskaidra.

## Izvēlieties diagrammu tipus pēc uzdevuma

| Uzdevums | Labi noklusējuma risinājumi | Piezīmes un brīdinājumi |
| --- | --- | --- |
| Salīdzināt kategorijas | Stabiņu diagramma, punktu diagramma, konfektes diagramma (lollipop chart) | Kārtojiet pēc vērtības, ja kategorijām nav dabiskas secības. Stabiņu diagrammām lietojiet nulles bāzlīniju, jo stabiņa garums kodē lielumu. |
| Ranžēt vienumus | Sakārtota stabiņu diagramma, sakārtota punktu diagramma, slīpuma diagramma (slope chart) ranga izmaiņām | Izceliet dažus svarīgos vienumus, nevis krāsojiet katru vienumu atšķirīgi. |
| Parādīt pārmaiņas laikā | Līniju diagramma, laukuma diagramma kopējiem lielumiem, kolonnu diagramma diskrētiem periodiem | Līnijas izmantojiet nepārtrauktam laikam. Nesavienojiet nesakārtotas kategorijas ar līniju. Laika logu izvēlieties godīgi. |
| Parādīt sadalījumu | Histogramma, blīvuma diagramma, kastu diagramma (box plot), vijoles diagramma (violin plot), punktu joslas diagramma (dot strip plot) | Histogrammas lietojiet formas izpētei, kastu diagrammas - kompaktam grupu salīdzinājumam, bet punktu diagrammas - ja svarīgi ir atsevišķi novērojumi. |
| Parādīt sakarību vai korelāciju | Izkliedes diagramma (scatter plot), burbuļu diagramma, sešstūru grupēšanas diagramma (hexbin plot), siltumkarte (heatmap) | Korelācija nav cēloņsakarība. Marķējiet izlecošās vērtības un blīviem datiem apsveriet caurspīdību vai agregēšanu. |
| Parādīt daļu un veseluma attiecību | Sakrauta stabiņu diagramma, 100 procentu sakrauta stabiņu diagramma, koka karte (treemap) hierarhijai, mazo vairākkārtņu stabiņu diagrammas (small multiples) | Sektoru diagrammas var derēt dažām acīmredzamām daļām, bet tās ir vājas precīziem salīdzinājumiem vai daudzām kategorijām. |
| Parādīt ģeogrāfiskus modeļus | Horoplēta karte (choropleth map) rādītājiem, proporcionālo simbolu karte skaitiem, punktu blīvuma karte sadalījumam | Nekartējiet neapstrādātus skaitus pēc teritorijas, ja iedzīvotāju skaits modeli izskaidro labāk nekā ģeogrāfija. |
| Parādīt plūsmu vai procesu | Sankeja diagramma (Sankey diagram), aluviālā diagramma (alluvial chart), plūsmas karte, piltuves diagramma (funnel chart) | Lietojiet tikai tad, ja galvenais ir pārvietošanās vai pāreja. Pārāk daudz plūsmu ātri kļūst nelasāmas. |
| Parādīt nenoteiktību | Kļūdu joslas, ticamības intervāli, vēdekļa diagramma (fan chart), prognozes intervāla lente | Neslēpiet nenoteiktību, ja tā maina interpretāciju. Izskaidrojiet, ko intervāls nozīmē. |
| Parādīt daudzus mainīgos | Mazās vairākkārtnes (small multiples), fasetēšana (faceting), siltumkarte, rūpīgi kodēta izkliedes diagramma | Dodiet priekšroku atkārtotām vienkāršām diagrammām, nevis vienai pārslogotai diagrammai. |

## Marķējuma un dizaina labā prakse

- Lietojiet virsrakstu, kas pasaka galveno secinājumu, nevis tikai diagrammas tipu.
- Asīm norādiet mērvienības. Procenti no kā? Eiro gadā? Novērojumi katrā grupā?
- Ja iespējams, svarīgās datu sērijas marķējiet tieši, nevis lieciet lasītājam lēkāt starp diagrammu un leģendu.
- Lietojiet viegli lasāmus skaitļu formātus: 1,2 miljoni bieži ir skaidrāk nekā 1 200 000.
- Režģlīnijām jābūt vieglām un noderīgām. Noņemiet rāmjus, ēnas, trīsdimensiju efektus un dekoratīvus fonus, ja tie nenes informāciju.
- Krāsu lietojiet ar nolūku: secīgas paletes sakārtotam lielumam, diverģējošas paletes vērtībām ap jēgpilnu viduspunktu un kvalitatīvas paletes kategorijām.
- Nepaļaujieties tikai uz krāsu, lai nodotu nozīmi. Pievienojiet marķējumu, formu, līnijas stilu vai teksta norādes.
- Mērogam jābūt godīgam. Stabiņu diagrammām rādiet nulli, paskaidrojiet transformētas asis un izvairieties no divām asīm, ja vien tam nav spēcīga iemesla un skaidra marķējuma.
- Norādiet avotu, ja datu izcelsme, filtrēšana vai transformācija ietekmē interpretāciju.
- Padariet svarīgo salīdzinājumu vieglu. Ja lasītājam rezultāts jārēķina galvā, pārveidojiet diagrammu.

Labs dizains mazina berzi. Tas neatņem nepieciešamo kontekstu.

## Izvairieties no nevajadzīgiem traucēkļiem

Tafti kritika par diagrammu lieko noformējumu (chartjunk) ir noderīgs praktisks rediģēšanas princips: katram redzamam elementam jāiekodē dati, jāizskaidro dati vai jāpalīdz lasītājam orientēties diagrammā. Ja elements nedara nevienu no šīm lietām, noņemiet to.

Bieži traucēkļi:

- trīsdimensiju stabiņi vai sektori, kas kropļo spriedumu;
- pārāk smagas režģlīnijas un biezi rāmji;
- pārāk daudz krāsu bez semantiskas nozīmes;
- dekoratīvas ikonas, kas atkārtotas kā datu zīmes, lai gan vienkārši stabiņi vai punkti būtu skaidrāki;
- leģendas, kuras var aizstāt ar tiešiem marķējumiem;
- fona attēli, gradienti vai faktūras, kas konkurē ar datiem;
- pārmērīgs decimālzīmju skaits vai marķējums katram punktam, ja svarīgi ir tikai daži marķējumi.

Mērķis nav minimālisms pats par sevi. Mērķis ir padarīt pierādījumus vieglāk lasāmus.

## Python vizualizācijas bibliotēkas

Python ekosistēmā ir daudz vizualizācijas bibliotēku. Šajā kursā galvenajām bibliotēkām jābūt Matplotlib, Seaborn un Plotly, jo tās nosedz lielāko daļu ikdienas vajadzību: statiskas diagrammas, statistisku izpēti un interaktīvas diagrammas.

| Bibliotēka | Instalēšana | Labākais lietojums | Oficiālā dokumentācija |
| --- | --- | --- | --- |
| Matplotlib | `pip install matplotlib` | Pamata grafiskās attēlošanas bibliotēka. Lietojiet precīzām statiskām diagrammām, apakšdiagrammu izkārtojumiem, pielāgotām anotācijām un publicēšanai piemērotai kontrolei. | <https://matplotlib.org/stable/> |
| Seaborn | `pip install seaborn` | Augsta līmeņa statistiskā vizualizācija, kas balstīta uz Matplotlib. Lietojiet sadalījumiem, kategoriju salīdzinājumiem, regresijas skatiem, siltumkartēm un ātrām izpētošām diagrammām. | <https://seaborn.pydata.org/> |
| Plotly | `pip install plotly` | Interaktīvas tīmekļa diagrammas. Lietojiet, ja rezultātu uzlabo rīka padomi (tooltips), mērogošana, filtrēšana, animācija vai HTML eksports. | <https://plotly.com/python/> |

### Matplotlib

Matplotlib ir pamatslānis lielai Python vizualizācijas ekosistēmas daļai. Salīdzinājumā ar dažām jaunākām bibliotēkām tā ir daudzvārdīgāka, bet dod spēcīgu kontroli pār attēla izmēru, asīm, iedaļām, anotācijām, leģendām, krāsu kartēm un eksporta formātiem. Tā ir labs noklusējuma risinājums, ja gala rezultāts ir statisks attēls ziņojumam, prezentācijai, PDF dokumentam vai rakstam.

Lietojiet Matplotlib, ja:

- nepieciešama precīza kontrole pār katru attēla daļu;
- veidojat vairāku paneļu attēlus ar vairākām asīm;
- nepieciešama stabila atkarība, ko saprot daudzas citas bibliotēkas;
- vēlaties saglabāt diagrammas PNG, SVG vai PDF formātā ar paredzamu noformējumu.

### Seaborn

Seaborn ir veidota statistiskām diagrammām un īpaši labi strādā ar sakārtotiem pandas datu rāmjiem (DataFrame). Tā samazina atkārtotu Matplotlib kodu un nodrošina labus noklusējuma iestatījumus biežiem analīzes uzdevumiem.

Lietojiet Seaborn, ja:

- salīdzināt sadalījumus starp grupām;
- vajadzīgas kastu diagrammas, vijoles diagrammas, histogrammas, blīvuma diagrammas, pāru diagrammas (pair plots) vai kategoriju diagrammas;
- vēlaties ātru izpētošo analīzi ar konsekventu stilu;
- vēlaties, lai ticamības intervāli vai agregēšana būtu iebūvēta augstāka līmeņa diagrammu funkcijās.

### Plotly

Plotly veido interaktīvus attēlus, kas labi parādās Jupyter piezīmju grāmatās un kurus var eksportēt uz HTML. Plotly Express ir vieglākais sākumpunkts, jo tas tieši kartē DataFrame kolonnas uz vizuālajiem kodējumiem, piemēram, `x`, `y`, `color`, `size`, `facet_col` un `animation_frame`.

Lietojiet Plotly, ja:

- lasītājam noder rīka padomi (tooltips) vai mērogošana;
- diagrammā ir daudz punktu un statiski marķējumi kļūtu pārslogoti;
- vēlaties publicēt pašpietiekamu HTML diagrammu;
- veidojat interaktīvus informācijas paneļus (dashboards) vai prototipus.

## Integrācija ar pandas

Pandas parasti ir datu sagatavošanas slānis. Lielākā daļa vizualizācijas darba jāsāk ar tīru datu rāmi (DataFrame): kolonnām jābūt jēgpilniem nosaukumiem, datu tipiem jābūt pareiziem, trūkstošajām vērtībām jābūt saprastām, un kategorijām jābūt sakārtotām, ja secībai ir nozīme.

Biežākie integrācijas modeļi:

- Pandas ir iebūvēta attēlošana ar `DataFrame.plot()` un `Series.plot()`. Šīs metodes pēc noklusējuma izmanto Matplotlib un ir noderīgas ātrām izpētošām diagrammām.
- Seaborn pieņem pandas datu rāmjus ar parametru `data=` un kolonnu nosaukumus ar argumentiem, piemēram, `x=`, `y=`, `hue=`, `row=` un `col=`.
- Plotly Express pieņem DataFrame tieši un izmanto kolonnu nosaukumus asīm, krāsām, fasetēm, uzvedņu datiem un animācijas kadriem.
- GeoPandas paplašina pandas ar ģeometrijas kolonnām. Tā nodrošina telpiskas operācijas, saglabājot DataFrame līdzīgu darbplūsmu.
- Daudzas specializētās bibliotēkas pieņem pandas datu rāmjus tieši vai var izmantot kolonnas, kas pārvērstas sarakstos, NumPy masīvos vai vārdnīcās.

Piemēra darbplūsma:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
summary = (
    df.groupby("category", as_index=False)
      .agg(mean_value=("value", "mean"))
      .sort_values("mean_value", ascending=False)
)

sns.barplot(data=summary, x="mean_value", y="category")
plt.xlabel("Mean value")
plt.ylabel("Category")
plt.title("Mean value by category")
plt.tight_layout()
```

Plotly piemērs:

```python
import plotly.express as px

fig = px.bar(
    summary,
    x="mean_value",
    y="category",
    orientation="h",
    title="Mean value by category",
)
fig.show()
```

## Specializētās vizualizācijas bibliotēkas

Šīs bibliotēkas nav obligātas. Pievienojiet tās tad, ja uzdevumam tiešām vajadzīgas to stiprās puses, nevis mēģiniet visu piespiest vienkāršai diagrammai.

| Joma | Bibliotēka | Instalēšana | Kad lietot | Oficiālā dokumentācija |
| --- | --- | --- | --- | --- |
| Ģeotelpiskā analīze | GeoPandas | `pip install geopandas` | Ja vajadzīgs pandas līdzīgs darbs ar shapefile datnēm, GeoJSON, telpiskajiem savienojumiem, projekcijām vai horoplētām kartēm. | <https://geopandas.org/en/stable/> |
| Interaktīvas tīmekļa kartes | Folium | `pip install folium` | Ja vajadzīgas Leaflet balstītas interaktīvas kartes piezīmju grāmatās vai HTML formātā, īpaši marķieri, horoplētas un kartes flīzes (map tiles). | <https://python-visualization.github.io/folium/latest/> |
| Kartes pamatnes flīzes | Contextily | `pip install contextily` | Ja GeoPandas vai Matplotlib kartēm vajadzīgas OpenStreetMap tipa fona flīzes. | <https://contextily.readthedocs.io/en/latest/> |
| Kartogrāfiskās projekcijas | Cartopy | `pip install cartopy` | Ja vajadzīgas zinātniskas kartes, projekcijas, koordinātu transformācijas vai globāla/reģionāla ģeotelpiskā attēlošana ar Matplotlib. | <https://cartopy.readthedocs.io/stable/> |
| Teksta vizualizācija | wordcloud | `pip install wordcloud` | Ja vēlaties ātru biežāko terminu vizuālu kopsavilkumu teksta datos. Lietojiet kā izpētošu papildinājumu, nevis kā precīzu statistisku diagrammu. | <https://amueller.github.io/word_cloud/> |
| Tematu modelēšana | pyLDAvis | `pip install pyLDAvis` | Ja vajag interaktīvi pārbaudīt LDA tematu modeļus, tematu attālumus un augstas varbūtības terminus. | <https://pyldavis.readthedocs.io/en/latest/> |
| Deklaratīvas diagrammas | Altair | `pip install altair` | Ja vēlaties īsas vizuālās gramatikas (grammar of graphics) stila diagrammas, kas balstītas uz Vega-Lite, īpaši tīriem piezīmju grāmatu piemēriem. | <https://altair-viz.github.io/> |
| Pārlūkprogrammas informācijas paneļi | Bokeh | `pip install bokeh` | Ja vajadzīgas interaktīvas pārlūkprogrammas diagrammas, saistītā atlase (linked brushing), straumēti dati vai pielāgotas informācijas paneļu lietotnes. | <https://docs.bokeh.org/en/latest/> |
| Trūkstošo datu pārbaude | missingno | `pip install missingno` | Ja pirms datu rāmja tīrīšanas vajag ātri vizuāli pārbaudīt trūkstošo vērtību modeļus. | <https://github.com/ResidentMario/missingno> |
| Tīklu grafi | NetworkX | `pip install networkx` | Ja vajadzīga grafu analīze un pamata grafu zīmēšana relācijām, piemēram, saitēm, atkarībām vai sociālajiem tīkliem. | <https://networkx.org/documentation/stable/reference/drawing.html> |
| Mašīnmācīšanās diagnostika | Yellowbrick | `pip install yellowbrick` | Ja vajadzīgas scikit-learn modeļu vizuālās diagnostikas, piemēram, atlikumu diagrammas, klasifikācijas pārskati, pazīmju svarīgums vai klasterizācijas diagnostika. | <https://www.scikit-yb.org/en/latest/> |

Ģeotelpiskajām bibliotēkām Windows vidē `conda` reizēm ir vienkāršāka nekā `pip`, jo tādas pakotnes kā GeoPandas, Cartopy, rasterio, pyproj un shapely ir atkarīgas no kompilētām ģeotelpiskām bibliotēkām:

```bash
conda install -c conda-forge geopandas folium contextily cartopy
```

Vieglai piezīmju grāmatu videi ar kursa galvenajiem rīkiem:

```bash
pip install pandas matplotlib seaborn plotly
```

NLP un tematu modelēšanas papildu vizualizācijām:

```bash
pip install wordcloud pyLDAvis
```

## Ieteicamā temata struktūra

1. Sāciet ar vēsturiskajiem piemēriem: Pleifērs, Snovs, Naitingeila, Minārs, Dibuā, Bertēns, Tafti, Klīvlends un Makgils.
2. Pārrunājiet, uz kādu jautājumu katra vizualizācija atbildēja un kādu darbību vai argumentu tā atbalstīja.
3. Praktizējiet mērķa teikuma rakstīšanu pirms diagrammas veidošanas.
4. Pieskaņojiet uzdevumus diagrammu tipiem, izmantojot diagrammu izvēles tabulu.
5. Pārveidojiet pārslogotu diagrammu, uzlabojot marķējumu, mērogu, krāsu un fokusu.
6. Salīdziniet Matplotlib, Seaborn un Plotly ar vienu un to pašu vienkāršo DataFrame.
7. Izveidojiet vai uzlabojiet vienu vizualizāciju Python vidē un izskaidrojiet dizaina izvēles.

## Atsauces

Saites pārbaudītas 2026-05-12.

- Friendly, Michael, and Daniel J. Denis. "Milestones in the History of Thematic Cartography, Statistical Graphics, and Data Visualization." <https://datavis.ca/milestones/>
- Playfair, William. *The Commercial and Political Atlas* (1786), Open Library record. <https://openlibrary.org/books/OL16924946M/The_commercial_and_political_atlas>
- Lehigh University Library Exhibits. "Playfair's Pie Chart." <https://exhibits.lib.lehigh.edu/exhibits/show/data_visualization/case_one/playfair>
- UCLA Department of Epidemiology. "Map, Myth and Error Making in Broad Street Pump Outbreak." <https://epi-snow.ph.ucla.edu/Stream2_BSPoutbreak_f.html>
- Nightingale, Florence. *Notes on Matters Affecting the Health, Efficiency, and Hospital Administration of the British Army* (1858), Open Library record. <https://openlibrary.org/works/OL17018094W/Notes_on_matters_affecting_the_health_efficiency_and_hospital_administration_of_the_British_Army>
- Lehigh University Library Exhibits. "Nightingale's Rose Diagram." <https://exhibits.lib.lehigh.edu/exhibits/show/data_visualization/science/nightingale>
- Wikimedia Commons. "Figurative Map of the Russian campaign 1812 by Minard." <https://commons.wikimedia.org/wiki/Category:Figurative_Map_of_the_Russian_campaign_1812_by_Minard>
- Edward Tufte / Graphics Press. "Books and Essays." <https://www.edwardtufte.com/tufte/books_vdqi>
- Cooper Hewitt, Smithsonian Design Museum. "Deconstructing Power: W. E. B. Du Bois at the 1900 World's Fair." <https://www.cooperhewitt.org/exhibition/deconstructing-power-w-e-b-du-bois-at-the-1900-worlds-fair/>
- Esri Press. *Semiology of Graphics: Diagrams, Networks, Maps* by Jacques Bertin. <https://www.esri.com/en-us/esri-press/browse/semiology-of-graphics-diagrams-networks-maps>
- Cleveland, William S., and Robert McGill. "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." *Journal of the American Statistical Association* 79, no. 387 (1984): 531-554. <https://www.tandfonline.com/doi/abs/10.1080/01621459.1984.10478080>
- Munzner, Tamara. *Visualization Analysis and Design*. CRC Press, 2014. <https://www.cs.ubc.ca/~tmm/vadbook/>
- Financial Times Visual Journalism Team. "Financial Times Visual Vocabulary." <https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary>
- W3C Web Accessibility Initiative. "Understanding Success Criterion 1.4.1: Use of Color." <https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html>
- Brewer, Cynthia, Mark Harrower, and The Pennsylvania State University. "ColorBrewer 2.0." <https://colorbrewer2.org/>
- pandas. "Chart visualization." <https://pandas.pydata.org/docs/user_guide/visualization.html>
- Matplotlib. "Matplotlib documentation." <https://matplotlib.org/stable/>
- Seaborn. "seaborn: statistical data visualization." <https://seaborn.pydata.org/>
- Plotly. "Plotly Python Graphing Library." <https://plotly.com/python/>
- GeoPandas. "GeoPandas documentation." <https://geopandas.org/en/stable/>
- Folium. "Folium documentation." <https://python-visualization.github.io/folium/latest/>
- Contextily. "contextily: context geo tiles in Python." <https://contextily.readthedocs.io/en/latest/>
- Cartopy. "Cartopy documentation." <https://cartopy.readthedocs.io/stable/>
- wordcloud. "WordCloud for Python documentation." <https://amueller.github.io/word_cloud/>
- pyLDAvis. "pyLDAvis documentation." <https://pyldavis.readthedocs.io/en/latest/>
- Vega-Altair. "Vega-Altair: Declarative Visualization in Python." <https://altair-viz.github.io/>
- Bokeh. "Bokeh documentation." <https://docs.bokeh.org/en/latest/>
- missingno. "Missing data visualization module for Python." <https://github.com/ResidentMario/missingno>
- NetworkX. "Drawing." <https://networkx.org/documentation/stable/reference/drawing.html>
- Yellowbrick. "Yellowbrick: Machine Learning Visualization." <https://www.scikit-yb.org/en/latest/>
- AkadTerm. "vizualizācija." <https://www.akadterm.lv/term.php?exact=1&lang=LV&term=vizualiz%C4%81cija>
- AkadTerm. "mašīnmācīšanās." <https://www.akadterm.lv/term.php?lang=LV&list=ma%C5%A1%C4%ABnm%C4%81c%C4%AB%C5%A1an%C4%81s&term=da%C4%BC%C4%93ji+uzraudz%C4%ABta+ma%C5%A1%C4%ABnm%C4%81c%C4%AB%C5%A1an%C4%81s>
- AkadTerm. "ticamības intervāls." <https://www.akadterm.lv/term.php?lang=LV&list=interv%C4%81ls&term=interv%C4%81ls>
