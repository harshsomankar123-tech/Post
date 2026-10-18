# AI LinkedIn Job Hunter Agent

A clean-architecture, zero-cost AI agent that monitors public LinkedIn hiring posts, screens them for genuine job opportunities, and matches them against candidate skills.

---

## 📚 Complete Project Documentation

* **[Product Requirements Document (PRD)](docs/PRD.md)**: Product scope, personas, functional requirements (FR1–FR10), and non-functional requirements.
* **[High-Level Design (HLD)](docs/HLD.md)**: System topology, Clean Architecture boundaries, sequence diagrams, and data flow.
* **[Agent Guidelines](docs/AGENT_GUIDELINES.md)**: Comprehensive guide for AI agents and developers implementing remaining modules.

---

## Clean Architecture Directory Map

```text
src/
├── domain/                      # Core business models and rules (Zero dependencies)
│   ├── entities/                # raw_post, verified_job, candidate_profile
│   └── value_objects/           # time_filter, match_score, email_contact
│
├── application/                 # Use cases and port interfaces
│   ├── ports/                   # search_harvester, post_classifier, resume_parser, pitch_generator
│   ├── use_cases/               # harvest_posts, classify_posts, parse_resume, score_and_rank
│   └── dtos/                    # search_request_dto, job_feed_dto
│
├── infrastructure/              # External adapters and tool implementations
│   ├── harvesting/              # duckduckgo_harvester, query_builder, url_cleaner, date_normalizer
│   ├── ai/                      # system1_classifier, system2_pitch_drafter, pypdf_resume_parser
│   └── persistence/             # sqlite_repository (Permanent deduplication, $0 cost)
│
└── presentation/                # Delivery layer
    └── api/                     # FastAPI main entrypoint and HTTP/SSE routes
```

---

## Quick Start (Search Harvester Test)

```bash
# 1. Clone repository
git clone https://github.com/harshsomankar123-tech/Post.git
cd Post

# 2. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Run standalone search harvester test
python test_harvester.py
```
