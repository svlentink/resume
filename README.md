# Resume

This is the source code of my resume
(on Github to share my format with others).

You should only edit the contents in `./content`,
run `docker-compose up`
and the generated files will be located in `./generated`.

## Yaml
<!--
Initially this was all LaTeX based,
but when I started working as a freelancer,
people asked for my resume in MS Word in Dutch.

My motivation for LaTeX was the decoupling
of layout from the content.
However, this was not enough.


We now have another layer of abstraction.
-->

+ The actual data is stored in yaml files
+ Python script generates docx, txt and HTML (we plan to do LaTeX or markdown later)

### Editable, why we use docx
If you give a pdf, people cannot edit it.
If you give latex source, you are just weird.

Large coorperations sometimes want to anonymize resumes,
preventing discrimination etc.

Recruiters also do things to your resume, deal with it,
they understand the HR language better than us techies.

## Links

+ US format: https://www.zipjob.com/blog/us-resume-format/
+ EU format: https://europa.eu/europass/en
+ Great examples: https://enhancv.com/resume-examples/
+ possible option for generation of PDF: https://themes.gohugo.io/hugo-theme-winning/


## Tips

- during interview
    - bring printed resume
    - have questions on paper about vacancy, test it
    - be relaxed, ask control questions
    - ask when project success, which challenges, which metrics
    - memorized tackeled problems and being able to explain them using STAR
    - ask ratio managing vs executing (technical work)
    - always close positive
    - able to state strong and learning points
    - do they work on projects (Prince2, ITIL, waterfall) or products (agile)

- Know your demands
    - work from home
    - no standby duty
