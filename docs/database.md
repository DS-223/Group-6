# Database

## Overview

The Supermarket Hot Deals database stores all key data for the project’s A/B testing and user interactions. It logs registered **users**, records each **Project** or campaign under test, tracks the **Bandit** variants (different deal versions) within each project, and saves each user’s **Transaction** (click or purchase) in the context of those variants. This allows the multi-armed bandit algorithm to assign users to different deal variants and then record their responses, enabling continuous experimentation and optimization of deals.

---

## Connection Setup

The application uses **SQLAlchemy** to connect to a PostgreSQL database. A `database.py` module typically does the setup by reading a database URL from environment variables and creating an engine. For example:

```python
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
```

## The DATABASE_URL is stored in a .env file:

```
DATABASE_URL=postgresql://user:password@localhost:5432/hotdeals
```

### The python-dotenv package loads this file at runtime.
