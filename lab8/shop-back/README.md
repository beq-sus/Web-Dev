# shop-back

Django REST API backend for the Online Shop project.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List all products |
| GET | `/api/products/<id>/` | Get product by ID |
| GET | `/api/categories/` | List all categories |
| GET | `/api/categories/<id>/` | Get category by ID |
| GET | `/api/categories/<id>/products/` | List products by category |

## Optional: Load sample data

```bash
python seed_data.py
```
