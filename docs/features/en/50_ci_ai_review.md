## CI (current: AI Review workflow)

### Purpose
- Run a lightweight Gemini-based review on each push to catch quick style/logic issues early.

### Trigger
- GitHub Actions: `on: [push]`

### Processing (current)
- Set up Python 3.12
- Install Gemini SDK (`google-genai`)
- Get `git diff HEAD~1 HEAD` and truncate to 500 characters
- Send it to `gemini-2.0-flash-lite` and print the review text

### Output
- Printed in the Actions logs as `=== AI Review ===`

### Failure behavior (important)
- Designed to avoid failing the job on Gemini errors (e.g. 429). It prints "Skipped review" instead.

### Constraints / notes
- Using `git diff HEAD~1 HEAD` can miss context when multiple commits are pushed at once
- Requires GitHub secret `GEMINI_API_KEY`

### Related files
- `.github/workflows/ai_review.yml`
- `.github/scripts/ai_review.py`

