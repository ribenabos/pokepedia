================================
Poképedia
================================

Overview
--------

This is a Django project for a web application with data from the Pokémon API using the `pokebase` library.

Installation
------------

1. Clone the repository:

   .. code-block:: shell

      $ git clone https://github.com/ribenabos/pokepedia.git

2. Create a virtual environment:

   .. code-block:: shell

      $ cd pokepedia
      $ python3 -m venv env

3. Activate the virtual environment:

   .. code-block:: shell

      $ source env/bin/activate

4. Install the project dependencies:

   .. code-block:: shell

      $ pip install -r requirements.txt

5. Run database migrations:

   .. code-block:: shell

      $ python manage.py migrate

Usage
-----

To launch the Poképedia web application, follow these steps:

1. Make sure your virtual environment is activated.

2. Start the development server:

   .. code-block:: shell

      $ python manage.py runserver

3. Open your web browser and visit `http://localhost:8000/` to access Pokepedia.


To populate the database with data for every Pokémon, run the following command:

.. code-block:: shell

   $ python manage.py populate_pokemon

This will fetch data for each Pokémon from the Pokémon API and store it in the database.

Contributing
------------

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
