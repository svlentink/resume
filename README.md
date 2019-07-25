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

+ Great examples: https://enhancv.com/resume-examples/
+ possible option for generation of PDF: https://themes.gohugo.io/hugo-theme-winning/

## TODO

- One page resume; use the items of knowledge tree, together with the items of all experiences and combine them into one set of items
- Add MBTI outcome, belbin?
- TODO: pdf (`texi2pdf`),
- HTML **(`pandoc --from=markdown`)** did not work, markdown needs table header
