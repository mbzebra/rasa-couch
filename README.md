CouchTrackerStore
~~~~~~~~~~~~~~~~~

:Description:
    `CouchTrackerStore` can be used to store the conversation history in `Couchbase <https://www.couchbase.com/>`_.
    Couchbase provides an enterprise-class, multicloud to edge database that offers the robust capabilities required for business-critical applications on a highly scalable and available platform.

:Configuration:
    1. Start your Couchbase instance.
    2. Add required configuration to your `endpoints.yml`

        .. code-block:: yaml

            tracker_store:
                type: couch
                url: <url to your mongo instance, e.g. couchbase://localhost:8091>
                db: <name of the bucket within your couchbase instance, e.g. rasabucket>
                username: <username used for authentication>
                password: <password used for authentication>

    3. To start the Rasa Core server using your configured Couch instance,
           add the :code:`--endpoints` flag, e.g.:

            .. code-block:: bash

                rasa run -m models --endpoints endpoints.yml
:Parameters:
    - ``url`` (default: ``couchbase://localhost:8091``): URL of your MongoDB
    - ``db`` (default: ``rasabucket``): The database name which should be used
    - ``username`` (default: ``None``): The username which is used for authentication
    - ``password`` (default: ``None``): The password which is used for authentication
