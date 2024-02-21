# Test Suite Example

For this project, I'm using poetry.
Poetry is a dependency management tool and I use it
to manage all the dependencies that I'll be using
for this project.

To install poetry navigate to the following link
https://python-poetry.org/
Click on documentation
Under installation, click "With the official install"

![Installation instructions](/documentation/screenshots/installation1.jpg?raw=true "poetry website")

Alternatively, you can do

```python
pip install poetry
```

However, this way of installing it is not recommended
as you'd have to install it separately for every
version of Python you have installed on your system.

To start the project first type poetry init to create a
`pyproject.toml` file that all dependencies meta data about
the project will be stored.

Use the screenshot below as a template for how to init
the project. Then you should see a pyproject.toml
file created

![Installation instructions](/documentation/screenshots/poetry_init.jpg?raw=true "poetry init")

Type poetry shell to activate the new virtual environment

Note: if it says that poetry is already activated some-
where else, go to folder folder it mentions and type
exit. Exit will deactivate your current virutal environment.
For example if you get:
Virtual environment already activated: /home/<user>/.cache/
pypoetry/virtualenvs/my-project-0wt3KWFj-py3.7

Do the following

```
cd /home/<user>/.cache/pypoetry/virtualenvs/
exit
```

To add a dependency, use poetry add --dev <package_name>@latest

for example:

```
poetry add --dev selenium@latest
poetry add --dev pytest@latest
```

Alternatively, you can install multiple dependencies
in one line by writing them one after another like so:

```
poetry add --dev black flake8 pre-commit tox python-dotenv
```

Selenium is used for UI automation, pytest and tox for
testing our code for different versions of Python, black
and flake8 for PEP-8 formatting, and pre-commit
for auto-linting during each commit. Finially, I'm using
python-dotenv to store environment variables and load them
securely.

Note: some packages may require a higher version
of Python to work. So you can jut go in the pyproject.toml
and update the version (e.g. python_version >= 3.9.)

After all dependencies have been install, a `poetry.lock`
file should have been generatered.

You can use the command `poetry show --tree` to see dep-
endencies in tree hierarchy format. This will give
you a better sense of what packages belong to what group
of dependencies.

![poetry dependency tree](/documentation/screenshots/poetry_show_tree.jpg?raw=true "poetry tree")

The first thing I did when creating this project was
to create my fixtures. Fixtures give your test contextual
information that they can use to set up your project.

In `conftest.py` I have 2 main fixtures. The first is
driver, which is the Chrome driver that is used
to spawn a new test window and gives other test
context as to what it should do.

The second fixture is called envars which is used
for tests that need to access sensitive information
such as username and password.

`test_suite.py` contains all the tests that
pytest will run.

The first, test will test that login is successful.
The second tests that we are able to add new customers
with no problems. The new customer's credentials are
saved in a file and accessed in the last test.
This test tries to log in as the new customer and
verifies that the login was successful.

I have a folder called pom which stands for page
object model. First I defined a base page that
describes the behavior of a web element we want
to use such as find, wait for, and find all.
It also takes a driver object upon
initialization. wait_for will wait for an
element to be loaded in the page before it attempts
to access it. This helps to account for race conditions.
I use find and wait interchangeably. However, I would
rather use wait_for if I'm changing pages and I want to
make sure all the elements have been loaded.
For the most part, I don't use find_all unless
the only selector I can find targets a group of
elements. In that case I would just refer to the
element that I need by index.

All subsequent classes inherit from this base class.
I tried my best to implement a separation of concerns
in how I defined my classes. I have all my selectors
defined in these classes. I try to make each
method pertain to the class it belongs in. If
I feel like there's a piece of functionality that
doesn't belong to that class, I'll define it in a
helper_functions folder and import it as needed.

To get my selectors, I would inspect each element,
copy the selector, and test that the selector
works by typing the following into the console:

```
document.querySelector(<CSS_SELECTOR>)
```


To run the tests, simply type:

```
pytest test_file.py
```

Make sure you are in the folder pom before you do so.

The `.pre-commit-config.yaml` file defines how
I want my commit hook to work

`tox.ini` contains which PEP-8 rules I want to ignore
when linting. It also defines tests that I want to
run with different version of Python. This will be
triggered when you commit a change to git.
