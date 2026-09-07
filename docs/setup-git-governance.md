# Git & governance setup (W0 prerequisite, alongside TF-01)

Until the repository is under git with branch protection, **CODEOWNERS and the autonomy matrix are only
statements of intent**: the operating model says it is the platform that enforces, not the AI. Minimum
checklist to turn them into real constraints:

1. `git init`, first commit, push to a remote (GitHub / GitLab / Azure DevOps).
2. Protect the `main` branch:
   - forbid direct pushes;
   - require a Pull Request to merge;
   - require **CODEOWNERS** review;
   - require the **status checks** (CI: test, lint, types, coherence, contract) to pass before merge.
3. Enable CODEOWNERS (the file is already in the repo).
4. (Once the stack is wired) connect CI to the verification commands → the **blocking** gates in
   `quality-gates` become real.

Until points 1–2 are active, the "blocking" gates are conventions in practice. Treat this as part of
**TF-01** (environments/CI), a prerequisite of W1.
