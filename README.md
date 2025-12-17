Cuteora E-commerce (Django)

Overview
- Small Django e-commerce sample project with product listing, cart, and templates under `products/templates/products`.

Prerequisites
- Python 3.10+ (venv recommended)
- SQLite (default) or another DB

Quick Setup
1. Create and activate virtualenv
   - Windows (Command Prompt):
     ```cmd
     python -m venv .venv
     .\.venv\\Scripts\\activate
     ```
   - macOS/Linux or Git Bash:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
   ```
3. Apply migrations
   ```powershell
   python manage.py migrate
   ```
4. Create superuser (optional)
   ```powershell
   python manage.py createsuperuser
   ```
5. Run development server
   ```powershell
   python manage.py runserver
   ```

Media & Static
- Uploaded images are served from the `media/` folder during development. Ensure `MEDIA_ROOT` and `MEDIA_URL` are configured in `cuteora/settings.py`.

Project Structure (key files)
- `manage.py` — Django CLI
- `cuteora/` — project settings and wsgi/asgi
- `products/` — app with models, views, templates
- `media/` — uploaded images


