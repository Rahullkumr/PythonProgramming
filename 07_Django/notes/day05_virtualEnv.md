# Day05: 22-Jan-2025

## Virtual Environment

- Every Django project should be inside a separate virtual env 
- so as to prevent the conflict between different versions of python or related packages

## Installation

1. Virtual Environment (what? and why?)

    > Virtual Environment is like a small room in a big house, like a Kitchen where you keep only the items related to food and eatery.

    > Each VE contains packages and dependencies related to that project only.

    > since different projects have different requirements, like a projects needs a particular version of a package and the other project needs a different version of the same package, that's why to keep multiple projects separately and isolated from each other

2. Create a virtual environment

    - open cmd and go inside your project root directory and run the following

    ```bash
        python -m venv virtual_Environment_ka_naam
    ```

3. Activate the virtual environment

    ```bash
        virtual_Environment_ka_naam\Scripts\activate
    ```

    - Display installed packages in the virtual env, run the following:

        ```bash
            pip freeze
        ```
    - Create `requirements.txt` file containing installed packages
        ```bash
            pip freeze > requirements.txt
        ```

5. To deactivate, run the following

    ```bash
        deactivate
    ```

6. Install Django

    ```bash
        pip install django
    ```

7. Check it's properly installed or not

    ```bash
        django-admin --version
    ```
    or
    ```python
        import django
        print(django.get_version())
        # exit()
    ```
