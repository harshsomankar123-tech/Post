# Agent Guidelines: Context & Instructions for AI Agents
## Project: AI-Powered LinkedIn Job & Internship Hunter Agent

> **FOR ANY AI AGENT WORKING ON THIS REPOSITORY**:  
> Read this document thoroughly before writing or modifying any code. It outlines the architectural boundaries, zero-cost constraints, and rules for implementing remaining modules.

---

### 1. Core Architectural Invariants (DO NOT VIOLATE)

1. **Clean Architecture Dependency Rule**:
   * Dependencies point **inward only**: `Domain` $\leftarrow$ `Application` $\leftarrow$ `Infrastructure` & `Presentation`.
   * **Domain Layer** (`src/domain/`) must **NEVER** import from FastAPI, LangChain, DuckDuckGo, PyPDF, or database libraries. It must only contain standard Python types, dataclasses, and pure business logic.
   * **Application Layer** (`src/application/`) defines business use cases and port interfaces (`Protocol`). It must never depend directly on infrastructure libraries.

2. **Zero-Cost ($0) Constraint**:
   * Do **NOT** introduce paid services or credentials.
   * Do **NOT** introduce Redis or external message brokers. Persistent storage and deduplication must use Python's built-in `sqlite3` or in-memory sets.
   * Search must use free search index adapters (`ddgs` / `duckduckgo_search`).
   * LLMs must use free-tier providers (Google Gemini Free via `google-genai` or Groq Free).

3. **No Automated LinkedIn Login**:
   * Never attempt to log in with user credentials or cookies. All post discovery relies on public search engine caches (`site:linkedin.com "hiring"`).

4. **Division of Labor: Python vs. LLM**:
   * **Pure Python handles**: Query formatting, URL cleaning, date arithmetic, search pagination, deduplication, and sorting.
   * **LLM handles only**: Resume parsing, post classification/entity extraction (System 1), and match scoring/outreach drafting (System 2).

---

### 2. Repository File Sitemap

```text
src/
├── domain/
│   ├── entities/
│   │   ├── raw_post.py             # Entity: RawPostItem (unclassified post)
│   │   ├── verified_job.py         # Entity: VerifiedJob (confirmed vacancy)
│   │   └── candidate_profile.py    # Entity: CandidateProfile (skills, exp)
│   └── value_objects/
│       ├── time_filter.py          # Enum: PAST_24H, PAST_WEEK, PAST_MONTH
│       ├── match_score.py          # Value Object: Score (0-100), Breakdown
│       └── email_contact.py        # Value Object: Validated recruiter email
│
├── application/
│   ├── ports/                      # Secondary Ports (Protocols)
│   │   ├── search_harvester_port.py# ISearchHarvester interface
│   │   ├── post_classifier_port.py # IPostClassifier interface (System 1)
│   │   ├── resume_parser_port.py   # IResumeParser interface
│   │   ├── pitch_generator_port.py # IPitchGenerator interface (System 2)
│   │   └── post_repository_port.py # IPostRepository interface
│   ├── use_cases/                  # Application Use Cases
│   │   ├── harvest_posts_use_case.py   # Coordinates search & pagination
│   │   ├── classify_posts_use_case.py  # Filters spam & extracts entities
│   │   ├── parse_resume_use_case.py    # Generates CandidateProfile from PDF
│   │   └── score_and_rank_use_case.py  # Computes match & drafts cold pitch
│   └── dtos/                       # Data Transfer Objects
│       ├── search_request_dto.py   # Input payload from API
│       └── job_feed_dto.py         # Output payload for frontend cards
│
├── infrastructure/                 # Adapters (Implement Ports)
│   ├── harvesting/
│   │   ├── query_builder.py        # Constructs hiring dorks
│   │   ├── url_cleaner.py          # Cleans tracking parameters
│   │   ├── duckduckgo_harvester.py # DDGS search index adapter
│   │   └── date_normalizer.py      # Relative strings to UTC datetimes
│   ├── ai/
│   │   ├── system1_classifier.py   # Gemini/Groq fast classifier
│   │   ├── system2_pitch_drafter.py# Reasoning LLM for personalized pitch
│   │   └── pypdf_resume_parser.py  # PyPDF text extractor
│   └── persistence/
│       └── sqlite_repository.py    # SQLite adapter for deduplication & storage
│
└── presentation/
    └── api/
        ├── main.py                 # FastAPI application factory
        └── routes.py               # REST and SSE streaming endpoints
```

---

### 3. Step-by-Step Implementation Guide for Agents

When implementing the remaining skeleton modules:

1. **Step 1: System 1 Classifier (`src/infrastructure/ai/system1_classifier.py`)**:
   * Implement `IPostClassifier` using `gemini-2.5-flash` or Groq `llama-3.2-3b`.
   * Bind structured output schema: `{ is_hiring: bool, role: str, company: str, email: str }`.
   * Prompt must strictly reject bootcamps, personal celebrations, and service promotions.

2. **Step 2: Resume Parser (`src/infrastructure/ai/pypdf_resume_parser.py`)**:
   * Implement `IResumeParser` using `pypdf.PdfReader`.
   * Extract text and pass to LLM to produce structured `{ skills: [], experience_level: str, target_roles: [] }`.

3. **Step 3: System 2 Pitch Drafter (`src/infrastructure/ai/system2_pitch_drafter.py`)**:
   * Implement `IPitchGenerator`.
   * Compare `CandidateProfile` skills with `VerifiedJob` requirements.
   * Output score (0–100) and draft a 3-sentence polite application email referencing matching candidate projects.

4. **Step 4: SQLite Repository (`src/infrastructure/persistence/sqlite_repository.py`)**:
   * Implement `IPostRepository` using Python's standard `sqlite3` module.
   * Create `seen_posts` table to prevent showing the same post across consecutive searches.

5. **Step 5: FastAPI Router (`src/presentation/api/routes.py`)**:
   * Wire the use cases via dependency injection.
   * Provide `POST /api/v1/jobs/search` and `POST /api/v1/resume/upload`.
