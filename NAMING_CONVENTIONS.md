# Django & Python Naming Conventions

This document outlines the standard naming conventions to be followed throughout the project to ensure professional, readable, and consistent code.

## 1. Folders and Directories
- **Format**: `snake_case` (lowercase with underscores)
- **Examples**: `00_foundations_and_environment_setup`, `core_app`, `static_files`, `templates`.
- **Guidelines**: 
  - Do NOT use spaces, hyphens, or uppercase letters in directory names.
  - Prefix with numbers (e.g., `01_...`, `02_...`) only when ordering is strictly required for educational or structural paths.

## 2. File Names
- **Python Files (`.py`)**: `snake_case`
  - Examples: `models.py`, `utils_functions.py`, `base_views.py`.
- **HTML/Template Files (`.html`)**: `snake_case`
  - Examples: `user_profile.html`, `dashboard_index.html`.
- **Static Files (`.css`, `.js`, Images)**: `kebab-case` or `snake_case` (Be consistent, `snake_case` is preferred if integrating closely with Django tags).
  - Examples: `main_style.css`, `app_script.js`, `logo_dark.png`.

## 3. Python Code Conventions

### Variables and Functions
- **Format**: `snake_case`
- **Examples**: 
  ```python
  user_count = 0
  
  def get_active_users():
      pass
  ```
- **Guidelines**: Use descriptive verbs for functions (`get_`, `is_`, `has_`).

### Classes and Models
- **Format**: `PascalCase` (CapWords)
- **Examples**: 
  ```python
  class UserProfile(models.Model):
      pass
      
  class ActiveUserListView(ListView):
      pass
  ```
- **Guidelines**: 
  - Django Model names should be singular (e.g., `Article`, not `Articles`).
  - Add descriptive suffixes for Class-Based Views (e.g., `...ListView`, `...DetailView`).

### Constants
- **Format**: `UPPER_SNAKE_CASE`
- **Examples**: 
  ```python
  MAX_UPLOAD_SIZE = 1048576
  DEFAULT_STATUS = 'pending'
  ```

### Private Variables and Methods
- **Format**: Prefix with a single underscore `_`
- **Examples**: `_internal_cache`, `def _calculate_tax():`
- **Guidelines**: Indicates that the attribute or method is intended for internal use only.

## 4. Django Specifics

### Model Fields
- **Format**: `snake_case`
- **Examples**: `created_at`, `first_name`.
- **Guidelines**: Avoid naming a field after the model itself (e.g., don't use `user_name` in the `User` model; just use `name`). Avoid using `id` or `pk` as field names manually unless customizing the primary key.

### Related Names (Reverse Relations)
- **Format**: `snake_case`, pluralized.
- **Examples**: 
  ```python
  author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
  ```

### Template Context Variables
- **Format**: `snake_case`
- **Examples**: `{{ user_list }}`, `{{ current_article }}`.

## 5. Environment Variables
- **Format**: `UPPER_SNAKE_CASE`
- **Examples**: `DJANGO_SECRET_KEY`, `DATABASE_URL`, `DEBUG_MODE`.

## 6. URLs and Routing
- **URL Paths**: `kebab-case` (lowercase with hyphens)
  - Examples: `path('user-profile/', ...)`
- **URL Names**: `snake_case`
  - Examples: `name='user_profile'`

By adhering to these conventions, we maintain a clean and predictable codebase that aligns with PEP 8 and Django best practices.
