# Product Requirements Document (PRD)
## Project: AI-Powered LinkedIn Job & Internship Hunter Agent

---

### 1. Executive Summary & Vision
The **AI-Powered LinkedIn Job Hunter Agent** is an autonomous application that eliminates the manual labor of job hunting. By monitoring public recruiter posts on LinkedIn, the agent continuously discovers active hiring opportunities, screens out promotional and spam noise, extracts actionable contact information (e.g. recruiter emails), and matches openings against an uploaded candidate resume—**all without requiring a LinkedIn user account, private login credentials, or paid third-party APIs**.

---

### 2. Problem Statement
1. **Manual Job Search Inefficiencies**: Candidates spend 3–5 hours daily scrolling LinkedIn feeds, wading through course promotions, celebratory posts, and marketing spam to find genuine job openings.
2. **Account Restriction Risks**: Automated bots that log into user LinkedIn accounts face strict rate limits, CAPTCHA challenges, and immediate account bans.
3. **Budget Barriers for Students & Freshers**: Existing scrapers and job-hunting tools rely on expensive paid APIs ($50–$200/month), making them inaccessible to students and job seekers with a $0 budget.

---

### 3. User Personas
* **Primary Persona**: College students, freshers, and junior developers (0–2 years experience) seeking internships or junior SDE roles.
* **Secondary Persona**: Experienced developers looking for remote or specific niche tech stack roles (e.g., Python/FastAPI, AI/ML, React).

---

### 4. Functional Requirements (FR)

| ID | Feature | Description | Priority |
| :--- | :--- | :--- | :--- |
| **FR-1** | **Resume Ingestion** | Candidate uploads a PDF resume. The system extracts raw text and normalizes candidate skills, experience level, and inferred target roles. | P0 (Must Have) |
| **FR-2** | **Role & Query Override** | Candidate can view suggested roles, add/remove target roles, and input custom search keywords (e.g., "Remote", "Python"). | P0 (Must Have) |
| **FR-3** | **Zero-Auth Post Harvesting** | Discovers public LinkedIn posts using search engine index crawlers without requiring a LinkedIn login or cookies. | P0 (Must Have) |
| **FR-4** | **Timestamp Filtering** | Allows filtering posts by publication recency: Past 24 Hours (`d`), Past Week (`w`), or Past Month (`m`). | P0 (Must Have) |
| **FR-5** | **Post Deduplication** | Identifies and removes duplicate posts across multi-query search results using canonical post IDs. | P0 (Must Have) |
| **FR-6** | **Hiring Intent Classification (System 1)** | Evaluates post text to classify `is_hiring: true/false`. Rejects bootcamps, personal celebrations, career advice, and services spam. | P0 (Must Have) |
| **FR-7** | **Entity Extraction** | Extracts role title, hiring company name, recruiter email, and application URLs from verified hiring posts. | P0 (Must Have) |
| **FR-8** | **Resume Skill Matching** | Compares candidate skills against job requirements to compute a 0–100 match percentage. | P1 (High) |
| **FR-9** | **Tailored Outreach Drafting (System 2)** | Drafts a 3-line personalized cold email or LinkedIn DM highlighting candidate projects relevant to that specific post. | P1 (High) |
| **FR-10**| **Interactive Post Feed UI** | Renders cards displaying author, timestamp badge ("2h ago"), role, match %, recruiter email, direct post link, and 1-click pitch copy. | P1 (High) |

---

### 5. Non-Functional Requirements (NFR)

* **NFR-1: Zero Cost ($0 Budget)**: Operates entirely within free tiers (Google Gemini Free / Groq Free, DuckDuckGo public search, built-in SQLite).
* **NFR-2: Zero Account Risk**: Never requests or stores LinkedIn user credentials; queries only publicly indexed data.
* **NFR-3: Latency**: Search and extraction of 30–50 posts completed within 15–20 seconds.
* **NFR-4: Clean Architecture**: Enforces strict separation of concerns across Domain, Application, Infrastructure, and Presentation layers.
* **NFR-5: Modularity & Extensibility**: Search providers and LLM providers must be interchangeable without modifying core domain use cases.

---

### 6. Out of Scope
* Automated direct messaging on LinkedIn using automated accounts (violates LinkedIn ToS and risks bans).
* Automatic email sending on the user's behalf without manual user review.
