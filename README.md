# Resume

This is the source code of my LaTeX resume
(on Github to share my format with others).

You should only edit the contents in `/content`
and the generated files will be located in `/output`.

## Yaml

Initially this was all LaTeX based,
but when I started working as a freelancer,
people asked for my resume in MS Word in Dutch.

My motivation for LaTeX was the decoupling
of layout from the content.
However, this was not enough.

We now have another layer of abstraction.
+ The actual data is stored in yaml files
+ Python script generates **LaTeX or markdown** docx, txt and HTML.
+ This is then converted to a;
  - TODO: pdf (`texi2pdf`),
  - HTML **(`pandoc --from=markdown`)** did not work, markdown needs table header
  - or .doc (for recruiters)

### Editable
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

Use the items of knowledge tree,
together with the items of all experiences
and combine them into one set of items
for one page resume.

Add MBTI outcome, belbin?

