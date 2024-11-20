# Contributing

Welcome to ``eodm`` contributor's guide!

This document focuses on getting any potential contributor familiarized
with the development processes, but
[other kinds of contributions](https://opensource.guide/how-to-contribute)
are also appreciated.

If you are new to using git or have never collaborated in a project previously,
please have a look at [contribution-guide.org](https://www.contribution-guide.org/).

Please notice, all users and contributors are expected to be **open,
considerate, reasonable, and respectful**. When in doubt,
[Python Software Foundation's Code of Conduct](https://policies.python.org/python.org/code-of-conduct/)
is a good reference in terms of behavior guidelines.

## Issue Reports

If you experience bugs or general issues with ``eodm``, please have a look
on the [issue tracker](https://github.com/geopython/eodm/issues).
If you don't see anything useful there, please feel free to create an issue report.

**TIP:** Please don't forget to include the closed issues in your search.
Sometimes a solution was already reported, and the problem is considered **solved**.

New issue reports should include information about your programming environment
(e.g., operating system, Python version) and steps to reproduce the problem.
Please try also to simplify the reproduction steps to a very minimal example
that still illustrates the problem you are facing. By removing other factors,
you help us to identify the root cause of the issue.

## Documentation Improvements

You can help improve ``eodm`` docs by making them more readable and coherent, or
by adding missing information and correcting mistakes.

``eodm`` documentation uses [mkdocs](https://www.mkdocs.org/) as
its main documentation compiler and markdown as documentation format.
This means that the docs are kept in the same repository as the project code, and
that any documentation update is done in the same way was a code contribution.

When working on documentation changes in your local machine, you can
compile them using [mkdocs](https://www.mkdocs.org/)

```shell
mkdocs build --site-dir public
```

or use mkdocs web server for a preview in your web browser

```shell
mkdocs serve
```

**Note**: If updating the CLI run the following to update the cli documentation.

```shell
typer eodm.__main__ utils docs --name eodm --output docs/cli.md
```

## Design philosophy

<!-- TODO - idea and architecture -->

### About

- What is the software application or feature?

The application is a library and a CLI application

- Who’s it intended for?

The package is intended for EO scientists and data engineers

- What problem does the software solve?

It serves as a library of common features for extracting, transforming and loading EO data
as well as a CLI application

- How is it going to work?

There are two ways to use the software.

- CLI Application - the purpose is to collect common functions for EO data ETL and allow cli orchestrators
like kubernetes, argo workflows to be used for these operations
- Library - collection common python functions for use in python like orchestrators such
as prefect, flyte, hamilton etc. or to be used directly in backend systems

### User interface

- What are the main concepts that are involved and how are they related?
- What are the main user stories (happy flows + alternative flows)?
- If you’re adding a new feature to an existing software application, what impact does
the feature have on the overall structure of the interface? (are there big changes in the
organization of menus, navigation, and so on?)

### Technical Specification

- What technical details need developers to know to develop the software or new
feature?
- Are there new tables to add to the database? What fields?
- How will the software technically work? Are there particular algorithms or libraries
that are important?
- What will be the overall design? Which classes are needed? What design patterns are
used to model the concepts and relationships?
- What third-party software is needed to build the software or feature?

### Testing and security

- Are there specific coverage goals for the unit tests?
- What kinds of tests are needed (unit, regression, end-to-end, etc)?
- (new feature only) Are there any potential side-effects on other areas of the application
when adding this feature?
- What security checks need to be in place to allow the software to ship?
- (new feature only) How does the feature impact the security of the software? Is there
a need for a security audit before the feature is shipped?

### Deployment

- Are there any architectural or DevOps changes needed (e.g. adding an extra
microservice, changes in deployment pipelines, adding secrets to services)?
- Are there any migration scripts that need to be written?

### Planning

- How much time will developing the software or feature cost?
- What are the steps and how much time does step take?
- What are the developmental milestones and in what order?
- What are the main risk factors and are there any alternative routes to take if you find
out something isn’t feasible?
- What parts are absolutely required, and what parts can optionally be done at a later
stage? (i.e. the Definition of Done)

## Code Contributions

### Submit an issue

Before you work on any non-trivial code contribution it's best to first create
a report in the [issue tracker](https://gitlab.eox.at/vs/eodm/issues) to start a
discussion on the subject.
This often provides additional considerations and avoids unnecessary work.

### Clone the repository

- Fork the project repository: click on the **Fork** button near the top of the
page. This creates a copy of the code under your account on [the repository service](https://github.com/geopython/eodm).
- Clone this copy to your local disk:

```shell
git clone https://github.com/geopython/eodm.git
cd eodm
```

### Create an environment

Before you start coding, we recommend creating an isolated virtual
environment to avoid any problems with your installed Python packages.
As the project uses poetry we can leverage some of its features.

```shell
poetry env use /path/to/python
poetry shell
poetry install
```

to be able to import the package under development in the Python REPL.

Setup commitizen and pre-commit.

```shell
pre-commit install --hook-type commit-msg --hook-type pre-push
```

### **Optional:** Configure VS Code

If you work with VS Code the following configurations can be reused to start two debug
sessions in docker or locally.

`.vscode/launch.json`

```json
{}
```

Ruff and mypy are used for linting and static type checking.

`.vscode/settings.json`

```json
{
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
          "source.fixAll": "explicit",
          "source.organizeImports": "explicit"
        },
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnPaste": true,
    },
    "mypy-type-checker.importStrategy": "fromEnvironment",
    "mypy-type-checker.preferDaemon": false,
    "python.testing.pytestArgs": [
      "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
}
```

`.vscode/tasks.json`

```json
{}
```

### Implement your changes

- Create a branch to hold your changes:

```shell
git checkout -b my-feature
```

and start making changes. If the change is small and pre-approved, feel free to push directly
to main. Branches should be short lived as this will allow faster pushes and more agility.

- Start your work on this branch. Don't forget to add docstrings using the
[Google style](https://google.github.io/styleguide/pyguide.html) to new
functions, modules and classes, especially if they are part of public APIs.

- Add yourself to the list of contributors in ``AUTHORS.rst``.

- When you’re done editing, do:

``` shell
git add <MODIFIED FILES>
git commit
```

to record your changes in git.

Don't forget to add unit tests and documentation in case your contribution adds an
additional feature and is not just a bugfix.

We are using commitizen with conventional commits.
In case of doubt, you can check the commit history with:

```shell
git log --graph --decorate --pretty=oneline --abbrev-commit --all
```

to look for recurring communication patterns

or use

```shell
cz commit
```

for help creating a guided message when making a conventional commit.

- Check that your changes don't break any tests with:

```shell
pytest
```

### Submit your contribution

- If everything works fine, push your local branch or changes to
[the repository service](https://gitlab.eox.at/vs/eodm) with:

```shell
git push -u origin my-feature
```

- Go to the web page of your fork and click Merge request to send your changes for review.
You may want to add `Draft:` in the title to mark as a draft first to setup for a review

### Troubleshooting

The following tips can be used when facing problems to build or test the
package:

- Make sure to fetch all the tags from the upstream repository.
The command ``git describe --abbrev=0 --tags`` should return the version you
are expecting. If you are trying to run CI scripts in a fork repository,
make sure to push all the tags.
You can also try to remove all the egg files or the complete egg folder, i.e.,
``.eggs``, as well as the ``*.egg-info`` folders in the ``src`` folder or
potentially in the root of your project.

- Pytest can drop you in an interactive session in the case an error occurs.
In order to do that you need to pass a ``--pdb`` option (for example by
running ``pytest -- -k <NAME OF THE FALLING TEST> --pdb``).
You can also setup breakpoints manually instead of using the ``--pdb`` option, or use the
VSCode debugger.

## Maintainer tasks

### Releases

If you are part of the group of maintainers and have correct user permissions
on gitlab, the following steps can be used to release a new version for
``eodm``:

- Make sure all tests are successful.
- On the main branch simply run

```shell
cz bump
git push && git push --tags
```

## Other

### Useful endpoints for testing

- [Microsoft planetary computer STAC](https://planetarycomputer.microsoft.com/api/stac/v1/)
- [AWS Element 84 STAC](https://earth-search.aws.element84.com/v1)
- [EURAC STAC](https://stac.eurac.edu/)
- [EOEPCA develop STAC](https://eoapi.develop.eoepca.org/stac/)
- [EOX hub-int STAC](https://stac.hub-int.eox.at/)

### Inspiration

- [vs harvester](https://gitlab.eox.at/vs/vs/-/tree/main/harvester/src/harvester?ref_type=heads)
- [vs preprocessor](https://gitlab.eox.at/vs/vs/-/tree/main/preprocessor?ref_type=heads)
- [vs registrar](https://gitlab.eox.at/vs/vs/-/tree/main/core/src/registrar?ref_type=heads)
- [EOEPCA registration library](https://github.com/EOEPCA/registration-library/tree/main)
- [osc-cataloguer](https://github.com/constantinius/open-science-catalog-cataloguer/tree/main)
- [eodash-catalog](https://github.com/eurodatacube/eodash-catalog)
- [eodag](https://eodag.readthedocs.io/en/stable/)
- [mapchete](https://mapchete.readthedocs.io/en/stable/)
