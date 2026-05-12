# Topic: Data Visualization - History, Purpose, and Practice

Data visualization is not decoration. It is a way to reason with data, expose patterns, and communicate evidence. The most important habit is to define the goal first: what should the audience understand, compare, question, or decide after seeing the visualization?

## Learning goals

By the end of this day, students should be able to:

- Explain why visualizations have been important in science, public policy, journalism, and statistics.
- Recognize several historical milestones in data visualization.
- Choose common chart types based on the task, not based on what looks impressive.
- Write a clear visualization goal before plotting.
- Improve charts by using clear labels, appropriate scales, meaningful color, and minimal distraction.

## Historical foundations

Modern visualization practice grew from cartography, statistics, public health, economics, sociology, and graphic design. The examples below are worth studying because each one solved a real communication problem.

| Period | Figure or work | Why it matters |
| --- | --- | --- |
| 1780s | William Playfair, *The Commercial and Political Atlas* | Playfair helped establish statistical graphics such as line charts, bar charts, and later pie charts as tools for economic argument. He showed that quantitative change could be read visually rather than only through tables. |
| 1854 | John Snow's Broad Street cholera maps | Snow's maps connected deaths to water-pump locations during a cholera outbreak in London. They remain a classic example of spatial evidence used for public-health reasoning. |
| 1858 | Florence Nightingale's polar-area mortality diagrams | Nightingale used statistical graphics to argue for sanitation reform in military hospitals. Her work shows that visualization can support policy change when it makes a problem visible. |
| 1869 | Charles Joseph Minard's graphic of Napoleon's 1812 march to Moscow and retreat | Minard combined geography, direction, army size, time, and temperature in one figure. The map is famous because it makes a complex historical disaster readable at a glance without reducing it to a single number. |
| 1900 | W. E. B. Du Bois and the Atlanta University data portraits | Du Bois and his collaborators used hand-drawn charts for the Paris Exposition to document Black American life, education, work, and social conditions. These charts show visualization as evidence, design, and civic argument. |
| 1967 | Jacques Bertin, *Semiology of Graphics* | Bertin formalized the idea that visual marks and channels such as position, size, shape, value, texture, orientation, and color carry different kinds of information. |
| 1983 onward | Edward Tufte, *The Visual Display of Quantitative Information* and later books | Tufte popularized a rigorous design vocabulary around graphical integrity, high information density, data-ink, and avoiding chartjunk. His work also helped bring historical examples such as Minard's Napoleon graphic into modern visualization teaching. |
| 1984 onward | William Cleveland and Robert McGill's graphical perception research | Their experiments gave visualization design an empirical foundation: people decode some visual encodings more accurately than others, especially position along a common scale. |

The main lesson from this history is that strong visualizations begin with a problem: explain trade, find disease patterns, argue for reform, document social conditions, compare evidence, or support a decision.

## Define the goal before choosing a chart

Before making a plot, write one sentence:

> I want this audience to see that ____ so they can ____.

Then answer these questions:

- Who is the audience: classmates, analysts, managers, the public, or domain experts?
- What is the task: compare, rank, find a trend, inspect a distribution, show a relationship, locate something, show a part-to-whole structure, or show uncertainty?
- What is the unit and denominator: count, percent, rate per capita, index, currency, time interval?
- What decision or interpretation should the chart support?
- What could be misunderstood if the chart is read quickly?
- What data source, filtering, aggregation, or missingness must be stated?

If the goal is vague, the chart will usually become vague too.

## Choose chart types by task

| Task | Good defaults | Notes and cautions |
| --- | --- | --- |
| Compare categories | Bar chart, dot plot, lollipop chart | Sort by value unless the categories have a natural order. Use a zero baseline for bars because bar length encodes magnitude. |
| Rank items | Sorted bar chart, ordered dot plot, slope chart for rank change | Highlight the few important items instead of coloring every item differently. |
| Show change over time | Line chart, area chart for totals, column chart for discrete periods | Use lines for continuous time. Do not connect unordered categories with a line. Choose the time window honestly. |
| Show a distribution | Histogram, density plot, box plot, violin plot, dot strip plot | Use histograms for shape, box plots for compact group comparison, and dot plots when individual observations matter. |
| Show relationship or correlation | Scatter plot, bubble chart, hexbin plot, heatmap | Correlation is not causation. Label outliers and consider transparency or aggregation for dense data. |
| Show part-to-whole | Stacked bar, 100 percent stacked bar, treemap for hierarchy, small-multiple bars | Pie charts can work for a few obvious parts, but they are weak for precise comparisons or many categories. |
| Show geographic patterns | Choropleth map for rates, proportional-symbol map for counts, dot-density map for distribution | Avoid mapping raw counts by region area when population size explains the pattern better than geography. |
| Show flow or process | Sankey diagram, alluvial chart, flow map, funnel chart | Use only when the movement or transition is the main point. Too many flows become unreadable quickly. |
| Show uncertainty | Error bars, confidence intervals, fan chart, prediction interval ribbon | Do not hide uncertainty when it changes the interpretation. Explain what the interval means. |
| Show many variables | Small multiples, faceting, heatmap, carefully encoded scatter plot | Prefer repeated simple charts over one overloaded chart. |

## Labeling and design best practices

- Use a title that states the takeaway, not only the chart type.
- Label axes with units. Percent of what? Euros per year? Observations per group?
- Directly label important series when possible instead of forcing the reader to jump between chart and legend.
- Use readable number formats: 1.2 million is often clearer than 1,200,000.
- Keep gridlines light and useful. Remove borders, shadows, 3D effects, and decorative backgrounds unless they carry information.
- Use color intentionally: sequential palettes for ordered magnitude, diverging palettes for values around a meaningful midpoint, and qualitative palettes for categories.
- Do not rely on color alone to communicate meaning. Add labels, shape, line style, or text cues.
- Keep scales honest. Show zero for bars, explain transformed axes, and avoid dual axes unless there is a strong reason and clear labeling.
- Show source notes when data origin, filtering, or transformation affects interpretation.
- Make the important comparison easy. If the reader must mentally calculate the result, redesign the chart.

Good design removes friction. It does not remove necessary context.

## Avoid unnecessary distractions

Tufte's critique of chartjunk is useful as a practical editing rule: every visible element should either encode data, explain the data, or help the reader navigate the chart. If it does none of those, remove it.

Common distractions:

- 3D bars or pies that distort judgment.
- Heavy gridlines and thick borders.
- Too many colors without semantic meaning.
- Decorative icons repeated as data marks when simple bars or points would be clearer.
- Legends that could be replaced with direct labels.
- Background images, gradients, or textures that compete with the data.
- Excessive decimals or labels on every point when only a few labels matter.

The goal is not minimalism for its own sake. The goal is to make the evidence easier to read.

## Suggested day 2 flow

1. Start with the historical examples: Playfair, Snow, Nightingale, Minard, Du Bois, Bertin, Tufte, Cleveland and McGill.
2. Discuss what question each visualization answered and what action or argument it supported.
3. Practice writing a goal sentence before plotting.
4. Match tasks to chart types using the chart-selection table.
5. Redesign a cluttered chart by improving labels, scale, color, and focus.
6. Build or improve one visualization in Python and explain the design choices.

## References

Links verified on 2026-05-12.

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
