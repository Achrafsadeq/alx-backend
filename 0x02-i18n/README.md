# 0x02. Internationalization (i18n)

## Description

This project focuses on implementing internationalization (i18n) and localization (l10n) in a Flask web application using Flask-Babel. You'll learn how to create multilingual applications, handle locale selection, and work with translation files. The tasks cover basic Flask setup, Babel configuration, template parametrization, locale forcing, user preferences, timezone handling, and displaying localized dates/times.

## Requirements

| Category | Details |
|----------|---------|
| Interpreter | Ubuntu 18.04 LTS using python3 (version 3.7) |
| File Endings | All files should end with a new line |
| Shebang | The first line of all files should be exactly `#!/usr/bin/env python3` |
| README | A README.md file at the root of the project folder is mandatory |
| Coding Style | pycodestyle (version 2.5.x) |
| Executable | All files must be executable |
| Documentation | Modules, classes and functions should be documented |
| Type Annotations | All functions and coroutines must be type-annotated |
| Dependencies | flask-babel==2.0.0, pytz |

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0 | Basic Flask app with single route | 0-app.py, templates/0-index.html |
| 1 | Basic Babel setup with Config class | 1-app.py, templates/1-index.html |
| 2 | Locale selection from request headers | 2-app.py, templates/2-index.html |
| 3 | Template parametrization with gettext | 3-app.py, babel.cfg, templates/3-index.html, translation files |
| 4 | Force locale via URL parameter | 4-app.py, templates/4-index.html |
| 5 | Mock user login system | 5-app.py, templates/5-index.html |
| 6 | User preferred locale | 6-app.py, templates/6-index.html |
| 7 | Timezone selection and validation | 7-app.py, templates/7-index.html |
| 8 | Display localized current time | app.py, templates/index.html, translation files |

## Learning Objectives

By completing this project, you will be able to:

* Implement internationalization in a Flask application
* Set up and configure Flask-Babel extension
* Create multilingual templates using gettext
* Handle locale selection from different sources (URL, user preferences, headers)
* Manage translation files (PO and MO files)
* Implement timezone handling and validation
* Display localized dates and times
* Work with Flask's application context (g object)
* Implement before_request handlers
* Create proper documentation for Python modules
* Follow Python coding style guidelines

## Base Configuration

All implementations use the following base configuration:

```python
#!/usr/bin/env python3
"""Basic Flask app with Babel configuration"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
```

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.


