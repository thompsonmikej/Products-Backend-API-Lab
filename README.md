# Products-Backend-API-Lab

**Developed at devCodeCamp**

This project involves building a RESTful backend API for managing products using Django REST Framework. The API supports CRUD operations with clearly defined endpoints that follow REST principles, enabling interaction with a products database.

---

## Description

- Designed and implemented a **Product** model with the following properties (in snake_case):  
  - `title` (CharField)  
  - `description` (CharField)  
  - `price` (DecimalField)  
  - `inventory_quantity` (IntegerField)  
- Created an Entity Relationship Diagram (ERD) to model the product data structure accurately.
- Developed REST API endpoints to:  
  - Retrieve all products (`GET /api/products/`)  
  - Retrieve a single product by ID (`GET /api/products/<int:pk>/`)  
  - Create a new product (`POST /api/products/`)  
  - Update an existing product (`PUT /api/products/<int:pk>/`)  
  - Delete a product (`DELETE /api/products/<int:pk>/`)  
- Each endpoint explicitly returns appropriate HTTP status codes such as 200, 201, and 204.
- Used Postman to test and document API requests, exporting collections as JSON for reproducibility and sharing.

---

## Features

- Consistent and descriptive Git commits to track project progress  
- Entity Relationship Diagram (ERD) designing for clear data modeling  
- RESTful API implementation adhering to best practices  
- Full CRUD (Create, Read, Update, Delete) support on Product entities  
- Integration and testing with Postman  
- Bonus: Support for an optional product image URL (as `image_url` CharField)

---

## Technologies Used

- Python 3  
- Django REST Framework  
- PostgreSQL / SQLite (configurable backend database)  
- Postman (for API testing and documentation)

---

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/thompsonmikej/Products-Backend-API-Lab.git
    cd Products-Backend-API-Lab
    ```

2. **Set up a virtual environment:**
    ```
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Configure the database:**  
   Update the `settings.py` with your preferred database credentials.

5. **Apply migrations:**
    ```
    python manage.py migrate
    ```

6. **Run the development server:**
    ```
    python manage.py runserver
    ```

7. **Test the API endpoints:**  
   Use Postman or any REST client to interact with the API on `http://127.0.0.1:8000/api/products/`.

---

## Usage

- Access the product list with `GET /api/products/`.
- Retrieve a single product by ID with `GET /api/products/<id>/`.
- Create new products via `POST /api/products/` with JSON payload.
- Update existing products via `PUT /api/products/<id>/`.
- Remove products via `DELETE /api/products/<id>/`.
- Use the exported Postman collection to quickly test all functionality.

---

## Challenges & Lessons Learned

- Structured a backend API with Django REST Framework following REST conventions.  
- Modeled product data using ERDs to ensure clarity and accuracy.  
- Managed CRUD operations with explicit HTTP status codes for robust client communication.  
- Improved API testing and documentation skills using Postman.

---

## Future Improvements

- Add authentication and permissions to protect endpoints.  
- Implement search and filtering capabilities on product listings.  
- Expand product fields to include categories, tags, or reviews.  
- Integrate with frontend clients for full-stack demonstration.

---

## Author

Feel free to reach out or connect:

**Michael Thompson**  
https://www.linkedin.com/in/thompsonmikej  
