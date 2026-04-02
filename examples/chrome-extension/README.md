# 🌐 Example: Building a Chrome Extension with Cocoon

## Goal
"Build a Chrome extension that summarizes research papers using LLMs."

## Execution
1. `cocoon init --name "paper_sum"`
2. `cocoon hatch --task "Chrome extension for paper summaries"`
3. `cocoon run` (Select Reviewer HitL: YES)
4. `cocoon emerge`

## Result
A production-ready folder containing `manifest.json`, `background.js`, and `popup.html` will be in `./output/`.
