# expense-tracker

## Running App Locally

To run the expense-tracker app locally on your machine follow these steps:

1. Install the dependencies

    ```sh
    pip install -r requirements.txt
    ```

1. Run the application

   ```sh
   uvicorn src.app.main:app --reload
   ```

The application is now running locally! Point your web browser at
<http://127.0.0.1:8000/docs> to view the OpenAPI specs for it and
to play around with making requests.

Note: Remember to remove the `--reload` when not in a development
environment. It helps a lot during development, but you shouldn't
use it in production.
